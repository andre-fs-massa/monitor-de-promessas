"""Busca em fontes oficiais federais (equivalente ao busca_rj.py para presidentes).

  python scripts/busca_br.py camara "<palavras>" --anos 2011,2012 [--tipos PL,PLP,PEC,MPV] [--executivo]
  python scripts/busca_br.py dou "<termos>" --de 2011-01-01 --ate 2014-12-31

Câmara dos Deputados: API de dados abertos (dadosabertos.camara.leg.br/api/v2/proposicoes).
O parâmetro keywords procura nas ementas e indexações; o filtro de data de apresentação não
aceita intervalo maior que 3 meses, por isso consultamos ano a ano com o parâmetro ano.
--executivo mantém só as proposições cujo autor é o Poder Executivo (consulta /autores).
É o equivalente federal da busca na Alerj: vale para promessas que dependem de lei.

DOU (Diário Oficial da União): a busca do site in.gov.br (consulta/-/buscar/dou) traz os
resultados num JSON embutido na página (script ..._BuscaDouPortlet_params, chave jsonArray).
Em 15/10/2026 o site recusou toda conexão automática desta máquina (403 ou conexão encerrada,
inclusive com Chrome headless: ERR_HTTP2_PROTOCOL_ERROR). Nesse caso a busca tem de ser feita
pelo navegador do usuário (extensão Claude in Chrome) com a mesma URL que `dou_url` monta.
O LexML e a API do Senado também responderam com verificação anti-robô / indisponível.
"""
import argparse, html, json, re, sys, urllib.parse, urllib.request

CAMARA = "https://dadosabertos.camara.leg.br/api/v2/"
DOU = "https://www.in.gov.br/consulta/-/buscar/dou"
UA = {"User-Agent": "Mozilla/5.0 (monitor-de-promessas)", "Accept": "application/json"}


def _json(url, timeout=90):
    return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read())


def _autores(uri):
    try:
        return [a.get("nome", "") for a in _json(uri + "/autores")["dados"]]
    except Exception:
        return []


def camara(palavras, anos, tipos=(), executivo=False):
    itens = []
    for ano in anos:
        q = {"keywords": palavras, "ano": ano, "itens": 100, "ordem": "ASC", "ordenarPor": "id"}
        if tipos:
            q["siglaTipo"] = ",".join(tipos)
        for p in _json(CAMARA + "proposicoes?" + urllib.parse.urlencode(q))["dados"]:
            uri = CAMARA + f"proposicoes/{p['id']}"
            item = {"tipo": p["siglaTipo"], "numero": p["numero"], "ano": p["ano"], "ementa": p["ementa"],
                    "link": f"https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao={p['id']}"}
            if executivo:
                item["autores"] = _autores(uri)
                if not any("Executivo" in a for a in item["autores"]):
                    continue
            itens.append(item)
    return itens


def dou_url(termos, de, ate):
    d = lambda x: "-".join(reversed(x.split("-")))
    return DOU + "?" + urllib.parse.urlencode({"q": termos, "s": "todos", "exactDate": "personalizado",
                                               "sortType": "0", "publishFrom": d(de), "publishTo": d(ate)})


def dou(termos, de, ate):
    pagina = urllib.request.urlopen(urllib.request.Request(dou_url(termos, de, ate), headers={"User-Agent": "Mozilla/5.0"}),
                                    timeout=90).read().decode("utf-8")
    m = re.search(r'BuscaDouPortlet_params" type="application/json">(.*?)</script>', pagina, re.S)
    hits = json.loads(m.group(1)).get("jsonArray", []) if m else []
    return [{"data": h.get("pubDate"), "titulo": html.unescape(h.get("title", "")), "orgao": h.get("hierarchyStr", ""),
             "resumo": re.sub(r"<[^>]+>", "", html.unescape(h.get("content", "")))[:300],
             "link": "https://www.in.gov.br/web/dou/-/" + h.get("urlTitle", "")} for h in hits]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("fonte", choices=["camara", "dou"])
    ap.add_argument("termos")
    ap.add_argument("--anos", default="")
    ap.add_argument("--tipos", default="")
    ap.add_argument("--executivo", action="store_true")
    ap.add_argument("--de", default="")
    ap.add_argument("--ate", default="")
    a = ap.parse_args()
    if a.fonte == "camara":
        r = camara(a.termos, a.anos.split(","), [t for t in a.tipos.split(",") if t], a.executivo)
    else:
        try:
            r = dou(a.termos, a.de, a.ate)
        except Exception as e:
            sys.exit(f"DOU recusou a conexão ({e}). Abra no navegador: {dou_url(a.termos, a.de, a.ate)}")
    json.dump(r, sys.stdout, ensure_ascii=False, indent=1)

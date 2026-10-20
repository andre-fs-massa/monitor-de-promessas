"""Busca em fontes oficiais do RJ que não têm API documentada.

  python scripts/busca_rj.py ioerj "<termos>" [--anos 2019,2020] [--ate 2020-08-28] [--jornal 12]
  python scripts/busca_rj.py alerj "<termos>" [--bases projetos,leis] [--legislatura 1923|2327]
  python scripts/busca_rj.py edicao "<link view_publicacao do resultado>" [--saida arq.txt]
  python scripts/busca_rj.py dorio "<termos>" [--de 2025-01-01] [--ate 2026-10-14] [--paginas 3] [--filtro "p1;p2"]

IOERJ (Diário Oficial): usa o formulário de busca textual (busca_do.php). A busca junta as
palavras com E, não aceita frase exata e devolve no máximo 100 matérias por consulta, por isso
consultamos ano a ano. Jornal 12 = Parte I (Poder Executivo); 3 = Parte II (Legislativo).
O texto mostrado é só o início da matéria; para ler a matéria inteira use `edicao`, que baixa o
PDF da edição pelo visualizador do site e extrai o texto com pdftotext.

Alerj: o sistema Lotus Notes aceita busca textual por URL (?SearchView&Query=). Bases:
  projetos = scpro<legislatura>.nsf (proposições: vlei, vleicomp, vemenda; 1923 = 2019-2023, 2327 = 2023-2027)
  leis     = contlei.nsf (visão geral de leis estaduais)

DO Rio (Diário Oficial do Município do Rio de Janeiro): a busca do site doweb.rio.rj.gov.br
chama um índice Elasticsearch que devolve JSON com o texto completo de cada página (10 por
página de resultado). Aceita uma "frase exata" entre aspas ou palavras soltas (OR), mas não
combina frase com outras palavras nem aceita AND; por isso o --filtro mantém só as páginas
cujo texto contém todas as palavras indicadas. Resultados vêm por data (mais recentes primeiro). O link de cada resultado baixa o PDF
da página: /portal/edicoes/download/<diario_id>/<pagina>. A Câmara Municipal
(aplicnt.camara.rj.gov.br) recusou conexão em out/2026; as leis sancionadas saem no DO Rio.
"""
import argparse, html, json, unicodedata, http.cookiejar, re, subprocess, sys, tempfile, urllib.parse, urllib.request

IOERJ = "https://www.ioerj.com.br/portal/modules/conteudoonline/"
ALERJ = "http://alerjln1.alerj.rj.gov.br/"
DORIO = "https://doweb.rio.rj.gov.br"
UA = {"User-Agent": "Mozilla/5.0 (monitor-de-promessas)"}
ALERJ_VIEWS = {
    "projetos": ["scpro{leg}.nsf/vlei", "scpro{leg}.nsf/vleicomp", "scpro{leg}.nsf/vemenda"],
    "leis": ["contlei.nsf/c8aa0900025feef6032564ec0060dfff"],
}


def _texto(fragmento):
    fragmento = re.sub(r"<script.*?</script>|<style.*?</style>", " ", fragmento, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragmento))).strip()


def _decodifica(raw):
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:  # páginas de documento do Lotus Notes vêm em Latin-1
        return raw.decode("latin-1")


def _get(url, data=None, opener=None, timeout=120):
    req = urllib.request.Request(url, data=data, headers=UA)
    return (opener.open if opener else urllib.request.urlopen)(req, timeout=timeout).read()


def ioerj(termos, ano, jornal="12", ordem="datapublicacao asc"):
    campos = {"textobusca": termos, "busca[jornal]": jornal, "tipobusca": "texto",
              "buscaordem": ordem, "buscar": "Buscar", "datapublicacao[ano]": str(ano)}
    pagina = _get(IOERJ + "busca_do.php?acao=busca",
                  urllib.parse.urlencode(campos, encoding="utf-8").encode()).decode("utf-8", "replace")
    pagina = re.sub(r"<!--.*?-->", "", pagina, flags=re.S)  # a página traz uma lista antiga comentada
    total = re.search(r"<b>(\d+)</b> mat", pagina)
    itens = []
    for bloco in re.split(r"(?=<a target=\"_blank\" href=\"/portal/modules/conteudoonline/view_publicacao)", pagina)[1:]:
        cab = re.search(r"(\d\d)/(\d\d)/(\d{4}) p\S+gina (\d+) - Mat\S+ria Id: (\d+)", bloco)
        if not cab:
            continue
        d, m, a, pag, mid = cab.groups()
        tipo = re.search(r"<b>Tipo:</b>(.*?)</span>", bloco, re.S)
        resumo = re.search(r'class="style4"[^>]*>(.*?)</td>', bloco, re.S)
        itens.append({"data": f"{a}-{m}-{d}", "pagina": pag, "id": mid,
                      "tipo": _texto(tipo.group(1)) if tipo else "",
                      "resumo": _texto(resumo.group(1)) if resumo else "",
                      "link": IOERJ + "view_publicacao.php?" + re.sub(r"&tb=.*", "&tb=", html.unescape(
                          re.search(r'view_publicacao\.php\?([^"]+)"', bloco).group(1)))})
    return (int(total.group(1)) if total else 0), itens


def edicao(link):
    """Baixa o PDF da edição (o visualizador passa por um redirecionamento com sessão) e devolve o texto."""
    link = re.sub(r"&tb=.*", "&tb=", link)  # o parâmetro tb traz o termo buscado, com espaços
    op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    redir = _get(link, opener=op).decode("utf-8", "replace")
    alvo = html.unescape(re.search(r"mostra_edicao\.php\?session=[^'\"]+", redir).group(0))
    visor = _get(IOERJ + alvo, opener=op).decode("utf-8", "replace")
    pd = re.search(r'var pd = "([^"]+)"', visor).group(1)
    pdf = _get(IOERJ + f"mostra_edicao.php?k={pd[:12]}P{pd[12:]}", opener=op, timeout=300)
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
        f.write(pdf)
    # sem -layout o pdftotext lê coluna por coluna, o que preserva o fluxo das matérias
    return subprocess.run(["pdftotext", "-enc", "UTF-8", f.name, "-"], capture_output=True).stdout.decode("utf-8", "replace")


def alerj(termos, bases=("projetos", "leis"), legislatura="1923"):
    out = []
    q = urllib.parse.quote(termos)
    for base in bases:
        for view in (v.format(leg=legislatura) for v in ALERJ_VIEWS[base]):
            url = f"{ALERJ}{view}?SearchView&Query={q}&SearchMax=50"
            try:
                pagina = _decodifica(_get(url, timeout=90))
            except Exception as e:
                out.append({"view": view, "erro": str(e)})
                continue
            for linha in re.findall(r"<tr[^>]*>(.*?)</tr>", pagina, re.S):
                link = re.search(r'href="(/[^"]+?\?OpenDocument)', linha)
                txt = _texto(linha)
                if link and txt:
                    out.append({"view": view, "texto": txt[:400], "link": ALERJ.rstrip("/") + link.group(1)})
    return out


def _sem_acento(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()


def dorio(termos, de="2025-01-01", ate="", paginas=3, filtro=()):
    """Resultados do DO Rio (mais recentes primeiro): data, link do PDF da página e trechos com os termos."""
    datas = f"/di:{de}" + (f"/df:{ate}" if ate else "")
    # trechos em volta das frases entre aspas ou, sem aspas, das palavras da busca
    palavras = re.findall(r'"([^"]+)"', termos) or [w for w in re.findall(r"\w{4,}", termos) if w not in ("AND", "NOT")]
    total, itens = 0, []
    for n in range(paginas):
        url = f"{DORIO}/busca/busca/buscar/query/{n}{datas}/?1=1&q=" + urllib.parse.quote(termos)
        dados = json.loads(_get(url, timeout=120))
        total = dados["hits"]["total"]
        for h in dados["hits"]["hits"]:
            s = h["_source"]
            txt = re.sub(r"\s+", " ", s["conteudo"])
            if not all(_sem_acento(f) in _sem_acento(txt) for f in filtro):
                continue
            trechos = []
            for w in (palavras[:2] + list(filtro))[:4]:
                m = re.search(re.escape(w).replace("\ ", r"\s+"), txt, re.I)
                if m:
                    trechos.append(txt[max(0, m.start() - 200):m.end() + 300])
            itens.append({"data": s["data"], "pagina": s["pagina"], "diario_id": s["diario_id"],
                          "link": f"{DORIO}/portal/edicoes/download/{s['diario_id']}/{s['pagina']}",
                          "trechos": trechos})
        if (n + 1) * 10 >= total:
            break
    return total, itens


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("fonte", choices=["ioerj", "alerj", "edicao", "dorio"])
    ap.add_argument("termos")
    ap.add_argument("--anos", default="2019,2020")
    ap.add_argument("--ate", default="2020-08-28")
    ap.add_argument("--jornal", default="12")
    ap.add_argument("--bases", default="projetos,leis")
    ap.add_argument("--legislatura", default="1923")
    ap.add_argument("--saida")
    ap.add_argument("--de", default="2025-01-01")
    ap.add_argument("--paginas", type=int, default=3)
    ap.add_argument("--filtro", default="")
    a = ap.parse_args()
    if a.fonte == "ioerj":
        for ano in a.anos.split(","):
            total, itens = ioerj(a.termos, ano, a.jornal)
            print(f"[{ano}] {total} matérias" + (" (mostrando 100)" if total > 100 else ""))
            for i in itens:
                if i["data"] <= a.ate:
                    print(f"  {i['data']} p.{i['pagina']} id {i['id']} | {i['tipo']} | {i['resumo'][:250]}")
    elif a.fonte == "alerj":
        for r in alerj(a.termos, a.bases.split(","), a.legislatura):
            print(f"  [{r['view']}] {r.get('erro') or r['texto']}\n     {r.get('link', '')}")
    elif a.fonte == "dorio":
        total, itens = dorio(a.termos, a.de, "" if a.ate == "2020-08-28" else a.ate, a.paginas,
                             [f for f in a.filtro.split(";") if f])
        print(f"{total} páginas encontradas" + (f", {len(itens)} passaram no filtro" if a.filtro else ""))
        for i in itens:
            print(f"  {i['data']} {i['link']}")
            for t in i["trechos"]:
                print(f"     ... {t[:400]}")
    else:
        txt = edicao(a.termos)
        if a.saida:
            open(a.saida, "w", encoding="utf-8").write(txt)
            print("salvo", a.saida, len(txt), "caracteres")
        else:
            print(txt)

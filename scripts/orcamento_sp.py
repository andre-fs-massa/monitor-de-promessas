# Despesa do Estado de São Paulo por programa e ação orçamentária, do Portal da Transparência do Estado
# (consulta "Despesas", https://www.transparencia.sp.gov.br/Despesas; a base começa em 2020).
#   python -I scripts/orcamento_sp.py baixar 2022 2023 ...   -> data/interim/orcamento_sp_acoes.csv
#   python -I scripts/orcamento_sp.py buscar "regex"          -> ações cujo nome (ou programa) bate, com o empenhado por ano
# Valores em reais: dotação atual, empenhado, liquidado e pago, por ação (soma de todos os órgãos).
import csv, re, sys, time
from pathlib import Path
import requests, urllib3

BASE = "https://www.transparencia.sp.gov.br/Despesas"
RAIZ = Path(__file__).resolve().parents[1]
SAIDA = RAIZ / "data" / "interim" / "orcamento_sp_acoes.csv"
CAMPOS = ["ano", "programa", "nome_programa", "acao", "nome_acao", "dotacao_atual", "empenhado", "liquidado", "pago"]
# O servidor não envia o certificado intermediário; a consulta é de dados públicos, só leitura.
urllib3.disable_warnings()


def sessao():
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0"
    s.verify = False
    s.get(BASE, timeout=60)
    return s


def consulta(s, **filtro):
    p = dict(tipoRetorno="programa", page=1, pageSize=1000, totalItens=0, **filtro)
    for tentativa in range(4):
        try:
            r = s.post(BASE + "/Buscar", json=p, timeout=180)
            r.raise_for_status()
            d = r.json()
            assert not d.get("hasNext"), "mais de uma página"
            return d["items"]
        except (requests.RequestException, ValueError):
            time.sleep(5 * (tentativa + 1))
    raise RuntimeError(f"falhou: {filtro}")


def chave(r):
    return tuple(int(r[k]) if str(r[k]).lstrip("-").isdigit() else -1 for k in ("ano", "programa", "acao"))


def baixar(anos):
    from concurrent.futures import ThreadPoolExecutor
    todas = []
    if SAIDA.exists():
        todas = [r for r in csv.DictReader(open(SAIDA, encoding="utf-8")) if int(r["ano"]) not in anos]
    for ano in anos:
        s = sessao()
        progs = consulta(s, anoExercicio=ano)

        def acoes(pg):
            # uma sessão por consulta: as threads não dividem a mesma conexão
            return pg, consulta(sessao(), anoExercicio=ano, codPrograma=pg["cod_programa"])

        n = 0
        with ThreadPoolExecutor(8) as ex:
            for pg, lista in ex.map(acoes, progs):
                for a in lista:
                    todas.append({"ano": ano, "programa": pg["cod_programa"], "nome_programa": pg["nome_programa"],
                                  "acao": a["cod_acao"], "nome_acao": a["nome_acao"], "dotacao_atual": a["vl_dotacao_atual"],
                                  "empenhado": a["vl_empenhado"], "liquidado": a["vl_liquidado"], "pago": a["vl_pago"]})
                    n += 1
        tot = sum(p["vl_empenhado"] or 0 for p in progs) / 1e9
        print(ano, len(progs), "programas,", n, "ações, empenhado R$", f"{tot:.1f} bi", flush=True)
        todas.sort(key=chave)
        with open(SAIDA, "w", encoding="utf-8", newline="") as fh:  # grava a cada ano
            w = csv.DictWriter(fh, CAMPOS)
            w.writeheader()
            w.writerows(todas)


def buscar(txt):
    por = {}
    for r in csv.DictReader(open(SAIDA, encoding="utf-8")):
        if re.search(txt, r["nome_acao"] + " | " + r["nome_programa"], re.I) or r["acao"] == txt:
            v = por.setdefault((r["acao"], r["nome_acao"], r["nome_programa"]), {})  # a mesma ação pode estar em vários programas
            v[r["ano"]] = v.get(r["ano"], 0) + float(r["empenhado"] or 0) / 1e6
    for (a, n, pg), v in sorted(por.items()):
        print(a, n[:55], "[" + pg[:35] + "]", " ".join(f"{k}: {v[k]:,.1f}" for k in sorted(v)), "(R$ mi empenhado)")


# --- SIGEO (Secretaria da Fazenda, consulta da Lei 131): anos desde 2010, uma ação por consulta ---------------------
SIGEO = "https://www.fazenda.sp.gov.br/SigeoLei131/Paginas/FlexConsDespesa.aspx"
P = "ctl00$ContentPlaceHolder1$"
CACHE_SIGEO = RAIZ / "data" / "interim" / "orcamento_sp_sigeo.csv"


def _campos(html):
    from bs4 import BeautifulSoup
    s = BeautifulSoup(html, "html.parser")
    f = {i["name"]: i.get("value", "") for i in s.find_all("input", {"type": "hidden"}) if i.get("name")}
    for sel in s.find_all("select"):
        op = sel.find("option", selected=True) or sel.find("option")
        if op is not None:
            f[sel["name"]] = op.get("value", "")
    return f, s


def _sigeo_ano(ano):
    """Sessão com o ano escolhido e a fase Empenhado marcada (cada mudança é um postback; marcar a fase
    no envio final zera os filtros, por isso ela vai antes)."""
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0"
    s.verify = False
    html = s.get(SIGEO, timeout=60).text
    for campo, valor in (("ddlAno", str(ano)), ("cblFase$2", "on")):
        f, _ = _campos(html)
        if campo != "ddlAno":
            f[P + "ddlAno"] = str(ano)
        f.update({P + campo: valor, P + "cblFase$2": "on" if campo != "ddlAno" else "", "__EVENTTARGET": P + campo, "__EVENTARGUMENT": ""})
        if campo == "ddlAno":
            f.pop(P + "cblFase$2")
        html = s.post(SIGEO, data=f, timeout=300).text
    return s, html


def sigeo_acoes(ano, txt):
    _, html = _sigeo_ano(ano)
    _, sp = _campos(html)
    for o in sp.find(id="ctl00_ContentPlaceHolder1_ddlAcao").find_all("option"):
        if re.search(txt, o.text, re.I):
            print(o.text)


def sigeo_empenhado(ano, acao):
    s, html = _sigeo_ano(ano)
    f, _ = _campos(html)
    f.update({P + "ddlAcao": acao, P + "cblFase$2": "on", "__EVENTTARGET": P + "ddlAcao", "__EVENTARGUMENT": ""})
    html = s.post(SIGEO, data=f, timeout=300).text
    f, _ = _campos(html)
    f.update({P + "cblFase$2": "on", P + "btnPesquisar": "Pesquisar", "__EVENTTARGET": "", "__EVENTARGUMENT": ""})
    f.pop(P + "Home", None)
    _, sp = _campos(s.post(SIGEO, data=f, timeout=600).text)
    t = sp.find(id="ctl00_ContentPlaceHolder1_gdvDespesas")
    for tr in (t.find_all("tr") if t else []):
        tds = [td.get_text(" ", strip=True) for td in tr.find_all("td")]
        if len(tds) >= 2 and tds[-2] == "TOTAL":
            return float(tds[-1].replace(".", "").replace(",", "."))
    return 0.0


def sigeo(anos, acoes):
    cache = {}
    if CACHE_SIGEO.exists():
        cache = {(r["ano"], r["acao"]): r["empenhado"] for r in csv.DictReader(open(CACHE_SIGEO, encoding="utf-8"))}
    for acao in acoes:
        linha = []
        for ano in anos:
            k = (str(ano), acao)
            if k not in cache:
                cache[k] = str(sigeo_empenhado(ano, acao))
            linha.append(f"{ano}: {float(cache[k]) / 1e6:,.1f}")
        print(acao, "  ".join(linha), "(R$ mi empenhado)", flush=True)
    with open(CACHE_SIGEO, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["ano", "acao", "empenhado"])
        w.writerows([[a, c, v] for (a, c), v in sorted(cache.items())])


if __name__ == "__main__":
    # sigeo-acoes <ano> "regex": lista as ações do ano no SIGEO; sigeo <anos separados por vírgula> <ação> ...: empenhado
    if sys.argv[1] == "baixar":
        baixar([int(x) for x in sys.argv[2:]])
    elif sys.argv[1] == "sigeo-acoes":
        sigeo_acoes(int(sys.argv[2]), sys.argv[3])
    elif sys.argv[1] == "sigeo":
        sigeo([int(x) for x in sys.argv[2].split(",")], sys.argv[3:])
    else:
        buscar(sys.argv[2])

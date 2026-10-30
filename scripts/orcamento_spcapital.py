# Despesa da Prefeitura de São Paulo por projeto/atividade, dos dados abertos da prefeitura
# (conjunto "Execução orçamentária", https://dados.prefeitura.sp.gov.br/dataset/execucao-orcamentaria, 2003 em diante).
#   python -I scripts/orcamento_spcapital.py baixar          -> data/interim/orcamento_spcapital_acoes.csv
#   python -I scripts/orcamento_spcapital.py buscar "regex"   -> projetos/atividades cujo nome (ou código) bate, com o empenhado por ano
# O arquivo bruto (~90 MB) fica em data/raw/spcapital_despesa/.
import csv, io, re, sys
from collections import defaultdict
from pathlib import Path
import requests, urllib3

RAIZ = Path(__file__).resolve().parents[1]
BRUTO = RAIZ / "data" / "raw" / "spcapital_despesa"
SAIDA = RAIZ / "data" / "interim" / "orcamento_spcapital_acoes.csv"
API = "https://dados.prefeitura.sp.gov.br/api/3/action/package_show?id=execucao-orcamentaria"
UA = {"User-Agent": "Mozilla/5.0"}
CAMPOS = ["ano", "acao", "nome_acao", "orgao", "empenhado", "liquidado"]
urllib3.disable_warnings()


def num(v):
    return float(v.replace(".", "").replace(",", ".")) if v and "," in v else float(v or 0)


def baixar():
    res = requests.get(API, headers=UA, timeout=120, verify=False).json()["result"]["resources"]
    url = next(r["url"] for r in res if r["format"].upper() == "CSV" and "2003" in r["name"])
    BRUTO.mkdir(parents=True, exist_ok=True)
    p = BRUTO / url.rsplit("/", 1)[1]
    if not p.exists():
        with requests.get(url, headers=UA, timeout=900, stream=True, verify=False) as r:
            r.raise_for_status()
            with open(p, "wb") as fh:
                for bloco in r.iter_content(1 << 20):
                    fh.write(bloco)
    soma = defaultdict(lambda: [0.0, 0.0])
    nomes = {}
    with open(p, encoding="latin-1", newline="") as fh:
        for r in csv.DictReader(fh, delimiter=";"):
            k = (r["Cd_AnoExecucao"], r["ProjetoAtividade"], r["Ds_Orgao"])
            nomes[k] = r["Ds_Projeto_Atividade"]
            soma[k][0] += num(r["Vl_EmpenhadoLiquido"])
            soma[k][1] += num(r["Vl_Liquidado"])
    with open(SAIDA, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(CAMPOS)
        for (a, c, o), (e, l) in sorted(soma.items()):
            w.writerow([a, c, nomes[(a, c, o)], o, round(e, 2), round(l, 2)])
    por_ano = defaultdict(float)
    for (a, _, _), (e, _) in soma.items():
        por_ano[a] += e
    for a in sorted(por_ano):
        print(a, f"empenhado R$ {por_ano[a] / 1e9:.1f} bi")


def buscar(txt):
    por = defaultdict(dict)
    for r in csv.DictReader(open(SAIDA, encoding="utf-8")):
        if re.search(txt, r["nome_acao"], re.I) or r["acao"] == txt:
            v = por[(r["acao"], r["nome_acao"], r["orgao"])]
            v[r["ano"]] = v.get(r["ano"], 0) + float(r["empenhado"]) / 1e6
    for (a, n, o), v in sorted(por.items()):
        print(a, n[:60], "[" + o[:30] + "]", " ".join(f"{k}: {v[k]:,.1f}" for k in sorted(v) if k >= "2012"), "(R$ mi empenhado)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    baixar() if sys.argv[1] == "baixar" else buscar(sys.argv[2])

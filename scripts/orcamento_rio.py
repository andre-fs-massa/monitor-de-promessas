# Despesa da Prefeitura do Rio de Janeiro por ação orçamentária, dos dados abertos da prefeitura (Data.Rio,
# conjunto "Execução Orçamentária Despesas", https://www.data.rio/datasets/PCRJ::execução-orçamentária-despesas).
# O conjunto cobre 2008 a 2019 e foi atualizado pela última vez em out/2019 (2019 está incompleto). Os portais
# Contas Rio e Rio Transparente recusam conexões feitas de fora do Brasil.
#   python -I scripts/orcamento_rio.py baixar          -> data/interim/orcamento_rio_acoes.csv
#   python -I scripts/orcamento_rio.py buscar "regex"   -> ações cujo nome (ou código) bate, com o empenhado por ano
import csv, io, re, sys
from collections import defaultdict
from pathlib import Path
import requests, urllib3

RAIZ = Path(__file__).resolve().parents[1]
BRUTO = RAIZ / "data" / "raw" / "rio_despesa" / "execucao_orcamentaria_despesas.csv"
SAIDA = RAIZ / "data" / "interim" / "orcamento_rio_acoes.csv"
URL = "https://www.data.rio/api/download/v1/items/3126e57d915b432fa25dcee803ae6c77/csv?layers=0"
UA = {"User-Agent": "Mozilla/5.0"}
urllib3.disable_warnings()


def num(v):
    return float(v) if v else 0.0


def baixar():
    BRUTO.parent.mkdir(parents=True, exist_ok=True)
    if not BRUTO.exists():
        r = requests.get(URL, headers=UA, timeout=900, verify=False)
        r.raise_for_status()
        BRUTO.write_bytes(r.content)
    soma = defaultdict(lambda: [0.0, 0.0])
    nomes = {}
    txt = BRUTO.read_bytes().decode("utf-8-sig", errors="replace")
    for r in csv.DictReader(io.StringIO(txt)):
        k = (r["Exercício"], r["Ação"], r["Órgão"])
        nomes[k] = r["Descrição da Ação"]
        soma[k][0] += num(r["Empenhado"])
        soma[k][1] += num(r["Liquidado"])
    with open(SAIDA, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["ano", "acao", "nome_acao", "orgao", "empenhado", "liquidado"])
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
            v = por[(r["acao"], r["nome_acao"])]
            v[r["ano"]] = v.get(r["ano"], 0) + float(r["empenhado"]) / 1e6
    for (a, n), v in sorted(por.items()):
        print(a, n[:60], " ".join(f"{k}: {v[k]:,.1f}" for k in sorted(v)), "(R$ mi empenhado)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    baixar() if sys.argv[1] == "baixar" else buscar(sys.argv[2])

# Despesa do Estado da Bahia por ação orçamentária, dos dados abertos do Estado (conjunto "Despesas",
# https://dados.ba.gov.br/dataset/despesas — extraído do FIPLAN/Sefaz, a mesma base do Portal da Transparência da Bahia).
#   python -I scripts/orcamento_ba.py agregar   -> data/interim/orcamento_ba_acoes.csv (lê data/raw/orcamento_ba/despesas.zip)
#   python -I scripts/orcamento_ba.py buscar "regex"   -> ações cujo nome (ou código) bate, com o empenhado por ano
# O zip (~226 MB, um CSV de 2,4 GB) é baixado à mão de dados.ba.gov.br. A série começa em 2013.
import csv, io, re, sys, zipfile
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
ZIP = RAIZ / "data" / "raw" / "orcamento_ba" / "despesas.zip"
SAIDA = RAIZ / "data" / "interim" / "orcamento_ba_acoes.csv"
CAMPOS = ["ano", "acao", "nome_acao", "unidade", "empenhado", "liquidado", "pago"]


def num(v):
    return float(v.replace(".", "").replace(",", ".")) if v else 0.0


def agregar():
    soma = defaultdict(lambda: [0.0, 0.0, 0.0])
    with zipfile.ZipFile(ZIP) as z, z.open("VW_PAINEL_DESPESA.csv") as fh:
        for i, r in enumerate(csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig"), delimiter=";")):
            v = soma[(r["ANO_EXERCICIO"], r["COD_ACAO_PROGRAMA_GOVERNO"], r["NOM_ACAO_PROGRAMA_GOVERNO"], r["NOM_RES_UNIDADE_ORCAMENTARIA"])]
            v[0] += num(r["VAL_EMPENHADO_TOTAL"]); v[1] += num(r["VAL_LIQUIDADO_TOTAL"]); v[2] += num(r["VAL_PAGO"])
            if i % 2_000_000 == 0:
                print(i, flush=True)
    linhas = [{"ano": a, "acao": c, "nome_acao": n, "unidade": u, "empenhado": round(e, 2), "liquidado": round(l, 2), "pago": round(p, 2)}
              for (a, c, n, u), (e, l, p) in soma.items()]
    linhas.sort(key=lambda r: (int(r["ano"]), r["acao"], r["unidade"]))
    with open(SAIDA, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, CAMPOS); w.writeheader(); w.writerows(linhas)
    tot = defaultdict(float)
    for r in linhas:
        tot[r["ano"]] += r["empenhado"]
    for a in sorted(tot):
        print(a, f"empenhado R$ {tot[a] / 1e9:.1f} bi")


def buscar(txt):
    por = defaultdict(dict)
    for r in csv.DictReader(open(SAIDA, encoding="utf-8")):
        if re.search(txt, r["nome_acao"], re.I) or r["acao"] == txt:
            v = por[(r["acao"], r["nome_acao"], r["unidade"])]
            v[r["ano"]] = v.get(r["ano"], 0) + float(r["empenhado"]) / 1e6
    for (a, n, u), v in sorted(por.items()):
        print(a, n[:60], "[" + u[:12] + "]", " ".join(f"{k}: {v[k]:,.1f}" for k in sorted(v)), "(R$ mi empenhado)")


if __name__ == "__main__":
    {"agregar": lambda: agregar(), "buscar": lambda: buscar(sys.argv[2])}[sys.argv[1]]()

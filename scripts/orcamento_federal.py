"""Orçamento federal por ação (dados abertos do Portal da Transparência / CGU).

  python scripts/orcamento_federal.py baixar 2022 2023 2024 2025 2026
  python scripts/orcamento_federal.py agregar            -> data/interim/orcamento_acoes.csv
  python scripts/orcamento_federal.py buscar "<regex no nome da ação ou do programa>"
  python scripts/orcamento_federal.py tesouro           -> data/interim/tesouro_pago_acoes.csv
  python scripts/orcamento_federal.py pago "<regex>"     (valor PAGO por ação, Tesouro, desde 2008)

Fonte: https://portaldatransparencia.gov.br/download-de-dados/orcamento-despesa/<ano>
(redireciona para dadosabertos-download.cgu.gov.br; CSV em Latin-1, separador ';', vírgula decimal).
`buscar` usa a despesa EMPENHADA (padrão em análise orçamentária; o realizado não inclui restos a pagar).
Colunas de valor: ORÇAMENTO INICIAL (dotação da LOA), ATUALIZADO (com créditos), EMPENHADO e
REALIZADO (despesa executada). O ano corrente vem parcial.

Antes de 2014 o Portal da Transparência não tem esse arquivo. Para 2008–2013 usamos o Tesouro Transparente,
"Despesas da União mensais desde 2008" (data/raw/tesouro/despesauniao.xlsx), que traz o valor PAGO
(inclui restos a pagar), não o empenhado.
"""
import csv, io, re, sys, unicodedata, urllib.request, zipfile
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "data" / "raw" / "transparencia"
AGG = RAIZ / "data" / "interim" / "orcamento_acoes.csv"
URL = "https://dadosabertos-download.cgu.gov.br/PortalDaTransparencia/saida/orcamento-despesa/{}_OrcamentoDespesa.zip"
VAL = ["ORÇAMENTO INICIAL (R$)", "ORÇAMENTO ATUALIZADO (R$)", "ORÇAMENTO EMPENHADO (R$)", "ORÇAMENTO REALIZADO (R$)"]


def baixar(anos):
    RAW.mkdir(parents=True, exist_ok=True)
    for a in anos:
        dados = urllib.request.urlopen(urllib.request.Request(URL.format(a), headers={"User-Agent": "Mozilla/5.0"}), timeout=300).read()
        (RAW / f"{a}_OrcamentoDespesa.zip").write_bytes(dados)
        print(a, len(dados))


def _num(s):
    return float(s.replace(".", "").replace(",", ".") or 0)


def agregar():
    soma = defaultdict(lambda: [0.0] * 4)
    for z in sorted(RAW.glob("*_OrcamentoDespesa.zip")):
        with zipfile.ZipFile(z) as zf:
            nome = [n for n in zf.namelist() if n.endswith(".csv")][0]
            for r in csv.DictReader(io.TextIOWrapper(zf.open(nome), encoding="latin-1"), delimiter=";"):
                k = (r["EXERCÍCIO"], r["NOME ÓRGÃO SUPERIOR"], r["NOME UNIDADE ORÇAMENTÁRIA"], r["CÓDIGO PROGRAMA ORÇAMENTÁRIO"], r["NOME PROGRAMA ORÇAMENTÁRIO"],
                     r["CÓDIGO AÇÃO"], r["NOME AÇÃO"])
                for i, c in enumerate(VAL):
                    soma[k][i] += _num(r[c])
    with open(AGG, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["ano", "orgao_superior", "unidade", "cod_programa", "programa", "cod_acao", "acao", "inicial", "atualizado", "empenhado", "realizado"])
        for k, v in sorted(soma.items()):
            w.writerow(list(k) + [f"{x:.2f}" for x in v])
    print(len(soma), "linhas ->", AGG)


def _sa(t):
    return unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()


def buscar(padrao, campo="empenhado"):
    rx = re.compile(_sa(padrao))
    tab = defaultdict(dict)
    for r in csv.DictReader(open(AGG, encoding="utf-8")):
        if rx.search(_sa(r["acao"] + " " + r["programa"] + " " + r["unidade"])):
            k = (r["cod_acao"], r["acao"], r["unidade"])
            tab[k][r["ano"]] = tab[k].get(r["ano"], 0) + float(r[campo]) / 1e9
    return tab


TES_XLSX = RAIZ / "data" / "raw" / "tesouro" / "despesauniao.xlsx"
TES_URL = ("https://www.tesourotransparente.gov.br/ckan/dataset/bcd753b8-e79d-4964-a565-977d23bada0d/"
           "resource/1043f379-e7fb-4c18-be52-345b8672ccfb/download/despesauniao.xlsx")
TES_AGG = RAIZ / "data" / "interim" / "tesouro_pago_acoes.csv"


def agregar_tesouro():
    import openpyxl
    soma = defaultdict(float)
    ws = openpyxl.load_workbook(TES_XLSX, read_only=True).worksheets[0]
    for r in ws.iter_rows(min_row=2, values_only=True):
        soma[(r[18], r[6], r[7], r[8], r[9])] += r[20] or 0
    with open(TES_AGG, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["ano", "cod_programa", "programa", "cod_acao", "acao", "pago"])
        for k, v in sorted(soma.items()):
            w.writerow(list(k) + [f"{v:.2f}"])
    print(len(soma), "linhas ->", TES_AGG)


def buscar_pago(padrao):
    rx = re.compile(_sa(padrao))
    tab = defaultdict(dict)
    for r in csv.DictReader(open(TES_AGG, encoding="utf-8")):
        if rx.search(_sa(r["cod_acao"] + " " + r["acao"] + " " + r["programa"])):
            k = (r["cod_acao"], r["acao"])
            tab[k][r["ano"]] = tab[k].get(r["ano"], 0) + float(r["pago"]) / 1e9
    return tab


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "baixar":
        baixar(sys.argv[2:])
    elif cmd == "agregar":
        agregar()
    elif cmd == "tesouro":
        agregar_tesouro()
    elif cmd == "pago":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        for (cod, acao), anos in sorted(buscar_pago(sys.argv[2]).items(), key=lambda kv: -max(kv[1].values())):
            print(cod, acao[:70], "|", " ".join(f"{a}:{v:.2f}" for a, v in sorted(anos.items()) if "2009" < a < "2017"))
    else:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        for (cod, acao, org), anos in sorted(buscar(sys.argv[2]).items(), key=lambda kv: -max(kv[1].values())):
            print(cod, acao[:70], "|", org[:30], "|", " ".join(f"{a}:{v:.2f}" for a, v in sorted(anos.items())))

# Despesa da Prefeitura de Belo Horizonte por programa, ação e subação, dos dados abertos da PBH
# (conjunto "Despesas Orçamentárias", https://dados.pbh.gov.br/dataset/despesas-orcamentarias, 2020 em diante;
# o portal não tem despesa por ação antes de 2018).
#   python -I scripts/orcamento_bh.py baixar 2020 2021 ...   -> data/interim/orcamento_bh_acoes.csv
#   python -I scripts/orcamento_bh.py buscar "regex"          -> ações/subações cujo nome bate, com o empenhado por ano
# Os arquivos brutos (~200 MB por ano, um movimento por linha) ficam em data/raw/bh_despesa/.
import csv, re, sys
from collections import defaultdict
from pathlib import Path
import requests, urllib3

RAIZ = Path(__file__).resolve().parents[1]
BRUTO = RAIZ / "data" / "raw" / "bh_despesa"
SAIDA = RAIZ / "data" / "interim" / "orcamento_bh_acoes.csv"
API = "https://dados.pbh.gov.br/api/3/action/package_show?id=despesas-orcamentarias"
UA = {"User-Agent": "Mozilla/5.0"}
CAMPOS = ["ano", "programa", "acao", "subacao", "empenhado", "liquidado"]
urllib3.disable_warnings()


def baixar(anos):
    res = requests.get(API, headers=UA, timeout=120, verify=False).json()["result"]["resources"]
    urls = {r["name"].strip()[:4]: r["url"] for r in res}
    linhas = []
    if SAIDA.exists():
        linhas = [r for r in csv.DictReader(open(SAIDA, encoding="utf-8")) if r["ano"] not in anos]
    BRUTO.mkdir(parents=True, exist_ok=True)
    for ano in anos:
        p = BRUTO / f"despesas_{ano}.csv"
        if not p.exists():
            with requests.get(urls[ano], headers=UA, timeout=1800, stream=True, verify=False) as r:
                r.raise_for_status()
                with open(p, "wb") as fh:
                    for bloco in r.iter_content(1 << 20):
                        fh.write(bloco)
        soma = defaultdict(lambda: [0.0, 0.0])
        with open(p, encoding="utf-8", errors="replace", newline="") as fh:
            for r in csv.DictReader(fh, delimiter=";"):
                v = soma[(r["PROGRAMA"], r["ACAO"], r["SUBACAO"])]
                v[0] += float(r["VL_EMPENHADO"] or 0)
                v[1] += float(r["VL_LIQUIDADO"] or 0)
        for (pg, ac, sa), (e, l) in soma.items():
            linhas.append({"ano": ano, "programa": pg, "acao": ac, "subacao": sa, "empenhado": round(e, 2), "liquidado": round(l, 2)})
        print(ano, len(soma), "subações, empenhado R$", f"{sum(v[0] for v in soma.values()) / 1e9:.1f} bi", flush=True)
        with open(SAIDA, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, CAMPOS)
            w.writeheader()
            w.writerows(sorted(linhas, key=lambda r: (r["ano"], r["acao"], r["subacao"])))


def buscar(txt):
    por = defaultdict(dict)
    for r in csv.DictReader(open(SAIDA, encoding="utf-8")):
        if re.search(txt, r["acao"] + " " + r["subacao"], re.I):
            v = por[(r["acao"][:55], r["subacao"][:55])]
            v[r["ano"]] = v.get(r["ano"], 0) + float(r["empenhado"]) / 1e6
    for (a, s), v in sorted(por.items()):
        print(a, "|", s, "|", " ".join(f"{k}: {v[k]:,.1f}" for k in sorted(v)), "(R$ mi empenhado)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    baixar(sys.argv[2:]) if sys.argv[1] == "baixar" else buscar(sys.argv[2])

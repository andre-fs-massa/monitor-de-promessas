# Despesa do Estado de Minas Gerais por ação orçamentária, dos dados abertos da Controladoria-Geral do Estado
# (conjunto "Despesa pública", https://dados.mg.gov.br/dataset/despesa — a mesma base do Portal da Transparência de MG).
#   python -I scripts/orcamento_mg.py baixar 2022 2023 ...   -> data/interim/orcamento_mg_acoes.csv
#   python -I scripts/orcamento_mg.py buscar "regex"          -> ações cujo nome (ou código) bate, com o empenhado por ano
# Os arquivos brutos (um por ano, ~50 MB comprimidos) ficam em data/raw/mg_despesa/.
import csv, gzip, io, re, sys
from collections import defaultdict
from pathlib import Path
import requests, urllib3

RAIZ = Path(__file__).resolve().parents[1]
BRUTO = RAIZ / "data" / "raw" / "mg_despesa"
SAIDA = RAIZ / "data" / "interim" / "orcamento_mg_acoes.csv"
API = "https://dados.mg.gov.br/api/3/action/package_show?id=despesa"
CAMPOS = ["ano", "acao", "nome_acao", "unidade", "empenhado", "liquidado", "pago"]
UA = {"User-Agent": "Mozilla/5.0"}
# O servidor não envia o certificado intermediário; a consulta é de dados públicos, só leitura.
urllib3.disable_warnings()


def recursos():
    d = requests.get(API, headers=UA, timeout=120, verify=False).json()["result"]["resources"]
    return {r["url"].rsplit("/", 1)[1]: r["url"] for r in d}


def arquivo(nome, urls):
    BRUTO.mkdir(parents=True, exist_ok=True)
    p = BRUTO / nome
    if not p.exists():
        with requests.get(urls[nome], headers=UA, timeout=600, stream=True, verify=False) as r:
            r.raise_for_status()
            with open(p, "wb") as fh:
                for bloco in r.iter_content(1 << 20):
                    fh.write(bloco)
    return p


def tabela(p):
    return csv.DictReader(io.TextIOWrapper(gzip.open(p), encoding="utf-8-sig"), delimiter=";")


def num(v):
    return float(v.replace(",", ".")) if v else 0.0


def baixar(anos):
    urls = recursos()
    acoes = {r["id_acao"]: (r["cd_acao"], r["nome"]) for r in tabela(arquivo("dm_acao.csv.gz", urls))}
    uos = {}
    for r in tabela(arquivo("dm_unidade_orc.csv.gz", urls)):
        uos[r[next(k for k in r if k.startswith("id_"))]] = next((r[k] for k in r if k.startswith("nome")), "")
    linhas = []
    if SAIDA.exists():
        linhas = [r for r in csv.DictReader(open(SAIDA, encoding="utf-8")) if int(r["ano"]) not in anos]
    for ano in anos:
        soma = defaultdict(lambda: [0.0, 0.0, 0.0])
        for r in tabela(arquivo(f"ft_despesa_{ano}.csv.gz", urls)):
            v = soma[(r["id_acao"], r["id_unidade_orc"])]
            v[0] += num(r["vr_empenhado"]); v[1] += num(r["vr_liquidado"]); v[2] += num(r["vr_pago"])
        for (ia, iu), (e, l, pg) in soma.items():
            cd, nome = acoes.get(ia, ("?", "?"))
            linhas.append({"ano": ano, "acao": cd, "nome_acao": nome, "unidade": uos.get(iu, iu),
                           "empenhado": round(e, 2), "liquidado": round(l, 2), "pago": round(pg, 2)})
        print(ano, len(soma), "pares ação/unidade, empenhado R$", f"{sum(v[0] for v in soma.values()) / 1e9:.1f} bi", flush=True)
        linhas.sort(key=lambda r: (int(r["ano"]), r["acao"], r["unidade"]))
        with open(SAIDA, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, CAMPOS)
            w.writeheader()
            w.writerows(linhas)


def buscar(txt):
    por = defaultdict(dict)
    for r in csv.DictReader(open(SAIDA, encoding="utf-8")):
        if re.search(txt, r["nome_acao"], re.I) or r["acao"] == txt:
            v = por[(r["acao"], r["nome_acao"], r["unidade"])]
            v[r["ano"]] = v.get(r["ano"], 0) + float(r["empenhado"]) / 1e6
    for (a, n, u), v in sorted(por.items()):
        print(a, n[:60], "[" + u[:30] + "]", " ".join(f"{k}: {v[k]:,.1f}" for k in sorted(v)), "(R$ mi empenhado)")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1] == "baixar":
        baixar([int(x) for x in sys.argv[2:]])
    else:
        buscar(sys.argv[2])

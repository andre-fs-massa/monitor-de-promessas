"""Gera data/promessas/cabral_rj_2010.csv a partir do censo (cabral_def.py), das decisões
(cabral_decisoes.py) e do lote do Diário Oficial (cabral_rj_2010.json).

python -I data/interim/busca_oficial/gera_cabral.py
"""
import csv, json, re, runpy
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
P = runpy.run_path(str(AQUI / "cabral_def.py"))["P"]
D = runpy.run_path(str(AQUI / "cabral_decisoes.py"))["D"]
L = json.load(open(AQUI / "cabral_rj_2010.json", encoding="utf-8"))
MID = "cabral_rj_2010"


def doerj(chave, data, padrao):
    # procura primeiro nos resultados da própria promessa, depois nos das outras
    blocos = [L[chave]] + [v for k, v in L.items() if k != chave]
    for v in (q for b in blocos for q in b["ioerj"].values()):
        for i in v.get("itens", []):
            if i["data"] == data and re.search(padrao, i["resumo"], re.I):
                return re.sub(r"&tb=.*", "&tb=", i["link"])
    raise SystemExit(f"link não achado: {chave} {data} {padrao}")


assert set(D) == {p[0] for p in P}, set(D) ^ {p[0] for p in P}
campos = ["id", "mandato_id", "paragrafo", "trecho_literal", "promessa", "area", "tipo", "depende_legislativo",
          "outro_ente", "status", "confianca", "evidencia", "fonte_url", "data_evidencia"]
with open(RAIZ / "data" / "promessas" / f"{MID}.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(campos)
    for n, (k, sec, tre, pro, area, tipo, leg, ente) in enumerate(P, 1):
        status, conf, ev, fonte, data = D[k]
        if isinstance(fonte, tuple):
            fonte = doerj(k, fonte[1], fonte[2])
        w.writerow([f"{MID}-{n:03d}", MID, "", tre, pro, area, tipo, leg, ente, status, conf, ev, fonte, data])
print(len(P))

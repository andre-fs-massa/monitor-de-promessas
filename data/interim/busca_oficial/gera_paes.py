"""Gera data/promessas/paes_rio_2024.csv a partir do censo (paes_def.py) e das decisões (paes_decisoes.py).

python -I data/interim/busca_oficial/gera_paes.py
"""
import csv, runpy
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
P = runpy.run_path(str(AQUI / "paes_def.py"))["P"]
D = runpy.run_path(str(AQUI / "paes_decisoes.py"))["D"]
MID = "paes_rio_2024"

assert set(D) == {p[0] for p in P}, set(D) ^ {p[0] for p in P}
campos = ["id", "mandato_id", "paragrafo", "trecho_literal", "promessa", "area", "tipo", "depende_legislativo",
          "outro_ente", "status", "confianca", "evidencia", "fonte_url", "data_evidencia"]
with open(RAIZ / "data" / "promessas" / f"{MID}.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(campos)
    for n, (k, sec, tre, pro, area, tipo, leg, ente) in enumerate(P, 1):
        status, conf, ev, fonte, data = D[k]
        w.writerow([f"{MID}-{n:03d}", MID, sec, tre, pro, area, tipo, leg, ente, status, conf, ev, fonte, data])
print(len(P))

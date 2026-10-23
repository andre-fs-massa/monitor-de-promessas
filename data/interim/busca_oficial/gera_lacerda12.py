# Gera data/promessas/lacerda_bh_2012.csv a partir de lacerda12_def.P e lacerda12_decisoes.D.
import csv, sys
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from lacerda12_def import P
from lacerda12_decisoes import D, AJUSTES
MID = "lacerda_bh_2012"
CAMPOS = ["id","mandato_id","paragrafo","trecho_literal","promessa","area","tipo","depende_legislativo","outro_ente","status","confianca","evidencia","fonte_url","data_evidencia"]
linhas, n = [], 0
for i, p in enumerate(P, 1):
    d = D[i]
    if d is None:
        continue
    n += 1
    r = dict(zip(CAMPOS, [f"{MID}-{n:02d}", MID, "", p[0], p[1], p[2], p[3], p[4], p[5], *d]))
    for k, v in AJUSTES.get(i, {}).items():
        r["depende_legislativo" if k == "leg" else k] = v
    linhas.append(r)
with open(AQUI.parents[1] / "promessas" / f"{MID}.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, CAMPOS); w.writeheader(); w.writerows(linhas)
print(n, "promessas")

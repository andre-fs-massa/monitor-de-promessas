# Gera data/promessas/jeronimo_ba_2022.csv a partir de jeronimo22_def.P e jeronimo22_decisoes.D.
import csv, sys
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from jeronimo22_def import P
from jeronimo22_decisoes import D
MID = "jeronimo_ba_2022"
CAMPOS = ["id","mandato_id","paragrafo","trecho_literal","promessa","area","tipo","depende_legislativo","outro_ente","status","confianca","evidencia","fonte_url","data_evidencia"]
linhas = []
for i, p in enumerate(P, 1):
    linhas.append(dict(zip(CAMPOS, [f"{MID}-{i:03d}", MID, "", p[0], p[1], p[2], p[3], p[4], p[5], *D[i]])))
with open(AQUI.parents[1] / "promessas" / f"{MID}.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, CAMPOS); w.writeheader(); w.writerows(linhas)
print(len(linhas), "promessas")

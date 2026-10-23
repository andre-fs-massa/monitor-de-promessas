# Busca nos dados abertos da Alesp (normas e projetos do Governador) para cada promessa do censo do Doria (jan/2019 a 31/03/2022).
import json, sys
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(AQUI.parents[2] / "scripts"))
from doria_def import P
import busca_sp
txt = (AQUI.parents[1] / "interim" / "doria_sp_2018.txt").read_text(encoding="utf-8")
out = {}
for i, p in enumerate(P, 1):
    assert any(p[0] in l for l in txt.splitlines()), f"trecho {i} não bate"
    out[str(i)] = {"normas": busca_sp.normas(p[6], "2019-01-01", "2022-03-31"),
                   "projetos": busca_sp.projetos(p[6], "2019-01-01", "2022-03-31")}
    print(i, len(out[str(i)]["normas"]), len(out[str(i)]["projetos"]))
(AQUI / "doria_sp_2018.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

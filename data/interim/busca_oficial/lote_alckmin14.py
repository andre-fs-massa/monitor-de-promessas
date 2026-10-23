# Busca nos dados abertos da Alesp (normas e projetos do Governador) para cada promessa do censo do Alckmin 2014 (jan/2015 a 06/04/2018).
import json, sys
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(AQUI.parents[2] / "scripts"))
from alckmin14_def import P
import busca_sp
txt = (AQUI.parents[1] / "interim" / "alckmin_sp_2014.txt").read_text(encoding="utf-8")
out = {}
for i, p in enumerate(P, 1):
    assert any(p[0] in l for l in txt.splitlines()), f"trecho {i} não bate"
    out[str(i)] = {"normas": busca_sp.normas(p[6], "2015-01-01", "2018-04-06"),
                   "projetos": busca_sp.projetos(p[6], "2015-01-01", "2018-04-06")}
    print(i, len(out[str(i)]["normas"]), len(out[str(i)]["projetos"]))
(AQUI / "alckmin_sp_2014.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

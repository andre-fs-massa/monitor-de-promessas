# Busca nos dados abertos da Alesp (normas e projetos do Governador) para cada promessa do censo do Alckmin 2010 (jan/2011 a dez/2014).
import json, sys
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(AQUI.parents[2] / "scripts"))
from alckmin10_def import P
import busca_sp
txt = (AQUI.parents[1] / "interim" / "alckmin_sp_2010.txt").read_text(encoding="utf-8")
out = {}
for i, p in enumerate(P, 1):
    assert any(p[0] in l for l in txt.splitlines()), f"trecho {i} não bate"
    out[str(i)] = {"normas": busca_sp.normas(p[6], "2011-01-01", "2014-12-31"),
                   "projetos": busca_sp.projetos(p[6], "2011-01-01", "2014-12-31")}
    print(i, len(out[str(i)]["normas"]), len(out[str(i)]["projetos"]))
(AQUI / "alckmin_sp_2010.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

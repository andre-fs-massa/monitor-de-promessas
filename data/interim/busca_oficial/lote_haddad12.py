# Busca no Catálogo de Legislação Municipal de SP para cada promessa do censo do Haddad 2012 (jan/2013 a dez/2016).
import json, sys, time
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(AQUI.parents[2] / "scripts"))
from haddad12_def import P
import busca_spcapital as b
txt = (AQUI.parents[1] / "interim" / "haddad_sp_2012.txt").read_text(encoding="utf-8")
linhas = txt.splitlines()
ruins = [i for i, p in enumerate(P, 1) if not any(p[0] in l for l in linhas)]
assert not ruins, f"trechos que não batem: {ruins}"
if "--so-validar" in sys.argv:
    print("trechos OK", len(P)); sys.exit()
out = {}
for i, p in enumerate(P, 1):
    for t in range(3):
        try:
            out[str(i)] = b.catalogo(p[6], "2013-01-01", "2016-12-31"); break
        except Exception as e:
            time.sleep(5)
    print(i, len(out.get(str(i), [])), flush=True)
(AQUI / "haddad_sp_2012.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

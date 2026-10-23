# Busca no Catálogo de Legislação Municipal de SP para cada promessa do censo do Covas (jan/2021 a dez/2024).
import json, sys, time
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(AQUI.parents[2] / "scripts"))
from covas_def import P
import busca_spcapital as b
txt = (AQUI.parents[1] / "interim" / "covas_sp_2020.txt").read_text(encoding="utf-8")
linhas = txt.splitlines()
ruins = [i for i, p in enumerate(P, 1) if not any(p[0] in l for l in linhas)]
assert not ruins, f"trechos que não batem: {ruins}"
if "--so-validar" in sys.argv:
    print("trechos OK", len(P)); sys.exit()
out = {}
for i, p in enumerate(P, 1):
    for t in range(3):
        try:
            out[str(i)] = b.catalogo(p[6], "2021-01-01", "2024-12-31"); break
        except Exception as e:
            time.sleep(5)
    print(i, len(out.get(str(i), [])), flush=True)
(AQUI / "covas_sp_2020.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

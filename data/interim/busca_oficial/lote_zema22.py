# Busca na legislação mineira (API da ALMG) para cada promessa do censo do Zema 2022 (jan/2023 a 22/03/2026, renúncia).
import json, sys, time
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(AQUI.parents[2] / "scripts"))
from zema22_def import P
import busca_mg as b
txt = (AQUI.parents[1] / "interim" / "zema_mg_2022.txt").read_text(encoding="utf-8")
linhas = txt.splitlines()
ruins = [i for i, p in enumerate(P, 1) if not any(p[0] in l for l in linhas)]
assert not ruins, f"trechos que não batem: {ruins}"
out = {}
for i, p in enumerate(P, 1):
    for t in range(3):
        try:
            out[str(i)] = b.normas(p[6], "2023-01-01", "2026-03-22", 60); break
        except Exception:
            time.sleep(5)
    print(i, len(out.get(str(i), [])), flush=True)
(AQUI / "zema_mg_2022.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

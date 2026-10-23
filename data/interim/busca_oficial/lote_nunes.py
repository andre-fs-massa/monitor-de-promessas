# Busca no Catálogo de Legislação Municipal de SP para cada promessa do censo do Nunes (jan/2025 a out/2026).
import json, sys, time
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(AQUI.parents[2] / "scripts"))
from nunes_def import P
import busca_spcapital as b
txt = (AQUI.parents[1] / "interim" / "nunes_sp_2024.txt").read_text(encoding="utf-8")
out = {}
for i, p in enumerate(P, 1):
    assert any(p[0] in l for l in txt.splitlines()), f"trecho {i} não bate: {p[0][:60]}"
    for t in range(3):
        try:
            out[str(i)] = b.catalogo(p[6], "2025-01-01", "2026-10-23"); break
        except Exception as e:
            time.sleep(5)
    print(i, len(out.get(str(i), [])), flush=True)
(AQUI / "nunes_sp_2024.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

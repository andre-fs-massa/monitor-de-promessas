"""Acrescenta promessas do censo completo ao CSV de um mandato.

Uso (na raiz do projeto): python -I scripts/censo_add.py <mandato_id> <arquivo_novas.py>
O arquivo de novas define N = [ (paragrafo, trecho, promessa, area, tipo, leg, ente,
status, confianca, evidencia, fonte_url, data), ... ] e ESPERADO (nº de linhas atuais).
"""
import csv
import runpy
import sys
from pathlib import Path

mid, arq_novas = sys.argv[1], sys.argv[2]
cfg = runpy.run_path(arq_novas)
ARQ = Path("data/promessas") / f"{mid}.csv"
with ARQ.open(encoding="utf-8", newline="") as f:
    linhas = list(csv.DictReader(f))
campos = list(linhas[0])
assert len(linhas) == cfg["ESPERADO"], f"CSV tem {len(linhas)} linhas, esperado {cfg['ESPERADO']}"
for i, t in enumerate(cfg["N"], start=len(linhas) + 1):
    assert len(t) == 12, t
    linhas.append(dict(zip(campos, [f"{mid}-{i:02d}", mid, *t])))
with ARQ.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=campos)
    w.writeheader()
    w.writerows(linhas)
print(mid, len(linhas), "promessas")

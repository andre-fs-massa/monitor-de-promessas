# Gera data/impacto_fiscal/<mandato>.csv a partir de data/interim/impacto_rj/<mandato>_imp.py (dicionário I).
# I[n] = (categoria, incremental, total, ano_ref, acumulado, periodo, recorrente, confianca, explicacao, fonte_oficial, fonte_comparacao)
import csv, importlib, sys
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
CAMPOS = ["id", "impacto_fiscal", "valor_incremental_rs_bi", "valor_total_rs_bi", "ano_ref", "valor_acumulado_rs_bi",
          "periodo_acumulado", "compensacao_rs_bi", "recorrente", "confianca", "explicacao", "fonte_oficial", "fonte_comparacao"]
for mid in sys.argv[1:]:
    I = importlib.import_module(f"{mid}_imp").I
    ids = [r["id"] for r in csv.DictReader(open(AQUI.parents[1] / "promessas" / f"{mid}.csv", encoding="utf-8"))]
    assert len(ids) == len(I), (mid, len(ids), len(I))
    linhas = []
    for n, pid in enumerate(ids, 1):
        cat, inc, tot, ano, acu, per, rec, conf, exp, fo, fc = I[n]
        f = lambda v: "" if v in (None, "") else (f"{v:.3f}".rstrip("0").rstrip(".") if isinstance(v, float) else str(v))
        linhas.append(dict(zip(CAMPOS, [pid, cat, f(inc), f(tot), ano, f(acu), per, "", rec, conf, exp, fo, fc])))
    with open(AQUI.parents[1] / "impacto_fiscal" / f"{mid}.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, CAMPOS); w.writeheader(); w.writerows(linhas)
    print(mid, len(linhas))

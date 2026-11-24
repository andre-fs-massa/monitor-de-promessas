# Gera <saida>_def.py a partir de uma spec (início da linha -> trecho literal) e valida unicidade.
# Uso: python -I gera_def.py <spec.py> <texto.txt> <saida_def.py> <cabecalho>
import re, sys, unicodedata, importlib.util
spec_path, txt, saida, cab = sys.argv[1:5]
sp = importlib.util.spec_from_file_location("spec", spec_path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
L = open(txt, encoding="utf-8").read().split("\n")
T = re.sub(r"\s+", " ", unicodedata.normalize("NFC", "\n".join(L)))
n = lambda s: re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()
out = [f"# {c}" for c in cab.split("|")] + ["# (trecho_literal, promessa, area, tipo, depende_legislativo, outro_ente)", "P = ["]
bad = []
for pre, *rest in m.S:
    hits = [l for l in L if l.startswith(pre)]
    if len(hits) != 1:
        bad.append((pre, len(hits))); continue
    t = hits[0] if len(hits[0]) <= 150 else hits[0][:150].rsplit(" ", 1)[0]
    t = t.rstrip(" ,;:.")
    if T.count(n(t)) != 1:
        bad.append((pre, "conta", T.count(n(t)))); continue
    out.append("    (%r,\n     %r, %r, %r, %r, %r)," % (t, *rest))
out.append("]")
open(saida, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(len(m.S), "spec;", len(out) - 3 - cab.count("|"), "ok; problemas:", bad)

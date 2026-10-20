"""Mostra os resultados do lote do DO Rio de uma promessa: python -I ver_crivella.py <chave> [max_itens] [max_chars]"""
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open(__file__.replace("ver_crivella.py", "crivella_rio_2016.json"), encoding="utf-8"))
n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
c = int(sys.argv[3]) if len(sys.argv) > 3 else 350
for q, r in d.get(sys.argv[1], {}).items():
    print("==", q, "|", r.get("erro") or f"{r['total']} -> {len(r['itens'])}")
    for i in r.get("itens", [])[:n]:
        print(" ", i["data"], i["link"])
        for t in i["trechos"][:2]:
            print("     ..", t[:c])

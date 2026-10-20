"""Busca no DO Rio e mostra trechos em volta de uma expressão regular:
python -I dorio_trecho.py '<frase>' '<regex>' [paginas] [de]"""
import json, re, sys, urllib.parse, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
frase, rx = sys.argv[1], sys.argv[2]
pags = int(sys.argv[3]) if len(sys.argv) > 3 else 3
de = sys.argv[4] if len(sys.argv) > 4 else "2025-01-01"
for n in range(pags):
    url = f"https://doweb.rio.rj.gov.br/busca/busca/buscar/query/{n}/di:{de}/?1=1&q=" + urllib.parse.quote(frase)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=120).read())
    for h in d["hits"]["hits"]:
        s = h["_source"]; t = re.sub(r"\s+", " ", s["conteudo"])
        for m in list(re.finditer(rx, t, re.I))[:2]:
            print(s["data"], f"https://doweb.rio.rj.gov.br/portal/edicoes/download/{s['diario_id']}/{s['pagina']}")
            print("   ..", t[max(0, m.start() - 300):m.end() + 400])
    if (n + 1) * 10 >= d["hits"]["total"]:
        break

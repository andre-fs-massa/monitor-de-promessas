"""Lote de buscas na Câmara (proposições do Poder Executivo) para promessas dos presidentes que dependem de lei.

python -I data/interim/busca_oficial/lote_presidentes.py  -> presidentes_camara.json
"""
import json, runpy, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
B = runpy.run_path(str(AQUI.parents[2] / "scripts" / "busca_br.py"))

A10, A14, A22 = ["2011", "2012", "2013", "2014"], ["2015", "2016"], ["2023", "2024", "2025", "2026"]
LOTE = {
    "lula_2022-42": [("justiça gratuita trabalho", A22), ("honorários sucumbência trabalhista", A22)],
    "dilma_2010-24": [("cultivares", A10)],
    "dilma_2010-25": [("CTNBio", A10), ("biossegurança", A10)],
    "dilma_2010-32": [("planos de saúde hospitais públicos", A10), ("dupla porta", A10)],
    "dilma_2010-36": [("carreira Ministério da Defesa", A10)],
    "dilma_2014-02": [("Simples Nacional", A14)],
    "dilma_2014-30": [("Sistema Nacional do Esporte", A14)],
}
saida = {}
for chave, consultas in LOTE.items():
    saida[chave] = []
    for termos, anos in consultas:
        try:
            r = B["camara"](termos, anos, executivo=True)
        except Exception as e:
            r = [{"erro": str(e)}]
        saida[chave].append({"termos": termos, "anos": anos, "executivo": r})
        print(chave, termos, len(r), file=sys.stderr)
json.dump(saida, open(AQUI / "presidentes_camara.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

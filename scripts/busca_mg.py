"""Busca na legislação mineira pela API de dados abertos da Assembleia de Minas (ALMG).

Uso como módulo:
    import busca_mg
    busca_mg.normas("Trilhas de Futuro", "2023-01-01", "2026-03-22")
    -> lista de (data, norma, ementa, url)

Parâmetros da API (descobertos na documentação Swagger em /api/ajuda/swagger/endpoints/lastest):
  ass = termos (busca em ementa, indexação, assunto, apelido, resumo e texto), ini/fim = período (aaaammdd),
  tp = tamanho da página, p = página. Cobre leis, decretos e demais normas estaduais.
"""
import json
import sys
import urllib.parse
import urllib.request

BASE = "https://dadosabertos.almg.gov.br/api/v2/legislacao/mineira/pesquisa/direcionada"


def normas(termo, de, ate, limite=100):
    out, p = [], 1
    while len(out) < limite:
        q = urllib.parse.urlencode({"tp": 50, "p": p, "formato": "json", "ass": termo,
                                    "ini": de.replace("-", ""), "fim": ate.replace("-", "")})
        req = urllib.request.Request(f"{BASE}?{q}", headers={"User-Agent": "Mozilla/5.0"})
        d = json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8"))["resultado"]
        itens = d.get("listaItem") or []
        for i in itens:
            data = i.get("data", "")
            data = f"{data[:4]}-{data[4:6]}-{data[6:]}" if len(data) == 8 else data
            url = f"https://www.almg.gov.br/legislacao-mineira/texto/{i.get('tipo','')}/{i.get('numero','')}/{i.get('ano','')}/"
            out.append((data, i.get("norma", ""), " ".join((i.get("ementa") or "").split()), url))
        if len(itens) < 50 or p * 50 >= d.get("noOcorrencias", 0):
            break
        p += 1
    return out[:limite]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for r in normas(sys.argv[1], sys.argv[2], sys.argv[3]):
        print(" | ".join(r))

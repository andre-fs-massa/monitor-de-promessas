"""Busca no Catálogo de Legislação Municipal da Prefeitura de São Paulo (legislacao.prefeitura.sp.gov.br).

  python -I scripts/busca_spcapital.py "<termo>" [--de 2025-01-01] [--ate 2026-12-31] [--tipos LEI,DECRETO,PORTARIA]

O catálogo reúne leis, decretos, portarias e outros atos publicados no Diário Oficial da Cidade, com ementa
e link. Não há API: a página de busca aceita POST com o termo (assunto), período, tipos e limite de resultados.
Conta como consulta ao Diário Oficial para a regra "sem registro = confiança média".
"""
import argparse
import html
import re
import urllib.parse
import urllib.request

BASE = "https://legislacao.prefeitura.sp.gov.br"
MESES = {m: i for i, m in enumerate(["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
                                     "setembro", "outubro", "novembro", "dezembro"], 1)}
TIPOS_PADRAO = ("LEI", "DECRETO", "PORTARIA", "PORTARIA INTERSECRETARIAL", "PORTARIA CONJUNTA", "RESOLUÇÃO")


def _data(titulo):
    m = re.search(r"de (\d{1,2}) de (\w+) de (\d{4})", titulo, re.I)
    if not m or m.group(2).lower() not in MESES:
        return ""
    return f"{m.group(3)}-{MESES[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"


def catalogo(termo, de="2025-01-01", ate="2026-12-31", tipos=TIPOS_PADRAO, limite=100):
    """Lista (data, título, ementa, url) dos atos cujo texto contém o termo, no período."""
    d1 = "/".join(reversed(de.split("-")))
    d2 = "/".join(reversed(ate.split("-")))
    campos = [("limite", str(limite)), ("ano-inicial", d1), ("ano-final", d2)] + [("tipo[]", t) for t in tipos]
    url = f"{BASE}/busca?assunto={urllib.parse.quote(termo)}"
    req = urllib.request.Request(url, data=urllib.parse.urlencode(campos).encode(), headers={"User-Agent": "Mozilla/5.0"})
    pagina = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "ignore")
    achou = []
    for href, tit, eme in re.findall(r'<div class="bx-resultado">\s*<a href="([^"]+)">\s*<h4>(.*?)</h4>\s*<p>(.*?)</p>', pagina, re.S):
        tit, eme = html.unescape(tit).strip(), html.unescape(re.sub("<[^>]+>", "", eme)).strip()
        data = _data(tit)
        if data and not (de <= data <= ate):
            continue
        achou.append((data, tit, eme, BASE + href))
    return sorted(achou)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("termo")
    ap.add_argument("--de", default="2025-01-01")
    ap.add_argument("--ate", default="2026-12-31")
    ap.add_argument("--tipos", default=",".join(TIPOS_PADRAO))
    a = ap.parse_args()
    for r in catalogo(a.termo, a.de, a.ate, a.tipos.split(",")):
        print(" | ".join(r))

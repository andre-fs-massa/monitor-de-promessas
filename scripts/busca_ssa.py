"""Busca no Diário Oficial do Município de Salvador (DOM) e nas notícias do site da Prefeitura.

Uso como módulo:
    import busca_ssa
    busca_ssa.dom("Casa Girassol", "2025-01-01", "2026-11-23")
    -> lista de (data, título, trecho, url)
    busca_ssa.noticias("Casa Girassol", "2025-01-01", "2026-11-23")
    -> lista de (data, título, resumo, url)

Uso em lote (gera um JSON com os resultados de cada promessa de um arquivo *_def.py):
    python -I scripts/busca_ssa.py lote <modulo_def> <de> <ate> <saida.json>
    python -I scripts/busca_ssa.py lote bruno24_def 2025-01-01 2026-11-23 data/interim/busca_oficial/bruno_ssa_2024.json

Fontes (sem documentação pública; parâmetros lidos do código das páginas):
  - DOM: https://dom.salvador.ba.gov.br/diario/busca?q=...&data_inicio=...&data_fim=... devolve a página com
    os resultados em JSON no atributo data-page (busca em texto completo nos atos e nas edições antigas).
  - Notícias: API do WordPress do site da Prefeitura, /wp-json/wp/v2/posts?search=...&after=...&before=...
"""
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130", "Accept": "text/html"}
DOM = "https://dom.salvador.ba.gov.br/diario/busca"
WP = "https://www.salvador.ba.gov.br/wp-json/wp/v2/posts"


def _get(url, tentativas=6):
    for i in range(tentativas):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read().decode("utf-8")
        except Exception as e:
            if i == tentativas - 1:
                raise
            # 429 = muitas consultas seguidas: o DOM limita a taxa, então espera mais a cada tentativa
            time.sleep(30 * (i + 1) if getattr(e, "code", None) == 429 else 3)


def _limpa(t):
    return " ".join(re.sub(r"<[^>]+>", "", html.unescape(t or "")).split())


def dom(termo, de, ate, limite=10):
    q = urllib.parse.urlencode({"q": termo, "data_inicio": de, "data_fim": ate})
    s = _get(f"{DOM}?{q}")
    m = re.search(r'data-page="([^"]*)"', s)
    if not m:
        return []
    pubs = json.loads(html.unescape(m.group(1)))["props"].get("publicacoes") or {}
    out = []
    for p in pubs.get("data", [])[:limite]:
        pl = p.get("payload") or {}
        data = pl.get("data_publicacao") or pl.get("data_edicao") or ""
        if p.get("tipo") == "publicacao":
            url = f"https://dom.salvador.ba.gov.br/diario/{p.get('id')}"
        else:
            url = pl.get("url", "")
        out.append((data, _limpa(p.get("titulo")), _limpa(p.get("snippet"))[:300], url))
    return out


def noticias(termo, de, ate, limite=10):
    q = urllib.parse.urlencode({"search": termo, "after": f"{de}T00:00:00", "before": f"{ate}T23:59:59",
                                "per_page": limite, "_fields": "date,link,title,excerpt"})
    try:
        d = json.loads(_get(f"{WP}?{q}"))
    except Exception:
        return []
    return [(i["date"][:10], _limpa(i["title"]["rendered"]), _limpa(i["excerpt"]["rendered"])[:300], i["link"])
            for i in d]


def lote(modulo, de, ate, saida, ini=1, fim=10**6):
    """ini/fim (opcionais) limitam a faixa de promessas, para rodar vários processos em paralelo."""
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "data" / "interim" / "busca_oficial"))
    P = __import__(modulo).P
    res = json.loads(Path(saida).read_text(encoding="utf-8")) if Path(saida).exists() else {}
    for i, p in enumerate(P, 1):
        if str(i) in res or not int(ini) <= i <= int(fim):
            continue
        termo = p[6]
        res[str(i)] = {"promessa": p[1], "termo": termo, "dom": dom(termo, de, ate), "noticias": noticias(termo, de, ate)}
        Path(saida).write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        print(i, termo, len(res[str(i)]["dom"]), len(res[str(i)]["noticias"]), flush=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1] == "lote":
        lote(*sys.argv[2:8])
    else:
        fn = {"dom": dom, "noticias": noticias}[sys.argv[1]]
        for r in fn(sys.argv[2], sys.argv[3], sys.argv[4]):
            print(" | ".join(r))

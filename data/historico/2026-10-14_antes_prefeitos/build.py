"""Valida a base de promessas e gera a base aberta e os dados da interface.

Uso:
    python -I scripts/build.py            # valida e gera
    python -I scripts/build.py --links    # também testa se cada fonte_url responde

Validações:
- cada linha tem todas as colunas e um status/confiança válidos;
- o trecho_literal aparece no texto extraído do plano (ignorando quebras de linha);
- toda promessa avaliada tem fonte_url, exceto nao_cumprida por falta de registro
  (confiança baixa), em que `evidencia` descreve a busca feita.

A página de cada trecho no PDF é calculada aqui e gravada na coluna `pagina`.

Saídas:
- data/base_aberta/promessas.csv e promessas.json (todas as promessas, todos os mandatos)
- web/data.js (dados consumidos pela interface)
"""
import csv
import json
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARGOS = {"presidente", "governador"}
STATUS = ["cumprida", "parcialmente_cumprida", "nao_cumprida", "em_andamento", "interrompida", "nao_avaliada"]
CONFIANCA = {"alta", "media", "baixa"}
OUTROS_ENTES = {"", "União", "Estados", "Municípios", "Estados e municípios"}
CAMPOS = ["id", "mandato_id", "paragrafo", "trecho_literal", "promessa", "area", "tipo",
          "depende_legislativo", "outro_ente", "status", "confianca", "evidencia", "fonte_url", "data_evidencia"]


def normaliza(texto: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", texto)).strip()


def localiza_pagina(trecho: str, paginas: list[str]) -> int | None:
    """Página (1-based) onde o trecho começa; considera trechos que cruzam a quebra de página."""
    inicio = trecho[:60]
    for i, pg in enumerate(paginas):
        proxima = paginas[i + 1] if i + 1 < len(paginas) else ""
        pos = f"{pg} {proxima}".find(inicio)
        if 0 <= pos < len(pg):
            return i + 1
    return None


def ler_csv(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def testa_link(url: str) -> int | str:
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except Exception as e:  # noqa: BLE001 - relatório, não fluxo de controle
        return getattr(e, "code", type(e).__name__)


def main(checar_links: bool) -> None:
    mandatos = ler_csv(ROOT / "data" / "mandatos.csv")
    erros: list[str] = []
    promessas: list[dict] = []

    for mand in mandatos:
        if mand["cargo"] not in CARGOS:
            erros.append(f"{mand['id']}: cargo inválido '{mand['cargo']}'")
        bruto = (ROOT / mand["texto_extraido"]).read_text(encoding="utf-8")
        texto = normaliza(bruto)
        paginas = [normaliza(pg) for pg in bruto.split("")]
        linhas = ler_csv(ROOT / "data" / "promessas" / f"{mand['id']}.csv")
        for p in linhas:
            if None in p or set(p) != set(CAMPOS):
                erros.append(f"{p.get('id')}: colunas inválidas")
                continue
            if p["status"] not in STATUS:
                erros.append(f"{p['id']}: status inválido '{p['status']}'")
            if p["mandato_id"] != mand["id"]:
                erros.append(f"{p['id']}: mandato_id diferente do arquivo")
            if p["depende_legislativo"] not in {"sim", "nao"}:
                erros.append(f"{p['id']}: depende_legislativo deve ser 'sim' ou 'nao'")
            if p["outro_ente"] not in OUTROS_ENTES:
                erros.append(f"{p['id']}: outro_ente inválido '{p['outro_ente']}'")
            if p["confianca"] not in CONFIANCA:
                erros.append(f"{p['id']}: confiança inválida '{p['confianca']}'")
            trecho = normaliza(p["trecho_literal"])
            if trecho not in texto:
                erros.append(f"{p['id']}: trecho_literal não encontrado no plano")
            p["pagina"] = localiza_pagina(trecho, paginas)
            # sem registro: confiança baixa (só imprensa) ou média (também Diário Oficial ou Assembleia)
            sem_registro = p["status"] == "nao_cumprida" and p["confianca"] in ("baixa", "media")
            if p["status"] != "nao_avaliada" and not p["fonte_url"] and not sem_registro:
                erros.append(f"{p['id']}: promessa avaliada sem fonte_url")
            if sem_registro and not p["fonte_url"] and not p["evidencia"]:
                erros.append(f"{p['id']}: sem fonte_url, a evidência precisa descrever a busca feita")
            promessas.append(p)

    if checar_links:
        for p in promessas:
            if p["fonte_url"]:
                status = testa_link(p["fonte_url"])
                if status != 200:
                    print(f"  link {p['id']}: {status} {p['fonte_url']}")

    if erros:
        print("Erros de validação:")
        for e in erros:
            print("  -", e)
        sys.exit(1)

    base = ROOT / "data" / "base_aberta"
    base.mkdir(parents=True, exist_ok=True)
    with (base / "promessas.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS + ["pagina"])
        w.writeheader()
        w.writerows(promessas)
    (base / "promessas.json").write_text(
        json.dumps(promessas, ensure_ascii=False, indent=2), encoding="utf-8")

    dados = {"status": STATUS, "mandatos": mandatos, "promessas": promessas}
    (ROOT / "web" / "data.js").write_text(
        "window.DADOS = " + json.dumps(dados, ensure_ascii=False) + ";\n", encoding="utf-8")

    print(f"OK: {len(mandatos)} mandato(s), {len(promessas)} promessas validadas.")


if __name__ == "__main__":
    main("--links" in sys.argv)

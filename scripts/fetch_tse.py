"""Baixa os planos de governo do TSE e extrai o texto de um candidato.

Uso:
    python -I scripts/fetch_tse.py <ano> <uf> <sq_candidato> <saida>
    python -I scripts/fetch_tse.py 2022 BR 280001607829 lula_2022
    python -I scripts/fetch_tse.py 2022 RJ 190001615753 castro_rj_2022

<uf> é BR para presidente ou a sigla do estado para governador. Baixa
proposta_governo_<ano>_<uf>.zip do portal de dados abertos do TSE, extrai os
PDFs em data/raw/tse/<ano>/pdf_<uf> e gera o texto do candidato indicado
(SQ_CANDIDATO) em data/interim/<saida>.txt via pdftotext.
"""
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = "https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_{ano}_{uf}.zip"


def main(ano: str, uf: str, sq_candidato: str, saida: str) -> None:
    uf = uf.upper()
    raw = ROOT / "data" / "raw" / "tse" / ano
    raw.mkdir(parents=True, exist_ok=True)
    zip_path = raw / f"proposta_governo_{ano}_{uf}.zip"
    if not zip_path.exists():
        url = URL.format(ano=ano, uf=uf)
        print(f"Baixando {url}")
        urllib.request.urlretrieve(url, zip_path)

    pdf_dir = raw / f"pdf_{uf.lower()}"
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(pdf_dir)

    matches = list(pdf_dir.rglob(f"*{sq_candidato}*.pdf"))
    if not matches:
        sys.exit(f"PDF do candidato {sq_candidato} não encontrado em {pdf_dir}")

    interim = ROOT / "data" / "interim"
    interim.mkdir(parents=True, exist_ok=True)
    txt = interim / f"{saida}.txt"
    subprocess.run(["pdftotext", "-enc", "UTF-8", str(matches[0]), str(txt)], check=True)
    print(f"Texto extraído: {txt}")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    main(*sys.argv[1:])

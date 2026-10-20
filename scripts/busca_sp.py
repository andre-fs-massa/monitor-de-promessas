"""Busca em fontes oficiais de São Paulo (dados abertos da Alesp).

  python scripts/busca_sp.py baixar
  python scripts/busca_sp.py normas "<regex na ementa>" [--de 2023-01-01] [--ate 2026-12-31] [--tipo lei|lc|decreto]
  python scripts/busca_sp.py projetos "<regex na ementa>" [--de ...] [--ate ...]   (só autoria do Governador)

`normas` procura no acervo de legislação estadual da Alesp (leis, leis complementares, decretos e
outras normas, com a data e o link da ficha), arquivo legislacao_normas.zip do portal de dados abertos
(https://www.al.sp.gov.br/dados-abertos/). `projetos` procura nas proposituras da Alesp (desde 2004) as de
autoria do Governador (proposituras.zip + documento_autor.zip). A busca ignora acentos e maiúsculas.
"""
import argparse, io, re, sys, unicodedata, urllib.request, zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "data" / "raw" / "alesp"
URL_NORMAS = "https://www.al.sp.gov.br/repositorioDados/legislacao/legislacao_normas.zip"
URL_PL = "https://www.al.sp.gov.br/repositorioDados/processo_legislativo/{}.zip"
TIPOS = {"2": "Lei Complementar", "3": "Decreto", "9": "Lei"}
FILTRO = {"lei": "9", "lc": "2", "decreto": "3"}


def _sa(t):
    return unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()


def baixar():
    RAW.mkdir(parents=True, exist_ok=True)
    dados = urllib.request.urlopen(urllib.request.Request(URL_NORMAS, headers={"User-Agent": "Mozilla/5.0"}), timeout=300).read()
    (RAW / "legislacao_normas.zip").write_bytes(dados)
    for nome in ("proposituras", "documento_autor"):
        d = urllib.request.urlopen(urllib.request.Request(URL_PL.format(nome), headers={"User-Agent": "Mozilla/5.0"}), timeout=300).read()
        (RAW / f"{nome}.zip").write_bytes(d)
    print("ok")


_CACHE = {}


def _xml(nome):
    if nome not in _CACHE:
        with zipfile.ZipFile(RAW / f"{nome}.zip") as z:
            _CACHE[nome] = ET.fromstring(z.read(f"{nome}.xml"))
    return _CACHE[nome]


def normas(padrao, de="", ate="9999", tipo=None):
    rx = re.compile(_sa(padrao))
    achou = []
    for n in _xml("legislacao_normas"):
        data = (n.findtext("Data") or "")[:10]
        if not (de <= data <= ate) or (tipo and n.findtext("IdTipo") != FILTRO[tipo]):
            continue
        if rx.search(_sa(n.findtext("Ementa"))):
            achou.append((data, TIPOS.get(n.findtext("IdTipo"), "Norma " + (n.findtext("IdTipo") or "")),
                          n.findtext("Numero"), n.findtext("Ementa"), n.findtext("URLFicha")))
    return sorted(set(achou))


def projetos(padrao, de="", ate="9999"):
    rx = re.compile(_sa(padrao))
    if "gov" not in _CACHE:
        _CACHE["gov"] = {a.findtext("IdDocumento") for a in _xml("documento_autor") if a.findtext("NomeAutor") == "Governador"}
    gov = _CACHE["gov"]
    achou = set()
    for p in _xml("proposituras"):
        data = (p.findtext("DtPublicacao") or "")[:10]
        if p.findtext("IdDocumento") in gov and de <= data <= ate and rx.search(_sa(p.findtext("Ementa"))):
            achou.add((data, p.findtext("IdNatureza"), p.findtext("NroLegislativo"), p.findtext("AnoLegislativo"),
                       p.findtext("Ementa"), "https://www.al.sp.gov.br/propositura/?id=" + p.findtext("IdDocumento")))
    return sorted(achou)


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["baixar", "normas", "projetos"])
    ap.add_argument("padrao", nargs="?")
    ap.add_argument("--de", default="")
    ap.add_argument("--ate", default="9999")
    ap.add_argument("--tipo", choices=list(FILTRO))
    a = ap.parse_args()
    if a.cmd == "baixar":
        baixar()
    elif a.cmd == "projetos":
        for data, nat, num, ano, ementa, url in projetos(a.padrao, a.de, a.ate):
            print(f"{data} | natureza {nat} nº {num}/{ano} | {ementa[:220]} | {url}")
    else:
        for data, tp, num, ementa, url in normas(a.padrao, a.de, a.ate, a.tipo):
            print(f"{data} | {tp} {num} | {ementa[:220]} | {url}")

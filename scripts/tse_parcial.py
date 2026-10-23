"""Extrai um único PDF de um zip de planos do TSE sem baixar o pacote inteiro (requisições HTTP com Range).

Uso:
    python -I scripts/tse_parcial.py <ano> <uf> <trecho_do_nome> <saida.pdf>
    python -I scripts/tse_parcial.py 2024 SP 250002098117 data/raw/tse/2024/pdf_sp/nunes.pdf
    python -I scripts/tse_parcial.py 2024 SP --listar 250002098117    (só lista os arquivos que batem)

Útil para os pacotes municipais, que passam de 1 GB (ex.: proposta_governo_2024_SP.zip).
"""
import io
import sys
import urllib.request
import zipfile
from pathlib import Path

URL = "https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_{ano}_{uf}.zip"


class HttpArquivo(io.RawIOBase):
    """Arquivo somente leitura e com seek, lido sob demanda por HTTP Range."""

    def __init__(self, url):
        self.url, self.pos = url, 0
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
        self.tam = int(urllib.request.urlopen(req, timeout=60).headers["Content-Length"])

    def seekable(self):
        return True

    def readable(self):
        return True

    def seek(self, off, whence=0):
        self.pos = {0: off, 1: self.pos + off, 2: self.tam + off}[whence]
        return self.pos

    def tell(self):
        return self.pos

    def read(self, n=-1):
        if n is None or n < 0:
            n = self.tam - self.pos
        if n == 0 or self.pos >= self.tam:
            return b""
        fim = min(self.pos + n, self.tam) - 1
        req = urllib.request.Request(self.url, headers={"User-Agent": "Mozilla/5.0", "Range": f"bytes={self.pos}-{fim}"})
        dados = urllib.request.urlopen(req, timeout=300).read()
        self.pos += len(dados)
        return dados

    def readinto(self, b):
        d = self.read(len(b))
        b[: len(d)] = d
        return len(d)


def main(ano, uf, alvo, saida):
    z = zipfile.ZipFile(io.BufferedReader(HttpArquivo(URL.format(ano=ano, uf=uf.upper())), buffer_size=1 << 20))
    nomes = [n for n in z.namelist() if alvo in n]
    if saida == "--listar" or len(nomes) != 1:
        print("\n".join(nomes) or "nenhum arquivo encontrado")
        return
    Path(saida).parent.mkdir(parents=True, exist_ok=True)
    Path(saida).write_bytes(z.read(nomes[0]))
    print(f"{nomes[0]} -> {saida}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) == 4 and a[2] == "--listar":
        main(a[0], a[1], a[3], "--listar")
    elif len(a) == 4:
        main(*a)
    else:
        sys.exit(__doc__)

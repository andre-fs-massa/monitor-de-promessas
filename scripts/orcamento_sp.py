# Despesa do Estado de São Paulo por programa e ação orçamentária, do Portal da Transparência do Estado
# (consulta "Despesas", https://www.transparencia.sp.gov.br/Despesas; a base começa em 2020).
#   python -I scripts/orcamento_sp.py baixar 2022 2023 ...   -> data/interim/orcamento_sp_acoes.csv
#   python -I scripts/orcamento_sp.py buscar "regex"          -> ações cujo nome (ou programa) bate, com o empenhado por ano
# Valores em reais: dotação atual, empenhado, liquidado e pago, por ação (soma de todos os órgãos).
import csv, re, sys, time
from pathlib import Path
import requests, urllib3

BASE = "https://www.transparencia.sp.gov.br/Despesas"
RAIZ = Path(__file__).resolve().parents[1]
SAIDA = RAIZ / "data" / "interim" / "orcamento_sp_acoes.csv"
CAMPOS = ["ano", "programa", "nome_programa", "acao", "nome_acao", "dotacao_atual", "empenhado", "liquidado", "pago"]
# O servidor não envia o certificado intermediário; a consulta é de dados públicos, só leitura.
urllib3.disable_warnings()


def sessao():
    s = requests.Session()
    s.headers["User-Agent"] = "Mozilla/5.0"
    s.verify = False
    s.get(BASE, timeout=60)
    return s


def consulta(s, **filtro):
    p = dict(tipoRetorno="programa", page=1, pageSize=1000, totalItens=0, **filtro)
    for tentativa in range(4):
        try:
            r = s.post(BASE + "/Buscar", json=p, timeout=180)
            r.raise_for_status()
            d = r.json()
            assert not d.get("hasNext"), "mais de uma página"
            return d["items"]
        except (requests.RequestException, ValueError):
            time.sleep(5 * (tentativa + 1))
    raise RuntimeError(f"falhou: {filtro}")


def chave(r):
    return tuple(int(r[k]) if str(r[k]).lstrip("-").isdigit() else -1 for k in ("ano", "programa", "acao"))


def baixar(anos):
    from concurrent.futures import ThreadPoolExecutor
    todas = []
    if SAIDA.exists():
        todas = [r for r in csv.DictReader(open(SAIDA, encoding="utf-8")) if int(r["ano"]) not in anos]
    for ano in anos:
        s = sessao()
        progs = consulta(s, anoExercicio=ano)

        def acoes(pg):
            # uma sessão por consulta: as threads não dividem a mesma conexão
            return pg, consulta(sessao(), anoExercicio=ano, codPrograma=pg["cod_programa"])

        n = 0
        with ThreadPoolExecutor(8) as ex:
            for pg, lista in ex.map(acoes, progs):
                for a in lista:
                    todas.append({"ano": ano, "programa": pg["cod_programa"], "nome_programa": pg["nome_programa"],
                                  "acao": a["cod_acao"], "nome_acao": a["nome_acao"], "dotacao_atual": a["vl_dotacao_atual"],
                                  "empenhado": a["vl_empenhado"], "liquidado": a["vl_liquidado"], "pago": a["vl_pago"]})
                    n += 1
        tot = sum(p["vl_empenhado"] or 0 for p in progs) / 1e9
        print(ano, len(progs), "programas,", n, "ações, empenhado R$", f"{tot:.1f} bi", flush=True)
        todas.sort(key=chave)
        with open(SAIDA, "w", encoding="utf-8", newline="") as fh:  # grava a cada ano
            w = csv.DictWriter(fh, CAMPOS)
            w.writeheader()
            w.writerows(todas)


def buscar(txt):
    por = {}
    for r in csv.DictReader(open(SAIDA, encoding="utf-8")):
        if re.search(txt, r["nome_acao"] + " | " + r["nome_programa"], re.I) or r["acao"] == txt:
            por.setdefault((r["acao"], r["nome_acao"], r["nome_programa"]), {})[r["ano"]] = float(r["empenhado"] or 0) / 1e6
    for (a, n, pg), v in sorted(por.items()):
        print(a, n[:55], "[" + pg[:35] + "]", " ".join(f"{k}: {v[k]:,.1f}" for k in sorted(v)), "(R$ mi empenhado)")


if __name__ == "__main__":
    if sys.argv[1] == "baixar":
        baixar([int(x) for x in sys.argv[2:]])
    else:
        buscar(sys.argv[2])

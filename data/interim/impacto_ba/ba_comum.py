# Funções comuns do impacto fiscal dos governadores da Bahia.
# Fonte oficial: despesa EMPENHADA por ação, dados abertos do Estado (conjunto "Despesas", FIPLAN/Sefaz — a mesma
# base do Portal da Transparência da Bahia), agregada por scripts/orcamento_ba.py em data/interim/orcamento_ba_acoes.csv.
# A série começa em 2013.
import csv
from collections import defaultdict
from pathlib import Path

FONTE = "https://dados.ba.gov.br/dataset/despesas"
NI = "; não implementada."
DA, DR, RA, RR = "despesa_aumenta", "despesa_reduz", "receita_aumenta", "receita_reduz"
SID, NEU, SIP, SVP = "sem_impacto_direto", "neutro", "sem_impacto_primario", "sem_valor_proprio"

_EMP = defaultdict(lambda: defaultdict(float))
for _r in csv.DictReader(open(Path(__file__).resolve().parents[1] / "orcamento_ba_acoes.csv", encoding="utf-8")):
    _EMP[_r["acao"]][int(_r["ano"])] += float(_r["empenhado"])


def emp(acoes, ano):
    return sum(_EMP[a][ano] for a in acoes) / 1e9


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


def mi(x):
    return f"R$ {x * 1000:,.0f} milhões".replace(",", ".") if x < 1 else f"R$ {x:.2f} bi".replace(".", ",")


def serie(acoes, base, fim):
    return ", ".join(f"{mi(emp(acoes, a))} em {a}" for a in range(base, fim + 1))


def v(acoes, base, fim, txt, conf="media", rec="sim", inicio=None):
    """Valor a mais no último ano (fim) e acumulado ano a ano contra o ano-base. Se o gasto no fim ficou abaixo do
    ano-base, fica só o custo do último ano. inicio = primeiro ano do mandato (padrão base+1)."""
    inicio = inicio or base + 1
    b = emp(acoes, base)
    tot = round(emp(acoes, fim), 3)
    inc = round(tot - b, 3)
    acu = round(sum(emp(acoes, a) - b for a in range(inicio, fim + 1)), 3)
    nums = f" Ações {', '.join(acoes)}: {serie(acoes, base, fim)}."
    if inc <= 0:
        return (DA, None, tot, str(fim), None, "", rec, conf,
                txt + nums + f" O gasto de {fim} ficou abaixo de {base} (ano anterior ao mandato); fica só o custo do último ano.", FONTE, "")
    return (DA, inc, tot, str(fim), acu, f"{inicio}-{fim}", rec, conf, txt + nums, FONTE, "")


def padrao(promessas, cats, sid_txt="Medida normativa ou de planejamento, sem efeito direto no orçamento"):
    """Classificação padrão: não cumpridas = só direção (n); implementadas sem ação própria = sem valor."""
    I = {}
    for i, p in enumerate(promessas, 1):
        cat = cats.get(i, DA)
        if p["status"] == "nao_cumprida":
            I[i] = n(p["promessa"].rstrip(".") + (" aumentaria a despesa" if cat == DA else ""), cat) if cat == DA else \
                d(p["promessa"].rstrip(".") + ": " + {SID: sid_txt.lower(), RR: "reduziria a receita", RA: "aumentaria a receita",
                                                       NEU: "efeito neutro para o Estado", SIP: "operação financeira (empréstimo), fora do resultado primário"}[cat] + NI, cat)
        elif cat == SID:
            I[i] = d(sid_txt + ".", SID)
        else:
            I[i] = d("Sem ação orçamentária própria identificada no orçamento do Estado (o gasto está em ações gerais); sem valor.", cat, "baixa")
    return I

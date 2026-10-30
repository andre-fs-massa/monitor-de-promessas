# Impacto fiscal das promessas de Jaques Wagner (governo da Bahia, 2010) no orçamento do Estado da Bahia.
# Mandato 2011-2014. A base aberta do Estado (FIPLAN) só começa em 2013, então não há o ano anterior ao mandato (2010)
# para comparar: não se calcula valor a mais nem acumulado, só o custo do programa em 2014 (último ano do mandato).
import csv
from pathlib import Path
from ba_comum import *

MID = "wagner_ba_2010"
P = list(csv.DictReader(open(Path(__file__).resolve().parents[2] / "promessas" / f"{MID}.csv", encoding="utf-8")))
SEM_BASE = " A base de dados aberta do Estado começa em 2013, sem o ano anterior ao mandato (2010); por isso fica só o custo de 2014, sem valor a mais nem acumulado."


def t(acoes, txt, conf="media", rec="sim"):
    tot = round(emp(acoes, 2014), 3)
    return (DA, None, tot, "2014", None, "", rec, conf,
            txt + f" Ações {', '.join(acoes)}: {serie(acoes, 2013, 2014)}." + SEM_BASE, FONTE, "")


I = padrao(P, {2: SID, 10: SID, 16: SID, 18: SID, 20: SID})
I.update({
    1: t(["3904", "4449", "3906"], "Ações do TOPA (formação e bolsas de alfabetizadores, alimentação dos alfabetizandos e material didático)."),
    2: d("As universidades federais são criadas e mantidas pela União; sem efeito direto no orçamento do Estado.", SID),
    4: t(["2631"], "Funcionamento e ampliação do Samu 192 (cofinanciamento estadual)."),
    6: (DA, None, 0.012, "2014", None, "", "nao", "baixa",
        "A nova fábrica da Bahiafarma, inaugurada em jun/2014, custou R$ 27 milhões, dos quais R$ 12 milhões do Estado (gasto único, valor divulgado pelo governo). Sem valor a mais, porque a base oficial do Estado começa em 2013.",
        "", "https://jornalgrandebahia.com.br/2014/06/governador-jaques-wagner-inaugura-moderna-industria-farmaceutica-em-simoes-filho/"),
    10: d("O Bolsa Família é pago pela União; sem efeito direto no orçamento do Estado.", SID),
    11: t(["1122"], "Requalificação de áreas urbanas para habitação (parte do Casa da Gente); as moradias do Minha Casa, Minha Vida são pagas pela União.", "baixa", "nao"),
    12: t(["7887", "1240", "3826", "5136", "1243", "1254"], "Ações do Água para Todos no orçamento do Estado: sistemas simplificados e integrados de abastecimento, ampliação de sistemas de água, cisternas e esgotamento sanitário (as obras da Embasa, empresa estatal, ficam fora).", "baixa", "nao"),
    13: t(["1177", "6009", "7673", "7671"], "Preservação, recuperação urbanística, fiscalização de obras e ações culturais no Centro Antigo de Salvador.", rec="nao"),
    14: t(["2393", "7582", "7425"], "Funcionamento da Arena Fonte Nova (contraprestação da parceria público-privada) e plano diretor e divulgação da Copa de 2014."),
    16: d("A Ferrovia de Integração Oeste-Leste é obra federal (Valec); sem efeito direto no orçamento do Estado.", SID),
    17: t(["2868"], "Conservação da rede rodoviária estadual. Subestima o custo, porque as restaurações de trechos específicos têm ações próprias por rodovia.", "baixa"),
    19: t(["7219", "6283"], "Funcionamento do Parque Tecnológico e implantação do laboratório compartilhado."),
    20: d("A Lei de Acesso à Informação e o portal Transparência Bahia são medidas de gestão, sem efeito relevante no orçamento.", SID),
})

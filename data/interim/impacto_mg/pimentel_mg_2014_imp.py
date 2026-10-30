# Impacto fiscal das promessas de Fernando Pimentel (governo de MG, 2014) no orçamento do Estado de Minas Gerais.
# Base: 2014 (ano anterior ao mandato). Mandato completo: 2015-2018.
# Fonte oficial: despesa EMPENHADA por ação, dados abertos da Controladoria-Geral do Estado ("Despesa pública",
# mesma base do Portal da Transparência de MG) — scripts/orcamento_mg.py.
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
CGE = "https://dados.mg.gov.br/dataset/despesa"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


I = {
    1: d("Os Fóruns Regionais de Governo funcionaram com reuniões nas regiões e a estrutura existente; não há ação orçamentária própria nem órgãos deslocados para o interior.", SID),
    2: n("Um novo modelo de ensino médio aumentaria a despesa com escolas e professores"),
    3: n("Ampliar a oferta estadual de educação infantil aumentaria a despesa"),
    4: (DA, 0.041, 0.06, "2017", 0.089, "2015-2018", "sim", "baixa",
        "Ações próprias de tempo integral da Secretaria de Educação (ensino fundamental, ensino médio, alimentação escolar e Educação Integral) e oficinas da Fundação Helena Antipoff: R$ 19 milhões em 2014, R$ 38 milhões em 2015, R$ 57 milhões em 2016, R$ 60 milhões em 2017 e R$ 8 milhões em 2018. A queda de 2018 parece mudança de classificação (o programa seguiu em vigor pelo Decreto 47.227/2017), por isso o acumulado subestima o custo; o salário dos professores das horas a mais fica nas ações gerais de pessoal.",
        CGE, ""),
    5: n("Ampliar o ensino técnico estadual aumentaria a despesa"),
    6: n("Investir nos vazios assistenciais da rede de saúde aumentaria a despesa"),
    7: n("Reforçar o apoio à atenção básica dos municípios aumentaria a despesa (o Estado, ao contrário, atrasou os repasses da saúde)"),
    8: n("Carreiras regionais na saúde aumentariam a despesa com pessoal"),
    9: n("Uma rede de atenção a usuários de drogas aumentaria a despesa"),
    10: d("Publicar os dados de violência no observatório da Secretaria de Segurança tem custo pequeno, sem ação orçamentária própria.", SID),
    11: n("Recompor o efetivo da PM aumentaria a despesa com pessoal"),
    12: n("Planejar a malha ferroviária teria custo pequeno (estudos)", SID),
}

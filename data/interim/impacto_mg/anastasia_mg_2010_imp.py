# Impacto fiscal das promessas de Antonio Anastasia (governo de MG, 2010) no orçamento do Estado de Minas Gerais.
# Base: 2010 (ano anterior ao mandato). Renunciou em 04/04/2014: anos completos 2011-2013.
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
    1: d("Criar estrutura física nas 66 microrregiões aumentaria a despesa, mas o modelo Estado em Rede ficou em comitês piloto, sem ação orçamentária própria; sem valor.", DA, "baixa"),
    2: d("Os comitês regionais funcionaram com servidores e estruturas já existentes, sem ação orçamentária própria.", SID),
    3: n("Unificar a regionalização dos órgãos é mudança administrativa", SID),
    4: (DA, 0.028, 0.046, "2013", 0.053, "2011-2013", "sim", "baixa",
        "Ações próprias de tempo integral da Secretaria de Educação (Ampliação das Escolas em Tempo Integral e alimentação escolar, ações 1225 e 4034 até 2011; Educação em Tempo Integral, ações 1077 e 1085, a partir de 2012): R$ 19 milhões em 2010, R$ 22 milhões em 2011, R$ 41 milhões em 2012 e R$ 46 milhões em 2013. Subestima o custo, porque o salário dos professores das horas a mais fica nas ações gerais de pessoal.",
        CGE, ""),
    5: (DA, 0.064, 0.169, "2013", 0.09, "2011-2013", "sim", "baixa",
        "Programa de Educação Profissional (PEP), que compra vagas de cursos técnicos em escolas privadas (ação 4306 até 2011; 4605 a partir de 2012, mais a ação 4190 de desenvolvimento do ensino profissional): R$ 105 milhões em 2010, R$ 109 milhões em 2011, R$ 127 milhões em 2012 e R$ 169 milhões em 2013.",
        CGE, ""),
    6: (DA, 0.018, 0.019, "2013", 0.074, "2011-2013", "sim", "baixa",
        "Ações do Programa Travessia, de combate à pobreza nos municípios mais pobres (Travessia Social, Renda, Saúde, Educação, Banco Travessia, Porta a Porta) e combate à pobreza rural: R$ 0,7 milhão em 2010, R$ 1,9 milhão em 2011, R$ 56 milhões em 2012 e R$ 19 milhões em 2013. A queda da extrema pobreza no período também vem de programas federais (Bolsa Família), que não entram aqui.",
        CGE, ""),
}

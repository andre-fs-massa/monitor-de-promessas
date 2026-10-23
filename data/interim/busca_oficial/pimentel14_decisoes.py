# Classificação do censo de Fernando Pimentel (governo de Minas Gerais, 2014). Mandato 2015-2018, encerrado.
# Chave = índice (1-based) em pimentel14_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia) ou None.
SEM = "Busca na imprensa, na Agência Minas e na legislação mineira (API da ALMG, jan/2015 a dez/2018) não localizou "
LEG = "https://www.almg.gov.br/legislacao-mineira/texto/"


def S(txt, url="", data="2018-12"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


D = {
    1: ("parcialmente_cumprida", "media", "O governo criou os Fóruns Regionais de Governo em 17 territórios (decreto de jun/2015), com reuniões e transferência simbólica do gabinete às regiões, mas não deslocou órgãos da Cidade Administrativa para o interior.", "https://www.agenciaminas.mg.gov.br/multimidia/galeria/governador-pimentel-anuncia-a-criacao-dos-foruns-regionais-de-governo-2015", "2015-06"),
    2: S("novo modelo estadual de ensino médio; o Reinventando o Ensino Médio é anterior a 2015 e a reforma de 2017 é federal."),
    3: S("aumento da participação do Estado na oferta de educação infantil."),
    4: ("cumprida", "alta", "O Decreto 47.227/2017 instituiu a Educação Integral e Integrada, e os alunos atendidos passaram de 102 mil em 2015 para cerca de 150 mil em 2017.", LEG + "DEC/47227/2017/", "2017-08"),
    5: S("ampliação do ensino técnico estadual ligado às vocações regionais."),
    6: S("plano de investimentos para os vazios assistenciais da rede de saúde."),
    7: ("nao_cumprida", "media", "Em vez de reforçar o apoio, o Estado acumulou atrasos nos repasses da saúde aos municípios; a dívida de 2009 a 2020, de R$ 6,7 bilhões, só foi parcelada em acordo de 2021.", "https://www.agenciaminas.mg.gov.br/noticia/governo-de-minas-assina-acordo-com-a-amm-para-pagamento-de-dividas-da-saude", "2018-12"),
    8: S("criação de carreiras regionais para médicos e outros profissionais de saúde."),
    9: S("rede estadual de atenção a usuários de crack, álcool e outras drogas."),
    10: ("cumprida", "baixa", "A Secretaria de Segurança Pública passou a publicar todo mês, pelo Observatório de Segurança Pública Cidadã, os dados de crimes violentos dos 853 municípios.", "https://agenciaminas.mg.gov.br/news/pdf/105195.pdf", "2017"),
    11: S("recomposição do efetivo da Polícia Militar; em 2015-2018 o efetivo de Minas esteve entre os que caíram no país."),
    12: S("plano de reativação e expansão da malha ferroviária; o Plano Estratégico Ferroviário só saiu em 2021."),
}
AJUSTES = {}

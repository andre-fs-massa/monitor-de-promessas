# Classificação do censo de Beto Richa (governo do Paraná, 2010). Mandato 2011-2014 encerrado (reeleito em 2014);
# avaliação até 31/12/2014: o que foi entregue depois conta como não cumprido neste mandato. Fontes: arquivo da Agência
# Estadual de Notícias (arquivo2011.aen.pr.gov.br), sites oficiais do Paraná e imprensa; o diagnóstico do plano de 2014
# (balanço do 1º mandato) serviu de pista. Sem registro = não cumprida, baixa.
# Chave = índice (1-based) em richa10_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia).
SEM = "Busca no arquivo da Agência Estadual de Notícias, em páginas oficiais do governo do Paraná e na imprensa (2011 a 2014) não localizou "
ARQ = "https://arquivo2011.aen.pr.gov.br/sites/default/arquivos_restritos/files/documento/migrados/"
PLANO14 = "https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2014_PR.zip"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


D = {
    1: ("cumprida", "alta", "O Decreto 1.947/2011 instituiu o contrato de gestão como instrumento de contratualização de resultados, e os secretários assinaram contratos com metas por área em jul/2011.", ARQ + "0807_contratos_gestao.doc", "2011-07"),
    2: ("parcialmente_cumprida", "baixa", "Em ago/2011 o governador anunciou o envio à Assembleia de um conjunto de projetos de reforma administrativa; não foi localizado balanço da reorganização (a extinção de cinco secretarias só veio no ajuste de 2015).", ARQ + "0510_mbc_e.doc", "2011-08"),
    3: ("cumprida", "media", "O Instituto das Águas retomou em dez/2011 os planos de bacia com recursos do Fundo Estadual de Recursos Hídricos, começou a cobrança pelo uso da água no Alto Iguaçu em 2012 e chegou a dez comitês de bacia instalados em 2013.", ARQ + "0712comitese.doc", "2013-11"),
    4: ("nao_cumprida", "media", "O Paraná só deixou de vacinar contra a aftosa em 2019 e foi reconhecido como área livre sem vacinação pela OIE em mai/2021.", "https://www.adapar.pr.gov.br/Noticia/Parana-conquista-status-internacional-de-area-livre-de-febre-aftosa-sem-vacinacao", "2021-05"),
    5: ("cumprida", "alta", "O programa Família Paranaense, lançado em mar/2012 e formalizado pela Lei 17.734/2013, atende em rede integrada as famílias mais vulneráveis, identificadas pelo Índice de Vulnerabilidade das Famílias do Paraná (IVF-PR).", "https://www.justica.pr.gov.br/sites/default/arquivos_restritos/files/migrados/File/familia_paranaense/legislacao/Lei-17734-alterada-2017.pdf", "2013-10"),
    6: ("parcialmente_cumprida", "baixa", "O Luz Fraterna atendia 158 mil domicílios em 2013 e o governo anunciou a ampliação do limite de consumo de 100 para 120 kWh/mês; não foi localizado balanço de ampliação da Tarifa Social da Água nem do Leite das Crianças.", ARQ + "1405economiae.doc", "2013-05"),
    7: ("nao_cumprida", "media", "O trabalho infantil caiu, mas não foi erradicado: pela Pnad, o Paraná tinha 42 mil crianças de 5 a 14 anos trabalhando em 2014 (62 mil em 2011).", ARQ + "1511_trabalho_infantil_e.doc", "2015-11"),
    8: ("cumprida", "media", "A Rede Mãe Paranaense foi implantada em 2012 e chegou a 100% dos municípios, segundo o balanço do 1º mandato no plano de 2014; a mortalidade materna caiu de 65,11 (2010) para 37,25 (2013) por 100 mil nascidos vivos.", PLANO14, "2014"),
    9: S("programa estadual de telemedicina no mandato; o núcleo de Telessaúde da UFPR (programa federal) atendia Curitiba e 28 municípios desde 2011, e a parceria para levá-lo aos 399 municípios só veio em set/2015.", ARQ + "0309_telessaude_e.doc"),
    10: ("cumprida", "alta", "A Lei 17.043/2011 instituiu o Programa Estadual de Fomento e Incentivo à Cultura (Profice) e o Fundo Estadual de Cultura.", "https://www.legisweb.com.br/legislacao/?id=144734", "2011-12"),
    11: S("a instituição de conselhos artísticos e de curadores."),
    12: S("a criação de uma política estadual do esporte, lazer e atividade física."),
    13: ("cumprida", "alta", "O governo lançou em jul/2011 o Talento Olímpico do Paraná (depois Geração Olímpica e Paralímpica), com bolsas mensais a atletas de 34 modalidades olímpicas e 14 paralímpicas.", ARQ + "1107bolsa_e.doc", "2011-07"),
    14: ("parcialmente_cumprida", "baixa", "A rede de fibra óptica da Copel ligava 240 dos 399 municípios em fev/2011, com previsão de chegar a todos no fim de 2012; o registro de cobertura dos 399 municípios localizado é de ago/2015.", ARQ + "1402_bel_100.doc", "2011-02"),
    15: ("cumprida", "media", "A Appa retomou a dragagem de manutenção do canal de acesso, parada desde 2009: os berços foram dragados em 2011 e os canais de acesso, incluindo a Galheta, em 2012 e 2013.", ARQ + "1001_dragagem_e.doc", "2013"),
    16: ("cumprida", "media", "O governo criou o programa Paraná Sem Lixões, com comitê gestor e recursos para que os municípios fizessem projetos de destinação adequada; em 2013 ainda metade dos municípios dava destinação inadequada ao lixo.", ARQ + "0605prazo_lixoes_e.doc", "2014-05"),
    17: ("cumprida", "media", "A Lei 17.042/2011 manteve a isenção de ICMS para empresas do Simples com receita de até R$ 360 mil, que atingia 85% das empresas, e a Lei Geral estadual da Micro e Pequena Empresa (2013) ampliou os benefícios.", "https://www.fazenda.pr.gov.br/Noticia/Nova-lei-estadual-amplia-beneficios-para-micro-e-pequenos-empresarios", "2013-09"),
}

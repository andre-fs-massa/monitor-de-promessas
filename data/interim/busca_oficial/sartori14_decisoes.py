# Classificação do censo de José Ivo Sartori (RS, 2014). Mandato 2015-2018, encerrado. Entregas posteriores ao
# mandato contam como não cumpridas; sem registro = não cumprida, confiança baixa.
SEM = "Busca nas notícias do governo do Rio Grande do Sul e na imprensa (2015 a 2018) não localizou "
RS = "https://estado.rs.gov.br/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


AF = "https://aosfatos.org/noticias/no-rs-sartori-piora-infraestrutura-mas-expande-educacao-integral/"
D = {
    1: S("a criação da Rede Gaúcha de Cidades Sustentáveis."),
    2: ("parcialmente_cumprida", "baixa", "A rede estadual ampliou as escolas de tempo integral (46 escolas de ensino fundamental em 2015 e as 12 primeiras de ensino médio em 2018, segundo o Aos Fatos), mas não se localizou a contagem por Coordenadoria que confirme ao menos duas em cada uma das 30.", AF, "2018"),
    3: ("cumprida", "media", "Checagem do Aos Fatos (2018) considerou cumprida a ampliação do tempo de permanência no ensino fundamental, com expansão das escolas de tempo integral.", AF, "2018"),
    4: S("a criação de escolas de educação profissional de referência em cada região."),
    5: S("a universalização do ensino médio de 15 a 18 anos."),
    6: S("a revitalização do Cete nem os centros poliesportivos nas CREs (a reforma do Cete voltou a ser prometida em 2022)."),
    7: S("a instituição de cinco formações obrigatórias por ano para os profissionais da rede."),
    8: ("nao_cumprida", "alta", "Em dez/2018 a Estratégia de Saúde da Família cobria 60,08% da população gaúcha (2.110 equipes), longe da meta de 100%.", "https://saude.rs.gov.br/upload/arquivos/carga20190349/27124914-situacao-saude-pessoa-idosa-rs-2015-2018.pdf", "2018-12"),
    9: S("dados que mostrem a duplicação das crianças atendidas pelo Primeira Infância Melhor."),
    10: S("a criação do comitê permanente do sistema de justiça criminal."),
    11: ("nao_cumprida", "media", "O efetivo da Brigada Militar não foi recomposto: em 2018 havia 11 municípios com efetivo zerado, cobertos com diárias e horas extras; a meta de 3 por mil exigiria cerca de 34 mil policiais.", RS + "distribuicao-de-2-mil-pms-garante-efetivo-minimo-em-municipios", "2019"),
    12: S("canal para o cidadão acompanhar o andamento dos inquéritos."),
    13: ("parcialmente_cumprida", "media", "Em 2018, na assinatura da ordem de início da Cadeia Pública de Alegrete, o secretário da Segurança Pública, Cezar Schirmer, falou em mais de 4 mil vagas criadas no governo, somando reformas, ampliações e novas unidades — cerca de metade da meta.", RS + "assinada-ordem-de-inicio-das-obras-da-cadeia-publica-de-alegrete", "2018"),
    14: S("bolsa para famílias de adolescentes infratores."),
    15: S("a duplicação das ligações Passo Fundo-Marau, Venâncio Aires-Santa Cruz e Santa Maria-Camobi."),
    16: ("nao_cumprida", "media", "A duplicação dos 21,5 km da ERS-118 entre Sapucaia do Sul e Gravataí só foi concluída em nov/2020, no governo seguinte.", RS + "aguardada-havia-duas-decadas-duplicacao-da-ers-118-e-inaugurada-pelo-governador-eduardo-leite", "2020-12"),
    17: S("a implantação da Rede Estadual de Cultura."),
    18: S("a retomada do polo regional de cinema."),
    19: ("cumprida", "baixa", "A Lei de Responsabilidade Fiscal Estadual (LC 14.836, de 14/01/2016) criou regras de controle da despesa; não se confirmou se a regra vincula o gasto ao crescimento da economia.", RS + "um-novo-estado-um-novo-futuro", "2016-01"),
    20: ("parcialmente_cumprida", "media", "O Estado obteve no STF a suspensão do pagamento da dívida e a Assembleia autorizou a adesão ao Regime de Recuperação Fiscal (LC 15.138/2018), mas o acordo com a União não foi assinado: Sartori entregou a minuta do pré-acordo a Eduardo Leite.", RS + "sartori-entrega-a-governador-eleito-minuta-do-pre-acordo-de-assinatura-do-regime-de-recuperacao-fiscal", "2018-12"),
    21: ("nao_cumprida", "alta", "A Assembleia aprovou em set/2015, a pedido do governo, a elevação do ICMS (alíquota básica de 17% para 18% e de 25% para 30% em energia, combustíveis e telecomunicações), prorrogada em dez/2018.", "https://www.legisweb.com.br/noticia/?id=14988", "2015-09"),
}

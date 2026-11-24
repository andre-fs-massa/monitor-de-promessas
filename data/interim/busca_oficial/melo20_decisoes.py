# Classificação do censo de Sebastião Melo (Porto Alegre, 2020). Mandato 2021-2024, encerrado (reeleito em 2024).
# Entregas posteriores ao mandato = não cumpridas; sem registro = não cumprida, confiança baixa.
SEM = "Busca nas notícias da Prefeitura de Porto Alegre e na imprensa (2021 a 2024) não localizou "
P = "https://prefeitura.poa.br/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


def C(txt, url, data, conf="alta"):
    return ("cumprida", conf, txt, url, data)


D = {
    1: C("O Decreto 21.007, de 26/04/2021, regulamentou a Declaração Municipal de Direitos de Liberdade Econômica (LC 876/2020).", P + "gp/noticias/decreto-que-regulamenta-lei-da-liberdade-economica-passa-valer-nesta-segunda-feira", "2021-04"),
    2: C("O decreto de 2021 dispensou de alvará e licença as atividades de baixo risco, com autodeclaração online; em jan/2024 o Decreto 22.444 ampliou a lista de atividades liberadas.", P + "smdet/noticias/prefeitura-disponibiliza-servico-online-de-consulta-de-dispensa-de-alvara", "2021-09"),
    3: S("regra municipal de aprovação tácita de licenças (a regulamentação fixou prazo máximo de 60 dias para as licenças)."),
    4: C("Não se localizou aumento de alíquota de imposto municipal na gestão; a Prefeitura suspendeu a atualização da planta de valores do IPTU (LC 912/2021) e afirmou que não haveria aumento de alíquota.", P + "gp/noticias/prefeitura-protocola-projetos-para-transporte-publico-e-cancelamento-de-reajuste-do", "2021", "media"),
    5: C("A LC 912/2021, proposta pela Prefeitura, suspendeu a atualização da planta de valores do IPTU feita pela LC 859/2019.", P + "gp/noticias/prefeitura-protocola-projetos-para-transporte-publico-e-cancelamento-de-reajuste-do", "2021"),
    6: S("a integração de microcrédito e qualificação profissional na Sala do Empreendedor."),
    7: ("cumprida", "baixa", "A Prefeitura tem incentivos sustentáveis no IPTU, cujas regras foram ajustadas por lei aprovada na Câmara; não se confirmou a data de criação.", P + "smf/noticias/aprovado-projeto-que-ajusta-regras-para-concessao-de-incentivos-sustentaveis-no-iptu", "2024"),
    8: C("A Prefeitura implantou o licenciamento expresso, automatizado e autodeclaratório, que aprova licenças em um dia e responde por mais de 60% dos projetos aprovados.", P + "smamus/noticias/prefeitura-lanca-sistema-que-aprova-licencas-em-um-dia", "2024", "media"),
    9: S("lei de credenciamento de empresas para avaliar projetos de maior porte."),
    10: ("cumprida", "baixa", "O licenciamento urbanístico está concentrado no Escritório de Licenciamento e no Portal de Licenciamento da Smamus.", P + "smamus/noticias/prefeitura-lanca-sistema-que-aprova-licencas-em-um-dia", "2024"),
    11: ("nao_cumprida", "media", "A Prefeitura anunciou em 2023 que a nova EMEF Laçador seria cívico-militar, mas a escola abriu em 2024 em tempo integral sem menção ao modelo; não se localizou escola cívico-militar municipal em funcionamento.", P + "smed/noticias/porto-alegre-tera-escola-municipal-civico-militar", "2024-04"),
    12: C("As escolas municipais receberam cobertura 100% wi-fi pela Procempa.", P + "procempa/noticias/escolas-municipais-de-porto-alegre-recebem-cobertura-100-wi-fi", "2022", "media"),
    13: C("O prefeito sancionou em jul/2021 a Política Municipal de Sustentabilidade Hidroviária, que busca ambiente jurídico favorável ao transporte hidroviário, e a LC 907/2021 tratou do tema no Plano Diretor.", P + "gp/noticias/prefeito-sanciona-projeto-de-lei-para-fortalecer-potencial-hidroviario", "2021-07"),
    14: C("Nenhum pedágio urbano foi criado na gestão; os projetos de transporte público enviados pela Prefeitura em 2021 não incluíram cobrança pelo uso das vias.", P + "gp/noticias/prefeitura-protocola-projetos-para-transporte-publico-e-cancelamento-de-reajuste-do", "2021", "baixa"),
    15: C("A Carris foi desestatizada: lei sancionada em dez/2021, leilão em out/2023 (R$ 109,9 milhões) e contratos assinados em jan/2024.", P + "gp/noticias/assinados-os-contratos-de-desestatizacao-da-carris", "2024-01"),
    16: C("A Prefeitura ampliou em mais de 60% os pontos de wi-fi gratuito, com mais de 420 pontos em praças, parques e outros espaços públicos em 2022.", P + "procempa/noticias/prefeitura-amplia-em-mais-de-60-pontos-de-wi-fi-na-capital", "2022"),
    17: S("a viabilização de um Centro de Eventos."),
    18: ("parcialmente_cumprida", "baixa", "A Prefeitura ampliou a rede de atendimento veterinário a animais silvestres; o atendimento a animais domésticos segue na Unidade de Saúde Animal Victória, anterior à gestão; não se localizou novo hospital veterinário.", P + "smamus/noticias/prefeitura-amplia-rede-de-atendimento-veterinario-animais-silvestres-em-porto", "2024"),
    19: ("nao_cumprida", "media", "A revisão do Plano Diretor não foi aprovada até 2024; o prefeito anunciou a conclusão para 2025.", "https://www.jornaldocomercio.com/economia/2024/02/amp/1141849-licenciamentos-serao-rapidos-promete-melo.html", "2024-02"),
    20: C("As Prefeituras nos Bairros, criadas em 2017, passaram a se chamar Subprefeituras (LC 897/2021) e funcionam nas 17 regiões do Orçamento Participativo.", P + "carta-de-servicos/subprefeituras", "2021-01", "media"),
    21: S("metas semestrais para zerar o uso de papel."),
}

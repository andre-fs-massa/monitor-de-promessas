# Classificação do censo de Jaques Wagner (governo da Bahia, 2010). Mandato 2011-2014 encerrado (completo).
# Mesmo critério dos demais mandatos encerrados. Os portais oficiais da Bahia recusam conexões feitas de fora do
# Brasil; a busca usou a imprensa e as páginas oficiais encontradas nos buscadores. Sem registro = não cumprida,
# confiança baixa. Como o plano é genérico, programas mantidos e ampliados contam como cumpridos.
# Chave = índice (1-based) em wagner10_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia).
SEM = "Busca na imprensa e em páginas oficiais do governo da Bahia (2011 a 2014) não localizou "


def S(txt, url="", data="2026-10"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


D = {
    1: ("cumprida", "media", "O TOPA foi mantido durante todo o mandato e chegou à sua 7ª etapa em 2013/2014.", "https://periodicos.ufpe.br/revistas/topicoseducacionais/article/view/22408", "2014"),
    2: ("cumprida", "alta", "Em jun/2013 foram criadas por lei duas universidades federais na Bahia: a do Sul da Bahia (UFSB) e a do Oeste da Bahia (UFOB).", "https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/lei/l12818.htm", "2013-06"),
    3: ("cumprida", "media", "A rede própria estadual passou de 5.490 leitos em 2010 para 5.998 em 2014, com novos hospitais e unidades no interior.", "https://www.bahianoticias.com.br/noticia/164014-saude-ultima-gestao-de-wagner-expande-rede-mas-leitos-do-sus-caem", "2014"),
    4: ("cumprida", "media", "O Samu 192 se expandiu no período; em 2015 atendia 269 municípios e cerca de 80% da população baiana.", "https://jornalgrandebahia.com.br/2015/12/moradores-do-interior-da-bahia-contam-com-novas-ambulancias-do-samu/", "2015-12"),
    5: ("parcialmente_cumprida", "media", "O governo afirma que mais que duplicou os leitos de UTI, mas o total de leitos de internação do SUS no estado caiu 470 entre jul/2010 e jul/2014.", "https://www.bahianoticias.com.br/noticia/164014-saude-ultima-gestao-de-wagner-expande-rede-mas-leitos-do-sus-caem", "2014"),
    6: ("parcialmente_cumprida", "media", "A nova fábrica da Bahiafarma em Simões Filho foi inaugurada em jun/2014, mas a produção de medicamentos para o SUS no mandato foi pequena (a oposição dizia que havia só um produto).", "https://jornalgrandebahia.com.br/2014/06/governador-jaques-wagner-inaugura-moderna-industria-farmaceutica-em-simoes-filho/", "2014-06"),
    7: ("cumprida", "baixa", "O secretário de Segurança afirmou que nenhum governo contratou tantos policiais, mas a SSP não divulgou o número de contratações do período.", "https://www.bahianoticias.com.br/noticia/164047-seguranca-investimentos-dos-ultimos-anos-nao-contem-violencia-dizem-especialistas", "2014"),
    8: ("cumprida", "media", "As Bases Comunitárias de Segurança (Ronda no Bairro) começaram em 2011; em mai/2013 eram 12 na capital e no interior, e novas bases foram anunciadas em 2014.", "https://www.bahianoticias.com.br/entrevista/303-mauricio-barbosa-faz-balanco-da-reducao-de-criminalidade-na-bahia-06052013", "2013-05"),
    9: ("cumprida", "media", "Segundo a Seap, foram criadas 1.285 vagas prisionais desde 2011 (2.921 somando o 1º mandato); a imprensa registrou só um presídio novo inaugurado no período, em Eunápolis.", "https://www.bahianoticias.com.br/noticia/164118-seap-apresenta-dados-atualizados-de-vagas-em-presidios", "2014"),
    10: ("cumprida", "media", "O Bolsa Família na Bahia passou de 1,66 milhão de famílias em dez/2010 para cerca de 1,8 milhão em 2013, com a busca ativa do Brasil sem Miséria.", "https://www.bahianoticias.com.br/noticia/124862-beneficios-do-bolsa-familia-aumentam-mais-de-quatro-vezes-em-nove-anos", "2013-11"),
    11: ("cumprida", "baixa", "O governo informou 140 mil moradias entregues desde 2007 pelo Casa da Gente e pelo Minha Casa, Minha Vida somados; não foi localizado o número só do Casa da Gente.", "https://jornalgrandebahia.com.br/2014/09/novas-moradias-beneficiam-992-familias-em-feira-de-santana/", "2014-09"),
    12: ("cumprida", "media", "O Água para Todos foi ampliado: as ligações de esgoto passaram de cerca de 495 mil para cerca de 1 milhão nos dois governos Wagner, e as de água de 2,3 milhões para 3,39 milhões.", "https://www.bahianoticias.com.br/artigo/813-a-embasa-e-patrimonio-das-baianas-e-baianos", "2014"),
    13: ("cumprida", "baixa", "O governo anunciou R$ 142 milhões para a recuperação do Centro Antigo de Salvador, com requalificação de ruas pela Conder.", "https://www.bahianoticias.com.br/noticia/147726-governo-anuncia-investimento-de-r-142-milhoes-para-recuperacao-do-centro-antigo-de-salvador", "2014"),
    14: ("cumprida", "alta", "A Arena Fonte Nova foi inaugurada em abr/2013 e Salvador sediou jogos da Copa de 2014.", "https://www.bnews.com.br/noticias/esporte/54897-bavi-inaugura-arena-fonte-nova-no-dia-07-de-abril.html", "2013-04"),
    15: ("parcialmente_cumprida", "media", "O Porto Sul obteve a licença de instalação do Ibama em set/2014 e os contratos foram assinados, mas as obras não começaram no mandato.", "https://jornalgrandebahia.com.br/2014/09/ibama-publica-licenca-de-instalacao-do-porto-sul-em-ilheus/", "2014-09"),
    16: ("parcialmente_cumprida", "media", "As obras da FIOL avançaram no período, mas a ferrovia não entrou em operação; em 2021 o trecho Ilhéus–Caetité tinha 80% das obras feitas.", "https://www.bahianoticias.com.br/noticia/258047-bamin-vence-leilao-da-fiol-e-retomara-obra-com-aplicacao-de-r-33-bilhoes", "2021-04"),
    17: ("cumprida", "media", "O programa de recuperação de estradas continuou: só em 2011 foram 292 km recuperados, e em 2013 o governador falava em 7.300 km de estradas em boas condições.", "https://jornalgrandebahia.com.br/?p=41040", "2011-07"),
    18: ("nao_cumprida", "media", "O Zoneamento Ecológico-Econômico passou por audiências públicas em 2013, mas não foi aprovado no mandato; voltou a ser promessa no plano de 2014.", "https://www.ba.gov.br/inema/2013/11/barreiras-sedia-audiencia-do-zee", "2013-11"),
    19: ("cumprida", "alta", "A primeira fase do Parque Tecnológico da Bahia (Tecnocentro) foi inaugurada em 19/09/2012, com empresas e incubadora.", "https://revistapesquisa.fapesp.br/parque-tecnologico-na-bahia/", "2012-09"),
    20: ("cumprida", "media", "A Lei estadual 12.618/2012 regulamentou o acesso à informação na Bahia, com pedidos pelo portal Transparência Bahia.", "https://ouvidoriageral.ba.gov.br/sites/site-oge/files/migracao_2024/arquivos/File/LAIBA.pdf", "2012-12"),
}

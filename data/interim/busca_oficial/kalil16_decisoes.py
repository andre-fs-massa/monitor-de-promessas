# Classificação do censo de Alexandre Kalil (prefeitura de Belo Horizonte, 2016). Mandato completo (2017-2020).
# Critério de mandato completo: obra ou meta não entregue até 31/12/2020 = não cumprida.
# Chave = índice (1-based) em kalil16_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia) ou None.
SEM = "Busca na imprensa e no site da Prefeitura (jan/2017 a dez/2020) não localizou "
PBH = "https://prefeitura.pbh.gov.br/noticias/"


def S(txt, url="", data="2020-12"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


D = {
    1: S("a criação de uma central de atendimento para marcar consultas e exames pela internet; o agendamento on-line de teleconsultas só apareceu na gestão seguinte."),
    2: ("cumprida", "alta", "O Hospital do Barreiro (Célio de Castro) passou a funcionar com 100% da capacidade em 12/12/2017, com 460 leitos e 16 salas cirúrgicas.", PBH + "hospital-do-barreiro-e-entregue-com-capacidade-maxima", "2017-12"),
    3: S("a retomada da pediatria do Hospital Risoleta Neves, mantido pela UFMG com recursos das três esferas."),
    4: ("nao_cumprida", "alta", "A cobertura do Saúde da Família estava em 81,3% (593 equipes) no início de 2021, abaixo dos 86% de 2016 e longe dos 93% prometidos.", "https://prefeitura.pbh.gov.br/sites/default/files/estrutura-de-governo/saude/2021/acontece-saude-119.pdf", "2021"),
    5: ("nao_cumprida", "media", "A rede passou de 2 para cerca de 4 Cersams AD (entre eles o da Pampulha/Noroeste, aberto em set/2019, e o Centro-Sul, credenciado em 2019); não houve 9 AD nem 9 para adolescentes.", PBH + "prefeito-visita-novo-centro-de-referencia-em-saude-mental-alcool-e-outras-drogas", "2019-09"),
    6: S("vacinação contra a dengue na rede pública; a vacina só entrou no SUS em 2024, por decisão do Ministério da Saúde."),
    7: S("cobertura de 100% do público-alvo na vacinação contra a gripe; a meta do Ministério da Saúde é de 90% e as campanhas da capital ficaram abaixo dela.", PBH + "campanha-de-vacinacao-contra-gripe-tem-inicio-no-dia-104"),
    8: ("nao_cumprida", "baixa", "O Maior Cuidado atendeu 3.062 famílias no acumulado de 2011 a 2022, segundo o BID; não foi localizado registro de 1.000 atendimentos por ano no mandato.", "https://publications.iadb.org/publications/portuguese/document/Programa-Maior-Cuidado-uma-intervencão-integrada-de-base-comunitaria-para-idosos.pdf", "2022-12"),
    9: ("nao_avaliada", "baixa", "Em 2019 a Prefeitura empenhou R$ 1,82 bilhão em educação (cerca de R$ 726 por habitante), segundo o Siconfi; não foi localizada a média nacional dos municípios no mesmo critério para comparar.", "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca?an_exercicio=2019&no_anexo=DCA-Anexo%20I-E&id_ente=3106200", "2019"),
    10: ("parcialmente_cumprida", "baixa", "A Prefeitura abriu 10 mil vagas na educação infantil em 2018, com prioridade para 4 e 5 anos, e passou a atender toda a demanda dessa faixa; não foi localizado registro de 50 mil matrículas na pré-escola.", PBH + "pbh-cria-10-mil-novas-vagas-para-educacao-infantil-em-2018", "2018"),
    11: S("distribuição de tablets ou material digital para metade dos alunos; a compra de tablets para empréstimo só foi anunciada em jan/2021, por causa das aulas remotas.", "https://www.em.com.br/app/noticia/gerais/2021/01/28/interna_gerais,1233265/pbh-pretende-comprar-tablets-para-viabilizar-aulas-remotas-para-estudantes.shtml", "2021-01"),
    12: ("parcialmente_cumprida", "baixa", "A rede municipal tinha 145 escolas de educação infantil (as Umeis viraram Emeis em 2018) por volta de 2020, acima das 126 de 2016, mas abaixo das 150 prometidas.", "https://revista.uemg.br/index.php/educacaoemfoco/article/download/4453/3157/17859", "2020"),
    13: ("nao_cumprida", "baixa", "Em 2019 o Escola Aberta funcionava em 171 escolas, com 898 oficinas e quase 118 mil participantes, longe dos 5 milhões de atendimentos prometidos.", "https://cmbhweb.cmbh.mg.gov.br/print/comunica%C3%A7%C3%A3o/not%C3%ADcias/2021/07/retomada-gradual-do-escola-aberta-%C3%A9-pleiteada-por-comunidade-escolar", "2019"),
    14: ("cumprida", "baixa", "O Programa de Metas 2017-2020 previu o Plano de Segurança Escolar em 100% das escolas (eram 18), e em 2019 a Secretaria de Educação publicou o guia Escola Lugar de Proteção para toda a rede, apoiado no plano.", "https://prefeitura.pbh.gov.br/sites/default/files/estrutura-de-governo/educacao/Escola%20Lugar%20de%20Prote%C3%A7%C3%A3o.%20Guia%20de%20Orienta%C3%A7%C3%B5es%20e%20Encaminhamentos%20_2019.pdf", "2019"),
    15: ("cumprida", "media", "A reforma administrativa de 2017 (Lei 11.065/2017) reestruturou a pasta como Secretaria Municipal de Segurança e Prevenção, com uma diretoria de prevenção social ao crime.", "https://prefeitura.pbh.gov.br/seguranca", "2017-08"),
    16: S("a criação de uma sala de crise para a segurança no COP-BH, que já tinha sala de controle integrado desde 2014.", "https://prefeitura.pbh.gov.br/seguranca/copbh"),
}
AJUSTES = {}

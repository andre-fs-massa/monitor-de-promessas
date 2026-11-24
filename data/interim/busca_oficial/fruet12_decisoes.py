# Classificação do censo de Gustavo Fruet (Curitiba, 2012). Mandato 2013-2016 encerrado; avaliação até 31/12/2016.
# Fontes: notícias da Prefeitura de Curitiba e imprensa, lidas por resumos de busca (o site da Prefeitura não pôde ser
# aberto diretamente). Sem registro = não cumprida, confiança baixa.
# Chave = índice (1-based) em fruet12_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia).
SEM = "Busca nas notícias da Prefeitura de Curitiba e na imprensa (2013 a 2016) não localizou "
CWB = "https://www.curitiba.pr.gov.br/noticias/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


D = {
    1: S("a mudança do Gabinete de Gestão Integrada de Segurança para o Gabinete do Prefeito, com plano de metas."),
    2: S("a criação do Conselho Municipal de Segurança Pública (um conselho do tipo só foi anunciado em 2025)."),
    3: S("sistema municipal de videomonitoramento no mandato (a Muralha Digital é de 2019)."),
    4: S("os Eixos Monitorados pela Guarda Municipal."),
    5: S("pesquisa de vitimização feita pela Prefeitura."),
    6: S("lei do Sistema Municipal de Cultura no mandato."),
    7: S("dados de alfabetização próxima de 100% (a taxa de analfabetismo era de 2,1% em 2010)."),
    8: S("balanço de vagas para todas as crianças de 4 e 5 anos."),
    9: S("balanço de bibliotecas e quadras cobertas em todas as escolas."),
    10: S("a ampliação da hora-atividade dos professores para 33%."),
    11: ("cumprida", "alta", "O Plano Municipal de Educação 2015-2025 foi aprovado pela Câmara e sancionado por Fruet como Lei 14.681, de 24/06/2015.", "https://mid-educacao.curitiba.pr.gov.br/2015/10/pdf/00087989.pdf", "2015-06"),
    12: S("o Observatório de Pesquisa no Esporte (o Observatório do Esporte com a UFPR é de 2022)."),
    13: S("o Plano Municipal das Juventudes."),
    14: S("o Plano de Conforto Ambiental Urbano."),
    15: S("sistema de monitoramento de fauna e flora."),
    16: S("sistema municipal de medição e divulgação da qualidade do ar."),
    17: S("o mapa de risco de desastres naturais."),
    18: S("sistema de monitoramento de emissões de gases de efeito estufa."),
    19: S("indicadores de áreas verdes por bairro."),
    20: ("cumprida", "alta", "A gestão criou sete unidades de conservação, entre elas os parques Mané Garrincha, Guairacá e Vista Alegre, somando quase 9 milhões de m² de áreas verdes.", CWB + "em-tres-anos-curitiba-ganhou-tres-vezes-mais-areas-verdes-que-em-duas-decadas/39606", "2016"),
    21: ("cumprida", "alta", "De 2013 a 2016 foram implantados 90,8 km de novas vias cicláveis, incluindo ciclorrotas e as Vias Calmas.", CWB + "curitiba-amplia-estrutura-cicloviaria-em-71-e-estimula-mais-gente-a-pedalar/40089", "2016"),
    22: ("parcialmente_cumprida", "baixa", "As Vias Calmas da Sete de Setembro (2014) e da João Gualberto/Paraná (jun/2016) reduziram a velocidade a 30 km/h e priorizaram ciclistas, mas não foram criadas zonas com ruas de pedestres e restrição a veículos.", CWB + "nova-via-calma-de-curitiba-e-inaugurada-nas-avenidas-joao-gualberto-e-parana/39992", "2016-06"),
    23: S("a revisão do projeto do metrô com nova pesquisa origem-destino (o projeto foi abandonado)."),
    24: ("nao_cumprida", "media", "A Linha Verde não foi completada no mandato: o trecho final só foi entregue em 2024.", CWB + "com-53-grandes-obras-viarias-e-1200-km-de-asfalto-novo-prefeitura-transforma-infraestrutura-urbana-de-curitiba/75422", "2024-12"),
    25: S("a criação do Comitê Municipal de Prevenção ao Uso de Drogas."),
}

# Classificação do censo de Fernando Haddad (prefeitura de São Paulo, 2012). Mandato 2013-2016, encerrado.
# Chave = índice (1-based) em haddad12_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia) ou None.
# Fonte principal: balanço final do Programa de Metas 2013-2016 (Suplemento do Diário Oficial de 31/12/2016).
SEM = "Busca na imprensa, em sites oficiais, no balanço final do Programa de Metas 2013-2016 e no Catálogo de Legislação Municipal (jan/2013 a dez/2016) não localizou "
BAL = "https://drive.prefeitura.sp.gov.br/cidade/secretarias/upload/gestao/arquivos/Balanco%20final%20de%20gestao%20-%20Haddad.pdf"
CAT = "https://legislacao.prefeitura.sp.gov.br/leis/"


def S(txt, url="", data="2016-12"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


D = {
    1: ("cumprida", "alta", "Meta 14 do Programa de Metas superada (149%): mais de 135 mil alunos com jornada ampliada em 2015, e o Programa São Paulo Integral começou em 2016.", BAL, "2016-12"),
    2: ("cumprida", "media", "A educação infantil ganhou 99.229 matrículas entre jan/2013 e nov/2016 (meta 19); foram implantadas 425 creches, mas só 45 CEIs construídos pela Prefeitura (meta 16, 57%).", BAL, "2016-11"),
    3: ("cumprida", "alta", "A Lei 16.213/2015 criou o Conselho de Representantes dos Conselhos de Escola (CRECE), regulamentado pelo Decreto 56.520/2015.", CAT + "lei-16213-de-17-de-junho-de-2015", "2015-10"),
    4: ("cumprida", "alta", "O Plano Municipal de Educação foi aprovado pela Lei 16.271/2015.", CAT + "lei-16271-de-17-de-setembro-de-2015", "2015-09"),
    5: S("criação de novas Diretorias Regionais de Educação."),
    6: ("cumprida", "media", "A Prefeitura aderiu ao Pronatec e criou, em 2014, o Comitê Gestor Intersecretarial do programa no município.", CAT + "portaria-gabinete-do-prefeito-170-de-12-de-abril-de-2014", "2014-04"),
    7: ("parcialmente_cumprida", "media", "Em 2015 foi criada a Coordenação Municipal de Regulação, Avaliação e Controle; não foi localizado que a Prefeitura tenha assumido a regulação dos serviços sob gestão estadual.", CAT + "portaria-secretaria-municipal-da-saude-246-de-18-de-marco-de-2015", "2015-03"),
    8: ("nao_cumprida", "media", "A Renda Básica da Cidadania não foi implantada; o projeto de lei do Executivo (PL 620/2016) só foi enviado no fim do mandato e não foi aprovado.", "https://www.saopaulo.sp.leg.br/iah/fulltext/justificativa/JPL0055-2021.pdf", "2016-12"),
    9: ("cumprida", "media", "Dois restaurantes comunitários (Mooca e Sé) entraram em funcionamento (meta 9) e foi inaugurado o Centro de Referência em Segurança Alimentar da Vila Maria (meta 13).", BAL, "2016-12"),
    10: ("cumprida", "media", "Foram entregues os 7 CREAS previstos (meta 4) e 5 novos CRAS (meta 3 previa 60).", BAL, "2016-12"),
    11: ("parcialmente_cumprida", "baixa", "O novo contrato do 156 criou canal exclusivo para denúncias de violação de direitos, mas a Ouvidoria Municipal de Direitos Humanos ficou em 50% (meta 62); não foi localizado um sistema de notificações.", BAL, "2016-12"),
    12: ("cumprida", "media", "A cidade aderiu ao Sistema Nacional de Cultura e criou o Fundo Municipal de Cultura (meta 31, concluída).", BAL, "2016-12"),
    13: ("nao_cumprida", "media", "O projeto que reorganiza o Conselho Municipal de Cultura como Conselho Municipal de Política Cultural (PL 248/2015) não foi aprovado até o fim do mandato.", "https://www.saopaulo.sp.leg.br/blog/composicao-do-conselho-municipal-de-politica-cultural-e-discutida-em-audiencia/", "2016-12"),
    14: ("cumprida", "media", "Meta 44 superada: Centro Olímpico ampliado e Núcleo de Alto Rendimento no Centro Esportivo Joerg Bruder; o Centro de Esportes Radicais abriu em mar/2016 (meta 46).", BAL, "2016-03"),
    15: S("realização de competições esportivas escolares anuais."),
    16: ("cumprida", "alta", "Os Conselhos Participativos foram criados nas 32 subprefeituras (Lei 15.764/2013, meta 113).", BAL, "2013-12"),
    17: ("cumprida", "alta", "A Controladoria Geral do Município foi criada em 2013 (Lei 15.764/2013), reunindo auditoria, corregedoria e ouvidoria.", "https://www.saopaulo.sp.leg.br/iah/fulltext/leis/L15764.pdf", "2013-05"),
    18: S("política integrada de saúde do servidor ou requalificação do HSPM."),
    19: None,  # pregão eletrônico: já usado pela Prefeitura antes de 2013
    20: ("cumprida", "alta", "Meta 73 superada: 120 praças com o WiFi Livre SP até abr/2015 (a meta era 42).", BAL, "2015-04"),
    21: S("instituição do Programa Cidade de Paz; houve ações do Plano Juventude Viva (meta 42, 64%)."),
    22: S("elaboração do Mapa da Violência e da Criminalidade da cidade."),
    23: S("modernização e expansão do sistema eletrônico de vigilância da GCM."),
    24: ("cumprida", "media", "O efetivo da GCM foi ampliado com 500 agentes nomeados por concurso, de 2 mil previstos na meta 38 (25%).", BAL, "2016-12"),
    25: ("cumprida", "alta", "Meta 74 superada: 52.143 novos pontos de iluminação em locais sem luz e 400 mil luminárias renovadas.", BAL, "2016-12"),
    26: ("parcialmente_cumprida", "media", "Não foi criada agência de pesquisa e inovação, mas o Decreto 55.461/2014 instituiu a política de estímulo a startups (Tech Sampa).", CAT + "decreto-55461-de-29-de-agosto-de-2014", "2014-08"),
    27: ("parcialmente_cumprida", "media", "A Prefeitura apoiou a implantação da Unifesp na Zona Leste e de unidades do IFSP (meta 82), mas não houve nova universidade federal na Zona Sul.", BAL, "2016-12"),
    28: S("criação do Conselho Municipal de Desenvolvimento Local."),
    29: S("Política Municipal de Economia Criativa."),
    30: ("parcialmente_cumprida", "baixa", "O Programa Operação Trabalho foi usado no De Braços Abertos (meta 12); não foi localizada a retomada do Bolsa Trabalho, do Começar de Novo e do Oportunidade Solidária.", BAL, "2016-12"),
    31: ("cumprida", "media", "A Lei 16.140/2015, regulamentada em 2016, previu a compra progressiva de orgânicos da agricultura familiar para a merenda, e a Prefeitura fez chamadas públicas em 2016.", "https://www.brasildefato.com.br/2017/06/12/gestao-doria-barra-compras-de-merenda-escolar-organica-e-agroecologica/", "2016"),
    32: ("cumprida", "alta", "O novo Plano Diretor Estratégico foi aprovado em 31/07/2014 (Lei 16.050), e o Programa de Metas 2013-2016 foi publicado em 2013.", BAL, "2014-07"),
    33: ("nao_cumprida", "media", "O Conselho Municipal de Política Urbana continuou existindo e foi reorganizado pelo Decreto 56.268/2015, sem virar o Conselho da Cidade.", "https://prefeitura.sp.gov.br/web/licenciamento/w/desenvolvimento_urbano/participacao_social/conselhos_e_orgaos_colegiados/cmpu/170181", "2015-07"),
    34: S("Programas de Parceria Público-Comunitários."),
    35: ("parcialmente_cumprida", "alta", "A nova Lei de Zoneamento (16.402) foi sancionada em mar/2016 (meta 121); o novo Código de Obras só foi aprovado em 2017, na gestão seguinte.", BAL, "2016-03"),
    36: ("cumprida", "alta", "O Plano Diretor de 2014 passou a aplicar o IPTU progressivo no tempo, a preempção e novas ZEIS, e a Prefeitura começou a notificar imóveis ociosos.", BAL, "2016-12"),
    37: S("programa de capacitação técnica Sul-Sul."),
    38: S("programa específico de moradia popular na região central."),
    39: ("cumprida", "media", "Meta 35: 55.627 moradias viabilizadas, muitas pelo Minha Casa, Minha Vida, com 14.951 entregues até dez/2016.", BAL, "2016-12"),
    40: ("cumprida", "media", "Meta 36: 60.494 famílias beneficiadas por urbanização de favelas, 14.114 em obras concluídas.", BAL, "2016-12"),
    41: S("formação de estoque de terrenos para habitação de interesse social."),
    42: S("programa de acompanhamento pós-ocupação."),
    43: ("cumprida", "alta", "Meta 96 superada: 423,3 km de faixas exclusivas de ônibus implantados (a cidade tinha 90 km em 2012).", BAL, "2016-12"),
    44: ("cumprida", "alta", "O Plano Municipal de Mobilidade Urbana foi instituído pelo Decreto 56.834/2016.", "https://legislacao.prefeitura.sp.gov.br/leis/decreto-56834-de-24-de-fevereiro-de-2016", "2016-02"),
    45: ("nao_cumprida", "media", "Em 2013 foi criado grupo de trabalho para estudar o transporte de cargas, mas não foi localizado o Plano de Logística e Carga.", CAT + "portaria-secretaria-municipal-dos-transportes-25-de-16-de-marco-de-2013", "2013-03"),
    46: S("criação de órgão de gerenciamento da logística de carga."),
    47: ("cumprida", "alta", "O Decreto 54.058/2013 criou o Conselho Municipal de Trânsito e Transporte (CMTT).", CAT + "decreto-54058-de-01-de-julho-de-2013", "2013-07"),
    48: S("criação de centrais de controle operacional do transporte."),
    49: ("cumprida", "alta", "Meta 94 concluída: Bilhete Único diário, semanal e mensal implantados.", BAL, "2016-02"),
    50: ("parcialmente_cumprida", "media", "O novo modelo de concessão dos ônibus foi elaborado e licitado em 2015, mas a licitação foi suspensa pelo Tribunal de Contas e não foi concluída no mandato.", "https://diariodotransporte.com.br/2016/12/29/opiniao-balanco-de-haddad-na-mobilidade-urbana/", "2016-12"),
    51: ("cumprida", "media", "Foram construídos ou requalificados 42,3 km de corredores de ônibus (meta 93 previa 150 km).", BAL, "2016-12"),
    52: S("criação de estações intermodais."),
    53: ("cumprida", "media", "Foi entregue o novo Terminal Campo Limpo, para 62 mil pessoas por dia.", "https://prefeitura.sp.gov.br/web/comunicacao/w/noticias/122995", "2015-10"),
    54: ("cumprida", "media", "Meta 98 superada: 4.840 cruzamentos reformados, 744 novos controladores e nobreaks na rede semafórica.", BAL, "2016-05"),
    55: ("cumprida", "alta", "Meta 50 superada: 1,19 milhão de m² de calçadas tornadas acessíveis.", BAL, "2016-12"),
    56: ("cumprida", "alta", "Meta 97 concluída: 477,7 km de vias com tratamento cicloviário permanente.", BAL, "2016-12"),
    57: ("cumprida", "alta", "A cidade passou a ter 6.247 vagas em bicicletários públicos integrados ao transporte.", BAL, "2016-12"),
    58: ("cumprida", "alta", "O Bike Sampa passou a ser usado com o Bilhete Único a partir de jan/2014.", "https://www.guiadasemana.com.br/turismo/noticia/bilhete-unico-e-integrado-a-projeto-bike-sampa", "2014-01"),
    59: ("parcialmente_cumprida", "media", "A Lei 15.688/2013 tornou a inspeção veicular gratuita, mas o programa foi suspenso em 2014, com o fim do contrato, e não foi retomado no mandato.", CAT + "lei-15688-de-11-de-abril-de-2013", "2014"),
    60: S("estacionamentos públicos para centros comerciais de bairro."),
    61: ("cumprida", "media", "Foram elaborados os Cadernos de Drenagem e criada instância municipal de drenagem (meta 106), e aprovado o Plano de Gestão Integrada de Resíduos Sólidos em 2014.", BAL, "2016-12"),
}
AJUSTES = {}

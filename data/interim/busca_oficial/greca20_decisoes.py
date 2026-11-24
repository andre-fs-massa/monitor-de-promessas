# Classificação do censo de Rafael Greca (Curitiba, 2020). Mandato 2021-2024 encerrado; avaliação até 31/12/2024: o
# que foi entregue depois (na gestão Pimentel) conta como não cumprido neste mandato. Fontes: notícias da Prefeitura
# de Curitiba (curitiba.pr.gov.br/noticias), balanço "3 anos de trabalho" (curitiba.pr.gov.br/3anosdetrabalho) e
# imprensa. Sem registro = não cumprida, confiança baixa (o Diário Oficial do Município não foi consultado).
# Chave = índice (1-based) em greca20_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia).
SEM = "Busca nas notícias da Prefeitura de Curitiba e na imprensa (2021 a 2024) não localizou "
CWB = "https://www.curitiba.pr.gov.br/noticias/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


def C(txt, url, data, conf="alta"):
    return ("cumprida", conf, txt, url, data)


def Pc(txt, url, data, conf="media"):
    return ("parcialmente_cumprida", conf, txt, url, data)


def N(txt, url, data, conf="media"):
    return ("nao_cumprida", conf, txt, url, data)


D = {
    1: S("contratação de agência de rating para o município (a nota registrada é a Capag do Tesouro Nacional, que não é avaliação contratada)."),
    2: C("O portal que reúne os serviços tributários e financeiros foi lançado em 2023 e o Domicílio Eletrônico do Contribuinte, regulamentado pelo Decreto 267/2024, foi implantado em 2024.", CWB + "novo-portal-reune-todos-os-servicos-tributarios-e-financeiros-de-curitiba/67979", "2024-02"),
    4: N("A Rua da Cidadania da CIC, na Vila Nossa Senhora da Luz, teve obras iniciadas em mar/2023, mas só foi inaugurada em 15/11/2025, já na gestão seguinte.", CWB + "prefeito-eduardo-pimentel-inaugura-nova-rua-da-cidadania-da-cic-com-servicos-e-programacao-especial/80529", "2025-11"),
    5: C("Os Espaços Cidadão funcionam em todas as Ruas da Cidadania e no Palácio 29 de Março, com atendimento presencial e por telefone.", CWB + "servicos-da-prefeitura-de-curitiba-estao-perto-de-sua-casa-nas-ruas-da-cidadania/76281", "2025-01", "baixa"),
    8: C("O Pinhão Hub, espaço de inovação do Vale do Pinhão, foi inaugurado em mar/2024 nos três andares do prédio central do Engenho da Inovação (antigo Moinho Rebouças).", CWB + "greca-inaugura-pinhao-hub-novo-espaco-de-inovacao-do-vale-do-pinhao-de-curitiba/72615", "2024-03", "media"),
    3: C("O Hipervisor Urbano, plataforma de integração de dados com centro de operação no Palácio da Inovação, foi lançado por Greca e Pimentel no início de 2024.", CWB + "greca-e-eduardo-pimentel-lancam-o-hipervisor-urbano-de-curitiba/72349", "2024-02"),
    15: S("o Projeto Luz de Curitiba (assistente virtual por voz)."),
    18: Pc("O Wi-Fi Curitiba foi lançado em mai/2021 e chegou a 280 pontos (praças, parques, escolas, terminais e Ruas da Cidadania), mas o Wi-Fi nos ônibus e estações-tubo não saiu.", CWB + "wi-fi-curitiba-completa-tres-anos-com-280-pontos-de-acesso-pela-cidade/73643", "2024-05"),
    24: S("o lançamento da plataforma MaaS; ela voltou a constar do plano de governo de 2024."),
    25: Pc("No BRT Leste-Oeste, a primeira intervenção (binário Olga Balster/Nivaldo Braga) foi entregue em set/2024, e a primeira obra viária do Novo Inter 2 em dez/2024; o grosso das obras ficou para a gestão seguinte.", CWB + "greca-entrega-primeira-obra-viaria-do-projeto-novo-inter-2/74992", "2024-12"),
    26: C("Os sete primeiros ônibus elétricos entraram em operação em jun/2024 (seis na Interbairros I e um na Água Verde), não no Inter 2.", CWB + "greca-entrega-os-primeiros-7-onibus-eletricos-do-transporte-coletivo-de-curitiba/74253", "2024-06", "media"),
    27: C("O sistema de bicicletas compartilhadas (Tembici) foi lançado em jul/2023 com 50 estações e ampliado para 780 bicicletas em 2024.", CWB + "curitiba-amplia-rede-de-bicicletas-compartilhadas-e-conta-agora-com-780-bikes/73953", "2024"),
    29: Pc("O transporte coletivo de Curitiba voltou a se integrar ao metropolitano em 2024, mas sem sistema e gestão únicos.", CWB + "transporte-coletivo-de-curitiba-volta-a-ser-forte-com-reintegracao-metropolitana-e-entrada-na-eletromobilidade/75311", "2024-12", "baixa"),
    31: C("O trecho final da Linha Verde foi entregue em 2024, com a liberação do trânsito pela trincheira da Rua Fúlvio Alice em dez/2024.", CWB + "com-53-grandes-obras-viarias-e-1200-km-de-asfalto-novo-prefeitura-transforma-infraestrutura-urbana-de-curitiba/75422", "2024-12", "media"),
    33: C("Os primeiros táxis 100% elétricos começaram a rodar em jun/2023, e um ato da Urbs (2023) definiu o padrão desses táxis.", CWB + "curitiba-comeca-a-testar-taxis-100-eletricos-para-o-transporte-de-passageiros/68919", "2023-06", "media"),
    34: C("O binário Olga Balster/Nivaldo Braga foi inaugurado em set/2024, primeira intervenção concluída do Ligeirão Leste-Oeste.", CWB + "greca-entrega-primeira-obra-viaria-do-projeto-novo-inter-2/74992", "2024-11"),
    35: S("a extensão do binário João Soares Barcelos/Oliveira Viana (implantado em 2019, antes do mandato; a extensão voltou ao plano de 2024)."),
    37: N("A trincheira da Lothário Meissner só teve convênio em jan/2026 e início de obras previsto para out/2026, na gestão seguinte.", CWB + "reuniao-de-partida-alinha-inicio-de-obras-da-trincheira-da-lothario-meissner-no-jardim-botanico/85084", "2026-10"),
    38: N("O viaduto da Anne Frank, parte do trinário da Marechal, só foi licitado em 2026.", CWB + "prefeitura-republica-licitacao-do-trinario-da-marechal-floriano/84327", "2026-09"),
    39: N("O viaduto da Ten. Francisco Ferreira de Souza, parte do trinário da Marechal, só foi licitado em 2026.", CWB + "prefeitura-republica-licitacao-do-trinario-da-marechal-floriano/84327", "2026-09"),
    40: N("O novo viaduto do Orleans só foi apresentado em set/2026, com recursos do Estado.", CWB + "novo-viaduto-do-orleans-tera-r-80-milhoes-em-investimentos/85001", "2026-09"),
    43: Pc("A PPP de iluminação (Engie, 2023) modernizou o parque com LED, mas a meta de 100% até o fim de 2024 não foi atingida: a cobertura chegou a 94% só em abr/2025.", CWB + "curitiba-chega-a-94-da-rede-de-iluminacao-modernizada-ruas-do-centro-sao-destaques/81076", "2025-04"),
    45: Pc("A Pirâmide Solar do Caximba e as usinas nos terminais passaram a gerar energia para os prédios públicos, mas a Pirâmide supria cerca de 30% do consumo municipal, abaixo dos 60% prometidos.", CWB + "piramide-solar-do-caximba-transforma-antigo-aterro-sanitario-em-gerador-de-energia-limpa-em-curitiba/67889", "2023"),
    63: C("As primeiras 60 casas do Bairro Novo do Caximba foram entregues em jul/2024 e o projeto chegou a 104 famílias reassentadas em dez/2024, com continuidade na gestão seguinte.", CWB + "greca-entrega-as-primeiras-casas-do-bairro-novo-da-caximba-em-dia-historico-para-curitiba/74344", "2024-12", "media"),
    64: N("A Fazenda Urbana da CIC só foi aberta em nov/2025, junto com a Rua da Cidadania, na gestão seguinte.", CWB + "regional-cic-comemora-abertura-da-rua-da-cidadania-e-da-fazenda-urbana-e-entrega-de-cmei/81072", "2025-11"),
    66: S("o Polo do Alimento e Inovação no Mercado Regional Cajuru (a reforma e o Armazém da Família no mercado são de 2025)."),
    68: N("As obras do Restaurante Popular do Tatuquara só foram lançadas em mai/2024 e não terminaram no mandato.", CWB + "greca-lanca-obra-do-restaurante-popular-com-autossuficiencia-energetica-em-curitiba/73568", "2024-05"),
    73: C("A rede municipal passou de 126 para 153 escolas com educação integral no mandato.", CWB + "rede-municipal-de-ensino-de-curitiba-ja-tem-153-escolas-com-oferta-de-educacao-integral/68529", "2023"),
    75: Pc("Foram anunciadas 12 novas unidades do Farol do Saber e Inovação e lançados os Faróis Móveis (2021-2022); o novo farol do complexo Rebouças não foi confirmado.", CWB + "curitiba-vai-ganhar-mais-12-farois-do-saber-e-inovacao-veja-os-locais/54731", "2022", "baixa"),
    78: C("O Curitibinhas Poliglotas foi ampliado e passou a atender 136 escolas em 2023.", CWB + "escolas-municipais-de-curitiba-oferecem-ate-cinco-opcoes-de-idiomas/69442", "2023", "media"),
    82: C("A Central Saúde Já foi ampliada com videoconsultas e atendimento virtual em 2023.", CWB + "central-saude-ja-completa-1-ano-de-ampliacao-dos-servicos-e-de-inovacoes-ao-sus-de-curitiba/73129", "2024"),
    83: S("programa municipal Remédio em Casa (o programa com esse nome é estadual, da Sesa, desde 2019)."),
    84: C("O teleatendimento 3350-9000 da Central Saúde Já foi ampliado para atendimento virtual em 2023, com presença da ministra da Saúde.", CWB + "com-presenca-da-ministra-nisia-trindade-greca-amplia-central-saude-ja-para-atendimento-virtual/68211", "2023"),
    100: C("O programa Anjos da Guarda, contra o trabalho infantil, foi lançado em 2021 e fez quase 7.500 abordagens.", CWB + "programas-e-servicos-garantem-direitos-e-protecao-a-criancas-e-adolescentes-em-vulnerabilidade/64598", "2022", "media"),
    101: C("A Pousada de Maria ganhou nova sede em 2024 para ampliar o atendimento a mulheres em situação de violência.", CWB + "pousada-de-maria-ganha-nova-sede-para-atender-melhor-mulheres-em-situacao-de-violencia-em-curitiba/73558", "2024", "media"),
    102: C("A Lei 16.106/2022 instituiu o Acolhimento Familiar para Pessoa Idosa na modalidade Família Extensa.", CWB + "curitiba-tera-acolhimento-familiar-para-pessoas-idosas-em-vulnerabilidade-social/66674", "2022"),
    104: C("A FAS ampliou vagas e locais de acolhimento para a população de rua, incluindo o hotel social Eilat.", CWB + "fas-ampliou-vagas-e-locais-de-acolhimento-para-pessoas-em-situacao-de-rua-em-curitiba/75326", "2024-12", "baixa"),
}
_RESTO = {
    6: "sistema digital de gestão de documentos com protocolo eletrônico", 7: "novos espaços FabLab", 9: "balanço de ampliação do Empreendedora Curitibana",
    10: "postos de agentes de crédito nos Espaços Empreendedor", 11: "balanço de ampliação do Bom Negócio", 12: "balanço de ampliação do Tecnoparque",
    13: "a recuperação dos imóveis listados no Rosto da Cidade", 14: "a modernização da feira de orgânicos do Largo da Ordem",
    16: "a modernização da Central 156", 17: "o aplicativo Executor de Serviços do SIAC 156", 20: "concurso da Guarda Municipal no mandato",
    21: "balanço de ampliação do Policiamento Ostensivo de Proximidade", 22: "a modernização do CCO", 23: "balanço de ampliação do Nova Morada e do Intervidas",
    28: "balanço da expansão da malha cicloviária", 30: "a conclusão da modernização da bilhetagem", 32: "acessibilidade plena em toda a frota e estações",
    36: "o binário Waldemiro Pedroso/João Bonat", 41: "novos estacionamentos públicos", 42: "a ligação de 100% dos semáforos à central de tráfego",
    44: "plano de ação metropolitano de cargas", 46: "balanço de implementação do PlanClima", 47: "a conclusão do Parque Linear do Barigui",
    48: "o Cadastro/Certificado Verde", 49: "comitês de microbacias formalizados", 50: "o censo arbóreo", 51: "o Museu Botânico Virtual",
    52: "atendimento veterinário de média e alta complexidade", 53: "o novo Museu de História Natural (voltou ao plano de 2024)", 54: "a unidade AMAS",
    55: "o CRAR", 56: "a eliminação do resíduo bruto em aterro", 57: "balanço de ampliação dos Ecopontos", 58: "o programa de compostagem domiciliar",
    59: "o Plano Decenal do Turismo e o Plano de Marketing", 60: "sinalização interpretativa nos atrativos", 61: "a revitalização do Zoológico com praça de alimentação",
    62: "selo dos produtos artesanais locais", 65: "circuito de feiras da agricultura urbana", 67: "a Feira 4.0", 69: "o Armazém da Família em Casa",
    70: "a plataforma virtual do Banco de Alimentos", 71: "a ampliação da rede de sacolões", 72: "a ampliação do Mesa Solidária com cozinhas comunitárias",
    74: "balanço de quadras construídas nas escolas", 76: "energia solar nas escolas", 77: "o CDP Unilivre do Professor", 79: "concurso de professores no mandato",
    80: "o centro especializado para síndrome de Down", 81: "a inclusão de Economia Doméstica no currículo", 85: "o Centro de Atenção ao Paciente Crônico",
    86: "o licenciamento sanitário digital", 87: "o hospital-dia municipal", 88: "Ruas de Lazer nas 10 regionais", 89: "o Espaço do Conhecimento Jovem",
    90: "novas Praças Olímpicas no mandato (as do Cajuru e da CIC são de 2018)", 91: "o Centro de Atenção ao Esporte e Atividade Física",
    92: "a Bolsa Desempenho Esportivo", 93: "o Selo Esportivo", 94: "o Memorial do Esporte", 95: "a Rede Jovem e o Indicador Jovem",
    96: "projeto de nova Lei de Incentivo à Cultura", 97: "o programa Mulheres Fortes", 98: "o programa Família Segura", 99: "o programa Eu Me Viro",
    103: "a República para Migrantes", 105: "o Liceu de Ofícios da Aprendizagem Profissionalizante", 106: "o LiceudeOficios.com",
    107: "o Liceu de Ofícios itinerante", 108: "o sistema de atendimento móvel da FAS", 109: "a UniFAS", 110: "balanço de ampliação do PPE e do 1º EmpregoTech",
    111: "o programa Impacta Curitiba", 112: "convênio com o Estado para regularizar ocupações em áreas estaduais", 113: "o sistema integrado de tratamento de resíduos do consórcio",
    114: "QR code nas placas de ruas", 115: "o programa Ruas de Convivência", 116: "a criação de festival de inverno no mandato",
    117: "os aplicativos temáticos do Viva Curitiba", 118: "e-books com histórias de Curitiba",
}
for _k, _v in _RESTO.items():
    D.setdefault(_k, S(_v + "."))
D.update({
    19: S("a criação da Patrulha Ambiental da Guarda Municipal."),
})
D.update({
    22: C("O Centro de Controle Operacional da Muralha Digital passou a operar com mais de 2 mil câmeras e recebeu em 2023 novas câmeras e 515 câmeras corporais da Guarda Municipal monitoradas em tempo real.", CWB + "mais-cameras-na-muralha-digital-e-investimentos-no-monitoramento-do-clima-impulsionam-seguranca-em-curitiba/71827", "2023-12", "media"),
    47: N("O Parque Linear do Bairro Novo do Caximba, às margens do Barigui, só teve o edital de obras aberto em 2026.", CWB + "prefeitura-abre-edital-do-parque-linear-do-bairro-novo-do-caximba-que-impede-cheias-e-devolve-dignidade-ao-bairro/84941", "2026"),
    57: C("Greca inaugurou em fev/2024 o Ecoponto Metropolitano do São Braz, 12º da cidade.", CWB + "rafael-greca-inaugura-o-ecoponto-metropolitano-no-sao-braz-o-12-de-curitiba/72143", "2024-02", "media"),
    58: Pc("Em 2022 a Prefeitura lançou a compostagem comunitária nos Ecopontos, com coleta de orgânicos trazidos pela população; não foi localizado programa de compostagem domiciliar.", CWB + "greca-lanca-o-programa-de-compostagem-em-ecopontos-de-curitiba/65653", "2022-10", "baixa"),
    79: C("O concurso de 2022 (589 vagas) teve resultado em abr/2023 e as nomeações seguiram em 2023 e 2024, quando foram nomeados mais de 1.300 professores.", CWB + "so-em-2024-prefeitura-de-curitiba-nomeou-mais-de-1300-professores/72363", "2024"),
})

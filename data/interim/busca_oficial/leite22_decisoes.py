# Classificação do censo de Eduardo Leite (RS, 2022). Mandato 2023-2026 em curso; data de corte 2026-11-24.
# Fontes: notícias do governo do Estado (estado.rs.gov.br) e imprensa, por resumos de busca. Medidas iniciadas =
# em_andamento; sem registro = não cumprida, confiança baixa (Diário Oficial e Assembleia não consultados). As
# enchentes de abr-mai/2024 redirecionaram parte da agenda para o Plano Rio Grande (reconstrução).
# Chave = índice (1-based) em leite22_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia).
SEM = "Busca nas notícias do governo do Rio Grande do Sul e na imprensa (jan/2023 a nov/2026) não localizou "
RS = "https://www.estado.rs.gov.br/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


def A(txt, url, data, conf="media"):
    return ("em_andamento", conf, txt, url, data)


def C(txt, url, data, conf="alta"):
    return ("cumprida", conf, txt, url, data)


D = {
    1: A("O Estado lançou o Mãe Gaúcha (kits para bebês e mães vulneráveis, 2024) e, em set/2025, o programa Família Gaúcha, que acompanha famílias em pobreza e extrema pobreza em 92 municípios; não há programa específico de pobreza infantil.", RS + "leite-lanca-programa-familia-gaucha-para-reduzir-vulnerabilidades-sociais-apos-eventos-meteorologicos-no-rs", "2025-09", "baixa"),
    2: S("o Plano Estadual da Juventude."),
    3: C("Os cinco Centros da Juventude prometidos foram entregues, o último (Restinga, sexta unidade do programa) em abr/2025.", RS + "leite-e-gabriel-concluem-entrega-historica-dos-centros-da-juventude-do-pod-com-inauguracao-da-sexta-unidade-na-restinga-em-por", "2025-04"),
    4: A("As obras dos Cases de Osório, Santa Cruz do Sul e Viamão (R$ 65 milhões) estão em andamento; nenhum foi inaugurado.", RS + "governador-visita-obra-de-construcao-do-centro-de-atendimento-socioeducativo-de-santa-cruz-do-sul", "2025"),
    7: S("a implantação de casas-abrigo regionalizadas para mulheres."),
    8: S("as obras da Casa da Mulher Gaúcha (a Casa da Mulher Brasileira de Porto Alegre, federal, seguia travada por falta de terreno em out/2025)."),
    10: S("casas-abrigo para pessoas trans."),
    11: S("o Plano Estadual da Pessoa LGBTQIA+."),
    14: A("O Alfabetiza Tchê (Lei 16.048/2023) reúne os 497 municípios, com mentoria a 1,8 mil escolas, material didático e premiação; a meta de alfabetizar todos até o 2º ano não foi alcançada (o indicador caiu em 2024).", RS + "como-o-governo-do-estado-esta-investindo-na-alfabetizacao-das-criancas", "2025"),
    21: C("O Estado criou bolsas em universidades comunitárias: o RS Talentos (engenharias e computação, R$ 2 mil por mês) e o Professor do Amanhã (500 bolsas em licenciaturas).", RS + "em-cerimonia-no-piratini-eduardo-leite-lanca-700-novas-bolsas-de-graduacao-em-licenciaturas-e-engenharias", "2025-11"),
    22: C("O Alfabetiza Tchê premia as 200 escolas com melhores resultados de alfabetização (R$ 40 mil a R$ 80 mil) e outras 200 em evolução.", RS + "governador-eduardo-leite-entrega-premiacao-para-as-200-escolas-com-os-melhores-resultados-no-programa-alfabetiza-tche", "2025"),
    23: A("O Estado criou o modelo Escola+, homologado pelo FNDE em 2025, com as primeiras obras licitadas (R$ 48 milhões), e concluiu 600 obras em escolas desde 2023.", RS + "governo-leite-atinge-a-marca-de-600-obras-concluidas-em-escolas-desde-2023", "2026"),
    24: A("O governo apresentou PPP de infraestrutura escolar para 98 escolas e mantém programa contínuo de obras de manutenção (600 concluídas desde 2023).", RS + "eduardo-leite-apresenta-ppp-da-infraestrutura-escolar-que-vai-qualificar-instalacoes-de-98-escolas-estaduais", "2025", "baixa"),
    30: C("A CIPTEA, criada em 2021, ganhou sistema digital de solicitação e acompanhamento pela Faders.", RS + "rio-grande-do-sul-avanca-em-inclusao-e-acessibilidade-com-lancamento-de-sistema-digital-do-passe-livre-e-da-ciptea", "2025", "media"),
    27: C("A Portaria SES 750/2023 destinou R$ 30 milhões a hospitais de pequeno porte, com novo repasse em 2024, e o SUS Gaúcho prevê mais R$ 40,2 milhões até 2026.", RS + "governo-do-estado-destina-r-30-milhoes-para-hospitais-de-pequeno-porte", "2023-08"),
    46: C("O Inventário Estadual de Emissões de Gases de Efeito Estufa (2018-2023), feito com o ICLEI, foi apresentado em out/2025.", RS + "governo-leite-reduz-em-26-8-as-emissoes-liquidas-de-gases-de-efeito-estufa-entre-2021-e-2023-no-rs", "2025-10"),
    61: A("Microaçudes do Irriga+ RS seguem sendo entregues nos municípios, mas não foi localizado balanço da conclusão das 6.025 obras previstas.", "https://www.revistacultivar.com.br/noticias/governo-do-rs-inaugura-microacudes-em-campina-das-missoes", "2025", "baixa"),
    62: A("A estrutura principal da barragem Jaguari foi concluída em abr/2026 (R$ 365,7 milhões) e a contratação dos canais começou; a do Taquarembó, retomada em 2025, tem conclusão prevista para o fim de 2026.", RS + "governo-leite-finaliza-estrutura-principal-da-barragem-jaguari-em-sao-gabriel", "2026-05", "alta"),
    69: A("Dos 62 municípios sem acesso asfáltico em 2019, 26 tiveram o acesso concluído até ago/2025; o governo previa iniciar em 2025 as obras de todos os 21 restantes, e várias seguem em execução (Pirapó, até 2027).", RS + "em-seis-anos-estado-realiza-maior-investimento-da-historia-em-acessos-asfalticos-com-recursos-proprios", "2025-08"),
    78: A("O Estado vem pagando precatórios pelo plano de quitação (R$ 2 bilhões até ago/2025 e R$ 976 milhões previstos para 2026), ajustado à EC 136/2025.", RS + "estado-destinara-r-976-milhoes-a-pagamento-de-precatorios-em-2026", "2026"),
    34: C("O Plano Estadual do Esporte e Lazer (2022-2032) foi sancionado e está em execução.", RS + "governador-sanciona-plano-estadual-do-esporte-e-lazer", "2022-12", "baixa"),
    39: S("lei que transforme o RS Seguro em política de Estado."),
    40: C("O Decreto 57.060, de 15/06/2023, instituiu 21 Regiões Integradas de Segurança Pública, cobrindo os 497 municípios.", RS + "em-seis-anos-rs-seguro-fortalece-a-integracao-entre-as-forcas-de-seguranca-e-investimentos-em-inteligencia", "2023-06"),
    41: S("a nova sede da Secretaria da Segurança Pública."),
    43: A("Entre as oito unidades prometidas, a nova Cadeia Pública de Porto Alegre (1.884 vagas) foi inaugurada em set/2025 e a Penitenciária de Charqueadas II começou a receber presos em dez/2023; as demais seguem em obras.", RS + "governador-leite-inaugura-nova-cadeia-publica-de-porto-alegre-marco-historico-na-seguranca-e-dignidade-do-sistema-prisional", "2025-09"),
}
D.update({
    53: C("O A Casa É Sua – Município prevê 2.052 moradias em 57 municípios (R$ 162,3 milhões), com mais de mil entregues até out/2025, e ganhou a modalidade Calamidade após as enchentes (2.857 unidades).", RS + "governo-do-estado-apresenta-balanco-de-acoes-nas-areas-da-habitacao-e-regularizacao-fundiaria-no-rio-grande-do-sul", "2025-10"),
    54: C("O Nenhuma Casa sem Banheiro entregou módulos sanitários a 1.410 famílias em 60 municípios (R$ 14,9 milhões) e foi incluído na Lei 16.138/2024.", RS + "estado-formaliza-convenios-para-a-construcao-de-501-casas-populares-e-222-modulos-sanitarios", "2024", "media"),
    57: A("O Agro Inovar RS, lançado na Expointer 2025, busca fazer do Parque Assis Brasil uma arena de inovação do agro, e um Hub Agro (Feevale e Prefeitura de Esteio) abriu no parque em ago/2024; o parque tecnológico ainda não existe.", "https://www.jornaldocomercio.com/agro/2025/08/1215902-agro-inovar-rs-transforma-expointer-em-vitrine-de-inovacao-rural.html", "2025-08", "baixa"),
    76: A("Abriram novas unidades do Tudo Fácil no interior (Canoas em fev/2026, Tramandaí em jun/2026, com Uruguaiana contratada) e a da Zona Sul de Porto Alegre foi reformada; a unidade no Centro Administrativo não foi localizada.", RS + "governo-leite-inaugura-unidade-do-tudo-facil-em-canoas-e-reforca-atendimento-na-regiao-metropolitana", "2026-06"),
    79: C("O Devolve ICMS teve a parcela fixa elevada de R$ 100 para R$ 150 por trimestre em 2024 e o teto variável ampliado em 55% em 2025.", RS + "em-tres-anos-de-devolve-icms-governo-do-estado-restituiu-mais-de-r-700-milhoes-para-pessoas-de-baixa-renda", "2025-01"),
})
_RESTO = {
    5: "programa integrado de acolhimento para a população de rua", 6: "plano estadual de moradia para a população de rua",
    9: "balanço de ampliação dos Centros Municipais de Referência da Mulher", 12: "plano estadual de acessibilidade com os municípios",
    13: "balanço de ampliação do programa de castração (Melhores Amigos)", 15: "balanço da ampliação do tempo integral nos anos finais",
    16: "balanço da ampliação das escolas de ensino médio em tempo integral", 17: "programa de inovação no contraturno do ensino médio",
    18: "programa de aprendizagem e empreendedorismo para jovens a partir de 14 anos", 19: "a oferta de duas refeições diárias pelo Merenda Melhor",
    20: "a ampliação das Cipaves pelo Cipave+", 25: "balanço de ampliação do Conecta RS", 26: "Centros de Vacinação nas maiores cidades",
    28: "plataforma pública dos contratos hospitalares", 29: "programa estadual de telemedicina com atendimento nos presídios",
    31: "ambulatórios de referência para idosos nas macrorregiões", 32: "a adesão ao Pacto Nacional da Pessoa Idosa",
    33: "rede de informações de saúde por SMS ou WhatsApp", 35: "a conclusão das obras do Cete",
    36: "a lei do financiamento parcialmente reembolsável na cultura", 37: "a conclusão das obras do MAC, do Museu Julio de Castilhos e do Multipalco",
    38: "sistema eletrônico de gestão dos investimentos culturais", 42: "novos núcleos de triagem como o Nugesp no interior",
    44: "a conclusão das reformas dos presídios de Passo Fundo e Cachoeira do Sul", 45: "pavilhões de trabalho nos presídios",
    47: "plano estadual de transição energética", 48: "editais de Pagamento por Serviços Ambientais", 49: "a conclusão do Plano Estadual de Saneamento",
    50: "programa permanente de suficiência hídrica além do Irriga+ e das barragens", 51: "regulamentação do mercado estadual de créditos de carbono",
    52: "o Plano de Desenvolvimento Urbano Integrado metropolitano", 55: "a atualização do Plano e do Fundo Estadual de Habitação",
    56: "a reunião de habitação, regularização e terras devolutas num só órgão", 58: "programa de fomento a edtechs",
    59: "programa de formação e atração de talentos para a inovação", 60: "a regulamentação do Bioma Pampa e dos Campos de Altitude",
    63: "balanço de ampliação do Energia Forte no Campo", 64: "a atualização da Política Estadual de Recursos Hídricos",
    65: "a Política Integrada de Desenvolvimento", 66: "a unificação das plataformas de promoção do turismo",
    67: "conteúdo de turismo no currículo", 68: "o projeto de ativos imobiliários do Estado",
    70: "o plano de mobilidade urbana sustentável e a nova concessão do transporte metropolitano", 71: "rede de terminais hidroviários interiores",
    72: "o escritório de projetos de obras estratégicas", 73: "a conclusão dos sistemas de compras, contratos e Portal do Fornecedor",
    74: "núcleo de monitoramento dos investimentos das concessões e PPPs", 75: "o portal de imóveis do Estado",
    77: "totens de autosserviço nas unidades do Tudo Fácil e em municípios", 80: "melhora da nota de capacidade de pagamento (Capag) do Estado",
}
for _k, _v in _RESTO.items():
    D.setdefault(_k, S(_v + "."))

# Classificação do censo de ACM Neto (prefeitura de Salvador, 2016). Mandato 2017-2020 encerrado; avaliado até
# 31/12/2020 (entregas de 2021 em diante não contam). Fontes: Relatórios de Atividades anuais 2017-2020 da Casa Civil
# (por eixo; cópia em ssa_relatorios_2017_2020/), imprensa (Bahia Notícias, Correio), o Diário Oficial do Município (scripts/busca_ssa.py; resultados em acmneto_ssa_2016.json), o balanço da gestão
# 2013-2020 feito no plano de 2020 de Bruno Reis (registrado no TSE), o Relatório de Atividades 2021-2024 (para datar
# o que só foi entregue depois) e a imprensa. As notícias do site da Prefeitura só existem a partir de 2021.
# Como o Diário Oficial foi consultado, "sem registro" = não cumprida com confiança média.
SEM = "Busca no Diário Oficial do Município (2017-2020), nos Relatórios de Atividades anuais 2017-2020 da Prefeitura, no balanço do plano de 2020, no Relatório 2021-2024 e na imprensa não localizou "
RA = "https://casacivil.salvador.ba.gov.br/wp-content/uploads/2025/02/Relatorio-Atividades-2020.pdf"
BN = "https://www.bahianoticias.com.br/noticia/237245-acm-neto-cumpriu-uma-de-cinco-promessas-para-a-comunidade-lgbt-feitas-na-campanha"
P20 = "https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2020_BA.zip"  # plano de 2020 (2020BA50000674223.pdf)
R24 = "https://salvadorpar.com.br/wp-content/uploads/2025/03/Relatorio-de-Atividades-PMS-2021-2024.pdf"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


def C(txt, url=P20, data="2020-09", conf="alta"):
    return ("cumprida", conf, txt, url, data)


def P_(txt, url=P20, data="2020-09", conf="media"):
    return ("parcialmente_cumprida", conf, txt, url, data)


def NC(txt, url=P20, data="2020-09", conf="alta"):
    return ("nao_cumprida", conf, txt, url, data)


D = {
    1: S("dado de que todas as creches municipais passaram a ter matrícula em tempo integral."),
    2: C("O balanço do plano de 2020 diz que Salvador foi a primeira do país em cobertura da educação infantil (PNAD 2019) e trata a pré-escola como universalizada.", conf="media"),
    3: P_("As Escolabs ofertaram 1.750 vagas de tempo integral em 2018 (a unidade piloto tinha 1.200), mas caíram para 1.166 em 2019; não houve expansão contínua.", "https://casacivil.salvador.ba.gov.br/wp-content/uploads/2024/11/2-Relatorio-de-Atividades-2018-DESENVOLVIMENTO-HUMANO.pdf", "2019", "baixa"),
    4: C("A Atenção Domiciliar foi implantada: o plano de 2020 propõe ampliá-la e em 2021 a cidade já tinha 13 equipes (EMAD).", conf="media"),
    5: NC("A rede continuou com quatro Multicentros de 2017 a 2020, os mesmos de 2016, segundo os Relatórios de Atividades.", RA, "2020-12"),
    6: C("O Hospital Municipal de Salvador, em Cajazeiras, iniciou as operações em 2019 (227 leitos, 47 de UTI).", "https://dom.salvador.ba.gov.br/diario/busca?q=Hospital+Municipal+de+Salvador+iniciou", "2019"),
    7: C("Com outro nome: em 2018 a Prefeitura conduzia com o Unicef o projeto da Plataforma dos Centros Urbanos, para reduzir as desigualdades que afetam crianças e adolescentes.", "https://casacivil.salvador.ba.gov.br/wp-content/uploads/2024/11/2-Relatorio-de-Atividades-2018-DESENVOLVIMENTO-HUMANO.pdf", "2018", "baixa"),
    8: NC("Em 2021 havia só 4 Espaços Boca de Brasa (Subúrbio, Valéria, Cajazeiras e Barroquinha), não 10.", R24, "2024-12"),
    9: NC("Os Relatórios de Atividades até 2020 só registram o CRAM Loreta Valadares e o CAMSID; não houve novos centros no Subúrbio e em Cajazeiras.", RA, "2020-12", "media"),
    10: S("funcionamento do Fundo Municipal da Pessoa Idosa."),
    11: C("Segundo o Relatório de Atividades 2020, o Programa de Combate ao Racismo Institucional mobilizou 100% dos servidores e colaboradores municipais.", RA, "2020-12", "media"),
    12: C("A Prefeitura criou o conselho municipal de promoção da cidadania LGBT, a única das cinco promessas LGBT cumprida até jun/2019, segundo o Bahia Notícias.", BN, "2019-06", "media"),
    13: C("O Programa de Combate à LGBTfobia Institucional foi implementado, segundo o balanço do plano de 2020."),
    14: NC("Até jun/2019 o atendimento itinerante do Centro de Referência LGBT não tinha sido implantado (Bahia Notícias); os relatórios de 2019 e 2020 não o registram.", BN, "2019-06", "media"),
    15: C("O Centro de Referência LGBT passou a oferecer acompanhamento e assistência jurídica para retificação de prenome e gênero (Relatórios de Atividades 2017 e 2018); o Bahia Notícias considerava a promessa pendente em jun/2019.", "https://casacivil.salvador.ba.gov.br/wp-content/uploads/2024/11/2-Relatorio-de-Atividades-2018-DESENVOLVIMENTO-HUMANO.pdf", "2018", "baixa"),
    16: NC("Até jun/2019 o programa de empreendedorismo LGBT não tinha sido criado (Bahia Notícias); os relatórios de 2019 e 2020 não o registram.", BN, "2019-06", "media"),
    17: C("O Centro Especializado em Reabilitação (CER) de Coutos, no Subúrbio, foi instalado, segundo o balanço do plano de 2020.", conf="media"),
    18: S("programa Ambulante Legal."),
    19: P_("Os mercados de São Miguel e de Jardim Cruzeiro foram requalificados até 2020; os de São Cristóvão e do Curtume ficaram para 2021-2024.", RA, "2020-12"),
    20: NC("A reforma do Mercado Modelo (três etapas) foi feita de 2021 a 2024, depois do mandato.", R24, "2024-12", "media"),
    21: S("os camelódromos prometidos no mandato (os de São Cristóvão, Sussuarana e Mussurunga são de 2021-2024)."),
    22: C("O SIMM Digital foi criado, segundo os Relatórios de Atividades 2018 e 2020.", RA, "2020-12", "media"),
    23: NC("O Escritório Público de Arquitetura e Engenharia já existia desde 2001, centralizado na Seinfra; não foram criados escritórios em cada prefeitura-bairro.", RA, "2020-12", "media"),
    24: S("plantas pré-aprovadas para novas construções."),
    25: NC("O Morar Melhor chegou a cerca de 54 mil moradias reformadas até 2024, das quais mais de 20 mil em 2021-2024; até 2020 ficou em torno de 34 mil, longe das 100 mil prometidas.", R24, "2024-12", "media"),
    26: S("programa habitacional Casa Segura."),
    27: S("programa habitacional Casa Solidária."),
    28: NC("A Central de Videomonitoramento da Guarda Municipal (R$ 20 milhões, Prodetur) foi construída na gestão seguinte, segundo o plano de 2024.", "https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2024_BA.zip", "2024-08", "media"),
    29: S("uso do Cartão Social como prontuário de acompanhamento das famílias."),
    30: P_("A nova licitação da limpeza urbana saiu em 2018, como contrato de serviço por lotes (24 meses, prorrogável), e não como concessão; não foi localizado o novo plano setorial de resíduos.", "https://www.bnews.com.br/noticias/salvador/208420-dois-consorcios-e-tres-empresas-disputam-licitacao-para-limpeza-urbana-da-capital.html", "2018", "baixa"),
    31: S("nova Estação de Transbordo."),
    32: S("usina de processamento de entulho."),
    33: S("pontos limpos em áreas de difícil acesso."),
    34: NC("A cidade não chegou a 9 ecopontos no mandato: o oitavo ecoponto só foi inaugurado em ago/2026.", "https://salvador.ba.gov.br/salvador-ganha-novos-ecopontos-para-facilitar-descarte-correto-de-residuos/", "2026-10"),
    35: S("uso de contêineres de carga lateral e ampliação dos subterrâneos no mandato."),
    36: S("rastreamento da frota de limpeza."),
    37: C("Em 2019 a Prefeitura lançou o Iluminando Nosso Bairro para levar LED a toda a cidade; até 2020 foram mais de 100 mil pontos de iluminação em LED.", RA, "2020-12"),
    38: NC("Os semáforos inteligentes foram introduzidos na gestão seguinte (176 implantados de 2021 a 2024).", R24, "2024-12", "media"),
    39: NC("O primeiro trecho da nova orla de Stella Maris começou em 2020 e ficou para ser concluído na gestão seguinte.", conf="media"),
    40: NC("A orla de Escada–Praia Grande–Periperi só começou a ser requalificada em 2024.", "https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2024_BA.zip", "2024-08"),
    41: C("O balanço do plano de 2020 lista Ondina entre os trechos de nova orla feitos (no balanço de 2016 só constava o Rio Vermelho).", conf="media"),
    42: P_("Foi executada a primeira fase da orla do Cantagalo, entre o Largo da Boa Viagem e o Forte de Monte Serrat; o restante ficou para a gestão seguinte."),
    43: S("concurso nacional de urbanismo para a orla de Pituaçu."),
    44: S("reurbanização do eixo Iguatemi–Retiro."),
    45: S("reestruturação do entorno do Dique do Tororó e da Arena Fonte Nova."),
    46: NC("As obras do Novo Mané Dendê só começaram em 2020; a primeira etapa foi entregue em set/2022.", conf="media"),
    47: S("programa Mirantes da Baía."),
    48: S("Programa Centro de Bairro."),
    49: NC("A primeira fase das obras de requalificação do Jardim Botânico só foi contratada em set/2019 e não foi concluída no mandato.", RA, "2019-09", "media"),
    50: NC("Os parques de Pirajá/São Bartolomeu e de Ipitanga I não foram implantados; o plano de 2020 os promete de novo.", conf="media"),
    51: NC("O BRT estava em obras em 2020 e só começou a operar em set/2022.", "https://www.bahianoticias.com.br/noticia/269231-brt-de-salvador-inicia-operacao-em-setembro-com-24-onibus-oito-veiculos-serao-eletricos", "2022"),
    52: C("A rede cicloviária passou de 87 km (2016) para mais de 280 km (2020)."),
    53: S("implantação da Avenida Mané Dendê."),
    54: NC("A ligação Mata Escura–BR-324 foi iniciada, mas não concluída no mandato; só ficou pronta (Av. Batatinha) em 2021-2024."),
    55: C("A Estrada Velha do Aeroporto virou a Nova Aliomar Baleeiro, segundo o balanço do plano de 2020.", conf="media"),
    56: S("pavimentação e drenagem do bairro de São Cristóvão."),
    57: S("duplicação da Alameda das Praias."),
    58: NC("A ligação Pau da Lima–Gal Costa estava em execução em 2020 e só ficou pronta (Av. Jayme Fygura) em 2021-2024."),
    59: P_("As obras do Canal do Paraguari começaram em nov/2019 e só foram concluídas em nov/2022, na gestão seguinte.", RA, "2020-12", "baixa"),
    60: S("a elaboração de 80 Planos Preventivos de Defesa Civil para encostas."),
    61: S("os 20 planos preventivos para áreas alagáveis."),
    62: S("a correção de 10 pontos críticos de alagamento."),
    63: C("A Estratégia de Resiliência de Salvador foi elaborada, com 60 iniciativas, segundo o plano de 2020."),
    64: NC("A Cidade da Música da Bahia (Museu da Música) foi implantada em 2021, depois do mandato.", R24, "2024-12"),
    65: NC("A Casa da História de Salvador estava com a obra recém-iniciada em 2020 e só foi inaugurada na gestão seguinte."),
    66: C("O Mercado de São Miguel foi requalificado até 2020, segundo o Relatório de Atividades 2020.", RA, "2020-12", "media"),
    67: S("Semana da Independência no calendário turístico (o Memorial 2 de Julho foi requalificado para o bicentenário, em 2022-2023)."),
    68: S("centrais de informações turísticas criadas no mandato."),
    69: S("editais de cursos livres de arte nos bairros."),
    70: C("O PIDI está entre os incentivos implementados pela gestão, segundo o Relatório de Atividades 2020.", RA, "2020-12", "media"),
    71: C("O Programa Revitalizar foi criado pela Lei 9.215/2017, com incentivos e edificação compulsória no Centro Antigo."),
    72: S("criação do Prolog."),
    73: S("novos centros de controle para limpeza urbana, comércio ambulante e Guarda Municipal."),
    74: S("contrato de programa com a Embasa."),
    75: S("concessões de iluminação pública, limpeza ou estacionamentos no mandato."),
    76: C("O Sistema de Informações Municipais (Salvador Dados) foi estruturado a partir de 2017.", "https://casacivil.salvador.ba.gov.br/wp-content/uploads/2024/11/8-Relatorio-de-Atividades-2017-DESENVOLVIMENTO-INSTITUCIONAL-E-ENGAJAMENTO-DO-CIDADAO.pdf", "2017", "baixa"),
    77: S("Consórcio Intermunicipal da Baía de Todos os Santos."),
    78: S("Marca Salvador e portal turístico no mandato."),
    79: S("Conselhos de Bairro."),
}
AJUSTES = {}

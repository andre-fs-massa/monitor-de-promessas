# Classificação do censo de Rafael Greca (Curitiba, 2016). Mandato 2017-2020 encerrado (reeleito); avaliação até
# 31/12/2020: o que foi entregue depois conta como não cumprido neste mandato. Fontes: notícias da Prefeitura de
# Curitiba e imprensa, lidas por resumos de busca (o site da Prefeitura não pôde ser aberto diretamente). Sem
# registro = não cumprida, confiança baixa.
# Chave = índice (1-based) em greca16_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia).
SEM = "Busca nas notícias da Prefeitura de Curitiba e na imprensa (2017 a 2020) não localizou "
CWB = "https://www.curitiba.pr.gov.br/noticias/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


D = {
    1: ("parcialmente_cumprida", "media", "A reforma administrativa aprovada em 2017 extinguiu e fundiu secretarias, mas o número de comissionados voltou a crescer: segundo o TCE-PR, chegou a 559 em 2019, 27% acima de 2017.", "https://www.gazetadopovo.com.br/parana/greca-comissionados-aumento-2019/", "2019"),
    2: S("balanço da revitalização dos seis bairros (o projeto do Bairro Novo do Caximba é do mandato seguinte)."),
    3: ("cumprida", "baixa", "O Centro de Controle Operacional da Muralha Digital começou a funcionar em 2020, integrando videomonitoramento, Guarda Municipal e outros serviços.", CWB + "centro-de-controle-operacional-da-muralha-digital-de-curitiba-comeca-a-funcionar/57562", "2020"),
    4: S("canal 24 horas com o prefeito e equipe de plantão."),
    5: ("cumprida", "alta", "O aplicativo Saúde Já, para agendamento de consultas, foi lançado nos primeiros 100 dias de gestão (2017) e premiado em 2018.", CWB + "audiencia-publicas-aplicativo-saude-ja-e-os-100-dias-de-gestao/41849", "2017-04"),
    6: ("cumprida", "baixa", "O Policiamento Ostensivo de Proximidade já operava ao fim do mandato: o plano de 2020 propõe ampliá-lo.", "https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2020_PR.zip", "2020"),
    7: ("nao_cumprida", "media", "A reintegração do transporte de Curitiba ao metropolitano só ocorreu em 2024, no mandato seguinte.", CWB + "transporte-coletivo-de-curitiba-volta-a-ser-forte-com-reintegracao-metropolitana-e-entrada-na-eletromobilidade/75311", "2024-12"),
    8: S("o veículo leve sobre a ferrovia até o aeroporto."),
    9: ("cumprida", "baixa", "A Prefeitura comprou ônibus novos a partir de 2017 (735 entre 2017 e 2025, 62% da frota).", CWB + "prefeito-de-curitiba-entrega-mais-42-onibus-para-a-frota-do-transporte-coletivo-que-passa-a-ser-100-acessivel/76204", "2025-04"),
    10: ("cumprida", "media", "A Urbs implantou em 2019 tarifa reduzida em linhas de menor demanda, ampliada a mais cinco linhas.", CWB + "urbs-implanta-tarifa-reduzida-em-mais-cinco-linhas-a-partir-desta-terca/53997", "2019"),
    11: ("cumprida", "alta", "A meta de 400 km foi superada: até dez/2020 o Asfalto Novo somou 537 km em 816 ruas (a cidade não ficou 100% asfaltada).", CWB + "asfalto-novo-percorre-537-km-dentro-de-curitiba/57458", "2020-12"),
    12: S("revitalização da área central por meio de PPP (o Rosto da Cidade foi executado diretamente pela Prefeitura)."),
    13: ("cumprida", "media", "O Plano Diretor de Drenagem foi concluído e integrado ao Plano Municipal de Saneamento Básico (Decreto 1.994/2017), e o programa Curitiba Contra Cheias executou obras de macrodrenagem desde 2017.", CWB + "prefeitura-de-curitiba-inicia-atualizacao-do-plano-diretor-de-drenagem-para-fortalecer-protecao-contra-enchentes/77140", "2017"),
    14: ("cumprida", "alta", "A usina solar do Palácio 29 de Março entrou em operação em jun/2019 e a Pirâmide Solar do Caximba, sobre o antigo aterro, foi contratada em 2020.", CWB + "comeca-a-geracao-de-energia-solar-no-palacio-29-de-marco/50791", "2019-06"),
    15: S("incentivo construtivo a empreendimentos com geração de energia."),
    16: ("cumprida", "alta", "A Cohab Solar entregou em mar/2018 as primeiras 26 casas com placas fotovoltaicas e foi ampliada em 2020.", CWB + "prefeitura-entrega-primeiro-conjunto-da-cohab-com-geracao-de-energia-solar/45537", "2018-03"),
    17: S("geração de energia a partir do processamento do lixo nos aterros (a usina do Caximba é solar)."),
    18: S("balanço de redução de 30% na conta de luz da Prefeitura."),
    19: ("cumprida", "alta", "O programa de modernização da iluminação lançado em 2018 trocou 16 mil pontos por LED em 2019, com meta de mais 44 mil em 2020.", CWB + "curitiba-vai-contar-com-60-mil-lampadas-led-ate-2020/52000", "2019"),
    20: S("programa de letramento com as quatro frentes prometidas."),
    21: S("a Faculdade Municipal com curso de Pedagogia."),
    22: ("nao_cumprida", "media", "A universidade para pessoas idosas (Unapi, com o Estado) só começou em nov/2025.", CWB + "universidade-do-idoso-abre-unidades-nas-regionais-cajuru-e-boa-vista/80553", "2025-11"),
    23: S("a retomada do programa Mãe Curitibana."),
    24: S("o Centro de Especialidades de Curitiba."),
    25: S("unidade de estabilização para pacientes de saúde mental em crise."),
    26: S("reativação de leitos e unidades de acolhimento psiquiátricos."),
    27: S("FabLabs e coworkings públicos nas Ruas da Cidadania."),
    28: ("cumprida", "media", "A Rede de Proteção Animal foi intensificada a partir de 2017, com programa municipal de castração que superou as metas.", CWB + "programa-de-castracao-de-caes-e-gatos-ultrapassa-a-meta-de-atendimentos/46966", "2018"),
    29: ("nao_cumprida", "media", "O novo Museu de História Natural não foi implantado: voltou a ser prometido nos planos de 2020 e de 2024.", "https://cdn.tse.jus.br/estatistica/sead/odsele/proposta_governo/proposta_governo_2024_PR.zip", "2026-11"),
}

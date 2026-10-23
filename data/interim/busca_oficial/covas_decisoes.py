# Classificação do censo de Bruno Covas (prefeitura de São Paulo, 2020). Covas morreu em 16/05/2021 e o vice,
# Ricardo Nunes, completou o mandato da mesma chapa: avaliado como mandato encerrado, até 31/12/2024.
# Chave = índice (1-based) em covas_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia)
# ou None para tirar do censo. Fonte principal: relatório de execução do Programa de Metas 2021-2024 (dez/2024).
SEM = "Busca na imprensa, em sites oficiais, no Programa de Metas 2021-2024 e no Catálogo de Legislação Municipal (jan/2021 a dez/2024) não localizou "
PDM = "https://prefeitura.sp.gov.br/documents/d/planejamento/relatorio-de-execucao-do-programa-de-metas-2021-2024_2024-pdf"
PSP = "https://prefeitura.sp.gov.br/"


def S(txt, url="", data="2024-12"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


D = {
    1: ("cumprida", "media", "Em 2022 a Prefeitura lançou o Mãe Paulistana Creche, que reserva vaga em creche para os filhos de gestantes que começam o pré-natal na rede municipal até o 4º mês.", PSP + "web/santana_tucuruvi/w/noticias/120570", "2022"),
    2: ("cumprida", "alta", "Meta 10 do Programa de Metas: a fila por vaga em creche foi zerada e seguia zerada em out/2024.", PSP + "w/noticia/prefeitura-zera-fila-de-creche-pela-primeira-vez-na-historia", "2024-10"),
    3: ("nao_cumprida", "alta", "Meta 25 do Programa de Metas: 5 novos CEUs implementados até nov/2024, de 12 previstos (menos da metade).", PDM, "2024-11"),
    4: S("ampliação da Bolsa Primeira Infância."),
    5: S("transformação de todas as salas de aula em ambientes digitais; houve compra de tablets e equipamentos para o retorno presencial."),
    6: None,  # tablets: a compra dos 465 mil foi contratada em nov/2020, antes da posse
    7: ("cumprida", "alta", "Meta 82 do Programa de Metas: o número de alunos do São Paulo Integral cresceu 133%, acima da meta de 35%.", PDM, "2024-12"),
    8: ("cumprida", "alta", "Os créditos para compra de uniforme e material escolar passaram a ser liberados diretamente às famílias, que compram nas lojas credenciadas.", PSP + "w/noticia/prefeitura-libera-creditos-para-compra-de-material-e-uniforme-escolar-para-mais-de-28-6-mil-novos-estudantes-matriculados-na-rede-municipal", "2022"),
    9: ("cumprida", "media", "O Hospital de Parelheiros ganhou 87 leitos em 2022 e o da Brasilândia passou a funcionar como hospital geral, com pronto-socorro, chegando a cerca de 270 leitos em 2024.", PSP + "w/noticia/pronto-socorro-do-hospital-municipal-da-brasilandia-comeca-a-atender-a-populacao", "2024"),
    10: ("parcialmente_cumprida", "media", "O Hospital Bela Vista - Santa Dulce dos Pobres funcionou como referência para a população de rua, mas foi fechado em nov/2024 após interdição da Vigilância Sanitária.", "https://www.metropoles.com/sao-paulo/nunes-decide-fechar-hospital-interditado-pela-vigilancia-sanitaria", "2024-11"),
    11: ("cumprida", "alta", "O Hospital Municipal Guarapiranga passou a atender pacientes de cuidados prolongados, com relatórios trimestrais de 2024.", PSP + "w/noticia/novo-hospital-municipal-guarapiranga-amplia-rede-de-atendimento-municipal", "2024"),
    12: ("nao_cumprida", "alta", "As obras de ampliação do Sorocabana (futuro Complexo Hospitalar da Lapa, com 317 leitos) só começaram em set/2024, com conclusão prevista para 2027.", PSP + "web/sampa-news/w/prefeitura-avan%C3%A7a-nas-obras-de-amplia%C3%A7%C3%A3o-e-moderniza%C3%A7%C3%A3o-do-complexo-hospitalar-da-lapa", "2024-09"),
    13: ("cumprida", "media", "O Programa Avança Saúde, financiado pelo BID, reformou e ampliou unidades da rede; o Programa de Metas registra 354 unidades de saúde reformadas (meta 04).", PDM, "2024-12"),
    14: ("cumprida", "alta", "Meta 79 do Programa de Metas: 19 novas UPAs até nov/2024, acima das 16 prometidas.", PDM, "2024-11"),
    15: ("nao_cumprida", "alta", "Só o primeiro Centro de Cuidados Integrados, em Ermelino Matarazzo, foi aberto (jun/2024), de 6 prometidos.", PSP + "w/noticia/ermelino-matarazzo-recebera-o-primeiro-centro-de-cuidados-integrados-cci-de-sao-paulo", "2024-06"),
    16: ("cumprida", "media", "A Lei 17.718/2021 regulamentou a telessaúde no município, e a rede passou a oferecer teleconsultas, inclusive de saúde mental, pelo app e-saúdeSP.", "https://ses.sp.bvs.br/wp-content/uploads/2021/11/M_LE-17718_231121.pdf", "2021-11"),
    17: S("treinamento de 60 mil profissionais para atendimento a distância."),
    18: ("parcialmente_cumprida", "alta", "Meta 12 do Programa de Metas: 48.441 moradias de interesse social providas até nov/2024 (meta de 49 mil), cerca de 69% das 70 mil prometidas.", PDM, "2024-11"),
    19: ("cumprida", "alta", "Meta 13 do Programa de Metas: 30.701 famílias beneficiadas com urbanização de assentamentos precários até jun/2024.", PDM, "2024-06"),
    20: ("cumprida", "media", "A Prefeitura informou ter chegado a cerca de 600 mil pontos de LED em dez/2021, 90% do parque de iluminação; a meta 38 (330 mil pontos) foi superada.", PSP + "web/spregula/w/iluminacao_publica/noticias/319281", "2021-12"),
    21: S("número de novos pontos de iluminação instalados; o Programa de Metas não separa os pontos novos dos modernizados."),
    22: ("cumprida", "alta", "Meta 29 do Programa de Metas: 2.015 novos guardas contratados até nov/2024, o dobro do prometido.", PDM, "2024-11"),
    23: ("cumprida", "alta", "Meta 30 do Programa de Metas: 21.320 câmeras integradas até nov/2024 (City Câmeras e, depois, Smart Sampa).", PDM, "2024-11"),
    24: S("instalação de equipamentos de vigilância nas escolas municipais até 2024; a instalação de câmeras em cerca de 400 escolas só foi anunciada em 2025.", "https://www.portaltela.com/politica/2025/09/01/smart-sampa-amplia-monitoramento-com-53-mil-novas-cameras/"),
    25: ("cumprida", "media", "A GCM ampliou a frota do Dronepol, de cerca de 10 drones em 2020 para 31 em 2022.", PSP + "w/noticia/drones-auxiliam-guarda-civil-metropolitana-no-monitoramento-da-cidade-de-sp", "2022-08"),
    26: ("parcialmente_cumprida", "alta", "Meta 49 do Programa de Metas: 75,3% da frota com wi-fi, tomadas USB e ar-condicionado em nov/2024.", PDM, "2024-11"),
    27: ("parcialmente_cumprida", "alta", "Um trecho de 4,1 km do corredor Itaquera-Líder foi entregue em jul/2024; o restante do Leste-Itaquera não foi concluído.", "https://diariodotransporte.com.br/2024/07/05/trecho-de-41-km-do-corredor-itaquera-lider-o-primeiro-exclusivo-para-onibus-na-zona-leste-de-sao-paulo-e-entregue-nesta-sexta-05/", "2024-07"),
    28: ("nao_cumprida", "alta", "O BRT Aricanduva não foi implantado até 2024; a meta 45 previa só viabilizá-lo, e as obras foram autorizadas em jul/2026.", PDM, "2024-12"),
    29: ("cumprida", "alta", "Meta 44 do Programa de Metas: o Aquático começou a operar na represa Billings, integrado ao Bilhete Único.", PDM, "2024-12"),
    30: ("nao_cumprida", "alta", "A duplicação da Estrada do M'Boi Mirim não saiu até 2024: a gestão passou do DER à Prefeitura em mar/2024 e as obras começaram em dez/2025.", PSP + "w/prefeito-anuncia-in%C3%ADcio-das-obras-de-duplica%C3%A7%C3%A3o-da-estrada-do-m-boi-mirim", "2025-12"),
    31: ("nao_cumprida", "alta", "As obras do complexo Pirituba-Lapa, paradas pela Justiça desde 2020, foram retomadas em jan/2024 com previsão de conclusão em dez/2026.", PSP + "w/noticia/prefeito-anuncia-retomada-das-obras-viarias-que-ligarao-pirituba-a-lapa-apos-3-anos-de-paralisacao-pela-justica", "2024-01"),
    32: ("cumprida", "alta", "A malha cicloviária chegou a 731 km no fim de 2023.", PSP + "w/noticia/malha-cicloviaria-da-capital-alcanca-os-731-quilometros-de-extensao", "2024-01"),
    33: ("parcialmente_cumprida", "alta", "Meta 40 do Programa de Metas: manutenção de 1.079.594 m² de calçadas até nov/2024, de 1,5 milhão prometidos.", PDM, "2024-11"),
    34: ("cumprida", "alta", "Meta 59 do Programa de Metas: 14.959 pontos públicos de wi-fi em nov/2024 (a meta era 20 mil).", PDM, "2024-11"),
    35: ("cumprida", "media", "Meta 74 do Programa de Metas: R$ 13,3 bilhões arrecadados com o plano de desestatização entre 2021 e 2024, acima dos R$ 9 bilhões previstos.", PDM, "2024-11"),
    36: ("cumprida", "alta", "Meta 72 do Programa de Metas: 32 praças de atendimento Descomplica SP remodeladas nas subprefeituras.", PDM, "2024-12"),
    37: ("cumprida", "media", "A Renda Básica Emergencial municipal foi prorrogada em 2021 (Lei 17.553/2021), e a meta 01 registra 2,07 milhões de pessoas em programas de transferência de renda ou apoio nutricional.", PDM, "2024-11"),
    38: S("triplicação das vagas em repúblicas de autogestão."),
    39: ("cumprida", "alta", "Meta 55 do Programa de Metas: 3 Estúdios Criativos da Rede Daora implantados até dez/2024.", PDM, "2024-12"),
    40: ("nao_cumprida", "media", "Meta 56 do Programa de Metas (quatro Distritos Criativos) sem nenhum implantado em dez/2024.", PDM, "2024-12"),
    41: ("cumprida", "media", "A Prefeitura abriu o Hub Green Sampa, espaço para startups de negócios sustentáveis, em jun/2021.", "https://forbes.com.br/negocios/2021/06/sao-paulo-ganha-espaco-para-promover-negocios-sustentaveis/", "2021-06"),
    42: ("parcialmente_cumprida", "baixa", "A rede TEIA passou de 7 coworkings públicos para cerca de 22 unidades, mas não foi localizado quantas abriram até 2024.", PSP + "web/desenvolvimento/w/teias-ampliam-programa%C3%A7%C3%A3o-gratuita-em-agosto-com-atividades-voltadas-%C3%A0-inova%C3%A7%C3%A3o-gest%C3%A3o-e-gera%C3%A7%C3%A3o-de-renda", "2026"),
    43: S("criação de áreas 24 horas nas macrorregiões."),
    44: ("parcialmente_cumprida", "alta", "Meta 64 do Programa de Metas: 234.472 árvores plantadas em 2021-2024, cerca de 59% das 400 mil prometidas.", PDM, "2024-11"),
    45: S("implantação do Parque Minhocão."),
    46: ("cumprida", "alta", "O Parque Augusta foi inaugurado em 06/11/2021.", PSP + "w/noticia/prefeitura-inaugura-o-parque-municipal-augusta-201cprefeito-bruno-covas201dno-centro-da-capital", "2021-11"),
    47: ("cumprida", "alta", "O Parque Paraisópolis foi inaugurado em 18/09/2021.", PSP + "w/noticia/com-entrega-neste-sabado-do-parque-de-paraisopolis-a-populacao-cidade-passa-a-ter-110-parques-municipais", "2021-09"),
    48: S("concessão dos parques Trianon, Chácara do Jockey e Chuvisco; a licitação do Jockey não atraiu interessados e a gestão anunciou que não faria novas concessões.", "https://www.gazetasp.com.br/cotidiano/49446-gestao-covas-diz-que-nao-fara-mais-concessao-de-parques/"),
    49: ("cumprida", "media", "Meta 69 do Programa de Metas: 1,14 milhão de toneladas de resíduos deixaram de ir para aterros entre 2021 e 2024, quase o dobro da meta.", PDM, "2024-11"),
}
AJUSTES = {}

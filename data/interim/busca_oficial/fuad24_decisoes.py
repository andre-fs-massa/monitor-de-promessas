# Classificação do censo de Fuad Noman (prefeitura de Belo Horizonte, 2024). Fuad morreu em 26/03/2025 e o vice da
# mesma chapa, Álvaro Damião, assumiu (mesmo tratamento de Covas/Nunes): mandato em curso, data de corte 2026-10-23.
# Critério de mandato em curso: iniciada = em andamento; entregue = cumprida; prazo vencido julgado normalmente.
# Chave = índice (1-based) em fuad24_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia) ou None.
SEM = "Busca na imprensa, no site da Prefeitura e no Plano de Metas 2025-2028 (jan/2025 a out/2026) não localizou "
PBH = "https://prefeitura.pbh.gov.br/noticias/"
PDM = "https://prefeitura.pbh.gov.br/sites/default/files/estrutura-de-governo/planejamento/2025/plano-de-metas-2025-2028-revisada-30.09.25.pdf"


def S(txt, url="", data="2026-10"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


D = {
    1: ("em_andamento", "alta", "Dois dos três viadutos da Cristiano Machado foram entregues (Waldomiro Lobo, com todas as alças em out/2025, e Saramenha, em jun/2026); o da Sebastião de Brito segue em obras.", PBH + "pbh-libera-transito-no-novo-viaduto-da-cristiano-machado-com-avenida-saramenha", "2026-06"),
    2: ("em_andamento", "alta", "A trincheira da Cristiano Machado com o boulevard em frente à Catedral Cristo Rei está em obras desde set/2025, com conclusão prevista para o 2º semestre de 2028.", PBH + "segundo-turno-de-trabalho-acelera-obras-da-trincheira-cristo-rei-regiao-norte-da-capital", "2026"),
    3: ("em_andamento", "baixa", "A obra da nova maternidade do Odilon Behrens começou em set/2022, com entrega prevista para 2025; não foi localizada a inauguração até out/2026.", "https://diariodocomercio.com.br/negocios/odilon-behrens-expandira-atendimento-nova-maternidade-2025/", "2026-10"),
    4: ("em_andamento", "alta", "Desde 2025 foram entregues cerca de 11 novos centros de saúde pela PPP (a cidade chegou a 154 unidades, a 61ª da PPP em mai/2026), de 20 prometidos.", PBH + "60-novos-centros-de-saude-entregues-pela-pbh-beneficiam-cerca-de-900-mil-pessoas", "2026-05"),
    5: ("em_andamento", "baixa", "A Prefeitura anunciou a continuidade do projeto de mobilidade do Belvedere, com obras previstas para começar no 1º semestre e terminar no fim de 2026.", PBH + "alvaro-damiao-anuncia-continuidade-de-projeto-de-mobilidade-no-belvedere", "2026"),
    6: ("em_andamento", "media", "O BRT Amazonas está em estudos e projetos (contrato aditado em out/2026); a licitação das obras está prevista para 2027 e a execução para 2028-2030.", "https://diariodotransporte.com.br/2026/10/07/contrato-dos-projetos-do-brt-amazonas-de-belo-horizonte-mg-aumenta-r-162-milhao-para-levantamentos-sondagens-e-ensaios/", "2026-10"),
    7: ("em_andamento", "media", "O reservatório Vilarinho II, parado em 2025 por suspeita de irregularidades, teve nova licitação para conclusão aberta até out/2026; a estrutura opera com metade da capacidade.", PBH + "pbh-abre-licitacao-para-conclusao-das-obras-do-reservatorio-vilarinho-ii-em-venda-nova", "2026-10"),
    8: ("em_andamento", "media", "O Anel Rodoviário foi municipalizado em jun/2025, com R$ 60 milhões da União para novas alças e viaduto; a Câmara aprovou empréstimo de até R$ 1 bilhão para as obras.", "https://diariodocomercio.com.br/economia/anel-rodoviario-transferido-prefeitura-belo-horizonte/", "2025-06"),
    9: ("em_andamento", "media", "O programa Centro de Todo Mundo segue com obras em praças e vias do Centro; a revitalização não foi concluída.", PBH + "programa-centro-de-todo-mundo-contabiliza-oito-obras-em-andamento-na-capital", "2026"),
    10: ("em_andamento", "media", "O Programa de Qualificação das Centralidades (Decreto 18.840/2024) entregou o plano de ação da centralidade Waldomiro Lobo e elabora os de outras regiões.", PBH + "pbh-entrega-plano-de-acao-waldomiro-lobo-durante-o-bhfeliz-no-guarani", "2026"),
    11: ("em_andamento", "media", "A licitação de R$ 110 milhões do Parque Ciliar do Onça, aberta em 2025, foi suspensa para revisão e deve ser retomada em 2026; uma primeira etapa de melhorias já foi entregue.", "https://ofator.com.br/informacao/pbh-adia-licitacao-de-r-110-milhoes-para-obras-no-ribeirao-do-onca/", "2026"),
    12: ("em_andamento", "baixa", "O Parque do Aterro (Taiobeiras) está em projeto, incluído no programa BH Verde Azul (consulta de jun/2026), sem obra iniciada.", "https://prefeitura.pbh.gov.br/sites/default/files/estrutura-de-governo/obras-e-infraestrutura/2026/apresentacao-consulta-bh-verde-azul-22-06-26.pdf", "2026-06"),
    13: ("em_andamento", "media", "O corredor verde da Avenida Antônio Carlos chegou a 2.095 árvores plantadas; o Plano de Metas prevê 4 corredores.", PBH + "pbh-planta-mil-arvores-no-corredor-verde-da-antonio-carlos-nesta-terca-feira-3", "2026"),
    14: ("em_andamento", "baixa", "A Mata do Jardim América foi desapropriada em 2024 para virar parque, mas a implantação não foi localizada até out/2026.", PBH + "prefeitura-viabiliza-implantacao-de-novo-parque-na-regiao-oeste-da-capital", "2026-10"),
    15: S("ampliação do Parque Tom Jobim, no Luxemburgo."),
    16: ("em_andamento", "alta", "Novas miniflorestas foram plantadas em 2025 e 2026 (ex.: legado do Carnaval na Tereza Cristina); o Plano de Metas prevê 60 até 2028.", PBH + "representantes-do-carnaval-de-bh-plantam-minifloresta-neste-sabado-28-como-legado-da-festa", "2026-02"),
    17: ("em_andamento", "media", "A Prefeitura entregou o primeiro refúgio climático fixo, no Centro, e os primeiros refúgios móveis, no bairro São Paulo; a meta é de 100.", PBH + "prefeitura-entrega-primeiro-refugio-climatico-de-belo-horizonte", "2026"),
    18: ("em_andamento", "media", "O Plano Municipal de Arborização Urbana foi lançado e a meta de 50 mil árvores plantadas em 2025 foi atingida; a promessa vai até 2050.", PBH + "prefeitura-de-bh-alcanca-meta-de-50-mil-arvores-plantadas-em-2025", "2025-12"),
    19: ("em_andamento", "media", "O atendimento veterinário público ganhou nova sede, o Centro Avançado de Saúde Animal no UniBH (set/2026); não foi localizada parceria com clínicas privadas.", PBH + "complexo-publico-veterinario-ganha-novas-unidades-e-estruturas-mais-modernas", "2026-09"),
    20: ("em_andamento", "media", "O programa Viver de Novo (dez/2025) começou a convocar pessoas em situação de rua para o Bolsa Moradia (300 convocadas).", "https://www.itatiaia.com.br/brasil/sudeste/mg/bh-comeca-a-convocar-pessoas-em-situacao-de-rua-para-programa-de-moradia/", "2026"),
    21: ("em_andamento", "baixa", "O eixo de saúde do Viver de Novo ampliou o Consultório na Rua de 8 para 10 equipes; não foram localizados serviços próprios de saúde mental para essa população.", "https://prefeitura.pbh.gov.br/assistencia-social-e-direitos-humanos/viver-de-novo", "2026"),
    22: ("em_andamento", "media", "A Prefeitura enviou à Câmara projeto que reserva até 5% das vagas não especializadas dos contratos de obras e serviços para pessoas em situação de rua.", PBH + "pbh-anuncia-acoes-para-populacao-em-situacao-de-rua-incluindo-vagas-em-obras-e-servicos", "2026"),
    23: ("parcialmente_cumprida", "media", "O prontuário eletrônico (SIGRAH) segue implantado em etapas, com novo contrato desde dez/2025 e queixas de médicos; não estava pleno em 2025, como prometido.", "https://prefeitura.pbh.gov.br/saude/sigrah", "2026-03"),
    24: S("aplicativo com consultas, exames e vacinas do usuário do SUS-BH; o PBH APP já mostrava resultados de exames desde 2019."),
    25: ("nao_cumprida", "alta", "Até o fim de 2025 foram entregues 3 das 12 novas escolas prometidas (EMEIs Estrela Dalva, Tupã e Parque da Aviação); outras ficaram para 2026.", "https://www.itatiaia.com.br/brasil/sudeste/mg/prefeitura-vai-comecar-a-construcao-de-mais-quatro-escolas-infantis-em-bh/", "2026"),
    26: ("nao_cumprida", "baixa", "Em 2025 as 3 novas EMEIs somaram cerca de 660 vagas integrais, longe das 2.400 prometidas, e a EMEF de 960 vagas ficou para 2026.", PDM, "2025-12"),
    27: S("abertura de mil novas vagas em creches conveniadas."),
}
AJUSTES = {}

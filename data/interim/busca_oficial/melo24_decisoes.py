# Classificação do censo de Sebastião Melo (Porto Alegre, 2024). Mandato 2025-2028 em curso; data de corte 2026-11-24.
# Fontes: notícias da Prefeitura (prefeitura.poa.br) e imprensa, por resumos de busca. Medidas iniciadas = em_andamento;
# sem registro = não cumprida, confiança baixa (Diário Oficial e Câmara não consultados sistematicamente).
SEM = "Busca nas notícias da Prefeitura de Porto Alegre e na imprensa (jan/2025 a nov/2026) não localizou "
P = "https://prefeitura.poa.br/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


def A(txt, url, data, conf="media"):
    return ("em_andamento", conf, txt, url, data)


def C(txt, url, data, conf="alta"):
    return ("cumprida", conf, txt, url, data)


D = {
    13: A("Até nov/2026 não se localizou aumento de alíquota nem criação de tributo; a Prefeitura aprovou programas de renegociação (RecuperaPOA 2025) e isenções de IPTU. Compromisso válido até o fim do mandato.", P + "smf/noticias/recuperapoa-2025-comeca-em-setembro-com-descontos-de-ate-90-em-juros-e-multas", "2026"),
    16: S("a implantação do Certa+ para autistas acima de 12 anos (as novas vagas de 2026 vieram de clínicas em parceria com o programa estadual TEAcolhe)."),
    17: A("Novos centros de atendimento ao autismo foram abertos em outras regiões, em parceria com o programa estadual TEAcolhe: na Zona Oeste (abr/2026, 150 vagas) e na Zona Sul (set/2026, 330 vagas); não são unidades do Certa.", P + "sms/noticias/porto-alegre-abre-330-novas-vagas-para-tratamento-do-autismo-pelo-sus", "2026-09"),
    21: A("A PPP do novo Hospital Materno-Infantil Presidente Vargas foi modelada, passou por audiência pública e pelo Tribunal de Contas e teve garantias aprovadas em 2024; não se localizou o leilão.", P + "smp/ppp-hospital-materno-infantil-presidente-vargas", "2024-11", "baixa"),
    22: S("a habilitação do Pronto Atendimento Cruzeiro do Sul como UPA (em 2026 a unidade seguia como pronto atendimento, agora com telemedicina)."),
    26: A("A fila da creche caiu de 3.077 crianças em 2024 para 920 no fim de 2025 e 873 no início de 2026; a meta da gestão é zerá-la até 2028.", P + "smed/noticias/ano-termina-com-reducao-historica-de-70-no-deficit-de-vagas-na-educacao-infantil", "2026-01", "alta"),
    32: S("a implantação de escolas cívico-militares municipais (projeto de lei de vereador de 2025 recebeu parecer prévio contrário)."),
    37: S("nova unidade da Casa Betânia."),
    39: S("novos restaurantes populares (a Prefeitura seguia com seis em 2026)."),
    41: S("nova unidade do Centro Dia do Idoso (seguem duas)."),
    43: A("O bônus-moradia teve novo reajuste em jun/2026 (para R$ 139,5 mil) e chegou a 571 pagamentos desde 2021.", P + "demhab/noticias/bonus-moradia-passa-para-r-139-mil-apos-novo-reajuste", "2026-06"),
    46: A("A Lei 14.186/2025 criou a Farmácia Veterinária Solidária, regulamentada em dez/2025, com doações de medicamentos para animais atendidos pela Unidade de Saúde Animal Victória e tutores de baixa renda.", P + "gvp/noticias/prefeitura-regulamenta-programa-de-doacao-de-medicamentos-veterinarios", "2025-12", "baixa"),
    51: C("A Prefeitura publicou o Edital 012/2025 de concurso para a Guarda Municipal.", P + "sites/default/files/usu_doc/sites/smap/Edital%20012-2025%20-%20Anexo%20I%20-%20Justificativas.pdf", "2025", "media"),
    52: A("Em fev/2026 a Prefeitura anunciou sistema de monitoramento com drones autônomos e inteligência artificial em parques e áreas públicas, em implantação.", P + "smseg/noticias/porto-alegre-tera-monitoramento-com-drones-autonomos-em-parques-e-areas-publicas", "2026-02"),
    61: A("A Prefeitura anunciou em mai/2026 a expansão do Bolsa Atleta (20 bolsistas em 2025) e prevê mais bolsas em 2027.", P + "smel/noticias/prefeitura-amplia-investimentos-no-esporte-de-rendimento", "2026-05"),
    69: C("O projeto de duplicação da avenida Juca Batista foi concluído, segundo o secretário de Obras (jan/2025).", "https://www.jornaldocomercio.com/colunas/pensar-a-cidade/2025/01/1186371-projeto-de-duplicacao-da-juca-batista-esta-concluido-informa-secretario.html", "2025-01", "media"),
    70: S("o início da duplicação da Protásio Alves em Porto Alegre (o projeto estadual do Caminho do Meio teve obras contratadas em Viamão e Alvorada, sem contrato localizado para o trecho da Capital)."),
    75: A("A Prefeitura assinou em jul/2026 financiamento de R$ 447,7 milhões com o BNDES para 100 ônibus elétricos articulados e abriu consulta a fabricantes em nov/2026; três linhas já operam com ônibus elétricos.", P + "smpg/noticias/prefeitura-assina-contrato-de-financiamento-para-compra-de-100-onibus-eletricos", "2026-11", "alta"),
    76: A("A Prefeitura informou R$ 32 milhões investidos em terminais até jun/2026 e incluiu quatro novos terminais nos projetos do Novo PAC; não se localizou terminal novo entregue.", "https://www.jornaldocomercio.com/geral/2026/06/1251610-porto-alegre-projeta-rs-447-milhoes-em-onibus-eletricos-e-ja-investiu-rs-32-milhoes-em-terminais.html", "2026-06", "baixa"),
    82: A("A PPP dos resíduos sólidos (concessão de 35 anos) foi enviada ao Tribunal de Contas em mar/2026, com edital previsto para 2026, e a regulação foi delegada à Agergs.", P + "smp/noticias/ppp-dos-residuos-solidos-e-enviada-para-analise-do-tribunal-de-contas", "2026-03", "alta"),
    83: A("A Prefeitura anunciou em set/2025 mudanças na gestão para acelerar a parceirização do Dmae; não se localizou o projeto de lei na Câmara.", P + "Editoria/parcerias", "2025-09", "baixa"),
    95: A("Cerca de um ano após a enchente, 92% dos 309 equipamentos públicos atingidos estavam em funcionamento, incluindo as 14 escolas municipais.", P + "smamus/noticias/mais-de-r-519-milhoes-ja-foram-investidos-na-reconstrucao-da-capital", "2025", "alta"),
    96: A("As obras do sistema de proteção contra cheias avançam: comportas modernizadas (jul/2026), reforço do Muro da Mauá, 17 bombas flutuantes (ago/2026) e R$ 2,3 bilhões em investimentos contratados.", P + "gp/noticias/dmae-conclui-modernizacao-das-comportas-do-sistema-de-protecao-contra-cheias", "2026-08", "alta"),
    97: A("As obras de recuperação da Orla de Ipanema, do Lami e do Trecho 3 foram iniciadas; não se localizou a entrega.", P + "gp/noticias/prefeito-abre-semana-da-superacao-com-balanco-do-programa-porto-alegre-forte", "2025"),
}
_RESTO = {
    1: "balanço de ampliação do Mais Comunidade", 2: "projeto de modernização do mobiliário urbano",
    3: "ampliação do programa Prefeitos de Praça", 4: "mapeamento de ruas e avenidas com inteligência artificial",
    5: "novas Unidades de Destino Certo", 6: "linha de microcrédito inovador para negócios atingidos pela enchente",
    7: "novos Hubs Comunitários de Inovação", 8: "expansão dos Territórios Inovadores",
    9: "o Programa Municipal de Desenvolvimento de Talentos", 10: "programa de renegociação específico para o setor de eventos",
    11: "novas hortas comunitárias", 12: "a revisão dos limites da Zona Rural",
    14: "cashback de ISS para turistas", 15: "cashback de ISS para empresas boas pagadoras",
    18: "o financiamento da duplicação do Hospital de Pronto Socorro", 19: "a criação de policlínicas por região de saúde",
    20: "a abertura de novos CAPS", 23: "lei que torne permanente o Agiliza Saúde", 24: "ampliação do horário noturno nas unidades de saúde",
    25: "ampliação das equipes do Melhor em Casa", 27: "as cinco escolas de excelência", 28: "ampliação do horário estendido nas creches",
    29: "a contratação da PPP Escola Bem-Cuidada", 30: "a oferta de contraturno em todas as escolas de ensino fundamental",
    31: "o cartão kit escola", 33: "a central de conteúdos pedagógicos online", 34: "o plano de inclusão profissional da população de rua",
    35: "a implantação do POATerritorial", 36: "o projeto piloto inspirado na Vila Reencontro", 38: "novas Salas Lilás na rede de saúde",
    40: "Centros de Referência de Segurança Alimentar nos restaurantes populares", 42: "ampliação do cartão alimentação",
    44: "a conclusão do Plano Municipal de Redução de Risco", 45: "ampliação dos recursos do Compra Compartilhada",
    47: "o auxílio a protetores de animais", 48: "o cadastro único de animais com microchip", 49: "o plano de contingência da causa animal",
    50: "o atendimento veterinário a animais atropelados", 53: "ampliação do cercamento eletrônico",
    54: "câmeras nos novos abrigos de ônibus", 55: "a integração do videomonitoramento aos bancos de foragidos e desaparecidos",
    56: "a ampliação do Ceic", 57: "a conclusão da revitalização do Paço Municipal e do Museu de Arte de Porto Alegre",
    58: "o Complexo Cultural do Porto Seco", 59: "os projetos dos museus do Negro, Étnico da Cultura Gaúcha e do Carnaval",
    60: "a reabertura do Ginásio Tesourinha", 62: "a extensão do Clube Escolar", 63: "a abertura das piscinas de novembro a março",
    64: "novas unidades do Centro de Desenvolvimento do Futebol Feminino", 65: "a proposta de revitalização da Orla 2",
    66: "a revitalização da orla entre o Pontal e o Iate Clube Guaíba", 67: "a destinação da área do Estádio Olímpico",
    68: "as obras do entorno da Arena do Grêmio", 71: "o projeto viário do cruzamento Antônio de Carvalho/Ipiranga/Bento Gonçalves",
    72: "o estudo da ciclovia da Ipiranga", 73: "avanço na duplicação da avenida Edgar Pires de Castro", 74: "o acesso norte do Porto Seco",
    77: "ampliação do Vou à Escola", 78: "a conclusão dos abrigos de ônibus por concessão", 79: "o Caminho Seguro nas Escolas",
    80: "ampliação do Sinal Verde", 81: "a revisão do Plano Diretor Cicloviário", 84: "novas áreas de Terrários Urbanos",
    85: "biodigestores em escolas", 86: "a operação urbana do Arroio Dilúvio e do Parque Linear", 87: "pontos de monitoramento da qualidade do ar",
    88: "a adutora da avenida A. J. Renner", 89: "a ampliação do Sistema de Abastecimento São João", 90: "a contratação da macrodrenagem do Arroio Moinho",
    91: "a drenagem do viaduto Obirici", 92: "a drenagem do Loteamento Túnel Verde", 93: "redes de esgoto no bairro Anchieta",
    94: "o projeto da Estação de Tratamento de Esgoto do Rubem Berta", 98: "a conclusão do Plano de Ação Climática",
    99: "o sistema de monitoramento e alerta de riscos climáticos", 100: "o plano de preparação para desastres",
    101: "a instalação da Sala de Situação da Defesa Civil", 102: "o plano urbanístico-ambiental das Ilhas",
    103: "projeto de plano de carreira dos servidores", 104: "reforma administrativa",
}
for _k, _v in _RESTO.items():
    D.setdefault(_k, S(_v + "."))

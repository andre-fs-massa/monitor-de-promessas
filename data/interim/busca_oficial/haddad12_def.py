# Censo do plano de Fernando Haddad (prefeitura de São Paulo, 2012): uma tupla por promessa testável.
# (trecho_literal, promessa, area, tipo, depende_legislativo, outro_ente, termo de busca)
# O documento registrado é de diretrizes; ficaram de fora verbos vagos (fortalecer, promover, apoiar, incentivar,
# valorizar, retomar o conceito) e intenções sem objeto concreto.
P = [
    # Educação
    ("1 – Desenvolver programas visando a educação integral na rede municipal de ensino.", "Implantar programas de educação integral na rede municipal", "Educação", "acao", "nao", "", "educação integral"),
    ("2 - Ampliar o atendimento em educação infantil por meio do aumento da oferta de vagas para crianças de 0 a 3 anos e 11 meses e da universalização do atendimento às crianças de 4 a 5 anos.", "Ampliar as vagas em creche e universalizar o atendimento de 4 e 5 anos, de preferência construindo novas unidades", "Educação", "resultado", "nao", "", "creche"),
    ("12 - Implementar e fortalecer o Conselho Regional dos Conselhos de Escola (CRECE).", "Implantar o Conselho Regional dos Conselhos de Escola (CRECE)", "Educação", "acao", "nao", "", "CRECE"),
    ("15 - Promover amplo debate sobre o Plano Municipal de Educação (PME), trabalhar para sua aprovação", "Aprovar o Plano Municipal de Educação e criar mecanismos de acompanhamento", "Educação", "acao", "sim", "", "Plano Municipal de Educação"),
    ("16 - Descentralizar e ampliar as Diretorias Regionais de Educação (DREs).", "Descentralizar e ampliar as Diretorias Regionais de Educação", "Educação", "acao", "nao", "", "Diretoria Regional de Educação"),
    ("trazer para São Paulo os programas federais, sobretudo, o Pronatec", "Firmar convênios para trazer o Pronatec e outros programas federais à cidade", "Educação", "acao", "nao", "União", "Pronatec"),
    # Saúde
    ("9 - Assumir e estruturar o sistema municipal de regulação do acesso", "Assumir e estruturar o sistema municipal de regulação do acesso, incluindo serviços hoje sob gestão estadual", "Saúde", "acao", "nao", "Estados", "regulação"),
    # Cidadania e assistência
    ("São Paulo pode tornar-se um exemplo pioneiro na implantação da Renda Básica da Cidadania (RBC)", "Implantar por etapas a Renda Básica da Cidadania", "Assistência social", "acao", "sim", "", "Renda Básica"),
    ("da organização da rede de equipamentos públicos de alimentação e nutrição, a ser integrada por restaurantes populares e cozinhas comunitárias", "Organizar rede de equipamentos públicos de alimentação com restaurantes populares e cozinhas comunitárias", "Assistência social", "acao", "nao", "", "segurança alimentar"),
    ("3 - Expandir a presença do poder público nos territórios ampliando a rede de Centros de Referência de Assistência Social (CRAS)", "Ampliar a rede de CRAS e CREAS", "Assistência social", "acao", "nao", "", "CRAS"),
    ("9 - Construir um sistema de notificações de situações de violação de direitos na cidade de São Paulo", "Criar um sistema de notificações de violação de direitos", "Direitos humanos", "acao", "nao", "", "violação de direitos"),
    # Cultura e esporte
    ("promovendo a adesão ao Sistema Nacional e a consequente implantação do Sistema Municipal de Cultura.", "Aderir ao Sistema Nacional de Cultura e implantar o Sistema Municipal de Cultura", "Cultura", "acao", "sim", "União", "Sistema Municipal de Cultura"),
    ("população, como o Conselho Municipal de Cultura e conselhos de gestão de programas e equipamentos.", "Recriar o Conselho Municipal de Cultura e conselhos de gestão de equipamentos", "Cultura", "acao", "nao", "", "Conselho Municipal de Política Cultural"),
    ("16 - Criar centros especializados e de excelência de várias modalidades esportivas e olímpicas de forma descentralizada", "Criar centros esportivos de excelência descentralizados", "Esporte", "acao", "nao", "", "centro olímpico"),
    ("18 - Promover, em parceria com a Secretaria da Educação, competições esportivas anuais no âmbito das escolas", "Realizar competições esportivas escolares anuais", "Esporte", "acao", "nao", "", "jogos escolares"),
    # Gestão
    ("implantar os Conselhos de Representantes nas Subprefeituras.", "Implantar os Conselhos de Representantes nas subprefeituras", "Gestão pública", "acao", "nao", "", "Conselho Participativo"),
    ("a partir da implantação de uma Controladoria Geral do Município", "Criar a Controladoria Geral do Município, integrando auditoria, corregedoria e ouvidoria", "Gestão pública", "acao", "sim", "", "Controladoria Geral"),
    ("da criação da política integrada de saúde do servidor público municipal e da requalificação do HSPM", "Criar política integrada de saúde do servidor e requalificar o HSPM", "Gestão pública", "acao", "nao", "", "saúde do servidor"),
    ("por meio da implantação de sistemas de custos e de compras eletrônicas no âmbito municipal, com a utilização do pregão eletrônico", "Implantar sistemas de custos e de compras eletrônicas com pregão eletrônico", "Gestão pública", "acao", "nao", "", "pregão eletrônico"),
    ("e a promoção do acesso da população à internet nos locais públicos de convívio social.", "Oferecer acesso à internet em locais públicos de convívio", "Inclusão digital", "acao", "nao", "", "WiFi Livre"),
    # Segurança
    ("1 - Instituir Programa Territorializado de Prevenção à Violência e à Criminalidade (Cidade de Paz)", "Instituir o Programa Cidade de Paz de prevenção à violência", "Segurança pública", "acao", "nao", "", "prevenção à violência"),
    ("bem como elaborar o Mapa da Violência e da Criminalidade da Cidade de São Paulo", "Elaborar o Mapa da Violência e da Criminalidade da cidade", "Segurança pública", "acao", "nao", "", "violência"),
    ("6 - Modernizar e expandir o sistema eletrônico de vigilância da Guarda Civil Metropolitana", "Modernizar e expandir o sistema eletrônico de vigilância da GCM, integrado a CET, SPTrans e polícias", "Segurança pública", "acao", "nao", "", "videomonitoramento"),
    ("8 - Capacitar os agentes e inspetores da Guarda Civil Metropolitana, ampliando o seu efetivo", "Ampliar o efetivo da Guarda Civil Metropolitana", "Segurança pública", "resultado", "nao", "", "Guarda Civil"),
    ("9 - Implantar um programa de iluminação pública orientado para a segurança.", "Implantar programa de iluminação pública voltado à segurança", "Infraestrutura", "acao", "nao", "", "iluminação"),
    # Desenvolvimento econômico
    ("por meio da criação de uma agência municipal de incentivo à pesquisa e inovação", "Criar agência municipal de incentivo à pesquisa e inovação e ampliar parques tecnológicos e incubadoras", "Ciência e tecnologia", "acao", "nao", "", "inovação"),
    ("10 - Firmar parcerias com o Governo Federal para a criação de universidades federais nas zonas leste e sul", "Firmar parceria com o governo federal para criar universidades federais nas zonas Leste e Sul", "Educação", "acao", "nao", "União", "universidade federal"),
    ("18 - Constituir Conselho Municipal de Desenvolvimento Local", "Criar o Conselho Municipal de Desenvolvimento Local", "Ambiente de negócios", "acao", "nao", "", "desenvolvimento local"),
    ("20 - Estabelecer Política Municipal de Economia Criativa", "Estabelecer a Política Municipal de Economia Criativa", "Cultura", "acao", "nao", "", "economia criativa"),
    ("21 - Retomar os programas de desenvolvimento e inclusão social pelo trabalho, a exemplo dos programas Bolsa Trabalho, Começar de Novo, Oportunidade Solidária", "Retomar os programas Bolsa Trabalho, Começar de Novo, Oportunidade Solidária e de microcrédito", "Trabalho", "acao", "nao", "", "Bolsa Trabalho"),
    ("com a utilização de recursos do FUNDEB para a compra de produtos oriundos da agricultura familiar para a merenda escolar.", "Comprar produtos da agricultura familiar para a merenda escolar", "Agricultura", "acao", "nao", "", "agricultura familiar"),
    # Desenvolvimento urbano e habitação
    ("1 - Revisar o Plano Diretor em 2013, com horizonte temporal em 2024", "Revisar o Plano Diretor e estabelecer um Programa de Metas até 2016", "Infraestrutura", "acao", "sim", "", "Plano Diretor"),
    ("a ser transformado no Conselho da Cidade de São Paulo.", "Transformar o Conselho Municipal de Desenvolvimento Urbano no Conselho da Cidade", "Gestão pública", "acao", "nao", "", "Conselho da Cidade"),
    ("4 - Instituir os Programas de Parceria Público-Comunitários (PPC)", "Instituir Programas de Parceria Público-Comunitários", "Gestão pública", "acao", "nao", "", "parceria"),
    ("10 - Regular os investimentos privados na cidade por meio da revisão do zoneamento e Código de Obras", "Revisar o zoneamento e o Código de Obras", "Infraestrutura", "acao", "sim", "", "zoneamento"),
    ("o IPTU Progressivo no Tempo, o Direito de Preempção e a outorga onerosa do direito de construir.", "Aplicar o IPTU progressivo no tempo, o direito de preempção e as ZEIS contra a especulação imobiliária", "Habitação", "acao", "nao", "", "IPTU progressivo"),
    ("criar um programa global de capacitação técnica bilateral Sul-Sul", "Criar programa de capacitação técnica Sul-Sul com cidades de países em desenvolvimento", "Gestão pública", "acao", "nao", "", "cooperação"),
    ("18 - Implantar programa de produção e acesso à moradia na região central", "Implantar programa de moradia popular na região central", "Habitação", "acao", "nao", "", "habitação centro"),
    ("19 - Promover parceria com o programa Minha Casa, Minha Vida, com prioridade para a modalidade MCMV - Entidades", "Fazer parceria com o Minha Casa, Minha Vida, com prioridade ao MCMV-Entidades, com terrenos e contrapartidas", "Habitação", "acao", "nao", "União", "Minha Casa Minha Vida"),
    ("20 - Ampliar o programa de urbanização e regularização de favelas e loteamentos irregulares", "Ampliar o programa de urbanização e regularização de favelas e loteamentos", "Habitação", "acao", "nao", "", "urbanização"),
    ("21 - Formar um estoque de terrenos e glebas destinados à produção de habitação de interesse social", "Formar estoque de terrenos para habitação de interesse social", "Habitação", "acao", "nao", "", "habitação de interesse social"),
    ("23 - Estabelecer um programa de acompanhamento de pós-ocupação", "Criar programa de acompanhamento pós-ocupação nos conjuntos habitacionais", "Habitação", "acao", "nao", "", "pós-ocupação"),
    # Transporte
    ("2 - Priorizar o transporte coletivo sobre o individual com a criação de faixas exclusivas", "Criar faixas exclusivas de ônibus", "Mobilidade", "acao", "nao", "", "faixa exclusiva"),
    ("4 - Desenvolver o Plano de Mobilidade Urbana Integrado", "Elaborar o Plano de Mobilidade Urbana", "Mobilidade", "acao", "nao", "", "Plano de Mobilidade"),
    ("6 - Elaborar o Plano de Logística e Carga", "Elaborar o Plano de Logística e Carga, com centros de logística e descentralização da Ceagesp", "Mobilidade", "acao", "nao", "", "carga"),
    ("7 - Criar um órgão de gerenciamento que cuide da logística de carga na cidade.", "Criar órgão de gerenciamento da logística de carga", "Mobilidade", "acao", "nao", "", "carga"),
    ("8 - Criar um Conselho Municipal de Gestão dos Transportes", "Criar um Conselho Municipal de Transportes", "Mobilidade", "acao", "nao", "", "Conselho Municipal de Transporte"),
    ("12 - Operar o sistema de maneira controlada e assistida em tempo real com a criação de centrais de controle operacional.", "Criar centrais de controle operacional do transporte em tempo real", "Mobilidade", "acao", "nao", "", "controle operacional"),
    ("cobranças diferenciadas (cartão semanal, mensal etc.).", "Criar tarifas diferenciadas do transporte (bilhete semanal, mensal etc.)", "Mobilidade", "acao", "nao", "", "Bilhete Único Mensal"),
    ("15 - Desenvolver novo modelo de delegação do sistema municipal de ônibus para subsidiar a renovação dos contratos com final previsto para 2013.", "Definir novo modelo de concessão dos ônibus para renovar os contratos que venciam em 2013", "Mobilidade", "acao", "nao", "", "concessão ônibus"),
    ("18 - Construir novos corredores de média capacidade, sobretudo perimetrais", "Construir novos corredores de ônibus", "Mobilidade", "acao", "nao", "", "corredor"),
    ("20 - Criar estações intermodais conectando a rede estrutural à rede sobre trilhos.", "Criar estações intermodais ligando ônibus a trens e metrô", "Mobilidade", "acao", "nao", "", "intermodal"),
    ("21 - Ampliar e melhorar os terminais de ônibus", "Ampliar os terminais de ônibus", "Mobilidade", "acao", "nao", "", "terminal"),
    ("23 - Modernizar a sinalização semafórica convertendo os sinais já conectados com fibra ótica para sinais inteligentes.", "Converter semáforos conectados por fibra em semáforos inteligentes", "Mobilidade", "acao", "nao", "", "semáforo"),
    ("28 - Renovar as calçadas, principalmente na periferia", "Renovar calçadas, principalmente na periferia", "Infraestrutura", "acao", "nao", "", "calçadas"),
    ("por meio da criação de ciclovias, ciclofaixas e ciclorotas.", "Criar ciclovias, ciclofaixas e ciclorrotas", "Mobilidade", "acao", "nao", "", "ciclovia"),
    ("30 - Integrar as bicicletas às estações de trem, metrô e terminais de ônibus com a criação de bicicletários", "Criar bicicletários nas estações e terminais", "Mobilidade", "acao", "nao", "", "bicicletário"),
    ("31 - Criar sistemas de BikeShare, incorporados ao Bilhete Único", "Criar sistema de bicicletas compartilhadas integrado ao Bilhete Único", "Mobilidade", "acao", "nao", "", "bicicletas compartilhadas"),
    ("32 - Garantir a gratuidade da inspeção veicular", "Manter a inspeção veicular gratuita", "Meio ambiente", "acao", "nao", "", "inspeção veicular"),
    ("36 - Viabilizar os centros comerciais de bairro através da criação de estacionamentos", "Criar estacionamentos públicos ou em PPP para centros comerciais de bairro", "Mobilidade", "acao", "nao", "", "estacionamento"),
    # Meio ambiente
    ("7 – Revisar, atualizar e implementar, com controle social, o Plano Municipal de Drenagem Urbana", "Revisar o Plano de Drenagem, o Plano de Águas e Esgoto e o Plano de Resíduos Sólidos", "Saneamento", "acao", "nao", "", "Plano Municipal"),
]

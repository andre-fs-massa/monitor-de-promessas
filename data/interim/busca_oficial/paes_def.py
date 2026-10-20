# Censo do plano de Eduardo Paes (2024, mandato 2025-2028, chapa Paes/Cavaliere): 55 itens numerados + objetivo VII.
# Fora (decidido em 14/10/2026): itens 2, 3, 5, 12, 19, 26, 45 e 52 (vagos, "buscar", "fortalecer" ou manutenção).
# chave, paragrafo, trecho_literal, promessa, area, tipo, depende_legislativo, outro_ente
P = [
 ("conscientizacao", "Objetivo VII", "Criar um amplo programa de conscientização para a cidadania nas escolas e nos espaços coletivos", "Criar programa de conscientização para a cidadania nas escolas e espaços públicos", "Educação", "acao", "nao", ""),
 # Saúde
 ("super_centros", "Saúde, item 1", "Criar dois novos Super Centros Cariocas de Saúde, um em Campo Grande e outro na Zona Norte, e já deixar prontos os projetos para a implantação de mais dois (um em Realengo e outro em Jacarepaguá)", "Criar 2 Super Centros Cariocas de Saúde (Campo Grande e Zona Norte) e deixar prontos os projetos de Realengo e Jacarepaguá", "Saúde", "acao", "nao", ""),
 ("autismo", "Saúde, item 4", "Implementar um programa dedicado às famílias com pessoas do espectro autista e", "Criar programa para famílias de pessoas autistas com 8 centros de referência", "Saúde", "acao", "nao", ""),
 # Educação
 ("tempo_integral", "Educação, item 6", "Ser a 1ª capital do país em matrículas com ensino em tempo integral, atingindo mais de 70% de cobertura em toda a cidade", "Chegar a mais de 70% das matrículas em tempo integral", "Educação", "resultado", "nao", ""),
 ("creches", "Educação, item 7", "Criar mais 13.000 novas vagas em creches e pré-escolas", "Criar 13 mil vagas em creches e pré-escolas", "Educação", "acao", "nao", ""),
 ("gets", "Educação, item 8", "Ampliar a implementação dos GETs, totalizando 500 novas escolas tecnológicas em tempo integral na rede municipal", "Chegar a 500 novos Ginásios Educacionais Tecnológicos (GETs) em tempo integral", "Educação", "acao", "nao", ""),
 ("programacao", "Educação, item 9", "Ofertar ensino de Programação Computacional para 200 mil alunos da rede pública municipal", "Ensinar programação de computadores a 200 mil alunos da rede municipal", "Educação", "resultado", "nao", ""),
 ("educ_especial", "Educação, item 10", "garantindo 1 profissional para cada 3 alunos na rede de apoio", "Garantir 1 profissional de apoio para cada 3 alunos da educação especial", "Educação", "resultado", "nao", ""),
 ("climatizacao", "Educação, item 11", "Recuperar a infraestrutura das escolas, sobretudo no que diz respeito a garantir a climatização de todas as salas de aula", "Climatizar todas as salas de aula da rede municipal", "Educação", "resultado", "nao", ""),
 # Transporte
 ("brt_vlt", "Transporte, item 13", "Iniciar a transição do sistema BRT de rodas para um sistema leve de trilhos (modelo VLT): a partir da Transcarioca e da Transoeste (do Jardim Oceânico ao Parque Olímpico)", "Iniciar a troca do BRT por VLT na Transcarioca e na Transoeste (Jardim Oceânico–Parque Olímpico)", "Mobilidade", "acao", "nao", ""),
 ("jae_tarifa", "Transporte, item 14", "Com a nova bilhetagem digital (Programa Jaé), reestruturar a política tarifária com mais integrações e benefícios para o usuário de transporte público na cidade", "Reestruturar a política tarifária com mais integrações usando a bilhetagem Jaé", "Mobilidade", "acao", "nao", ""),
 ("faixa_azul", "Transporte, item 15", "Implantar um projeto de ordenamento do trânsito com a implantação de faixa azul para motos nas principais vias da cidade", "Implantar faixa azul para motos nas principais vias", "Mobilidade", "acao", "nao", ""),
 ("eletrificacao", "Transporte, item 16", "Implementar o programa de incentivo à transição energética da mobilidade da cidade, incluindo a eletrificação da frota de ônibus", "Criar programa de transição energética da mobilidade, com eletrificação da frota de ônibus", "Mobilidade", "acao", "nao", ""),
 # Emprego e renda / Turismo
 ("qualificacao", "Emprego e renda, item 17", "Criar um programa unificado de qualificação de mão de obra carioca, direcionado a empregos verdes, inovação, turismo e tecnologia", "Criar programa unificado de qualificação profissional (empregos verdes, inovação, turismo e tecnologia)", "Trabalho", "acao", "nao", ""),
 ("formalizacao", "Emprego e renda, item 18", "Aumentar a formalização no mercado de trabalho no Rio, por meio de um programa de incentivos, treinamento, cursos e auxílio financeiro", "Criar programa de incentivo à formalização do trabalho, com cursos e auxílio financeiro", "Trabalho", "acao", "nao", ""),
 ("fundo_turismo", "Turismo, item 20", "Criar um Fundo do Turismo dedicado ao aumento do número de passageiros internacionais e que financiará a promoção do “Destino Rio” no exterior", "Criar Fundo do Turismo para atrair voos internacionais e promover o Rio no exterior", "Turismo", "acao", "sim", ""),
 ("bolsa_valores", "Turismo, item 21", "Fazer o projeto da Bolsa de Valores do Rio virar realidade até 2026", "Fazer a Bolsa de Valores do Rio funcionar até 2026", "Ambiente de negócios", "acao", "nao", ""),
 # Ordem pública
 ("rondas_gm", "Ordem pública, item 22", "Ampliar as rondas escolares e a presença da Guarda Municipal nas praças e parques da cidade", "Ampliar as rondas escolares e a Guarda Municipal em praças e parques", "Segurança pública", "acao", "nao", ""),
 ("brt_seguro", "Ordem pública, item 23", "Expandir o Programa BRT Seguro, fortalecendo o combate à violência e ao vandalismo nas estações e terminais", "Expandir o programa BRT Seguro", "Segurança pública", "acao", "nao", ""),
 ("gm_armada", "Ordem pública, item 24", "Permitir que um grupo de elite da Guarda Municipal (incluindo o Grupo de Operações Especiais, o Grupo Tático Móvel e a Ronda Maria da Penha), após a implantação de um treinamento rigoroso, possa fazer uso de armas de fogo", "Armar um grupo de elite da Guarda Municipal após treinamento", "Segurança pública", "acao", "sim", ""),
 ("iluminacao_cameras", "Ordem pública, item 25", "Continuar fazendo a nossa parte, ampliando a iluminação pública nos bairros, a instalação de câmeras de seguranças ligadas ao COR, o cerco eletrônico do Programa Civitas", "Ampliar iluminação pública, câmeras ligadas ao COR e o cerco eletrônico do Civitas", "Segurança pública", "acao", "nao", ""),
 # Gestão / Finanças públicas
 ("ppps", "Gestão, item 27", "Atrair pelo menos R$ 2 bilhões em investimentos privados por meio de projetos de concessão e PPPs", "Atrair R$ 2 bilhões em investimentos privados por concessões e PPPs", "Ambiente de negócios", "resultado", "nao", ""),
 ("whatsapp_wifi", "Gestão, item 28", "Expandir os serviços de atendimento ao cidadão por meio de WhatsApp e ampliar a oferta de Wi-Fi público em toda a cidade", "Expandir o atendimento por WhatsApp e o Wi-Fi público", "Inclusão digital", "acao", "nao", ""),
 ("selo_diamante", "Gestão, item 29", "Conquistar o Selo Diamante do Programa Nacional de Transparência Pública (PNTP) da Associação Nacional dos Tribunais de Contas", "Conquistar o Selo Diamante do Programa Nacional de Transparência Pública", "Transparência", "resultado", "nao", ""),
 # Meio ambiente, clima e prevenção a desastres
 ("acari", "Meio ambiente, item 30", "Implantar o Projeto de Controle de Enchentes da Bacia do Rio Acari nos Trechos 1 e 2", "Fazer as obras de controle de enchentes do Rio Acari (trechos 1 e 2)", "Saneamento", "acao", "nao", ""),
 ("reassentamento", "Meio ambiente, item 31", "Criar um programa destinado à construção de habitações para o reassentamento de populações ribeirinhas", "Criar programa de moradias para reassentar ribeirinhos em áreas inundáveis", "Habitação", "acao", "nao", ""),
 ("sirenes", "Meio ambiente, item 32", "Ampliar o sistema de sirenes para as comunidades suscetíveis a enchentes ordinárias", "Ampliar as sirenes de alerta para comunidades sujeitas a enchentes", "Clima", "acao", "nao", ""),
 ("jardim_maravilha", "Meio ambiente, item 33", "Seguir com o Projeto Jardim Maravilha, que visa expandir e melhorar os sistemas de drenagem", "Continuar as obras de drenagem do Projeto Jardim Maravilha", "Saneamento", "acao", "nao", ""),
 ("zn_verde", "Meio ambiente, item 34", "Criar o projeto ZN Verde, que visa produzir mudas em larga escala para arborizar e reduzir as ilhas de calor na Zona Norte da cidade", "Criar o projeto ZN Verde de arborização da Zona Norte", "Meio ambiente", "acao", "nao", ""),
 # Assistência social
 ("carioquinha", "Assistência social, item 35", "Implantar o Programa de transferência de renda Carioquinha destinado a famílias vulneráveis com crianças de 0 a 6 anos", "Criar o Carioquinha, transferência de renda para famílias com crianças de 0 a 6 anos", "Assistência social", "acao", "nao", ""),
 ("prato_feito", "Assistência social, item 36", "Expandir o programa de combate à fome Prato Feito Carioca por meio das cozinhas comunitárias e da criação do Programa Restaurante Popular Carioca", "Expandir o Prato Feito Carioca e criar o Restaurante Popular Carioca", "Assistência social", "acao", "nao", ""),
 ("pop_rua", "Assistência social, item 37", "Acolher pelo menos 7 mil pessoas em situação de rua", "Acolher 7 mil pessoas em situação de rua, com tratamento e recolocação no trabalho", "Assistência social", "resultado", "nao", ""),
 # Favelas e comunidades
 ("morar_carioca", "Favelas, item 38", "Ampliar a cobertura dos programas Morar Carioca e Bairro Maravilha em toda a cidade", "Ampliar os programas Morar Carioca e Bairro Maravilha", "Habitação", "acao", "nao", ""),
 ("casa_carioca", "Favelas, item 39", "Promover melhorias habitacionais em 20.000 moradias de famílias identificadas", "Reformar 20 mil moradias pelo programa Casa Carioca", "Habitação", "resultado", "nao", ""),
 ("hub_favela", "Favelas, item 40", "Criar o programa HUB Favela Empreendedora", "Criar o programa HUB Favela Empreendedora", "Trabalho", "acao", "nao", ""),
 # Mulher
 ("empreend_feminino", "Mulher, item 41", "Ampliar o Programa de Capacitação Profissional voltado para o empreendedorismo feminino", "Ampliar a capacitação para o empreendedorismo feminino em áreas vulneráveis", "Mulheres", "acao", "nao", ""),
 ("cartao_mulheres", "Mulher, item 42", "Expandir no Programa Cartão Carioca, o cadastro de mulheres chefes de família, mulheres mães e mulheres grávidas", "Incluir mais mulheres chefes de família, mães e grávidas no Cartão Carioca", "Mulheres", "acao", "nao", ""),
 ("maria_penha", "Mulher, item 43", "Ampliar o Programa Ronda Maria da Penha", "Ampliar a Ronda Maria da Penha", "Mulheres", "acao", "nao", ""),
 # PCD
 ("pcd_capacitacao", "PCD, item 44", "capacitação de 15 mil PCDs e de seus familiares", "Capacitar 15 mil pessoas com deficiência e familiares", "Pessoa com deficiência", "resultado", "nao", ""),
 ("pcd_transporte", "PCD, item 46", "Viabilizar transporte adequado para a realização de consultas, exames e cirurgias destinadas a pessoas com deficiência na rede municipal de Saúde", "Oferecer transporte para consultas, exames e cirurgias de pessoas com deficiência", "Pessoa com deficiência", "acao", "nao", ""),
 # Jovem
 ("pacto_juventude", "Jovem, item 47", "Formar 3 mil jovens por ano no Programa Pacto Pela Juventude", "Formar 3 mil jovens por ano no Pacto pela Juventude", "Juventude", "resultado", "nao", ""),
 ("espacos_juventude", "Jovem, item 48", "Ampliar o número de Espaços da Juventude para 20 unidades e garantir a presença de pelo menos uma Casa da Juventude em todas as áreas de planejamento da cidade", "Chegar a 20 Espaços da Juventude e ter uma Casa da Juventude em cada área de planejamento", "Juventude", "acao", "nao", ""),
 ("rio_vestibular", "Jovem, item 49", "Atender 40 mil jovens no Programa Rio Vestibular", "Atender 40 mil jovens no Rio Vestibular", "Juventude", "resultado", "nao", ""),
 # Cultura
 ("jae_cultural", "Cultura, item 50", "Ampliar o Programa Jaé Cultural que visa garantir a gratuidade da tarifa do transporte público", "Ampliar o Jaé Cultural (transporte gratuito para espetáculos)", "Cultura", "acao", "nao", ""),
 ("oficina_cultural", "Cultura, item 51", "Expandir o Programa Oficina Cultural Carioca", "Expandir o programa Oficina Cultural Carioca", "Cultura", "acao", "nao", ""),
 # Esporte e legado
 ("museu_olimpico", "Esporte, item 53", "Inaugurar o Museu Rio Olímpico e implantar o Parque do Legado Olímpico", "Inaugurar o Museu Rio Olímpico e implantar o Parque do Legado Olímpico", "Esporte", "acao", "nao", ""),
 ("vilas_olimpicas", "Esporte, item 54", "4 novas Vilas Olímpicas, em Rio das Pedras, Sepetiba, Parque Oeste e", "Construir 4 Vilas Olímpicas (Rio das Pedras, Sepetiba, Parque Oeste e Cidade de Deus)", "Esporte", "acao", "nao", ""),
 ("time_rio", "Esporte, item 55", "Expandir, renovar e monitorar continuamente os resultados do programa Time Rio", "Expandir o programa Time Rio", "Esporte", "acao", "nao", ""),
]

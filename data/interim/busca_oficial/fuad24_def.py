# Censo do plano de Fuad Noman (prefeitura de Belo Horizonte, 2024): uma tupla por promessa testável.
# (trecho_literal, promessa, area, tipo, depende_legislativo, outro_ente, termo de busca)
# Só as propostas para 2025-2028 (abertura e seções Meio Ambiente, Assistência Social, Saúde e Educação); a segunda
# metade do plano é balanço da gestão 2017-2024 e ficou de fora, assim como metas com prazo até o fim de 2024.
P = [
    # Abertura
    ("terminaremos as obras dos viadutos da Avenida Cristiano Machado", "Concluir os viadutos da Avenida Cristiano Machado", "Mobilidade", "acao", "nao", "", "Cristiano Machado"),
    ("construiremos um boulevard entre a Catedral do Cristo Rei e o Shopping Estação", "Construir boulevard entre a Catedral Cristo Rei e o Shopping Estação", "Mobilidade", "acao", "nao", "", "Cristo Rei"),
    ("vamos entregar a Maternidade do Odilon Behrens", "Entregar a Maternidade do Hospital Odilon Behrens", "Saúde", "acao", "nao", "", "maternidade Odilon Behrens"),
    ("e mais 20 centros de saúde novinhos para a cidade", "Entregar 20 novos centros de saúde", "Saúde", "resultado", "nao", "", "centro de saúde"),
    ("faremos os viadutos da BR-040 no Belvedere", "Construir os viadutos da BR-040 no Belvedere", "Mobilidade", "acao", "nao", "", "Belvedere"),
    ("e o BRT da Avenida Amazonas", "Implantar o BRT da Avenida Amazonas", "Mobilidade", "acao", "nao", "", "BRT Amazonas"),
    ("Vamos concluir as obras contra enchentes da Vilarinho e Tereza Cristina", "Concluir as obras contra enchentes da Vilarinho e da Tereza Cristina", "Saneamento", "acao", "nao", "", "Vilarinho"),
    ("vamos entregar as obras do Anel Rodoviário com a redução de seus estreitamentos", "Entregar as obras do Anel Rodoviário que eliminam os estreitamentos", "Mobilidade", "acao", "nao", "União", "Anel Rodoviário"),
    ("vamos terminar toda a revitalização do Centro da cidade", "Concluir a revitalização do Centro (Centro de Todo Mundo)", "Infraestrutura", "acao", "nao", "", "Centro de Todo Mundo"),
    ("e entregar os projetos das obras urbanísticas nas centralidades definidas no plano diretor", "Entregar os projetos das obras urbanísticas nas centralidades do Plano Diretor", "Infraestrutura", "acao", "nao", "", "centralidades"),
    # Meio ambiente
    ("1. Implantação do Parque Ciliar do Onça.", "Implantar o Parque Ciliar do Onça (7 km, 20 mil árvores)", "Meio ambiente", "acao", "nao", "", "Parque Ciliar do Onça"),
    ("2. Implantação do Parque Taiobeiras no antigo aterro da Rodovia BR 040.", "Implantar o Parque Taiobeiras no antigo aterro da BR-040", "Meio ambiente", "acao", "nao", "", "Taiobeiras"),
    ("3. Implantação de corredores verdes nas grandes avenidas", "Implantar corredores verdes nas grandes avenidas", "Meio ambiente", "acao", "nao", "", "corredor verde"),
    ("4. Implantação do novo parque do bairro Jardim América", "Implantar o parque do bairro Jardim América", "Meio ambiente", "acao", "nao", "", "Jardim América"),
    ("e ampliação do Parque Tom Jobim no bairro Luxemburgo", "Ampliar o Parque Tom Jobim, no Luxemburgo", "Meio ambiente", "acao", "nao", "", "Tom Jobim"),
    ("5. Implantação de novas miniflorestas para contribuir com a melhoria do clima", "Implantar novas miniflorestas", "Meio ambiente", "acao", "nao", "", "minifloresta"),
    ("6. Instalação de novos refúgios climáticos", "Instalar refúgios climáticos contra o calor", "Meio ambiente", "acao", "nao", "", "refúgio climático"),
    ("7. Implantação do planejamento estratégico de arborização da cidade até 2050.", "Implantar o plano de arborização até 2050 (500 mil árvores a mais)", "Meio ambiente", "acao", "nao", "", "arborização"),
    ("Agora, vamos ampliar o atendimento veterinário e aumentar a rede de atendimento com parcerias com clínicas privadas.", "Ampliar o atendimento veterinário público com parcerias com clínicas privadas", "Meio ambiente", "acao", "nao", "", "veterinário"),
    # Assistência social
    ("» diversificação do acesso à moradia, possibilitando o aluguel social,", "Oferecer aluguel social, albergue e auxílio de acolhimento familiar à população de rua (Estamos Juntos 2)", "Assistência social", "acao", "nao", "", "Estamos Juntos"),
    ("» ampliação dos serviços de saúde mental com a criação de serviços", "Criar serviços próprios de saúde mental para a população de rua", "Saúde", "acao", "nao", "", "população em situação de rua"),
    ("» contratação, pela Prefeitura, dos beneficiários do programa para", "Contratar pela Prefeitura os beneficiários do Estamos Juntos para zeladoria e outros serviços", "Trabalho", "acao", "nao", "", "Estamos Juntos"),
    # Saúde
    ("A expectativa é que em 2025 estejamos rodando todo o sistema de forma plena.", "Pôr o prontuário eletrônico integrado em pleno funcionamento em 2025", "Saúde", "acao", "nao", "", "prontuário eletrônico"),
    ("o cidadão terá acesso a todas elas em um aplicativo de celular", "Lançar aplicativo com consultas, exames e vacinas do usuário do SUS-BH", "Saúde", "acao", "nao", "", "aplicativo saúde"),
    # Educação
    ("Vamos entregar 12 novas escolas até 2025 e reinaugurar a Emei Pilar Olhos d’Água.", "Entregar 12 novas escolas até 2025", "Educação", "resultado", "nao", "", "Emei"),
    ("Em 2025 haverá a expansão de vagas na educação infantil (cerca de 2.400 novas vagas em tempo integral ou 4.800 em tempo parcial) e no ensino fundamental (960 novas vagas).", "Abrir em 2025 cerca de 2.400 vagas integrais na educação infantil e 960 no ensino fundamental", "Educação", "resultado", "nao", "", "vagas educação infantil"),
    ("Outras mil vagas serão disponibilizadas nas creches conveniadas com a PBH.", "Abrir mil vagas nas creches conveniadas", "Educação", "resultado", "nao", "", "creches conveniadas"),
]

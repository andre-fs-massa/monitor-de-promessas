# Censo do plano de Alexandre Kalil (prefeitura de Belo Horizonte, 2016): uma tupla por promessa testável.
# (trecho_literal, promessa, area, tipo, depende_legislativo, outro_ente, termo de busca)
# O plano cobre só Saúde, Educação e Segurança; ficaram de fora diretrizes vagas ("fortalecer", "estimular",
# "desenvolver modelos"), campanhas genéricas, continuidade de programas e o que depende só de reivindicar.
P = [
    # Saúde
    ("Criação de uma Central de Atendimento eletrônica e física aos serviços de saúde", "Criar central de atendimento eletrônica e física para marcar consultas e exames pela internet", "Saúde", "acao", "nao", "", "agendamento online"),
    ("Fazer funcionar o Hospital Metropolitano do Barreiro em sua totalidade", "Pôr o Hospital Metropolitano do Barreiro em funcionamento pleno", "Saúde", "acao", "nao", "", "Hospital do Barreiro"),
    ("retomar a operação do setor de pediatria", "Retomar a pediatria do Hospital Risoleta Neves", "Saúde", "acao", "nao", "", "Risoleta Neves pediatria"),
    ("Ampliar a cobertura do Saúde da Família para 93%", "Ampliar a cobertura do Saúde da Família para 93%", "Saúde", "resultado", "nao", "", "Saúde da Família cobertura"),
    ("Criação de nove Cersams AD, um em cada região da cidade, e mais nove Cersams para adolescentes", "Criar 9 Cersams AD e 9 Cersams para adolescentes (um por regional)", "Saúde", "resultado", "nao", "", "Cersam AD"),
    ("Vacinação de 100% da população de risco contra a dengue.", "Vacinar 100% da população de risco contra a dengue", "Saúde", "resultado", "nao", "União", "vacina dengue"),
    ("100% de vacinação da população de risco contra o vírus H1N1.", "Vacinar 100% da população de risco contra o H1N1", "Saúde", "resultado", "nao", "", "vacinação gripe"),
    ("Cuidador, buscando a chegar a 1.000 atendimentos ano.", "Chegar a 1.000 atendimentos por ano no programa de cuidadores de idosos (Maior Cuidado)", "Assistência social", "resultado", "nao", "", "Maior Cuidado"),
    # Educação
    ("Aumentar o gasto per capita com a educação para, pelo menos, o nível da média nacional.", "Elevar o gasto per capita com educação ao menos à média nacional dos municípios", "Educação", "resultado", "nao", "", "gasto educação"),
    ("Triplicar o número de crianças matriculadas em ensino pré-escolar, passando para mais de 50 mil matriculados", "Triplicar as matrículas na pré-escola, para mais de 50 mil", "Educação", "resultado", "nao", "", "pré-escola vagas"),
    ("Até o final de nossa administração esperamos que pelo menos a metade dos estudantes matriculados tenham acesso a esse tipo de material de aprendizado", "Dar a pelo menos metade dos alunos acesso a tablets e sistemas de apoio ao ensino", "Educação", "resultado", "nao", "", "tablets alunos"),
    ("Aumentar número de Umeis de 126 para 150", "Aumentar as Umeis de 126 para 150", "Educação", "resultado", "nao", "", "Umei"),
    ("intensificados para mais de 5 milhões de atendimento", "Levar o Escola Aberta a mais de 5 milhões de atendimentos", "Educação", "resultado", "nao", "", "Escola Aberta"),
    ("Retomar e implementar o Plano Municipal já elaborado de Segurança Escolar.", "Retomar e implementar o Plano Municipal de Segurança Escolar", "Educação", "acao", "nao", "", "segurança escolar"),
    # Segurança
    ("Criação da Secretaria de Prevenção Social da Violência e Segurança.", "Criar a Secretaria de Prevenção Social da Violência e Segurança", "Segurança", "acao", "sim", "", "Secretaria de Segurança e Prevenção"),
    ("Organizar uma sala de crise no interior do Centro de Comando e Controle", "Criar sala de crise de segurança no Centro de Operações (COP-BH)", "Segurança", "acao", "nao", "", "COP-BH"),
]

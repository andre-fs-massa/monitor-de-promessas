# Censo do plano de Beto Richa (PR, 2010): uma tupla por promessa testável.
# (trecho_literal, promessa, area, tipo, depende_legislativo, outro_ente)
# O plano registrado no TSE (34 págs.) é diagnóstico, diretrizes e uma lista de "objetivos de governo" por área, quase
# todos genéricos (promover, incentivar, melhorar, fortalecer, ampliar sem objeto). Entram só os itens com objeto concreto
# (implantar/criar programa, sistema ou política nomeados, concluir obra ou rede) ou com programas de nome próprio a
# ampliar. Itens repetidos em várias áreas contam uma vez. Fora: "manter" (controle público das estatais, salário mínimo
# regional), "reestruturar a governança" das estatais, "checar" passivos e itens de gestão genéricos.
P = [
    ("Implantar modelo de gestão pública para resultados (contratos de gestão)",
     "Implantar modelo de gestão para resultados, com contratos de gestão", "Gestão pública", "acao", "nao", ""),
    ("Reorganizar a máquina administrativa do Estado",
     "Reorganizar a estrutura administrativa do Estado", "Gestão pública", "acao", "sim", ""),
    ("1. Retomar a implantação do Sistema Estratégico de Gestão de Recursos Hídricos",
     "Retomar a implantação do sistema estadual de gestão de recursos hídricos", "Meio ambiente", "acao", "nao", ""),
    ("Aprimorar o sistema de defesa animal (livre de aftosa sem vacinação)",
     "Tornar o Paraná área livre de febre aftosa sem vacinação", "Agricultura e abastecimento", "resultado", "nao", ""),
    ("Implantar a Rede Paranaense de Proteção às Famílias Vulneráveis",
     "Implantar rede estadual de proteção às famílias vulneráveis, com índice de vulnerabilidade social", "Assistência social", "acao", "nao", ""),
    ("Ampliar e promover os programas sociais da Tarifa Social da Água, Luz",
     "Ampliar os programas Tarifa Social da Água, Luz Fraterna e Leite das Crianças", "Assistência social", "acao", "nao", ""),
    ("Erradicar o trabalho infantil",
     "Erradicar o trabalho infantil no Paraná", "Assistência social", "resultado", "nao", ""),
    ("atenção ao recém nascido",
     "Implantar a Rede Mãe Paranaense de atenção ao pré-natal, parto e recém-nascido", "Saúde", "acao", "nao", ""),
    ("Implantar programa estadual de telemedicina",
     "Implantar programa estadual de telemedicina", "Saúde", "acao", "nao", ""),
    ("Implantar programa de fomento à cultura",
     "Implantar programa estadual de fomento à cultura", "Cultura", "acao", "sim", ""),
    ("Instituir conselhos artísticos e curadores",
     "Instituir conselhos artísticos e curadores na área da cultura", "Cultura", "acao", "nao", ""),
    ("Criar a política estadual do esporte, lazer e atividade física",
     "Criar a política estadual do esporte, lazer e atividade física", "Esporte", "acao", "nao", ""),
    ("Implantar programas que oportunizem a revelação de atletas",
     "Implantar programa estadual de revelação de atletas", "Esporte", "acao", "nao", ""),
    ("Concluir a instalação do sistema público de transmissão de dados de alta",
     "Concluir a rede de fibra óptica da Copel em todo o território paranaense", "Inclusão digital", "acao", "nao", ""),
    ("Resolver os problemas de dragagem do Canal da Galheta",
     "Resolver a dragagem do Canal da Galheta (Porto de Paranaguá)", "Mobilidade", "acao", "nao", ""),
    ("Implantar programa de tratamento e destinação de lixo",
     "Implantar programa estadual de tratamento e destinação de lixo", "Saneamento", "acao", "nao", ""),
    ("a manutenção e a ampliação da isenção de impostos para microempresas",
     "Ampliar a isenção de impostos para microempresas", "Ambiente de negócios", "acao", "sim", ""),
]

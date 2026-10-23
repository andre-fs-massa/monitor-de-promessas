# Censo do plano de Marcio Lacerda (prefeitura de Belo Horizonte, 2012): uma tupla por promessa testável.
# (trecho_literal, promessa, area, tipo, depende_legislativo, outro_ente, termo de busca)
# Plano de 4 páginas, de diretrizes; ficaram de fora continuidade (Vila Viva, metrô, OP, obras em andamento, cirurgias
# eletivas), frases vagas ("investimentos reforçados", "maior integração") e o programa de combate às pichações (já
# existia no Movimento Respeito por BH em 2012). Os trechos têm espaços duplos, como no texto extraído do PDF.
P = [
    ('programa\xa0 para\xa0 reduzir\xa0 o\xa0 tempo\xa0 de\xa0 espera\xa0 por\xa0 consultas\xa0especializadas', 'Implantar programa para reduzir o tempo de espera por consultas especializadas', 'Saúde', 'acao', 'nao', '', 'consultas especializadas'),
    ('programa\xa0 para\xa0 atendimentos\xa0 e\xa0 esclarecimentos\xa0 pediátricos,\xa0 24h\xa0por\xa0dia', 'Implantar programa de atendimento e orientação pediátrica 24 horas', 'Saúde', 'acao', 'nao', '', 'pediatria 24h'),
    ('será\xa0 criada\xa0 a\xa0 Coordenadoria\xa0 de\xa0 Defesa\xa0 dos\xa0Animais', 'Criar a Coordenadoria de Defesa dos Animais', 'Meio ambiente', 'acao', 'nao', '', 'Coordenadoria de Defesa dos Animais'),
    ('Expansão\xa0 da\xa0 Educação\xa0Infantil', 'Expandir a educação infantil (Umeis)', 'Educação', 'acao', 'nao', '', 'Umei'),
    ('Expansão\xa0 da\xa0 Escola\xa0 Integrada', 'Expandir a Escola Integrada', 'Educação', 'acao', 'nao', '', 'Escola Integrada'),
    ('a\xa0 vigilância\xa0 eletrônica\xa0 será\xa0 expandida', 'Expandir a vigilância eletrônica por câmeras', 'Segurança', 'acao', 'nao', '', 'câmeras Olho Vivo'),
    ('como\xa0 também\xa0 o\xa0 numero\xa0 de\xa0 Guardas\xa0 Municipais', 'Aumentar o efetivo da Guarda Municipal', 'Segurança', 'acao', 'nao', '', 'Guarda Municipal'),
    ('O\xa0 Programa\xa0 de\xa0Qualificação\xa0e\xa0Profissionalização,\xa0visando\xa0melhores\xa0condições\xa0de\xa0empregabilidade', 'Ampliar o Programa de Qualificação e Profissionalização em parceria com a iniciativa privada', 'Trabalho', 'acao', 'nao', '', 'qualificação profissional'),
    ('o\xa0acesso\xa0à\xa0internet\xa0livre\xa0será\xa0expandido', 'Expandir o acesso gratuito à internet (BH Digital)', 'Infraestrutura', 'acao', 'nao', '', 'internet gratuita'),
    ('o\xa0 BH\xa0 Resolve,\xa0 com\xa0 tão\xa0 ampla\xa0 e\xa0 consolidada\xa0 aceitação,\xa0 terá\xa0seus\xa0 serviços\xa0 ampliados', 'Ampliar os serviços do BH Resolve', 'Gestão pública', 'acao', 'nao', '', 'BH Resolve'),
    ('além\xa0 de\xa0 expandir\xa0 na\xa0 capital\xa0 o\xa0 Programa\xa0MCMV', 'Expandir o Minha Casa Minha Vida na capital', 'Habitação', 'acao', 'nao', 'União', 'Minha Casa Minha Vida'),
    ('será\xa0 implantado\xa0 o\xa0Orçamento\xa0 Participativo\xa0 da\xa0 Criança\xa0 e\xa0do\xa0 Adolescente\xa0 nas\xa0 Escolas\xa0 Municipais', 'Implantar o Orçamento Participativo da Criança e do Adolescente nas escolas municipais', 'Participação', 'acao', 'nao', '', 'OPCA'),
    ('o\xa0Planejamento\xa0Participativo\xa0Regionalizado\xa0também\xa0será\xa0ampliado', 'Ampliar o Planejamento Participativo Regionalizado', 'Participação', 'acao', 'nao', '', 'Planejamento Participativo Regionalizado'),
    ('o\xa0 programa\xa0 Cidadão\xa0 Auditor\xa0 será\xa0 expandido\xa0 para\xa0outros\xa0serviços', 'Expandir o Cidadão Auditor para outros serviços', 'Gestão pública', 'acao', 'nao', '', 'Cidadão Auditor'),
    ('será\xa0expandido\xa0também\xa0para\xa0os\xa0estudantes\xa0do\xa0Pró\xa0Uni\xa0e\xa0do\xa0EJA', 'Estender o meio passe escolar aos estudantes do ProUni e da EJA', 'Mobilidade', 'acao', 'nao', '', 'meio passe'),
    ('com\xa0 a\xa0 expansão\xa0 do\xa0 Programa\xa0 Vida\xa0 Ativa', 'Expandir o Programa Vida Ativa para idosos', 'Assistência social', 'acao', 'nao', '', 'Vida Ativa'),
    ('e\xa0 do\xa0 Programa\xa0 Maior\xa0Cuidado', 'Expandir o Programa Maior Cuidado para idosos', 'Assistência social', 'acao', 'nao', '', 'Maior Cuidado'),
]

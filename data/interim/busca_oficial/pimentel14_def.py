# Censo do plano de Fernando Pimentel (governo de Minas Gerais, 2014): uma tupla por promessa testável.
# (trecho_literal, promessa, area, tipo, depende_legislativo, outro_ente, termo de busca)
# O documento registrado é de "propostas e diretrizes", em parágrafos numerados; ficaram de fora diagnósticos,
# verbos vagos (fortalecer, potencializar, articular, intensificar) e intenções sem objeto concreto.
P = [
    ("O deslocamento de órgãos de administração para as diversas regiões de Minas Gerais", "Descentralizar a administração, levando órgãos estaduais para as regiões", "Gestão pública", "acao", "nao", "", "regionalização"),
    ("e de um novo modelo de ensino médio a ser implementado pelo novo Governo do Estado.", "Implantar um novo modelo de ensino médio", "Educação", "acao", "nao", "", "ensino médio"),
    ("A ampliação da educação infantil, que já vem sendo feita pelo Governo Federal e os Municípios, com participação pífia do Estado, é o primeiro passo estruturante.", "Ampliar a participação do Estado na oferta de educação infantil", "Educação", "acao", "nao", "Municípios", "educação infantil"),
    ("ampliando radicalmente a educação de tempo integral", "Ampliar a educação em tempo integral", "Educação", "acao", "nao", "", "tempo integral"),
    ("Ampliar, com novos conceitos, o ensino técnico e tecnológico, relacionado à dinâmica econômica e social regional.", "Ampliar o ensino técnico e tecnológico ligado às vocações regionais", "Educação", "acao", "nao", "", "ensino técnico"),
    ("estabelecer um plano de investimentos em tecnologia e recursos humanos que preencha estes vazios", "Fazer plano de investimentos para preencher os vazios assistenciais da rede de saúde", "Saúde", "acao", "nao", "", "vazios assistenciais"),
    ("que terão a sua atenção básica fortalecida e apoiada financeiramente pelo Estado.", "Apoiar financeiramente a atenção básica dos municípios", "Saúde", "acao", "nao", "Municípios", "atenção primária"),
    ("ser decisivo na construção de carreiras regionais para os médicos e outros profissionais de saúde", "Criar carreiras regionais para médicos e outros profissionais de saúde", "Saúde", "acao", "sim", "", "carreira saúde"),
    ("priorizar as grandes necessidades das população como a rede cuidadora para os dependentes químicos do crack, álcool e outras drogas", "Construir rede de atenção aos usuários de crack, álcool e outras drogas", "Saúde", "acao", "nao", "", "drogas"),
    ("O primeiro passo é tornar pública e transparente as informações sobre violência e performance da segurança.", "Tornar públicas as informações sobre violência e desempenho da segurança", "Segurança pública", "acao", "nao", "", "estatísticas criminalidade"),
    ("(a Polícia Militar é menor do que há doze anos e sequer tem o efetivo previsto em lei)", "Recompor o efetivo da Polícia Militar", "Segurança pública", "resultado", "nao", "", "efetivo Polícia Militar"),
    ("O planejamento para reativar, redimensionar e expandir a malha ferroviária de Minas é um exemplo", "Planejar a reativação e expansão da malha ferroviária", "Infraestrutura", "acao", "nao", "União", "ferrovia"),
]

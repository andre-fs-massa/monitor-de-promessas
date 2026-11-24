# Censo do plano de Beto Richa (PR, 2014): uma tupla por promessa testável.
# (trecho_literal, promessa, area, tipo, depende_legislativo, outro_ente)
# O "Plano de Metas 2015-2018" registrado no TSE (54 págs.) é quase todo diagnóstico do 1º mandato e diretrizes gerais;
# o próprio texto diz que seria "concluído ao longo da campanha". Entram só os compromissos com objeto concreto ou meta.
# Fora: "Política de Estado" genérica, ODS, green buildings, autossuficiência energética em 2025 (prazo além do mandato),
# PPPs como modelo genérico, estudos de óleo e gás, reforma do Estado em termos genéricos, cultura/esporte genéricos.
P = [
    ("Beto Richa propõe uma ampla reforma da estrutura administrativa do governo",
     "Fazer ampla reforma da estrutura administrativa do governo, reduzindo custos", "Gestão pública", "acao", "sim", ""),
    ("tendo ainda a meta de equipar e mobiliar 900 unidades até 2015",
     "Equipar e mobiliar 900 escolas estaduais até 2015 (Renova Escola)", "Educação", "resultado", "nao", ""),
    ("O Paraná definirá prioridades para a implantação de uma rede integrada de logística abrangendo todos os modais no Estado, num horizonte mínimo de 10 anos.",
     "Definir plano de prioridades para uma rede integrada de logística de todos os modais, com horizonte de 10 anos", "Mobilidade", "acao", "nao", ""),
    ("que dotará o estado de um novo e estratégico terminal de importação e exportação",
     "Implantar a faixa de infraestrutura de Pontal do Paraná, ligada a novo terminal portuário", "Mobilidade", "acao", "nao", ""),
    ("o governo implantará uma política específica para o setor, de forma a proteger os cidadãos de catástrofes naturais decorrentes das mudanças no clima do planeta",
     "Implantar política específica de proteção contra catástrofes decorrentes das mudanças climáticas", "Meio ambiente", "acao", "nao", ""),
    ("A administração estadual trabalhará, em parceria com a União, na concretização do Trem Pé-Vermelho",
     "Implantar, com a União, o Trem Pé-Vermelho entre Ibiporã e Paiçandu", "Mobilidade", "acao", "nao", "União"),
    ("O Paraná implantará uma política de aproveitamento de energias alternativas, particularmente óleo, gás e etanol",
     "Implantar política estadual de aproveitamento de energias alternativas (gás, etanol, biogás)", "Energia", "acao", "nao", ""),
    ("Formulação e implementação de nova etapa da Política Estadual de Desenvolvimento Científico e Tecnológico",
     "Formular e implementar nova etapa da Política Estadual de Desenvolvimento Científico e Tecnológico", "Ciência e tecnologia", "acao", "nao", ""),
    ("Aperfeiçoamento do marco legal da inovação do Estado do Paraná.",
     "Aperfeiçoar o marco legal da inovação do Paraná", "Ciência e tecnologia", "acao", "sim", ""),
]

# Classificação do censo de Marcio Lacerda (prefeitura de Belo Horizonte, 2012). Reeleito; mandato completo (2013-2016).
# Critério de mandato completo: não entregue até 31/12/2016 = não cumprida; "ampliar" sem número = cumprida se houve
# ampliação registrada (mesmo critério do Haddad 2012). O site da PBH foi refeito em 2017 e quase não guarda notícias
# de 2013-2016, por isso a busca se apoiou em imprensa, Câmara Municipal e trabalhos acadêmicos.
# Chave = índice (1-based) em lacerda12_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia) ou None.
SEM = "Busca na imprensa, na Câmara Municipal e no site da Prefeitura (jan/2013 a dez/2016) não localizou "


def S(txt, url="", data="2016-12"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


D = {
    1: S("um programa novo para reduzir a espera por consultas especializadas no mandato."),
    2: S("a implantação de um serviço de atendimento e orientação pediátrica 24 horas."),
    3: ("cumprida", "baixa", "O Decreto 16.431/2016 instituiu a Política de Proteção e Defesa dos Animais, que cita a Coordenadoria de Defesa dos Animais na Secretaria de Meio Ambiente; em mar/2014 a Secretaria já anunciava a criação do órgão.", "https://cmbh.mg.gov.br/sites/default/files/publicacoes/2024/05/nt_012_2024.pdf", "2016"),
    4: ("cumprida", "alta", "As 32 Umeis da PPP foram construídas entre 2013 e 2015, além das obras com recursos próprios e do MEC; em dez/2016 a cidade tinha 129 Umeis.", "https://www.em.com.br/app/noticia/gerais/2016/12/12/interna_gerais,831979/bh-comemora-aniversario-e-ganha-casa-de-acolhimento-infantil-e-umei.shtml", "2016-12"),
    5: ("cumprida", "media", "A Escola Integrada passou de 140 escolas em 2011 para 173 em 2014, com 53% dos alunos da rede municipal.", "https://periodicos.ufsc.br/index.php/perspectiva/article/download/2175-795X.2018v36n3p1072/pdf/203826", "2014"),
    6: S("a expansão da rede de câmeras de vigilância pela Prefeitura no mandato; o Olho Vivo é um convênio com o Estado e a CDL."),
    7: S("aumento do efetivo da Guarda Municipal no mandato (o concurso seguinte localizado é o de 2019)."),
    8: S("a ampliação do Programa de Qualificação e Profissionalização em parceria com a iniciativa privada."),
    9: S("a expansão dos pontos de internet gratuita no mandato; notícia posterior registra só 52 pontos da rede BH Digital.", "https://prefeitura.pbh.gov.br/noticias/pbh-vai-aumentar-em-mais-de-dez-vezes-o-numero-de-pontos-de-internet-gratuita"),
    10: ("cumprida", "media", "Em 2015 a Prefeitura lançou o aplicativo BH Resolve Mobile e licitou novas unidades do BH Resolve no Barreiro e em Venda Nova, com recursos do BNDES.", "https://www.em.com.br/app/noticia/gerais/2015/03/24/interna_gerais,630547/independentes-do-centro.shtml", "2015-03"),
    11: ("cumprida", "baixa", "Até 2016 a cidade somava 4.679 moradias da faixa 1 e 1.414 da faixa 2 do Minha Casa Minha Vida concluídas, segundo a Urbel; não foi localizado o recorte anual.", "https://cmbhweb.cmbh.mg.gov.br/sites/default/files/eventos/politicas_publicas_em_debate_-_habitacao.pdf", "2016"),
    12: ("cumprida", "alta", "O Orçamento Participativo da Criança e do Adolescente (OPCA) começou em 2014, com R$ 20 mil para cada uma de 16 escolas, e chegou a 70 escolas em quatro anos.", "https://prefeitura.pbh.gov.br/educacao/orcamento-participativo-da-crianca-e-do-adolescente-opca", "2014"),
    13: S("a ampliação do Planejamento Participativo Regionalizado no mandato."),
    14: S("a expansão do programa Cidadão Auditor para outros serviços."),
    15: ("parcialmente_cumprida", "baixa", "O meio passe passou a atender alunos do ensino médio e da EJA da rede pública, mas não foi estendido aos bolsistas do ProUni (em 2018 eram cerca de 8 mil beneficiários).", "https://www.brasildefato.com.br/2018/03/13/passe-estudantil-de-belo-horizonte-mg-atende-a-poucas-pessoas-e-nao-e-integral/", "2018-03"),
    16: S("registro da expansão do Vida Ativa no mandato (um artigo de 2014 cita 24 núcleos regionais, sem série anual)."),
    17: S("registro da expansão do Maior Cuidado no mandato."),
}
AJUSTES = {}

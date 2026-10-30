# Impacto fiscal das promessas de Fernando Haddad (prefeitura de São Paulo, 2012) no orçamento do Município de São Paulo.
# Base: 2012 (ano anterior ao mandato). Mandato completo: 2013-2016.
# Fonte oficial: despesa EMPENHADA (líquida) por projeto/atividade nos dados abertos da Prefeitura
# ("Execução orçamentária", scripts/orcamento_spcapital.py). O PPA 2014-2017 renumerou várias ações:
# a ação nova é somada à que ela substituiu. Quando o gasto do mandato fica abaixo de 2012, fica só o custo de 2016.
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
FO = "fora_do_orcamento"
PMSP = "https://dados.prefeitura.sp.gov.br/dataset/execucao-orcamentaria"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


def so(total, txt, conf="media"):
    return (DA, None, total, "2016", None, "", "sim", conf, txt, PMSP, "")


def acum(incr, total, acumulado, txt, rec="sim", conf="media"):
    return (DA, incr, total, "2016", acumulado, "2013-2016", rec, conf, txt, PMSP, "")


I = {
    1: acum(0.013, 0.013, 0.042, "Ampliação da jornada escolar (Programa Mais Educação, atividade 4303): sem gasto próprio em 2012 e 2013, R$ 13 milhões em 2014, R$ 16 milhões em 2015 e R$ 13 milhões em 2016. Subestima o custo, porque os professores da jornada ampliada são pagos pelas ações gerais de remuneração; parte do Mais Educação era paga com dinheiro federal.", "sim", "baixa"),
    2: acum(0.757, 1.824, 1.734, "Creches da rede conveniada (atividade 2825) e construção de CEIs e EMEIs (projetos 1452, 1427, 3359 e 3358): R$ 1,07 bi em 2012, R$ 1,15 bi em 2013, R$ 1,37 bi em 2014, R$ 1,66 bi em 2015 e R$ 1,82 bi em 2016. Inclui o reajuste do valor pago por criança às entidades conveniadas, não só as vagas novas.", "sim", "baixa"),
    3: d("Criar o conselho de representantes dos conselhos de escola é regra de participação.", SID),
    4: d("Aprovar o Plano Municipal de Educação é regra de planejamento.", SID),
    5: n("Criar novas diretorias regionais aumentaria a despesa administrativa"),
    6: d("Os cursos do Pronatec são pagos pelo governo federal.", FO),
    7: d("A coordenação de regulação usa servidores e sistemas existentes, com custo pequeno.", SID),
    8: n("A Renda Básica da Cidadania aumentaria a despesa"),
    9: d("Os dois restaurantes comunitários e o centro de segurança alimentar têm custo pequeno, sem ação própria no orçamento.", DA, "baixa"),
    10: acum(0.019, 0.064, 0.041, "Manutenção e implantação de CRAS e CREAS (atividades 6239 e 6236 e projetos 5841 e 3395): R$ 45 milhões em 2012, R$ 40 milhões em 2013, R$ 57 milhões em 2014, R$ 60 milhões em 2015 e R$ 64 milhões em 2016."),
    11: d("O canal de denúncias no 156 entrou no contrato da central de atendimento, com custo pequeno.", SID),
    12: d("Aderir ao Sistema Nacional de Cultura e criar o fundo de cultura é regra de gestão; o fundo reorganiza recursos já existentes.", SID),
    13: n("Recriar o conselho de cultura é regra de participação", SID),
    14: d("Ampliar o Centro Olímpico e criar núcleos de alto rendimento tem custo pequeno, sem ação própria no orçamento.", DA, "baixa"),
    15: n("Competições esportivas escolares teriam custo pequeno", SID),
    16: d("Os Conselhos Participativos das subprefeituras são regra de participação.", SID),
    17: d("A Controladoria reúne órgãos que já existiam, com custo pequeno.", SID),
    18: n("Uma política de saúde do servidor e a requalificação do HSPM aumentariam a despesa"),
    19: acum(0.004, 0.004, 0.004, "Conectividade e inclusão digital (Proconecta, atividade 4307): R$ 4 milhões em 2016; nos anos anteriores o WiFi Livre SP não tinha ação própria.", "sim", "baixa"),
    20: n("Um programa de prevenção à violência aumentaria a despesa"),
    21: n("Elaborar um mapa da violência tem custo pequeno", SID),
    22: n("Expandir a videovigilância da GCM aumentaria a despesa"),
    23: d("Os 500 guardas nomeados aumentam a folha de pagamento, paga pelas ações gerais de pessoal, sem valor separado."),
    24: acum(0.193, 0.577, 0.275, "Rede de iluminação pública: operação e manutenção (4912, que a partir de 2014 inclui a energia antes paga pelo FUNDIP, 4913), eficientização (5607) e novos pontos (5160 e 5606): R$ 384 milhões em 2012, R$ 354 milhões em 2013, R$ 343 milhões em 2014, R$ 537 milhões em 2015 e R$ 577 milhões em 2016. Inclui o aumento da conta de energia de 2015.", "sim", "baixa"),
    25: d("A política de estímulo a startups (Tech Sampa) tem custo pequeno.", SID),
    26: d("As universidades e institutos federais são pagos pela União; a Prefeitura apoiou com terrenos e articulação.", FO),
    27: n("Criar um conselho é regra de participação", SID),
    28: n("Uma política de economia criativa aumentaria a despesa"),
    29: d("O Programa Operação Trabalho foi usado no De Braços Abertos, sem ação própria separada; os demais programas não foram retomados.", DA, "baixa"),
    30: d("Comprar alimentos da agricultura familiar troca fornecedores da merenda, sem aumentar a despesa.", SID),
    31: d("Revisar o Plano Diretor e publicar o Programa de Metas é regra de planejamento.", SID),
    32: n("Transformar o conselho é regra de participação", SID),
    33: n("Parcerias público-comunitárias teriam custo pequeno", SID),
    34: d("Revisar o zoneamento é regra urbanística.", SID),
    35: d("O IPTU progressivo sobre imóveis ociosos aumenta a receita só a partir do 3º ano de notificação; o valor arrecadado não foi localizado.", "receita_aumenta", "baixa"),
    36: n("Um programa de cooperação técnica teria custo pequeno", SID),
    37: n("Moradia popular no centro aumentaria a despesa"),
    38: acum(0.108, 0.173, 0.602, "Construção de unidades habitacionais e de habitação de interesse social (projetos 3354 e 1060, desde 2014) e projetos e ações de apoio habitacional (1276): R$ 65 milhões em 2012, R$ 97 milhões em 2013, R$ 357 milhões em 2014, R$ 235 milhões em 2015 e R$ 173 milhões em 2016. O Minha Casa, Minha Vida é pago sobretudo pela União; antes de 2014 a construção pode ter sido paga por outras ações (como as operações urbanas), por isso a confiança é baixa. Gasto único.", "nao", "baixa"),
    39: so(0.397, "Urbanização de favelas, Programa Mananciais e regularização fundiária (1277/3357, 1254/3355 e 1281/3356): R$ 680 milhões em 2012, R$ 591 milhões em 2013, R$ 396 milhões em 2014, R$ 443 milhões em 2015 e R$ 397 milhões em 2016; no mandato ficou abaixo de 2012."),
    40: n("Formar estoque de terrenos aumentaria a despesa com desapropriações"),
    41: n("Acompanhamento pós-ocupação teria custo pequeno", SID),
    42: d("As faixas exclusivas são sinalização feita pela CET, sem ação própria no orçamento.", DA, "baixa"),
    43: d("Elaborar o Plano de Mobilidade é regra de planejamento.", SID),
    44: n("Um plano de logística é estudo, com custo pequeno", SID),
    45: n("Um órgão de gestão de cargas teria custo pequeno", SID),
    46: d("Criar o conselho de transportes é regra de participação.", SID),
    47: n("Centrais de controle do transporte aumentariam a despesa"),
    48: d("Os bilhetes diário, semanal e mensal reduzem a tarifa média e são cobertos pela compensação às empresas de ônibus, sem valor separado.", DA, "baixa"),
    49: d("Definir o novo modelo de concessão dos ônibus é regra contratual.", SID),
    50: acum(0.107, 0.125, 0.75, "Implantação e requalificação de corredores de ônibus (projetos 3701, 3702 e 3748 até 2013; 3378 a partir de 2014): R$ 18 milhões em 2012, R$ 94 milhões em 2013, R$ 272 milhões em 2014, R$ 331 milhões em 2015 e R$ 125 milhões em 2016. Gasto único de obra.", "nao", "media"),
    51: n("Estações intermodais exigiriam obra"),
    52: acum(0.001, 0.037, 0.103, "Implantação e requalificação de terminais de ônibus urbanos (projetos 3749 e 3750): R$ 36 milhões em 2012, R$ 57 milhões em 2013, R$ 78 milhões em 2014, R$ 75 milhões em 2015 e R$ 37 milhões em 2016. Gasto único de obra.", "nao", "media"),
    53: d("A modernização dos semáforos foi paga em contratos da CET, sem ação própria no orçamento.", DA, "baixa"),
    54: so(0.022, "Reforma de calçadas (projeto 1169): R$ 29 milhões em 2012 e entre R$ 1 milhão e R$ 22 milhões por ano no mandato, abaixo de 2012."),
    55: acum(0.019, 0.02, 0.108, "Implantação de ciclovias, ciclofaixas e ciclorrotas (projetos 7137 e 3377): R$ 1 milhão em 2012 e 2013, R$ 41 milhões em 2014, R$ 50 milhões em 2015 e R$ 20 milhões em 2016. Inclui os bicicletários (promessa 56). Gasto único de obra.", "nao", "media"),
    56: d("O custo dos bicicletários está somado na promessa 55."),
    57: d("O Bike Sampa é operado e patrocinado por empresa privada, sem gasto da Prefeitura.", FO),
    58: d("A inspeção veicular gratuita em 2013 transferiu à Prefeitura o custo da taxa; não há ação própria no orçamento, e o programa acabou em 2014.", DA, "baixa"),
    59: n("Estacionamentos públicos aumentariam a despesa"),
    60: d("Revisar os planos de drenagem, água e esgoto e resíduos é regra de planejamento.", SID),
}

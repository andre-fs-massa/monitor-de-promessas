# Impacto fiscal das promessas de Eduardo Paes (prefeitura do Rio de Janeiro, 2012) no orçamento do Município.
# Base: 2012 (ano anterior ao mandato). Mandato completo: 2013-2016.
# Fonte oficial: despesa EMPENHADA por ação nos dados abertos da prefeitura (Data.Rio, "Execução Orçamentária
# Despesas", 2008-2019; scripts/orcamento_rio.py). Quando o gasto do mandato fica abaixo de 2012, fica só o custo de 2016.
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
FO = "fora_do_orcamento"
RIO = "https://www.data.rio/datasets/PCRJ::execução-orçamentária-despesas"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


def so(total, txt, conf="media"):
    return (DA, None, total, "2016", None, "", "sim", conf, txt, RIO, "")


def acum(incr, total, acumulado, txt, rec="sim", conf="media"):
    return (DA, incr, total, "2016", acumulado, "2013-2016", rec, conf, txt, RIO, "")


I = {
    1: n("IDEB da rede municipal de pelo menos 6,0 nos anos iniciais e 5,0 nos anos finais em 2015 é meta de resultado ou regra, sem gasto próprio direto", SID),
    2: n("Ter ao menos 95% das crianças de 7 anos alfabetizadas em 2016 é meta de resultado ou regra, sem gasto próprio direto", SID),
    3: d("Meta de resultado educacional; o custo está nas ações gerais da educação.", SID),
    4: d("A ação própria das Escolas do Amanhã caiu de R$ 45 milhões em 2012 para R$ 1 milhão em 2016; o turno único é pago pelas ações gerais de pessoal e manutenção da educação, sem valor separado.", DA, "baixa"),
    5: d("Meta de resultado educacional; o custo está nas ações gerais da educação.", SID),
    6: acum(0.294, 0.7, 0.577, "Educação infantil: construção de EDIs (projetos 1024 e 1789), manutenção (2306/2133) e pessoal das unidades (2567): R$ 406 milhões em 2012, R$ 399 milhões em 2013, R$ 482 milhões em 2014, R$ 620 milhões em 2015 e R$ 700 milhões em 2016. Inclui reajustes salariais, não só as vagas novas.", "sim", "baixa"),
    7: d("As aulas de inglês do Rio Criança Global são dadas por professores da rede, pagos pelas ações gerais de pessoal.", DA, "baixa"),
    8: acum(0.069, 0.101, 0.09, "Construção, ampliação e reforma de unidades de Saúde da Família (projeto 1887): R$ 32 milhões em 2012, R$ 3 milhões em 2013, R$ 15 milhões em 2014, R$ 99 milhões em 2015 e R$ 101 milhões em 2016. Gasto único de obra; o custeio está na promessa 9.", "nao", "media"),
    9: acum(0.21, 1.005, 0.443, "Custeio da rede de atenção primária (atividade 2854, contratos com as Organizações Sociais das Clínicas da Família): R$ 795 milhões em 2012, R$ 879 milhões em 2013, R$ 848 milhões em 2014, R$ 891 milhões em 2015 e R$ 1,0 bi em 2016.", "sim", "media"),
    10: n("Chegar a 46 equipes e 70% de cobertura do PADI (atendimento domiciliar ao idoso) aumentaria a despesa"),
    11: n("Contratar mais 2 mil médicos para reduzir a espera por consultas aumentaria a despesa"),
    12: d("Meta de resultado da saúde; o custo está nas ações gerais da rede.", SID),
    13: d("Meta de resultado da saúde; o custo está nas ações gerais da rede.", SID),
    14: d("Meta de gestão de leitos, sem gasto relevante.", SID),
    15: n("Mortalidade infantil abaixo de 10 por mil nascidos vivos até 2016 é meta de resultado ou regra, sem gasto próprio direto", SID),
    16: n("Mortalidade materna abaixo de 41 por 100 mil nascidos vivos até 2016 é meta de resultado ou regra, sem gasto próprio direto", SID),
    17: (DA, None, None, "", 0.036, "2013-2016", "nao", "baixa", "Sistemas das unidades de saúde e central de regulação (atividade 2784): sem gasto próprio em 2012, R$ 28 milhões em 2013 e R$ 8 milhões em 2014.", RIO, ""),
    18: n("O esgoto da AP5 é concessão (Foz Águas 5); chegar a 55% de cobertura dependeria da concessionária", FO),
    19: d("O reflorestamento (Mutirão Reflorestamento) não tem ação própria identificada no orçamento.", DA, "baixa"),
    20: n("Plantar 500 mil árvores em parques, praças e unidades de conservação até 2016 aumentaria a despesa"),
    21: (DA, None, None, "", 0.051, "2013-2016", "nao", "media", "Implantação de ciclovias e ciclofaixas (projetos 1711, 1797 e 3003): R$ 1 milhão em 2012, R$ 9 milhões em 2013, R$ 15 milhões em 2014, R$ 31 milhões em 2015 e nada em 2016. Gasto único de obra.", RIO, ""),
    22: n("Coletar 25% do lixo reciclável da cidade até 2016 aumentaria a despesa"),
    23: n("Reduzir em 16% as emissões de gases de efeito estufa até 2016, sobre 2005 é meta de resultado ou regra, sem gasto próprio direto", SID),
    24: d("As obras de macrodrenagem (reservatórios da Praça da Bandeira e outros) não têm ação própria identificada depois de 2012 (a ação 3716 teve R$ 92 milhões em 2012 e nada depois); devem estar em ações gerais de obras.", DA, "baixa"),
    25: n("Elaborar plano de adaptação às mudanças climáticas e plano municipal de gestão costeira é meta de resultado ou regra, sem gasto próprio direto", SID),
    26: n("Reformar mais de 170 mil m² de praças e parques (15 Minutos Verdes) aumentaria a despesa"),
    27: n("Urbanizar 100 comunidades, levando infraestrutura a mais 81 mil domicílios (Morar Carioca) até 2016 aumentaria a despesa"),
    28: d("As moradias do Minha Casa, Minha Vida são pagas sobretudo pela União; a prefeitura entra com terrenos, infraestrutura e cadastro, sem valor separado.", FO, "baixa"),
    29: n("Não ter mais famílias em áreas de alto risco (encostas) até 2016 aumentaria a despesa"),
    30: n("Reduzir em ao menos 5% a área ocupada por favelas até 2016, sobre 2008 é meta de resultado ou regra, sem gasto próprio direto", SID),
    31: acum(0.311, 0.435, 0.595, "Urbanização e revitalização em espaços públicos (projetos 1922 e 1796), que pagam o Bairro Maravilha: R$ 124 milhões em 2012, R$ 18 milhões em 2013, R$ 209 milhões em 2014, R$ 429 milhões em 2015 e R$ 435 milhões em 2016. Inclui outras obras de urbanização. Gasto único de obra.", "nao", "baixa"),
    32: acum(0.045, 0.218, 0.142, "Aporte de capital na CDURP, a companhia do Porto Maravilha (1924), e revitalização da área portuária (1915, 2603 e 3638): R$ 173 milhões em 2012, R$ 167 milhões em 2013, R$ 196 milhões em 2014, R$ 253 milhões em 2015 e R$ 218 milhões em 2016. A maior parte das obras foi paga fora do orçamento, com a venda de CEPACs ao FGTS.", "nao", "baixa"),
    33: acum(0.004, 0.004, 0.015, "Implantação da UPP Social e indicadores do Rio+Social (projetos 3720 e 3304): sem gasto em 2012, R$ 5 milhões em 2013, R$ 4 milhões em 2014, R$ 2 milhões em 2015 e R$ 4 milhões em 2016.", "sim", "media"),
    34: acum(0.477, 0.477, 1.576, "Projetos e obras do Parque Olímpico (projeto 3724): sem gasto em 2012, R$ 48 milhões em 2013, R$ 342 milhões em 2014, R$ 709 milhões em 2015 e R$ 477 milhões em 2016. A PPP com a concessionária Rio Mais foi paga em parte com terrenos, fora do orçamento. Gasto único de obra.", "nao", "media"),
    35: d("O fechamento da Av. Rio Branco veio com o VLT; o custo está na promessa 44."),
    36: n("Criar operação urbana consorciada para revitalizar a Cidade Nova é meta de resultado ou regra, sem gasto próprio direto", SID),
    37: d("Meta de resultado dos BRTs e BRS; o custo dos corredores está na promessa 41.", SID),
    38: d("Meta de resultado de segurança no trânsito, sem gasto separado.", SID),
    39: d("A integração do Bilhete Único Carioca é paga por subsídio às empresas de transporte, sem ação própria identificada no orçamento.", DA, "baixa"),
    40: n("Ter 60% dos usuários de transporte público usando trem, metrô ou BRT até 2016 é meta de resultado ou regra, sem gasto próprio direto", SID),
    41: acum(0.269, 0.876, 2.233, "BRTs: infraestrutura viária da TransCarioca (1719) e da TransOlímpica (1720) e implantação da TransBrasil (1753): R$ 607 milhões em 2012, R$ 1,15 bi em 2013, R$ 1,19 bi em 2014, R$ 1,44 bi em 2015 e R$ 876 milhões em 2016. Inclui recursos federais repassados pelo orçamento municipal. Gasto único de obra.", "nao", "media"),
    42: n("Modernizar 100% da frota de ônibus (ar-condicionado, motor traseiro, acessibilidade) até 2016 é meta de resultado ou regra, sem gasto próprio direto", SID),
    43: n("Ter 100% dos táxis no padrão do Rio Boa Praça até 2016 é meta de resultado ou regra, sem gasto próprio direto", SID),
    44: acum(0.237, 0.237, 0.55, "Implantação do VLT do Centro (projeto 1755): sem gasto em 2012, R$ 49 milhões em 2013, R$ 43 milhões em 2014, R$ 221 milhões em 2015 e R$ 237 milhões em 2016. Inclui recursos federais (PAC) repassados pelo orçamento municipal; a operação é paga pela PPP. Gasto único de obra.", "nao", "media"),
    45: d("Racionalizar as linhas de ônibus é regra de operação do sistema.", SID),
    46: d("Elaborar o Plano de Mobilidade é regra de planejamento.", SID),
    47: n("Destinar 2/3 (ou 70%) dos recursos da prefeitura às Zonas Norte e Oeste é meta de resultado ou regra, sem gasto próprio direto", SID),
    48: n("Investir R$ 34,3 bilhões é meta fiscal agregada, não um gasto próprio da promessa", "regra_fiscal"),
    49: acum(0.015, 0.015, 0.12, "Apoio e fomento à produção cultural (atividade 2739): sem gasto nessa ação em 2012, R$ 38 milhões em 2013, R$ 33 milhões em 2014, R$ 34 milhões em 2015 e R$ 15 milhões em 2016. Em 2012 o fomento pode ter sido pago por outra ação.", "sim", "baixa"),
    50: n("Dobrar a frequência nos equipamentos culturais municipais até 2016, sobre 2011 é meta de resultado ou regra, sem gasto próprio direto", SID),
    51: d("O Museu de Arte do Rio e o Museu do Amanhã foram feitos com a Fundação Roberto Marinho e o Porto Maravilha (CEPACs), em grande parte fora do orçamento municipal.", FO, "baixa"),
    52: d("A recuperação de imóveis do centro histórico teve gasto pequeno na ação própria (projeto 1773: R$ 2 milhões em 2013 e em 2014).", DA, "baixa"),
    53: d("A restauração do Centro Cultural José Bonifácio não tem ação própria identificada no orçamento.", DA, "baixa"),
    54: d("O escritório de projetos culturais tem custo pequeno.", SID),
    55: n("Reduzir à metade a população abaixo da linha de pobreza até 2015, sobre 2007 aumentaria a despesa"),
    56: n("Eliminar a pobreza entre os beneficiários do Bolsa Família e do Cartão Família Carioca até 2016 aumentaria a despesa"),
    57: acum(0.007, 0.021, 0.015, "Ações de atenção psicossocial e desinstitucionalização em saúde mental (atividades 2850 e 2748): R$ 14 milhões em 2012, R$ 17 milhões em 2013, R$ 13 milhões em 2014, R$ 20 milhões em 2015 e R$ 21 milhões em 2016. Os CAPS são pagos também pelo custeio geral da rede.", "sim", "media"),
    58: n("Atender pelo Saúde da Família 100% dos beneficiários do Cartão Família Carioca nas áreas cobertas aumentaria a despesa"),
    59: n("Levar o Rio em Forma a 100% das Escolas do Amanhã até 2016 aumentaria a despesa"),
    60: acum(0.239, 0.481, 0.608, "Pessoal da Guarda Municipal (provisão de pessoal da administração indireta da Ordem Pública, 4522) e atividades operacionais da Guarda (4564): R$ 242 milhões em 2012, R$ 275 milhões em 2013, R$ 389 milhões em 2014, R$ 431 milhões em 2015 e R$ 481 milhões em 2016. Inclui reajustes salariais, não só os guardas novos.", "sim", "baixa"),
    61: so(0.242, "Recapeamento e obras de pavimentação e drenagem em logradouros (Asfalto Liso 1722, 1022 e 1718): R$ 478 milhões em 2012 e entre R$ 87 milhões e R$ 242 milhões por ano no mandato, abaixo de 2012.", "baixa"),
    62: n("Revitalizar 700 mil m² de calçadas e 5 mil rampas (Rio Acessível) até 2016 aumentaria a despesa"),
    63: acum(0.106, 0.259, 0.249, "Manutenção da iluminação pública (2330, 2153 e 4153): R$ 153 milhões em 2012, R$ 165 milhões em 2013, R$ 172 milhões em 2014, R$ 265 milhões em 2015 e R$ 259 milhões em 2016. Pode incluir a conta de energia, que subiu em 2015.", "sim", "baixa"),
    64: d("Mapear a iluminação e elaborar o plano é estudo, com custo pequeno.", SID),
    65: d("Investir 15% do orçamento é meta fiscal agregada, não um gasto próprio da promessa.", "regra_fiscal"),
    66: so(0.005, "Central 1746 (atividade 2706): R$ 18 milhões em 2012, R$ 20 milhões em 2013, R$ 19 milhões em 2014, R$ 4 milhões em 2015 e R$ 5 milhões em 2016 (parte do custo passou a outras ações).", "baixa"),
    67: ("despesa_reduz", None, 0.033, "2015", 0.033, "2015", "nao", "media", "O projeto de compras estratégicas reduziu em R$ 32,7 milhões os gastos conduzidos em 2015, segundo os Resultados de 2015 do Acordo de Resultados (Diário Oficial de 11/04/2016); não há valor para os outros anos.", "https://doweb.rio.rj.gov.br/portal/edicoes/download/3075/7", ""),
    68: n("Fazer a receita própria crescer 15% ao ano aumentaria a receita", "receita_aumenta"),
    69: d("A rede de alta velocidade e o datacenter da IplanRio não têm ação própria identificada no orçamento.", DA, "baixa"),
    70: n("Transformar as 33 administrações regionais em centros de atendimento ao cidadão até 2016 aumentaria a despesa"),
    71: d("O sistema de monitoramento de metas é regra de gestão.", SID),
    72: n("Ampliar os sorteios da Nota Carioca para 5.000 premiados por ano aumentaria a despesa"),
    73: n("Consolidar as leis tributárias municipais em um único ato normativo é meta de resultado ou regra, sem gasto próprio direto", SID),
    74: d("Emitir alvarás por meio eletrônico é mudança de procedimento.", SID),
    75: n("Atrair R$ 1 bilhão de investimentos de empresas de energia e P&D até 2016 é meta de resultado ou regra, sem gasto próprio direto", SID),
    76: d("Os novos quartos de hotel foram investimento privado.", SID),
    77: n("Elevar de 2,2% para 2,75% a fatia do emprego na economia criativa até 2016 é meta de resultado ou regra, sem gasto próprio direto", SID),
    78: n("Criar condomínio industrial na Zona Oeste (mais de 500 mil m²) e novo parque tecnológico para o setor de energia aumentaria a despesa"),
    79: n("Fazer PPP para construir centro de convenções na Zona Portuária aumentaria a despesa"),
    80: n("Criar agência de capacitação e investimento para a indústria criativa aumentaria a despesa"),
}

# Impacto fiscal das promessas de Ricardo Nunes (prefeitura de São Paulo, 2024) no orçamento do Município de São Paulo.
# Base: 2024 (ano anterior ao mandato). Mandato em curso (2025-2028): único ano completo é 2025; 2026 fica fora.
# Fonte oficial: despesa EMPENHADA (líquida) por projeto/atividade nos dados abertos da Prefeitura ("Execução
# orçamentária", scripts/orcamento_spcapital.py). 2024 foi ano de pico de obras; quando o gasto de 2025 ficou abaixo
# de 2024, fica só o custo de 2025.
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
    """Gasto de 2025 abaixo de 2024: só o custo de 2025."""
    return (DA, None, total, "2025", None, "", "sim", conf, txt, PMSP, "")


def inc(incr, total, txt, rec="sim", conf="media"):
    return (DA, incr, total, "2025", incr, "2025", rec, conf, txt, PMSP, "")


I = {
    1: n("Um planejamento de longo prazo tem custo pequeno (estudos)", SID),
    2: inc(0.031, 0.125, "Construção e implantação de equipamentos de atenção básica e especialidades (projeto 1525): R$ 93,5 milhões em 2024 e R$ 124,5 milhões em 2025. Inclui outros equipamentos além das UBSs; o custeio das novas unidades fica na manutenção geral da atenção básica.", "nao", "baixa"),
    3: n("Ampliar o Hospital do Servidor exigiria obra"),
    4: d("As novas equipes de Saúde da Família são pagas pela manutenção geral da atenção básica (atividade 2520, que mistura especialidades e serviços auxiliares), sem valor separado."),
    5: d("A Central de Saúde Digital começou a operar em ago/2026, fora do período com ano completo (2025).", DA, "media"),
    6: n("Expandir a acreditação das unidades teria custo de consultoria e adequação"),
    7: (DA, None, 5.974, "2025", None, "", "sim", "media",
         "Manter a fila zerada depende sobretudo da rede parceira de creches (atividade 2828): R$ 5,90 bi em 2024 e R$ 5,97 bi em 2025. É o custo de manter o atendimento, não um gasto novo.", PMSP, ""),
    8: so(0.072, "Ações de Educação Integral (atividade 4303): R$ 129 milhões em 2024 e R$ 72 milhões em 2025. Subestima o custo, porque os professores das horas a mais são pagos pelas ações gerais de remuneração do ensino fundamental.", "baixa"),
    9: n("Polos de empreendedorismo nos CEUs aumentariam a despesa"),
    10: n("Bebetecas nos CEUs aumentariam a despesa"),
    11: d("As Olimpíadas do Conhecimento ainda estão em edital; a premiação aumentará a despesa, sem valor em 2025."),
    12: d("O projeto Rolê Agroecológico está em seleção de parceria (2026), sem gasto em 2025."),
    13: inc(0.009, 0.071, "Programa Reencontro (atividade 4884): R$ 62,3 milhões em 2024 e R$ 70,9 milhões em 2025. As Vilas Reencontro em obra podem estar em outras ações."),
    14: d("Os Centros Dia para Idosos são pagos pela manutenção geral dos equipamentos de assistência social, sem valor separado."),
    15: d("O serviço Família Acolhedora e o auxílio maior (Lei 18.406/2026) aumentam a despesa; não há ação própria no orçamento e o aumento do auxílio é de 2026."),
    16: n("Um programa para cuidadores aumentaria a despesa"),
    17: n("Casas do Adolescente aumentariam a despesa"),
    18: n("Um plano de juventude tem custo pequeno", SID),
    19: d("O Meu Trampo não tem ação própria no orçamento (as ações de juventude ficaram estáveis: R$ 21,0 milhões em 2024 e R$ 20,3 milhões em 2025).", DA, "baixa"),
    20: d("A unidade móvel está prevista para 2028, sem gasto em 2025."),
    21: so(0.028, "Centros Municipais para Pessoas com TEA (projeto 5407): R$ 47,3 milhões em 2024 e R$ 27,8 milhões em 2025; o Centro TEA Leste só teve ordem de início em jun/2026."),
    22: d("As salas de descompressão começam no 2º semestre de 2026, sem gasto em 2025."),
    23: inc(0.008, 0.077, "Proteção social especial à pessoa com deficiência (atividade 6152), que paga a Casa Mãe Paulistana aberta em nov/2025: R$ 69,3 milhões em 2024 e R$ 76,8 milhões em 2025. A ação inclui outros serviços.", "sim", "baixa"),
    24: d("O concurso de 2 mil guardas está em andamento e as nomeações estão previstas para 2027; ainda não há despesa com o novo efetivo."),
    25: d("A ronda escolar está em projeto-piloto e a diária especial ainda está em regulamentação, sem valor separado."),
    26: inc(0.052, 0.115, "Redes de monitoramento remoto para segurança urbana, que pagam o Smart Sampa (atividade 2199): R$ 63,6 milhões em 2024 e R$ 115,2 milhões em 2025."),
    27: n("Atualizar o mapeamento de risco tem custo pequeno (estudos)", SID),
    28: n("Ampliar os núcleos comunitários de Defesa Civil tem custo pequeno", SID),
    29: n("Construir Centros Olímpicos aumentaria a despesa"),
    30: inc(0.002, 0.004, "Bolsa Atleta (atividade 4550): R$ 2,9 milhões em 2024 e R$ 4,4 milhões em 2025."),
    31: n("Academias nos centros esportivos aumentariam a despesa"),
    32: n("Uma lei de incentivo ao esporte reduziria a receita (renúncia de tributos)", "receita_reduz"),
    33: n("Cursos técnicos nos equipamentos culturais aumentariam a despesa"),
    34: n("Pontos de reciclagem criativa aumentariam a despesa"),
    35: n("O VAI 60+ aumentaria a despesa com fomento"),
    36: n("O Programa Longevidade na Cultura aumentaria a despesa"),
    37: n("Os OASES aumentariam a despesa"),
    38: inc(0.006, 0.01, "Programa Sampa+Rural (atividade 2015): R$ 3,9 milhões em 2024 e R$ 9,7 milhões em 2025."),
    39: n("Uma plataforma de dados tem custo pequeno", SID),
    40: d("O Centro de Inovação da Praça Victor Civita está em obras; não há ação própria que separe o custo (as ações de inovação caíram de R$ 4,2 milhões em 2024 para zero em 2025).", DA, "baixa"),
    41: d("O Distrito de Inovação é um grupo de trabalho intersecretarial, sem gasto relevante.", SID),
    42: d("Renovar as certificações ISO tem custo pequeno.", SID),
    43: d("O credenciamento de projetos em ambiente regulatório experimental é regra, sem gasto relevante.", SID),
    44: (DA, None, 0.006, "2025", None, "", "sim", "media",
          "Conectividade e inclusão digital (Proconecta, atividade 4307), que paga o WiFi Livre SP: R$ 6,0 milhões em 2024 e R$ 6,2 milhões em 2025, praticamente estável.", PMSP, ""),
    45: d("Elaborar o Plano de Cidade Inteligente tem custo pequeno.", SID),
    46: n("Uma semana temática de promoção teria custo pequeno", SID),
    47: d("O Vai de Roteiro é feito pela SPTuris com custo pequeno, dentro do apoio geral ao turismo.", SID),
    48: d("O SP CityPass está em planejamento, sem gasto em 2025; com transporte incluído, como prometido, aumentaria a despesa.", DA, "baixa"),
    49: n("Expandir o City Tour aumentaria a despesa"),
    50: so(1.053, "Programa Mananciais (projeto 3355): R$ 1,25 bi em 2024 e R$ 1,05 bi em 2025."),
    51: so(0.131, "Construção e requalificação de parques e arborização (projetos 1702 e 1703 e atividade 6655): R$ 367 milhões em 2024 (vários dos parques entregues em 2025 foram construídos em 2024) e R$ 131 milhões em 2025. A manutenção dos parques (atividade 2703) subiu de R$ 350 milhões para R$ 392 milhões e não está somada."),
    52: n("Um programa de entregas com veículos de emissão zero depende de regras e de parceiros", SID),
    53: n("Expandir o Plarc aumentaria a despesa"),
    54: n("Qualificar os centros de bairro aumentaria a despesa"),
    55: n("Ecoportos no Rio Pinheiros aumentariam a despesa"),
    56: d("As 853 moradias do PIU Vila Leopoldina estão em desapropriação e permuta de áreas, sem ação própria com gasto em 2025."),
    57: d("O prolongamento da Marginal Pinheiros (PIU Arco Jurubatuba) está em licitação, sem gasto separado em 2025."),
    58: n("A Ponte de Veleiros exigiria obra"),
    59: n("O VLT no centro exigiria obra (foi trocado por um veículo elétrico sem trilhos, com obras previstas para 2027)"),
    60: n("Destamponar o Rio Tamanduateí exigiria obra"),
    61: n("O projeto da Foz do Ipiranga exigiria obra"),
    62: so(0.02, "Construção de ciclovias, ciclofaixas e ciclorrotas (projeto 1097): R$ 127,1 milhões em 2024 e R$ 20,1 milhões em 2025."),
    63: d("A ciclopassarela foi inaugurada em jan/2025; a obra foi paga antes do mandato.", DA, "baixa"),
    64: inc(0.051, 0.123, "Implantação e construção de terminais de ônibus (projeto 1095): R$ 72,1 milhões em 2024 e R$ 123,2 milhões em 2025. Gasto único de obra.", "nao"),
    65: d("A Faixa Azul é sinalização feita pela CET, sem ação própria no orçamento.", DA, "baixa"),
    66: inc(0.004, 0.164, "Corredores e BRTs (projeto 1099 de implantação de corredores e projetos do BRT Aricanduva 1094, 3762 e 3763): R$ 160 milhões em 2024 e R$ 164 milhões em 2025. Gasto único de obra; inclui as obras iniciadas da promessa 67.", "nao"),
    67: d("O custo das obras iniciadas está somado na promessa 66 (concluir corredores)."),
    68: inc(0.045, 0.209, "Contraprestação das PPPs de terminais urbanos (atividade 4663), que inclui a concessão do Bloco Leste desde set/2025: R$ 164 milhões em 2024 e R$ 209 milhões em 2025. A concessão troca o custo de operar os terminais (atividade 2096: R$ 162 milhões em 2024 e R$ 124 milhões em 2025) pela contraprestação.", "sim", "baixa"),
    69: d("A expansão do Aquático SP para a Billings e a Guarapiranga está em projeto e estudos, sem obra contratada; o gasto do sistema hidroviário existente ficou estável (R$ 25 milhões em 2024 e R$ 26 milhões em 2025)."),
    70: d("Os ônibus elétricos são comprados pelas empresas e pagos na remuneração do sistema (compensações tarifárias de R$ 7,1 bi em 2025), sem valor separado.", DA, "baixa"),
    71: so(1.215, "Programa Pode Entrar (projeto 3340): R$ 2,46 bi em 2024 e R$ 1,22 bi em 2025."),
    72: n("Acompanhar obras e filas pela internet tem custo pequeno", SID),
    73: so(0.104, "Regularização fundiária (projeto 3356): R$ 336 milhões em 2024 e R$ 104 milhões em 2025; o novo programa só foi lançado em mai/2026.", "baixa"),
    74: n("Acomodações temporárias em imóveis públicos aumentariam a despesa"),
    75: inc(0.005, 0.024, "Ampliação, reforma e requalificação de unidades habitacionais (projeto 3353): R$ 19,0 milhões em 2024 e R$ 23,8 milhões em 2025. Gasto único de obra.", "nao"),
    76: so(0.973, "Intervenções no sistema de drenagem (projeto 5013), que paga os reservatórios: R$ 2,25 bi em 2024 e R$ 0,97 bi em 2025.", "baixa"),
    77: so(0.017, "Obras nas áreas de risco geológico (projeto 1193): R$ 33,7 milhões em 2024 e R$ 16,9 milhões em 2025; as obras dos 14 editais estão começando."),
    78: n("Monitorar as galerias pluviais aumentaria a despesa"),
    79: d("A pavimentação de vias de terra é paga pela mesma ação do recapeamento (projeto 1137: R$ 2,09 bi em 2024 e R$ 0,56 bi em 2025), sem valor separado.", DA, "baixa"),
    80: n("Um piloto de pisos permeáveis teria custo pequeno", SID),
    81: d("Os bosques urbanos são uma regra de uso do solo, com custo pequeno.", SID),
    82: d("Ampliar o programa de integridade é regra de gestão, sem gasto relevante.", SID),
    83: d("Implantar a gestão de riscos é regra de gestão, sem gasto relevante.", SID),
    84: d("A concessão do Parque Campo de Marte passa o investimento e a operação à concessionária.", FO),
    85: d("A concessão dos parques da Orla do Guarapiranga passaria o custeio à concessionária; ainda não há contrato.", FO),
    86: d("A PPP do Parque Dom Pedro II foi assinada em mar/2026; a contraprestação só começa depois de 2025.", DA, "baixa"),
    87: n("Transformar o arquivo em centro de documentação aumentaria a despesa"),
    88: d("Padronizar as compras públicas é regra de gestão; pode reduzir custos, sem valor medido.", SID),
    89: d("O conselho de segurança jurídica tributária é regra, sem gasto relevante.", SID),
    90: d("Consulta pública antes de normas tributárias é regra, sem gasto relevante.", SID),
    91: d("Reestruturar o comitê gestor da concessão da Sabesp é regra, sem gasto relevante.", SID),
    92: d("Atualizar o Plano de Saneamento tem custo pequeno; as obras são da concessionária.", SID),
}

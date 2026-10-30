# Impacto fiscal das promessas de Bruno Covas (prefeitura de São Paulo, 2020) no orçamento do Município de São Paulo.
# Base: 2020 (ano anterior ao mandato). Mandato completo 2021-2024 (Covas morreu em mai/2021; Ricardo Nunes, vice,
# completou o mandato e é contado, como na classificação). Fonte oficial: despesa EMPENHADA (líquida) por
# projeto/atividade nos dados abertos da Prefeitura ("Execução orçamentária", scripts/orcamento_spcapital.py).
# Quando o gasto do mandato fica abaixo de 2020, fica só o custo de 2024.
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
FO = "fora_do_orcamento"
PMSP = "https://dados.prefeitura.sp.gov.br/dataset/execucao-orcamentaria"
METAS = "https://prefeitura.sp.gov.br/documents/d/planejamento/relatorio-de-execucao-do-programa-de-metas-2021-2024_2024-pdf"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


def so(total, txt, conf="media", ano="2024"):
    """Gasto do mandato abaixo de 2020: só o custo do último ano."""
    return (DA, None, total, ano, None, "", "sim", conf, txt, PMSP, "")


def acum(incr, total, acumulado, txt, rec="sim", conf="media"):
    return (DA, incr, total, "2024", acumulado, "2021-2024", rec, conf, txt, PMSP, "")


I = {
    1: d("A reserva de vaga em creche para filhos de mães do pré-natal (Mãe Paulistana Creche) é regra de prioridade; o custo das vagas está na promessa 2.", SID),
    2: acum(3.516, 5.947, 10.316,
            "Rede parceira de creches (atividade 2828) e construção de CEIs e EMEIs (projetos 3359 e 3361): R$ 2,43 bi em 2020, R$ 4,31 bi em 2021, R$ 5,10 bi em 2022, R$ 4,69 bi em 2023 e R$ 5,95 bi em 2024. Inclui o reajuste do valor pago por criança às entidades conveniadas, não só as vagas novas.",
            "sim", "baixa"),
    3: n("Construir 12 CEUs aumentaria a despesa (só 5 saíram; a construção de CEUs teve R$ 158 milhões em 2020 e R$ 440 milhões em 2021-2024)"),
    4: n("Ampliar a Bolsa Primeira Infância aumentaria a despesa (o gasto caiu de R$ 4,5 milhões em 2020 para zero em 2022)"),
    5: n("Digitalizar todas as salas de aula aumentaria a despesa"),
    6: acum(0.125, 0.129, 0.155,
            "Ações de Educação Integral (atividade 4303): R$ 4 milhões em 2020, R$ 1 milhão em 2021, R$ 17 milhões em 2022, R$ 24 milhões em 2023 e R$ 129 milhões em 2024. Subestima o custo, porque os professores das horas a mais são pagos pelas ações gerais de remuneração.",
            "sim", "baixa"),
    7: d("Repassar o crédito de uniforme e material às famílias muda a forma de compra, não o valor da despesa.", SID),
    8: d("Ampliar os leitos de Parelheiros e Brasilândia aumenta o custeio, pago pela manutenção geral dos hospitais (atividade 2507), sem valor separado."),
    9: d("O custeio do Hospital Santa Dulce dos Pobres fica na manutenção geral dos hospitais, sem valor separado.", DA, "baixa"),
    10: d("Mudar o perfil do Hospital Guarapiranga para cuidados prolongados troca um custeio por outro, sem valor separado.", SID, "baixa"),
    11: n("Ampliar o Hospital Sorocabana exigiria obra (só começou em set/2024)"),
    12: so(0.066, "Avança Saúde SP (projetos 9204 e 5204, mais a construção de hospitais 5416 em 2020): R$ 227 milhões em 2020, R$ 181 milhões em 2021, R$ 169 milhões em 2022, R$ 269 milhões em 2023 e R$ 66 milhões em 2024, ou R$ 685 milhões no mandato. O programa, financiado pelo BID, já gastava em 2020, por isso o gasto do mandato ficou abaixo do de 2020."),
    13: so(0.032, "Construção de UPAs e equipamentos hospitalares (projetos 1512 e 1535): R$ 21 milhões em 2020 e R$ 32 milhões em 2024 (R$ 71 milhões no mandato). O custeio das novas UPAs fica na manutenção geral da urgência, sem valor separado.", "baixa"),
    14: n("Abrir 6 Centros de Cuidados Integrados aumentaria a despesa (só 1 foi aberto)"),
    15: d("A telessaúde usa a rede e o app existentes, com custo pequeno e sem ação própria.", DA, "baixa"),
    16: n("Treinar 60 mil profissionais teria custo pequeno", SID),
    17: acum(2.809, 2.919, 5.428,
             "Moradias de interesse social: Pode Entrar (projeto 3340, desde 2023), construção de unidades habitacionais (3354) e PPP da habitação (3661): R$ 110 milhões em 2020, R$ 565 milhões em 2021, R$ 625 milhões em 2022, R$ 1,76 bi em 2023 e R$ 2,92 bi em 2024. Gasto único de obra e aquisição.",
             "nao", "media"),
    18: acum(1.287, 1.551, 2.649,
             "Urbanização de favelas e assentamentos precários: Programa de Mananciais (3355), urbanização de favelas (3357) e urbanização de assentamentos do Programa de Metas (5405, em 2020): R$ 264 milhões em 2020, R$ 207 milhões em 2021, R$ 710 milhões em 2022, R$ 1,24 bi em 2023 e R$ 1,55 bi em 2024. Gasto único de obra.",
             "nao", "media"),
    19: acum(0.169, 0.602, 0.548,
             "PPP da iluminação pública (atividade 6027), que fez a troca por LED, mais a manutenção antiga da rede (6161), que ela absorveu: R$ 433 milhões em 2020, R$ 521 milhões em 2021, R$ 557 milhões em 2022, R$ 600 milhões em 2023 e R$ 602 milhões em 2024. O contrato é de 2018; o aumento reflete o avanço da modernização.",
             "sim", "baixa"),
    20: n("Instalar 20 mil novos pontos de luz aumentaria a despesa"),
    21: d("Os 2.015 guardas contratados aumentam a folha de pagamento, paga pelas ações gerais de pessoal, sem valor separado."),
    22: acum(0.064, 0.064, 0.064,
             "Redes de monitoramento remoto para segurança urbana (atividade 2199, Smart Sampa): sem gasto próprio até 2023 e R$ 64 milhões em 2024. A integração ao City Câmeras antes de 2024 não tinha ação própria.",
             "sim", "baixa"),
    23: n("Instalar 12 mil equipamentos de vigilância nas escolas aumentaria a despesa"),
    24: d("Ampliar a frota de drones da GCM tem custo pequeno.", SID),
    25: d("O wi-fi nos ônibus é instalado pelas empresas e pago na remuneração do sistema (compensações tarifárias), sem valor separado.", DA, "baixa"),
    26: acum(0.085, 0.142, 0.474,
             "Implantação e requalificação de corredores de ônibus (projetos 5392, 1099, 1100 e 5393): R$ 57 milhões em 2020, R$ 44 milhões em 2021, R$ 208 milhões em 2022, R$ 308 milhões em 2023 e R$ 142 milhões em 2024. Inclui outros corredores e reformas além do Leste-Itaquera. Gasto único de obra.",
             "nao", "baixa"),
    27: n("Implantar o BRT Aricanduva exigiria obra"),
    28: acum(0.025, 0.025, 0.058,
             "Implantação do transporte hidroviário (projeto 5362): sem gasto em 2020 e 2021, R$ 2 milhões em 2022, R$ 31 milhões em 2023 e R$ 25 milhões em 2024. Gasto único de implantação; a operação começou a ser paga em 2025.",
             "nao", "media"),
    29: n("Duplicar a Estrada do M'Boi Mirim exigiria obra (começou em dez/2025)"),
    30: n("Concluir o complexo Pirituba-Lapa exigiria obra (retomada em jan/2024)"),
    31: so(0.127, "Construção e requalificação de ciclovias (projetos 1097 e 1098): R$ 103 milhões em 2020, R$ 42 milhões em 2021, R$ 117 milhões em 2022, R$ 85 milhões em 2023 e R$ 127 milhões em 2024; no mandato, ficou abaixo do ritmo de 2020."),
    32: so(0.075, "Reforma de calçadas (projeto 1169): R$ 141 milhões em 2020, quase nada em 2021 e 2022, R$ 56 milhões em 2023 e R$ 75 milhões em 2024."),
    33: so(0.006, "Conectividade e inclusão digital (Proconecta, atividade 4307), que paga o WiFi Livre SP: entre R$ 3 milhões e R$ 6 milhões por ano, praticamente estável."),
    34: ("receita_aumenta", None, 13.3, "2024", 13.3, "2021-2024", "nao", "media",
         "Plano de desestatização (concessões, PPPs e venda de ativos): o Programa de Metas registra R$ 13,3 bi arrecadados entre 2021 e 2024 (meta 74). Receita única; a divisão por ano não foi separada.",
         METAS, ""),
    35: acum(0.077, 0.077, 0.177,
             "Descomplica SP (construção, projeto 1358, e manutenção, atividade 2403): sem gasto próprio em 2020, R$ 3 milhões em 2021, R$ 45 milhões em 2022, R$ 52 milhões em 2023 e R$ 77 milhões em 2024."),
    36: so(0.524, "A prorrogação da Renda Básica Emergencial em 2021 (Lei 17.553/2021) foi paga como benefício eventual (atividade 6167): R$ 524 milhões em 2021. Em 2020 a Renda Básica Emergencial custou R$ 417 milhões; depois de 2021 o gasto voltou a cerca de R$ 40 milhões por ano.", "media", "2021"),
    37: n("Triplicar as vagas em repúblicas aumentaria a despesa"),
    38: acum(0.017, 0.021, 0.027,
             "Políticas e ações para juventude (atividade 4318), que paga a Rede Daora: R$ 4 milhões em 2020 e R$ 21 milhões em 2024. A ação inclui outros programas de juventude.",
             "sim", "baixa"),
    39: n("Zonas de flexibilização tributária reduziriam a receita", "receita_reduz"),
    40: d("O Hub Green Sampa funciona em espaço da Prefeitura, com custo pequeno.", SID),
    41: d("Os TEIAs (coworkings públicos) têm custo pequeno, sem ação própria.", SID),
    42: n("Áreas 24 horas dependem de regras de funcionamento", SID),
    43: acum(0.009, 0.016, 0.016,
             "Plantio de árvores e arborização (atividades 7130 e 6655): R$ 7 milhões em 2020, R$ 4 milhões em 2021, R$ 8 milhões em 2022 e R$ 16 milhões em 2023 e em 2024.",
             "sim", "media"),
    44: n("Implantar o Parque Minhocão exigiria obra"),
    45: d("O Parque Augusta foi feito em acordo com as construtoras donas do terreno; a construção de parques da Prefeitura em 2021 (projeto 1702, R$ 29 milhões) não separa cada parque.", DA, "baixa"),
    46: d("A construção de parques em 2021 (projeto 1702, R$ 29 milhões) inclui o Parque Paraisópolis, sem valor separado.", DA, "baixa"),
    47: n("Conceder os parques passaria o custeio às concessionárias", FO),
    48: so(0.01, "Apoio às cooperativas e centrais de triagem (atividades 2410 e 6006): R$ 9 milhões em 2020 e R$ 10 milhões em 2024. A coleta seletiva em si é paga nos contratos de limpeza urbana, sem valor separado.", "baixa"),
}

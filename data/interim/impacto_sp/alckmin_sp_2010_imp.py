# Impacto fiscal das promessas de Geraldo Alckmin (governo de SP, 2010) no orçamento do Estado de São Paulo.
# Base: 2010 (ano anterior ao mandato). Anos do mandato: 2011-2014.
# Fonte oficial: despesa EMPENHADA por ação no SIGEO (Secretaria da Fazenda, consulta da Lei 131)
# (scripts/orcamento_sp.py sigeo).
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
FO = "fora_do_orcamento"
SIP = "sem_impacto_primario"
SIGEO = "https://www.fazenda.sp.gov.br/SigeoLei131/Paginas/FlexConsDespesa.aspx"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


I = {
    1: (DA, 0.061, 0.061, "2014", 0.074, "2011-2014", "sim", "baixa",
        "Educação integral (ação 6136), criada com o Programa Ensino Integral: sem empenho até 2012, R$ 12 milhões em 2013 e R$ 61 milhões em 2014. Subestima o custo, porque a maior parte do salário e da gratificação dos professores estava nas ações gerais de pessoal.",
        SIGEO, ""),
    2: n("Instituir o Aluno em Tempo Integral aumentaria a despesa"),
    3: d("O Via Rápida Emprego paga bolsas e cursos, mas o gasto fica em ações gerais de qualificação profissional, sem separação.", conf="baixa"),
    4: (DA, 0.632, 1.789, "2014", 1.683, "2011-2014", "sim", "baixa",
        "Soma das ações do Centro Paula Souza (Etecs e Fatecs): expansão e desenvolvimento da educação profissional técnica e tecnológica (1515, 2226, 5290, 5292) e ensino médio (5852). Foram R$ 1,16 bi em 2010, R$ 1,26 bi em 2011, R$ 1,38 bi em 2012, R$ 1,89 bi em 2013 e R$ 1,79 bi em 2014. Inclui pessoal e reajustes, não só as unidades novas; o valor também cobre as Fatecs da promessa 7.",
        SIGEO, ""),
    5: n("Criar meios de compra de computadores aumentaria a despesa ou seria crédito"),
    6: d("O programa Rede paga cursos técnicos em instituições parceiras, mas o gasto não aparece em ação própria do orçamento.", conf="baixa"),
    7: d("As novas Fatecs estão nas ações do Centro Paula Souza, contadas na promessa 4; as vagas das universidades estaduais são pagas pelo repasse fixo do ICMS, sem despesa nova do Tesouro.", conf="baixa"),
    8: (DA, None, 0.029, "2014", None, "", "sim", "media",
        "Univesp (ação 2076 até 2012 e ação 6137 depois): R$ 23 milhões em 2010, R$ 20 milhões em 2011, R$ 22 milhões em 2012, R$ 16 milhões em 2013 e R$ 29 milhões em 2014. No mandato o gasto ficou abaixo de 2010, por isso só o custo de 2014.",
        SIGEO, ""),
    9: d("Os novos AMEs aumentam a despesa (obra e custeio), mas o gasto não aparece em ação própria do orçamento.", conf="baixa"),
    10: d("As novas unidades da Rede Lucy Montoro aumentam a despesa, mas o gasto não aparece em ação própria do orçamento até 2015.", conf="baixa"),
    11: d("O programa Recomeço e suas unidades aumentam a despesa, mas no período o gasto não aparece em ação própria do orçamento.", conf="baixa"),
    12: n("Ampliar a reforma dos hospitais estaduais aumentaria a despesa"),
    13: n("Ampliar o Dose Certa aumentaria a despesa"),
    14: n("Ampliar a entrega de medicamentos em casa aumentaria a despesa"),
    15: d("A Rede Hebe Camargo teve investimento anunciado de R$ 190 milhões, mas o gasto não aparece em ação própria do orçamento.", conf="baixa"),
    16: d("O Centro de Referência do Idoso e o São Paulo Amigo do Idoso têm custo pequeno frente ao orçamento.", conf="baixa"),
    17: n("Ampliar o efetivo policial aumentaria a despesa com pessoal"),
    18: n("Aumentar o número de delegados aumentaria a despesa com pessoal"),
    19: d("A Atividade Delegada é paga pelas prefeituras conveniadas, não pelo orçamento do Estado.", FO),
    20: d("Transferir presos das delegacias exige vagas em presídios (promessa 23); a desativação das carceragens não tem gasto próprio separado.", SID),
    21: n("Expandir a Delegacia Eletrônica teria custo pequeno", SID),
    22: d("O Detecta (2014) tem custo pequeno frente ao orçamento e não aparece em ação própria no período.", conf="baixa"),
    23: d("As novas unidades prisionais aumentam a despesa com obra e custeio. A consulta ao SIGEO da ação de adequação do sistema prisional (1898) foi interrompida antes de terminar, por isso não há valor.", conf="baixa"),
    24: n("Ampliar as videoconferências aumentaria a despesa no início e reduziria a escolta depois"),
    25: n("Ampliar o monitoramento eletrônico aumentaria a despesa no início e poderia reduzir o custo de vagas depois"),
    26: n("O Banco do Povo empresta recursos que voltam ao Estado; levá-lo a mais municípios é crédito, sem efeito no resultado primário", SIP),
    27: n("Expandir o Emprega São Paulo teria custo pequeno", SID),
    28: d("O Via Rápida e a Escola de Qualificação do Fundo Social pagam cursos, mas o gasto fica em ações gerais de qualificação, sem separação.", conf="baixa"),
    29: n("Ampliar o Renda Cidadã e o Ação Jovem aumentaria a despesa"),
    30: d("Implantação de Centros de Integração da Cidadania (ação 1218): R$ 1 milhão em 2010 e quase nada no mandato; o custeio dos novos CICs fica em ações gerais, com custo pequeno frente ao orçamento.", conf="media"),
    31: n("Ampliar e recuperar as vicinais aumentaria a despesa"),
    32: (DA, 0.014, 0.018, "2014", 0.024, "2011-2014", "nao", "media",
        "Microbacias II (ação 2286), projeto com financiamento do Banco Mundial: R$ 3,6 milhões em 2010, R$ 5,4 milhões em 2011, R$ 5,5 milhões em 2012, R$ 9,3 milhões em 2013 e R$ 18 milhões em 2014.",
        SIGEO, ""),
    33: n("Ampliar o Melhor Caminho aumentaria a despesa"),
    34: n("Ampliar o Viva Leite aumentaria a despesa"),
    35: n("Ampliar o Bom Prato aumentaria a despesa"),
    36: d("O aumento da vegetação nativa veio de regras ambientais e de recomposição feita por proprietários, sem gasto próprio do Estado.", SID),
    37: d("Criar parques estaduais é ato de proteção; a gestão das unidades é paga por ações gerais da Fundação Florestal, com custo pequeno.", SID),
    38: n("Universalizar o esgoto é obra da Sabesp, fora do orçamento do Estado", FO),
    39: (DA, None, 0.116, "2014", 0.242, "2011-2014", "nao", "media",
        "Reservatórios de retenção, os piscinões (ação 1573), e drenagem contra enchentes (ação 1021): R$ 180 milhões em 2010, R$ 269 milhões em 2011, R$ 244 milhões em 2012, R$ 332 milhões em 2013 e R$ 116 milhões em 2014. Gasto único de obra.",
        SIGEO, ""),
    40: n("Implantar o Parque das Várzeas do Tietê aumentaria a despesa"),
    41: d("O Projeto Tietê é obra da Sabesp, fora do orçamento do Estado.", FO),
    42: n("Ampliar a urbanização de favelas aumentaria a despesa"),
    43: d("A CDHU seguiu entregando moradias, mas sem balanço de ampliação; a despesa da produção não foi comparada.", conf="baixa"),
    44: d("Os convênios da Defesa Civil para obras preventivas aumentam a despesa, mas o valor não aparece separado no orçamento.", conf="baixa"),
    45: n("Ampliar o Vila Dignidade aumentaria a despesa"),
    46: d("Criar a Secretaria de Desenvolvimento Metropolitano tem custo administrativo pequeno.", SID),
    47: d("Instituir os fundos metropolitanos só cria as contas; o gasto depende de aportes, não separados.", SID),
    48: (DA, 1.368, 3.93, "2014", 3.351, "2011-2014", "nao", "media",
        "Subscrição de ações do Metrô (ação 1695), da CPTM (1856) e da EMTU (1693), forma pela qual o Estado paga as obras de metrô, trens e corredores: R$ 2,56 bi em 2010, R$ 2,77 bi em 2011, R$ 3,20 bi em 2012, R$ 3,71 bi em 2013 e R$ 3,93 bi em 2014. Inclui também a modernização das linhas existentes. Gasto único de obra.",
        SIGEO, ""),
    49: n("Modernizar as linhas da CPTM aumentaria a despesa"),
    50: n("Levar o trem a Guarulhos aumentaria a despesa"),
    51: n("Implantar o VLT da Baixada aumentaria a despesa"),
    52: n("Concluir o Corredor Noroeste aumentaria a despesa"),
    53: (DA, 0.566, 1.319, "2014", 0.984, "2011-2014", "nao", "baixa",
        "Obras do Rodoanel Norte (ação 2283: R$ 34 milhões em 2012, R$ 2,01 bi em 2013 e R$ 1,20 bi em 2014) e subscrição de ações da Dersa, que fez o Trecho Sul (ação 1679: R$ 753 milhões em 2010, R$ 630 milhões em 2011 e R$ 119 milhões em 2014). O Trecho Leste foi feito pela concessionária, fora do orçamento. A subscrição da Dersa também paga outras obras. Gasto único de obra.",
        SIGEO, ""),
    54: n("Ampliar a capacidade da hidrovia aumentaria a despesa"),
    55: d("Levar a Virada Cultural a mais cidades tem custo pequeno frente ao orçamento.", conf="baixa"),
    56: n("Criar o Ruas 24 Horas aumentaria a despesa (custo pequeno)"),
    57: n("Criar o Museu da História de São Paulo aumentaria a despesa"),
    58: d("A reforma do antigo prédio do Detran para o MAC USP foi gasto único, pequeno frente ao orçamento e sem ação própria.", conf="baixa"),
    59: n("Criar o Cine Cidade aumentaria a despesa (custo pequeno)"),
    60: d("Ampliar o Bolsa Talento Esportivo tem custo pequeno frente ao orçamento.", conf="baixa"),
    61: d("O Cartão VidAtiva começou em fase piloto em dez/2013, com custo pequeno.", conf="baixa"),
    62: n("Construir o Centro Olímpico aumentaria a despesa"),
    63: n("Reformar as unidades esportivas aumentaria a despesa"),
    64: d("O incentivo da Copa (Decreto 58.339/2012) é crédito de ICMS para investimento esportivo e reduz a receita, mas a renúncia não foi separada.", "receita_reduz", "baixa"),
    65: n("Ampliar a desburocratização é gestão, sem gasto relevante", SID),
    66: (DA, 0.136, 0.399, "2014", 0.424, "2011-2014", "sim", "media",
        "Operação do Poupatempo (ação 5372): R$ 263 milhões em 2010, R$ 316 milhões em 2011, R$ 358 milhões em 2012, R$ 403 milhões em 2013 e R$ 399 milhões em 2014. Inclui o reajuste dos contratos, não só os postos novos.",
        SIGEO, ""),
    67: d("Os novos postos do Acessa São Paulo aumentam a despesa. A consulta ao SIGEO da ação do programa (5636) foi interrompida antes de terminar, por isso não há valor; o custo é pequeno frente ao orçamento.", conf="baixa"),
    68: d("A Banda Larga Popular é isenção de ICMS para planos de internet baratos e reduz a receita, mas a renúncia não foi separada.", "receita_reduz", "baixa"),
}

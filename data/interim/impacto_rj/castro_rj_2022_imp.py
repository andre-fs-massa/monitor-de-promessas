# Impacto fiscal das promessas de Cláudio Castro (governo do RJ, 2022) no orçamento do Estado do RJ.
# Base: 2022 (ano anterior ao mandato). Renunciou em 23/03/2026: anos completos 2023-2025.
# Os portais oficiais do Estado (Transparência, SEFAZ, TCE, Alerj) recusam conexões feitas daqui; os valores são os
# investimentos anunciados pelo governo e publicados na imprensa (fonte_comparacao) e por isso têm confiança média ou baixa.
# Investimento em obra ou equipamento é gasto único (recorrente = "nao"); o acumulado é o valor investido no mandato.
NI = "; não implementada."
PORTAIS = " O portal de transparência do Estado não pôde ser consultado; valor anunciado pelo governo e publicado na imprensa."


def d(txt, cat="despesa_aumenta", conf="media"):
    """Direção sem valor."""
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


I = {
    1: d("Meta de emprego; é resultado da economia e de outros programas, não de uma despesa própria.", "sem_valor_proprio"),
    2: d("Mudança de regras de gestão; não implementada.", "sem_impacto_direto"),
    3: d("Construir o metrô leve aumentaria a despesa com investimento" + NI),
    4: d("Reativar o teleférico aumentaria a despesa (obra e operação); não voltou a operar até a renúncia."),
    5: d("Concluir o museu aumentaria a despesa com obra; só abriu depois da renúncia."),
    6: ("despesa_aumenta", None, 0.115, "2025", None, "", "nao", "baixa",
        "Abertura e reforma de Restaurantes do Povo: o governo diz ter investido mais de R$ 115 milhões no programa (ex.: R$ 12 milhões na unidade de Nova Iguaçu, dez/2024, e R$ 1,6 milhão na de Barra Mansa), sem divisão por ano. O custeio das refeições não foi divulgado." + PORTAIS,
        "", "https://digital.correiodamanha.com.br/jornalcorreiodamanha/2025/12/24/23221b/pdf/2412cmanha17.pdf"),
    7: d("Reforma de Cieps como E-Tecs: o governo anunciou R$ 150 milhões para as 50 escolas, mas só 22 foram entregues e não há valor do que foi gasto." + PORTAIS, conf="baixa"),
    8: d("Construir moradias aumentaria a despesa; a meta não foi atingida e não há valor do que foi gasto."),
    9: d("Novas bases da Segurança Presente aumentam a despesa (policiais em horário extra pago e viaturas), parte paga pela Fecomércio e por prefeituras; o custo anual do programa não é divulgado." + PORTAIS, conf="baixa"),
    10: ("despesa_aumenta", None, 0.09, "2023", 0.09, "2023", "nao", "media",
         "Construção e equipamentos do Rio Imagem Baixada (Nova Iguaçu), com recursos do Pacto RJ: R$ 90 milhões. O custeio anual do centro não foi divulgado." + PORTAIS,
         "", "https://digital.correiodamanha.com.br/jornalcorreiodamanha/2025/09/29/222151/pdf/2909cmanha11.pdf"),
    11: d("Observatório de dados, com custo pequeno frente ao orçamento.", "sem_impacto_direto"),
    12: d("Obra da Cedae, empresa estatal com orçamento próprio, fora do orçamento fiscal do Estado.", "fora_do_orcamento"),
    13: ("despesa_aumenta", None, 0.021, "2024", 0.021, "2024", "nao", "media",
         "Repasse do Estado de R$ 21 milhões para o Hospital do Coração de Duque de Caxias, hospital municipal inaugurado em set/2024." + PORTAIS,
         "", "https://www.correiodamanha.com.br/baixada/2026/08/311264-hospital-do-coracao-de-caxias-e-referencia-na-baixada.html"),
    14: d("Lançar o museu aumentaria a despesa" + NI),
    15: d("Concessão de ferrovia federal; não passa pelo orçamento do Estado.", "sem_impacto_direto"),
    16: d("Construir as moradias aumentaria a despesa" + NI),
    17: d("Fazer a ligação viária aumentaria a despesa" + NI),
    18: ("despesa_aumenta", None, 0.287, "2024", None, "", "nao", "baixa",
         "Corredor MUVI (Neves–Guaxindiba), em parceria com a Prefeitura de São Gonçalo: investimento anunciado de R$ 287 milhões (R$ 262 milhões no início das obras), sem divisão entre Estado e prefeitura nem por ano; a obra não estava concluída." + PORTAIS,
         "", "https://folhadoleste.com.br/obras-muvi-sao-goncalo-mobilidade/"),
    19: d("Revitalizar as vias aumentaria a despesa; sem balanço do que foi feito."),
    20: d("Construir moradias aumentaria a despesa; as entregas ficaram muito abaixo da meta e não há valor."),
    21: d("Reformar as casas aumentaria a despesa; só os projetos foram entregues, sem valor divulgado.", conf="baixa"),
    22: d("Bases do Samu e motolâncias aumentam a despesa; a compra das 30 motolâncias e de ambulâncias (R$ 87,4 milhões no programa Samu 100% RJ) foi feita em 2022, antes do mandato, e o custeio das novas bases não foi divulgado.", conf="baixa"),
    23: d("Levar o curso ao Cantagalo aumentaria a despesa" + NI),
    24: d("Plantio pago pelo Fundo da Mata Atlântica (recursos de compensação ambiental geridos pelo Funbio) e por parceiros privados, fora do orçamento fiscal do Estado; o programa soma mais de R$ 100 milhões.", "fora_do_orcamento"),
    25: d("Ligar os incentivos a metas poderia aumentar a receita" + NI + " A Lei 11.071/2025 aumentou a contribuição das empresas beneficiadas ao Fundo Orçamentário Temporário, mas não é o que foi prometido.", "receita_aumenta", "baixa"),
    26: d("Novas escolas interculturais aumentam a despesa com educação, sem valor separado.", conf="baixa"),
    27: d("Levar cursos a novas cidades aumentaria a despesa" + NI),
    28: ("despesa_aumenta", None, 0.087, "2026", 0.087, "2023-2026", "nao", "media",
         "Construção do Instituto Estadual de Oncologia da Baixada (Nova Iguaçu), inaugurado em fev/2026: R$ 87,3 milhões do Estado, sem divisão por ano. O custeio do hospital não foi divulgado." + PORTAIS,
         "", "https://www.tupi.fm/?p=2284749"),
    29: ("despesa_aumenta", None, 0.075, "2024", None, "", "nao", "baixa",
         "Obra do Hospital Estadual de Oncologia de Nova Friburgo, retomada em 2022 e não inaugurada: o governo citava cerca de R$ 75 milhões em 2024 (R$ 65,3 milhões em outra reportagem), sem divisão por ano." + PORTAIS,
         "", "https://www.correiodamanha.com.br/correio-serrano/2024/07/144296-hospital-oncologico-de-nova-friburgo-sera-entregue-em-novembro-de-2024.html"),
    30: d("Consolidar o hospital aumentaria a despesa" + NI),
    31: d("Ampliar o hospital aumentaria a despesa" + NI),
    32: d("Concluir a maternidade aumentaria a despesa; até a renúncia só houve a cooperação com a EMOP e uma reserva de R$ 1,65 milhão (nov/2025).", conf="baixa"),
    33: ("despesa_aumenta", None, 0.011, "2024", 0.011, "2024", "nao", "media",
         "Primeira fase da reforma do Hospital Getúlio Vargas (emergência e CTI), entregue em set/2024: R$ 10,6 milhões com equipamentos. Azevedo Lima e Roberto Chabo não tiveram obra." + PORTAIS,
         "", "https://www.correiodamanha.com.br/nacional/sudeste/2024/09/156984-modernizacao-do-hospital-estadual-getulio-vargas.html"),
    34: d("Ampliar o programa aumentaria a despesa" + NI),
    35: d("Mudança de gestão; não implementada.", "sem_impacto_direto"),
    36: d("Base da Segurança Presente em Búzios; o valor do programa está no item 9.", "sem_valor_proprio"),
    37: d("Novas bases aumentariam a despesa" + NI),
    38: d("Construir o complexo aumentaria a despesa" + NI),
    39: d("Contratar médicos e profissionais de saúde para a PM aumentaria a despesa com pessoal; os aprovados não tinham tomado posse até a renúncia."),
    40: d("Novos módulos do Bairro Presente aumentam a despesa (policiais em horário extra pago e viaturas); custo não divulgado.", conf="baixa"),
    41: d("Sistema de dados, com custo pequeno frente ao orçamento; não implementado.", "sem_impacto_direto"),
    42: d("Ampliar a via aumentaria a despesa" + NI),
    43: d("Reformar as casas aumentaria a despesa" + NI),
    44: d("Zona de processamento de exportação: regime fiscal federal; a implantação não chegou a funcionar.", "sem_impacto_direto"),
    45: d("Regime aduaneiro federal em aeroporto federal; não implementado.", "sem_impacto_direto"),
    46: d("Novos centros aumentariam a despesa" + NI),
    47: d("Pacto de articulação entre órgãos, sem orçamento próprio.", "sem_impacto_direto"),
    48: d("Criar a casa aumentaria a despesa" + NI),
    49: d("Novos polos aumentariam a despesa" + NI),
}

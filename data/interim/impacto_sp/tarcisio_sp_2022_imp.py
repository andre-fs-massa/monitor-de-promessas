# Impacto fiscal das promessas de Tarcísio de Freitas (governo de SP, 2022) no orçamento do Estado de São Paulo.
# Base: 2022 (ano anterior ao mandato). Mandato em curso: último ano completo 2025, acumulado 2023-2025.
# Fonte oficial: despesa EMPENHADA por ação no Portal da Transparência do Estado (scripts/orcamento_sp.py ->
# data/interim/orcamento_sp_acoes.csv). O PPA 2024-2027 renumerou e reagrupou muitas ações; quando a ação nova
# não é comparável à de 2022, não há valor a mais.
NI = "; não implementada."
DA = "despesa_aumenta"
PT = "https://www.transparencia.sp.gov.br/Despesas"
REORG = " O PPA 2024-2027 reagrupou as ações orçamentárias e a de 2024 em diante não é comparável à de 2022, por isso não há valor a mais."


def d(txt, cat=DA, conf="media"):
    """Direção sem valor."""
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


SID = "sem_impacto_direto"

I = {
    1: d("Recomposição das aprendizagens: a Prova Paulista e a busca ativa usam a estrutura da Secretaria da Educação; o custo próprio não é separado no orçamento (a ação de avaliação e material didático mistura outras despesas).", SID, "baixa"),
    2: n("Fixar metas de aprendizagem é regra de gestão, sem gasto relevante", SID),
    3: d("A ampliação do Programa Ensino Integral (2.029 escolas em 2022, 2.338 em 2024) aumenta a despesa com professores em jornada integral." + REORG),
    4: n("Ampliar o Profesp aumentaria a despesa"),
    5: (DA, 0.625, 0.967, "2025", 1.276, "2023-2025", "sim", "media",
        "Ensino técnico integrado ao médio na rede estadual (ação 6424, criada em 2024): R$ 916 milhões em 2024 e R$ 967 milhões em 2025, contra R$ 342 milhões do Novotec Integrado (ação 6289) em 2022; em 2023 o Novotec Integrado teve R$ 419 milhões.",
        PT, ""),
    6: n("Atender toda a demanda por creche com as prefeituras aumentaria a despesa"),
    7: n("Contratar atendimento na rede privada aumentaria a despesa"),
    8: n("Criar o centro de controle de doenças aumentaria a despesa"),
    9: (DA, 5.332, 10.091, "2025", 9.138, "2024-2025", "sim", "media",
         "A Tabela SUS Paulista (desde jan/2024) é paga pela ação de serviços contratados e conveniados de saúde (5532) e substituiu o Santas Casas SUStentáveis (ação 6221). Somando as duas: R$ 8,57 bi em 2024 e R$ 10,09 bi em 2025, contra R$ 4,76 bi em 2022, ou R$ 3,8 bi a mais em 2024 e R$ 5,3 bi a mais em 2025. O governo informou R$ 4,3 bi pela Tabela SUS Paulista em 2024 e cerca de R$ 10 bi até jun/2026. A ação também paga outros contratos, que podem ter crescido no período.",
         PT, "https://www.correiodamanha.com.br/colunistas/brasilianas/2026/05/284651-brasilianas-sus-paulista-modelo-que-inspira-o-df-mostra-alto-custo-e-forte-expansao.html"),
    10: d("A Lei 17.745/2023 obriga a publicar a fila; é regra de transparência, sem gasto relevante.", SID),
    11: n("Novo plano de cargos e salários aumentaria a despesa com pessoal"),
    12: n("Novos serviços para idosos aumentariam a despesa"),
    13: (DA, 0.498, 0.502, "2025", 0.967, "2024-2025", "sim", "media",
         "Ação Muralha Paulista (6557, criada em 2024 com o programa do Decreto 68.828/2024): R$ 473 milhões em 2024 e R$ 502 milhões em 2025, contra R$ 4 milhões de videomonitoramento policial (ação 6058) em 2022. Inclui câmeras, leitura de placas e sistemas de dados.",
         PT, "https://www.bnewssaopaulo.com.br/noticias/politica/tce-questiona-contrato-milionario-de-cameras-em-sp-e-abre-fiscalizacao-sobre-programa-muralha-paulista.html"),
    14: d("O aumento do efetivo (9,1 mil agentes até abr/2025) aumenta a despesa com pessoal, mas a folha das polícias também muda com reajustes e aposentadorias, e o custo das novas contratações não é separado no orçamento."),
    15: d("O novo contrato de 12 mil câmeras corporais (2024) substituiu o anterior; a mudança é de regra de uso, sem gasto novo relevante.", "neutro"),
    16: d("Publicar mapas de crimes usa dados que a Secretaria já tem, sem gasto relevante.", SID),
    17: n("Reformular as delegacias de homicídios é reorganização administrativa", SID),
    18: n("Instalar bloqueadores de celular aumentaria a despesa"),
    19: d("A ampliação das tornozeleiras aumenta a despesa com monitoramento eletrônico, mas o contrato não aparece em ação própria do orçamento.", conf="baixa"),
    20: d("As tornozeleiras dos agressores foram cedidas pela Secretaria da Administração Penitenciária e são monitoradas pelo Copom; o custo está dentro do monitoramento eletrônico (promessa 19).", "sem_valor_proprio"),
    21: d("Mais Delegacias da Mulher 24 horas aumentam a despesa com pessoal, que não é separada no orçamento (a ação Delegacia da Mulher 24h tinha só R$ 4 milhões em 2022 e deixou de existir em 2024)."),
    22: d("Os abrigos para mulheres aumentam a despesa, mas não aparecem em ação própria do orçamento.", conf="baixa"),
    23: d("A requalificação do Recomeço aumenta a despesa com acolhimento terapêutico, mas as ações do programa foram reagrupadas em 2024 (política sobre drogas) e não são comparáveis às de 2022.", conf="baixa"),
    24: n("Expandir os centros de acolhimento aumentaria a despesa"),
    25: n("Criar o programa de emprego aumentaria a despesa"),
    26: n("Criar um plano de logística é planejamento, sem gasto relevante", SID),
    27: d("Na PPP das travessias (leilão em nov/2025, contrato em mai/2026), o Estado pagará contraprestação anual de cerca de R$ 400 milhões (desconto de 12,6% sobre R$ 461 milhões) a partir de 2027, no lugar da operação própria, que custou R$ 353 milhões em 2025 (ação 6414). Nada mudou no orçamento até 2025.",
          conf="baixa"),
    28: (DA, None, 1.428, "2023", 1.428, "2023", "nao", "alta",
         "Aporte do Estado na concessão do Rodoanel Norte (Via Appia, contrato de ago/2023): R$ 1,43 bi empenhados em 2023 na ação 2283; em 2024 e 2025 nada, e em 2026 mais R$ 1,46 bi (ano ainda não completo, fora do acumulado). O governo prevê pagar ainda R$ 4,4 bi por reequilíbrio do contrato.",
         PT, "https://www.metropoles.com/sao-paulo/tarcisio-44-bilhoes-rodoanel"),
    29: d("A obra do pedral, em convênio com o DNIT, aumenta a despesa, mas não aparece em ação própria do orçamento depois de 2023 (a ação da Hidrovia Tietê-Paraná teve R$ 99 milhões em 2023).", conf="baixa"),
    30: (DA, 1.361, 2.291, "2025", 3.213, "2023-2025", "nao", "media",
         "Aportes do Estado na PPP da Linha 6-Laranja (ação 2475): R$ 1,31 bi em 2023, R$ 2,40 bi em 2024 e R$ 2,29 bi em 2025, contra R$ 0,93 bi em 2022. As Linhas 17, 2 e 15 são pagas por aumento de capital do Metrô, que em 2024 foi lançado numa ação única (R$ 3,48 bi) e não dá para separar por linha; por isso o valor conta só a Linha 6 e subestima o gasto.",
         PT, "https://abcdoabc.com.br/linha-6-laranja-aporte-37-bi/"),
    31: (DA, 0.145, 0.158, "2025", 0.145, "2025", "nao", "media",
         "Acompanhamento da implantação do Trem Intercidades (ação 2621): R$ 158 milhões em 2025, contra R$ 13 milhões em 2022; o contrato (2024) prevê aporte público de até cerca de R$ 8,9 bi ao longo da obra, com conclusão prevista para 2031.",
         PT, "https://diariodotransporte.com.br/2024/03/01/tic-grupo-comporte-c2-mobilidade-sobre-trilhos-vence-leilao-do-tic-trem-intercidades-entre-sao-paulo-e-campinas-via-jundiai-nesta-quinta-29-desconto-so-de-001/"),
    32: d("Os ônibus intermunicipais são comprados pelas empresas operadoras, fora do orçamento do Estado.", "fora_do_orcamento"),
    33: d("A recuperação de vicinais aumenta a despesa, mas a ação Estradas Vicinais (R$ 2,87 bi em 2022) foi trocada em 2024 por Estradas Municipais (R$ 0,86 bi em 2025) dentro do SP Pra Toda Obra, sem comparação direta."),
    34: d("Adotar o iRAP é regra técnica das concessões, sem gasto relevante.", SID),
    35: d("O wi-fi nas rodovias é pago pelas concessionárias, fora do orçamento do Estado.", "fora_do_orcamento"),
    36: d("O aumento da oferta de moradias com fomento do Estado tem o gasto contado na carta de crédito do Casa Paulista (promessa 38).", "sem_valor_proprio"),
    37: d("O monitoramento por satélite tem custo pequeno frente ao orçamento.", SID),
    38: (DA, None, 0.299, "2025", None, "", "sim", "media",
         "Carta de crédito do Casa Paulista (ação 16822742 da CDHU): R$ 182 milhões em 2024 e R$ 299 milhões em 2025; o subsídio estadual ao crédito habitacional já existia e foi maior em 2022 (R$ 1,03 bi, ação 2486), por isso não há despesa a mais, só o custo total. O governo diz ter investido R$ 1,2 bi em cartas de crédito desde 2023.",
         PT, "https://www.portaltela.com/noticias/economia/2026/06/03/casa-paulista-amplia-acesso-a-moradias-por-meio-de-cartas-de-credito/"),
    39: d("O Polo Administrativo será uma PPP: o Estado pagaria contraprestação depois da obra, mas a concessão só teve a licitação autorizada (Decreto 69.620/2025), sem contrato.", conf="baixa"),
    40: n("Construir moradias no centro aumentaria a despesa"),
    41: n("Enterrar os trilhos na Água Branca aumentaria a despesa"),
    42: d("O IntegraTietê reúne ações já existentes: a ação de revitalização dos rios Tietê e Pinheiros (6562) teve R$ 395 milhões em 2025, contra R$ 343 milhões das ações Novo Rio Pinheiros e manutenção do Tietê em 2022; parte do programa (esgoto) é paga pela Sabesp, fora do orçamento. A diferença é pequena e as ações não são diretamente comparáveis.", conf="baixa"),
    43: d("A universalização do saneamento é feita pela Sabesp, privatizada em jul/2024, fora do orçamento do Estado.", "fora_do_orcamento"),
    44: n("Criar o Código Ambiental é lei, sem gasto relevante", SID),
    45: n("O leilão reverso é regra de logística reversa, paga pelas empresas", SID),
    46: n("Criar o Código de Fauna é lei, sem gasto relevante", SID),
    47: d("Zerar a perda de cobertura florestal depende de fiscalização e monitoramento já existentes; sem gasto novo separado.", SID),
    48: n("Criar o banco genético aumentaria a despesa"),
    49: n("Instalar energia solar aumentaria o investimento (e reduziria a conta de luz depois)"),
    50: d("A política de distritos de inovação (Decreto 70.683/2026) é regra, sem gasto relevante até agora.", SID),
    51: d("A reestruturação do Fundo de Aval (Lei 18.375/2025) mexe num fundo garantidor de empréstimos, que não entra no resultado primário.", "sem_impacto_primario"),
    52: d("A linha de microcrédito do Banco do Povo é empréstimo reembolsável, fora do resultado primário.", "sem_impacto_primario"),
    53: (DA, None, 0.146, "2023", None, "", "sim", "baixa",
         "O Estado paga a formação dos aprendizes (pelo CIEE); o governo anunciou R$ 145,5 milhões para o programa no lançamento (2023). O gasto não aparece em ação própria do orçamento, por isso não há valor por ano.",
         "", "https://jcconcursos.com.br/noticia/brasil/governo-de-sp-oferece-programa-de-jovem-aprendiz-sem-custo-para-empresario-110917"),
    54: d("Tirar mercadorias da substituição tributária muda a forma de cobrar o ICMS (quem recolhe e quando), sem efeito previsto na arrecadação.", SID),
    55: n("O planejamento do uso do solo por satélite teria custo pequeno", SID),
    56: n("Abrir novas Fábricas de Cultura aumentaria a despesa"),
    57: n("Criar centros de esporte olímpico aumentaria a despesa"),
    58: d("Os repasses às estâncias aumentam a despesa, mas o empenhado da ação de apoio aos municípios turísticos caiu de R$ 374 milhões (2022) para R$ 284 milhões (2023), e a ação foi reorganizada em 2024; o recorde de 2023 citado pelo governo (R$ 197 milhões) é de valores pagos, não comparável.", conf="baixa"),
    59: d("O portal único SP.GOV.BR reorganiza canais digitais que já existiam; custo pequeno frente ao orçamento.", SID),
    60: n("Contratar soluções inovadoras é forma de compra, sem gasto novo relevante", SID),
    61: d("Aceitar a assinatura gov.br é regra, sem gasto relevante.", SID),
    62: d("A aprovação tácita é regra, sem gasto relevante.", SID),
    63: d("A Lei de Liberdade Econômica é regra, sem gasto relevante.", SID),
    64: n("Oferecer os sistemas aos municípios teria custo pequeno", SID),
    65: d("Aceitar Pix nos tributos muda o meio de pagamento, sem efeito relevante na arrecadação.", SID),
    66: n("Adotar CPF e CNPJ como identificadores é regra, sem gasto relevante", SID),
    67: d("O plano de integridade é regra de gestão, sem gasto relevante.", SID),
    68: d("O código de ética é regra, sem gasto relevante.", SID),
    69: n("Reduzir o número de secretarias reduziria a despesa", "despesa_reduz"),
    70: d("A reorganização da Controladoria (LC 1.419/2024) criou a carreira de Auditor Estadual, o que aumenta a despesa com pessoal, mas o custo não foi divulgado e a Controladoria não tem ação própria comparável a 2022.", conf="baixa"),
    71: n("Criar a política de segurança cibernética é regra", SID),
    72: n("Criar a gestora de investimentos mexe no patrimônio, não no resultado primário", "sem_impacto_primario"),
    73: n("Criar o núcleo de avaliação teria custo pequeno", SID),
    74: d("Os decretos de fev/2023 renovaram ou criaram benefícios de ICMS até o fim de 2024, o que reduz a receita; a Fazenda não divulgou a renúncia desses decretos separadamente (a LDO 2026 estima R$ 78,7 bi de renúncias de ICMS no total).", "receita_reduz", "baixa"),
    75: n("Reduzir o ICMS sobre veículos reduziria a receita", "receita_reduz"),
    76: n("Reduzir a alíquota do IPVA reduziria a receita", "receita_reduz"),
    77: n("Reduzir as taxas do Detran reduziria a receita", "receita_reduz"),
}

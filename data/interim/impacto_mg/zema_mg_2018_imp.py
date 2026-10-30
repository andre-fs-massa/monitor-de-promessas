# Impacto fiscal das promessas de Romeu Zema (governo de MG, 2018) no orçamento do Estado de Minas Gerais.
# Base: 2018 (ano anterior ao mandato). Mandato completo: 2019-2022.
# Fonte oficial: despesa EMPENHADA por ação, dados abertos da Controladoria-Geral do Estado ("Despesa pública",
# mesma base do Portal da Transparência de MG) — scripts/orcamento_mg.py. O PPAG 2020-2023 renumerou várias ações:
# a ação de 2020 em diante é comparada com a que ela substituiu.
NI = "; não implementada."
DA = "despesa_aumenta"
DR = "despesa_reduz"
SID = "sem_impacto_direto"
FO = "fora_do_orcamento"
SIP = "sem_impacto_primario"
CGE = "https://dados.mg.gov.br/dataset/despesa"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


I = {
    1: (DR, 0.225, None, "2022", 0.9, "2019-2022", "sim", "baixa",
        "Reforma administrativa (Lei 23.304/2019): secretarias de 21 para 12 e corte de cerca de 1.700 cargos em comissão e funções. O governo estimou economia de R$ 235 milhões por ano (R$ 1 bi no mandato) ao apresentar o projeto; na sanção, em mai/2019, a estimativa caiu para cerca de R$ 900 milhões em quatro anos, usada aqui (R$ 225 milhões por ano). É estimativa, não economia medida.",
        "https://www.agenciaminas.mg.gov.br/noticia/governador-romeu-zema-apresenta-reforma-administrativa-que-deve-gerar-economia-de-r-1-bilhao-durante-mandato-105052",
        "https://diariodocomercio.com.br/?p=199008"),
    2: d("A seleção técnica dos cargos de liderança (Transforma Minas) muda a forma de escolha, sem gasto relevante.", SID),
    3: n("Auditorias patrimoniais teriam custo pequeno, feitas pelos órgãos de controle", SID),
    4: n("Exigir seguro nas contratações é regra de licitação, sem gasto direto", SID),
    5: d("O acordo com a AMM (abr/2019) pagou R$ 7 bi de ICMS, IPVA e Fundeb que pertenciam aos municípios e estavam atrasados desde governos anteriores (cerca de R$ 6 bi herdados), quitados em jun/2022. É pagamento de dívida já existente, sem despesa nova no resultado primário, mas pesou no caixa do Estado em 2020–2022.", SIP),
    6: n("Bonificar servidores pela avaliação da população aumentaria a despesa com pessoal"),
    7: d("As concessões do mandato (Aeroporto da Pampulha, Mineirinho, lotes 1 e 2 de rodovias, Rodoanel) transferem os investimentos às concessionárias, fora do orçamento; os leilões de rodovias foram pelo menor pedágio, e a contraprestação do Rodoanel só começa depois da obra.", FO, "baixa"),
    8: (DA, 0.014, 0.017, "2022", 0.013, "2019-2022", "sim", "baixa",
        "Aporte do Estado para a Prevcom-MG (ação 7021): R$ 3,0 milhões em 2018, R$ 2,5 milhões por ano em 2019–2021 e R$ 17,4 milhões em 2022, ano seguinte à abertura da migração dos servidores antigos. No curto prazo a migração custa ao Estado (deixa de receber contribuições ao regime próprio); a economia de longo prazo com aposentadorias menores não foi estimada. A economia da reforma da previdência de 2020 vem de idades e alíquotas e não foi atribuída a esta promessa.",
        CGE, ""),
    9: d("Manter a sede na Cidade Administrativa não cria gasto novo.", SID),
    10: d("Abrir o Palácio da Liberdade à visitação tem custo pequeno, dentro do Circuito Liberdade.", SID),
    11: n("Reduzir o salário do governador teria efeito desprezível no orçamento", SID),
    12: d("Não usar o Palácio das Mangabeiras como moradia reduz pouco o custeio; economia não divulgada.", DR, "baixa"),
    13: d("Não criar tributos nem elevar alíquotas mantém a receita como estava; o adicional de ICMS sobre supérfluos, anterior a 2019, continuou até 2022.", SID),
    14: n("Divulgar os incentivos fiscais é medida de transparência, sem gasto relevante", SID),
    15: n("Aceitar certificações privadas é mudança de regra", SID),
    16: d("A dispensa de alvará e a aprovação tácita (Minas Livre para Crescer) mudam regras, sem gasto relevante.", SID),
    17: d("O registro automático na Jucemg é mudança de procedimento, sem gasto relevante.", SID),
    18: n("Vender participação nas estatais traria receita de capital", "receita_aumenta"),
    19: n("Um cadastro voluntário de bens teria custo pequeno", SID),
    20: n("Monitorar indicadores de inquéritos tem custo pequeno", SID),
    21: n("Trocar parte das prisões por tornozeleiras reduziria o custo do sistema prisional", DR),
    22: (DA, 0.002, 0.002, "2022", 0.002, "2022", "nao", "baixa",
          "Compra de 1.040 câmeras corporais pela PM em 2022, junto com 65 docas e 1.040 pistolas de impulso elétrico: R$ 2,4 milhões no total, segundo a imprensa; não há ação orçamentária própria. Gasto único.",
          "", "https://pradosonline.com.br/?p=51475"),
    23: n("Expandir APACs e PPPs prisionais aumentaria a despesa com vagas"),
    24: n("Integrar os sistemas das polícias exigiria investimento em tecnologia"),
    25: n("Criar um setor de inteligência teria custo pequeno", SID),
    26: n("Cerco eletrônico, drones e GPS exigiriam investimento"),
    27: n("PPPs de escolas gerariam contraprestações anuais do Estado"),
    28: n("Redistribuir recursos entre escolas muda a divisão, não o total", SID),
    29: n("Premiar escolas e profissionais aumentaria a despesa"),
    30: n("Ceder prédios ociosos em troca de bolsas não passa pelo orçamento", SID),
    31: n("Um voucher educacional aumentaria a despesa"),
    32: n("Parcerias com o Sistema S para cursos teriam custo pequeno", SID),
    33: n("Um sistema online para os pais teria custo pequeno", SID),
    34: d("Pagar salários e fornecedores em dia muda o calendário de pagamentos, não o valor da despesa. Os repasses atrasados da saúde aos municípios (R$ 6,7 bi) foram parcelados em 96 vezes a partir de 2022, com R$ 716 milhões pagos em 2022; é pagamento de dívida já existente.", SID),
    35: n("Concluir os hospitais regionais exigiria obras e custeio (as obras só foram retomadas em out/2022: R$ 7,5 milhões em 2022)"),
    36: (DA, 0.304, 0.726, "2022", 0.722, "2019-2022", "sim", "baixa",
          "Rede de urgência e emergência do Fundo Estadual de Saúde, que inclui o SAMU regional: ação 4491 até 2019 e ações 4459 (SAMU regional) e 4461 (rede de urgência) a partir de 2020. R$ 422 milhões em 2018, R$ 680 milhões em 2019, R$ 551 milhões em 2020, R$ 453 milhões em 2021 e R$ 726 milhões em 2022 (R$ 585 milhões só do SAMU). Inclui outros serviços da rede, como UPAs e leitos de retaguarda, por isso a confiança é baixa.",
          CGE, ""),
    37: n("Passar a gestão de unidades a OS ou PPP troca custeio direto por contratos, sem efeito líquido estimado", SID),
    38: (DA, 0.863, 1.333, "2022", 1.4, "2020-2022", "sim", "baixa",
          "Política de Atenção Hospitalar (Valora Minas, desde 2020): módulos Valor em Saúde (4457), Hospitais Plataforma (4453) e Novos Prestadores (4454), que substituíram a ação 4623 (Pro-Hosp). R$ 470 milhões em 2018 (base), R$ 510 milhões em 2020, R$ 966 milhões em 2021 e R$ 1,33 bi em 2022. 2019 (R$ 723 milhões) ficou fora porque a nova política ainda não existia. A promessa era mudar a forma de pagamento; o aumento também reflete mais hospitais e mais recursos.",
          CGE, ""),
    39: n("Prontuário eletrônico e centros de telemedicina exigiriam investimento"),
}

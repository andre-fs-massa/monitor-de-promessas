# Impacto fiscal das promessas de Eduardo Paes (prefeitura do Rio de Janeiro, 2020) no orçamento do Município.
# Base: 2020. Mandato completo: 2021-2024. Os dados abertos da prefeitura (Data.Rio) só vão até 2019, e os portais
# Contas Rio e Rio Transparente recusam conexões feitas de fora do Brasil; como nos governadores do RJ, os valores
# são os divulgados pela prefeitura e pela imprensa (fonte_comparacao), com confiança média ou baixa. Investimento em
# obra é gasto único (recorrente = "nao"); o acumulado é o valor investido no mandato.
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


I = {
    1: (DA, None, 0.2, "2023", 0.2, "2021-2024", "nao", "baixa",
        "A revitalização do eixo da Avenida Brasil teve como principal obra a conclusão do BRT TransBrasil, retomada em ago/2021 e inaugurada em fev/2024. Em 2023 a prefeitura liberou R$ 164 milhões de recursos próprios para cobrir o orçamento da obra, além de R$ 36 milhões destinados no início do ano; o restante foi financiado pela Caixa e pelo BNDES. Os portais de transparência do Rio não puderam ser consultados.",
        "", "https://diariodotransporte.com.br/2023/10/17/eduardo-paes-libera-r-164-milhoes-para-cobrir-orcamento-das-obras-do-corredor-brt-transbrasil/"),
    2: n("Convênios de ética e transparência têm custo pequeno", SID),
    3: d("Pagar os salários em dia muda o calendário de pagamento; quitar o 13º de 2020 em atraso foi pagamento de dívida já existente, sem despesa nova.", SID),
    4: d("O Acordo de Resultados paga bônus de até uma remuneração aos servidores que cumprem as metas; o valor pago de 2021 a 2024 não foi localizado (o ciclo de 2025, pago em 2026, custou mais de R$ 270 milhões).", DA, "baixa"),
    5: n("Ampliar o Cartão Família Carioca aumentaria a despesa"),
    6: n("Abrir restaurantes e farmácias populares aumentaria a despesa"),
    7: d("As frentes de trabalho (Guardiões dos Rios, Garis e Agentes Comunitários) aumentam a despesa com bolsas e contratos; o valor não foi localizado.", DA, "baixa"),
    8: n("Um programa de conscientização teria custo pequeno", SID),
    9: d("O plano de 100 dias organizou ações de gestão (vacinação, volta às aulas, Plano BRT), cujo custo está nas ações gerais de cada área.", SID),
}

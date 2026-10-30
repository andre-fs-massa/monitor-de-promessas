# Impacto fiscal das promessas de Fuad Noman (prefeitura de Belo Horizonte, 2024) no orçamento do Município.
# Base: 2024 (ano anterior ao mandato). Fuad morreu em 26/03/2025 e Álvaro Damião, vice, segue no cargo; o mandato
# (2025-2028) está em curso e o único ano completo é 2025. Fonte oficial: despesa EMPENHADA por ação e subação nos
# dados abertos da PBH ("Despesas Orçamentárias", scripts/orcamento_bh.py).
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
PBH = "https://dados.pbh.gov.br/dataset/despesas-orcamentarias"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


def so(total, txt, conf="media", rec="nao"):
    """Gasto de 2025 abaixo de 2024: só o custo de 2025."""
    return (DA, None, total, "2025", None, "", rec, conf, txt, PBH, "")


def inc(incr, total, txt, rec="sim", conf="media"):
    return (DA, incr, total, "2025", incr, "2025", rec, conf, txt, PBH, "")


I = {
    1: so(0.044, "Obras nas interseções da Avenida Cristiano Machado (subação 1330.011), que pagam os viadutos e a trincheira da Cristo Rei: R$ 116,7 milhões em 2024 e R$ 43,5 milhões em 2025. Gasto único de obra."),
    2: d("A trincheira e o boulevard da Cristo Rei são pagos pela mesma subação das obras da Cristiano Machado; o custo está na promessa 1."),
    3: d("A obra da maternidade do Odilon Behrens não tem ação própria no orçamento; o hospital é pago pela rede hospitalar geral.", DA, "baixa"),
    4: inc(0.046, 0.182, "Contraprestação da PPP de unidades de atenção primária (subação 2902.001), que constrói e mantém os novos centros de saúde: R$ 135,1 milhões em 2024 e R$ 181,5 milhões em 2025."),
    5: d("As obras dos viadutos da BR-040 no Belvedere estão previstas para 2026, sem gasto separado em 2025."),
    6: d("O BRT Amazonas está em estudos e projetos, com custo pequeno; a obra está prevista para 2028-2030."),
    7: so(0.059, "Drenagem e gestão do risco de inundações (ações 1400 e 1203), que pagam o Vilarinho e outras bacias: R$ 174 milhões em 2024 e R$ 59 milhões em 2025. A obra do Vilarinho II parou em 2025 e foi relicitada.", "baixa"),
    8: d("As obras do Anel Rodoviário dependem de R$ 60 milhões da União e de empréstimo de até R$ 1 bi aprovado pela Câmara; sem gasto separado em 2025."),
    9: d("O Centro de Todo Mundo não tem ação própria no orçamento; as obras em praças e vias estão em ações gerais de infraestrutura.", DA, "baixa"),
    10: d("Elaborar os planos das centralidades tem custo pequeno.", SID),
    11: d("A licitação do Parque Ciliar do Onça (R$ 110 milhões) foi suspensa; sem obra principal em 2025."),
    12: d("O Parque Taiobeiras está em projeto, sem obra."),
    13: d("O plantio dos corredores verdes está somado na arborização (promessa 18)."),
    14: d("A área do parque do Jardim América foi desapropriada em 2024; a implantação ainda não começou."),
    15: n("Ampliar o Parque Tom Jobim exigiria obra"),
    16: d("As miniflorestas são plantadas com a arborização (promessa 18), com custo pequeno."),
    17: d("Os primeiros refúgios climáticos têm custo pequeno, sem ação própria.", DA, "baixa"),
    18: so(0.037, "Preservação da arborização municipal (subação 2811.001): R$ 38,2 milhões em 2024 e R$ 36,9 milhões em 2025; as 50 mil árvores de 2025 não aumentaram o gasto dessa ação.", "media", "sim"),
    19: inc(0.001, 0.004, "Atendimento médico-veterinário (subação 2877.009): R$ 2,8 milhões em 2024 e R$ 3,7 milhões em 2025. O Centro Avançado de Saúde Animal abriu em set/2026."),
    20: inc(0.006, 0.013, "Bolsa Moradia e Locação Social (ação 2792), que paga o aluguel social do Viver de Novo: R$ 7,9 milhões em 2024 e R$ 13,4 milhões em 2025. A ação também atende famílias de áreas de risco.", "sim", "baixa"),
    21: d("As duas novas equipes do Consultório na Rua são pagas pela atenção primária geral, sem valor separado.", DA, "baixa"),
    22: d("Reservar vagas em contratos para pessoas em situação de rua é regra de contratação (projeto de lei).", SID),
    23: d("O novo contrato do prontuário eletrônico (dez/2025) não tem ação própria no orçamento.", DA, "baixa"),
    24: n("Um aplicativo de saúde teria custo pequeno", SID),
    25: n("Entregar 12 novas escolas exigiria obra (só 3 foram entregues)"),
    26: n("Abrir vagas integrais na educação infantil aumentaria a despesa"),
    27: n("Abrir mil vagas em creches conveniadas aumentaria a despesa (o gasto com as creches parceiras subiu de R$ 398 milhões em 2024 para R$ 471 milhões em 2025, mas a ampliação de vagas não foi localizada)"),
}

# Impacto fiscal das promessas de Romeu Zema (governo de MG, 2022) no orçamento do Estado de Minas Gerais.
# Base: 2022 (ano anterior ao mandato). Renunciou em 22/03/2026: anos completos 2023-2025.
# Fonte oficial: despesa EMPENHADA por ação, dados abertos da Controladoria-Geral do Estado ("Despesa pública",
# mesma base do Portal da Transparência de MG) — scripts/orcamento_mg.py. O PPAG 2024-2027 renumerou várias ações:
# a ação de 2024 em diante é somada à que ela substituiu.
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
FO = "fora_do_orcamento"
SIP = "sem_impacto_primario"
CGE = "https://dados.mg.gov.br/dataset/despesa"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


I = {
    1: (DA, 0.283, 0.289, "2025", 0.643, "2023-2025", "nao", "media",
        "Implantação dos hospitais regionais (ação 1085, paga com recursos do acordo de reparação da Vale, e ação 1020 a partir de 2024): R$ 6,5 milhões em 2022, R$ 275 milhões em 2023, R$ 98 milhões em 2024 e R$ 289 milhões em 2025. O custeio dos hospitais depois de abertos não está somado. Gasto único de obra.",
        CGE, ""),
    2: (DA, 0.052, 0.25, "2025", 0.46, "2023-2025", "sim", "baixa",
        "Módulo de cirurgias eletivas da política hospitalar (Valora Minas / Opera Mais, ação 4454, chamada Acesso Eletivo, ação 4135, a partir de 2024): R$ 198 milhões em 2022, R$ 385 milhões em 2023, R$ 419 milhões em 2024 e R$ 250 milhões em 2025. Em 2022 a ação tinha outro nome (novos prestadores da política hospitalar), por isso a comparação é aproximada.",
        CGE, ""),
    3: d("Os blocos regionais de saneamento são regra (Lei 25.668/2025) para atrair investimento privado, sem gasto próprio relevante do Estado.", SID),
    4: d("A base integrada de segurança fica no data lake do Estado, com custo pequeno frente ao orçamento.", SID),
    5: n("Ampliar o Plantão Digital teria custo pequeno (a ação própria teve R$ 0,7 milhão em 2022 e quase nada depois)"),
    6: (DA, None, 0.574, "2025", None, "", "sim", "media",
         "Trilhas de Futuro (ação 4203 até 2023; ações 2118, estudantes, e 2099, educadores, a partir de 2024): R$ 683 milhões em 2022, R$ 711 milhões em 2023, R$ 601 milhões em 2024 e R$ 574 milhões em 2025. Mesmo com mais vagas, o gasto ficou abaixo de 2022 em 2024 e 2025, por isso só o custo de 2025.",
         CGE, ""),
    7: (DA, None, 0.006, "2025", None, "", "sim", "media",
         "Projeto Somar (ação 2040 até 2023 e 2105 depois): R$ 12 milhões em 2022, R$ 10 milhões em 2023, R$ 13 milhões em 2024 e R$ 6 milhões em 2025. A expansão foi suspensa e o gasto ficou abaixo de 2022, por isso só o custo de 2025.",
         CGE, ""),
    8: (DA, 0.016, 0.097, "2025", 0.067, "2023-2025", "sim", "baixa",
         "Ensino médio integral da Secretaria da Educação (ação 4314 até 2023 e 2093 depois) e da Fundação Helena Antipoff (EMTI): R$ 81 milhões em 2022, R$ 105 milhões em 2023, R$ 107 milhões em 2024 e R$ 97 milhões em 2025. Subestima o custo, porque o salário dos professores das novas escolas integrais fica nas ações gerais de pessoal; a ação nova de educação integral de 2025 (R$ 146 milhões) mistura fundamental e médio e não foi somada.",
         CGE, ""),
    9: d("As concessões e PPPs de rodovias, aeroportos e travessias transferem o investimento para as concessionárias, fora do orçamento do Estado; os leilões de rodovias de MG são pelo menor pedágio, sem outorga relevante.", FO, "baixa"),
    10: d("As leis setoriais de biogás, energia rural e hidrogênio verde são regras e programas de fomento, sem gasto ou renúncia separados no orçamento.", SID, "baixa"),
    11: n("Licenciar automaticamente é mudança de regra, sem gasto relevante", SID),
    12: (DA, 0.016, 0.028, "2025", 0.061, "2023-2025", "sim", "media",
          "Regularização fundiária: Minas Reurb (ações 1020 e 1082, mais a da Região Metropolitana do Vale do Aço) e regularização de imóveis rurais e territórios coletivos (ações 4342, 4343 e 4363): R$ 12 milhões em 2022, R$ 47 milhões em 2023, R$ 22 milhões em 2024 e R$ 28 milhões em 2025.",
          CGE, ""),
    13: d("A venda das ações da Copasa, autorizada pela Lei 25.664/2025, só foi concluída em jun/2026, depois da renúncia; não houve receita de privatização no período do mandato.", "receita_aumenta", "media"),
    14: n("Um fundo de microcrédito empresta recursos que voltam ao Estado, sem efeito no resultado primário", SIP),
    15: n("Regulamentar a rastreabilidade é regra, sem gasto relevante", SID),
    16: d("O novo Regulamento do ICMS consolida regras, sem efeito direto separado na receita.", SID),
    17: n("Uma Lei de Responsabilidade Fiscal mineira é regra fiscal, sem efeito direto", SID),
    18: d("Cargos em comissão vagos não geram despesa; extingui-los não muda o gasto.", SID),
    19: (DA, 2.5, 2.5, "2025", 5.0, "2024-2025", "sim", "media",
          "Revisão geral de 4,62% dos salários em 2024 (Lei 24.838/2024, inflação de 2023), retroativa a janeiro: o governo estimou impacto de cerca de R$ 2,5 bi por ano na folha do Executivo (ativos, inativos e pensionistas). Não houve revisão em 2023 nem em 2025, por isso conta 2024 e 2025.",
          "https://www.agenciaminas.mg.gov.br/noticia/governo-de-minas-sanciona-nesta-quinta-feira-27-6-reajuste-salarial-de-4-62-para-os-servidores-publicos/", ""),
    20: d("A concessão dos parques do Ibitipoca e do Itacolomi transfere o custeio e os investimentos para a concessionária e gera outorga, mas os valores são pequenos frente ao orçamento e não foram separados.", "receita_aumenta", "baixa"),
    21: n("Prover internet, equipamentos e cursos aumentaria a despesa"),
    22: (DA, 0.032, 0.032, "2025", 0.044, "2023-2025", "sim", "media",
          "Reformas e melhorias de casas do Moradas Gerais (ação 4103 em 2023 e 4388 em 2025): sem gasto em 2022, R$ 13 milhões em 2023 e R$ 32 milhões em 2025.",
          CGE, ""),
    23: (DA, 0.01, 0.012, "2025", 0.04, "2023-2025", "sim", "baixa",
          "Qualificação profissional da Secretaria de Desenvolvimento Social (ação 1012 até 2023 e 4158 depois), que paga o Minas Forma: R$ 2 milhões em 2022, R$ 20 milhões em 2023, R$ 15 milhões em 2024 e R$ 12 milhões em 2025. A bolsa-auxílio pode estar em outras ações.",
          CGE, ""),
}

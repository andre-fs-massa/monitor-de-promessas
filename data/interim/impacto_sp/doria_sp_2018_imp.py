# Impacto fiscal das promessas de João Doria (governo de SP, 2018) no orçamento do Estado de São Paulo.
# Base: 2018 (ano anterior ao mandato). Renunciou em 31/03/2022: anos completos 2019-2021.
# Fonte oficial: despesa EMPENHADA por ação — Portal da Transparência de SP para 2020-2021 e SIGEO (Secretaria da
# Fazenda) para 2018-2019 (scripts/orcamento_sp.py baixar | sigeo).
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
PT = "https://www.transparencia.sp.gov.br/Despesas"
SIGEO = "https://www.fazenda.sp.gov.br/SigeoLei131/Paginas/FlexConsDespesa.aspx"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


I = {
    1: (DA, 0.019, 0.019, "2021", 0.019, "2021", "sim", "media",
        "Atendimento médico virtual / telemedicina (ação 2603, criada em 2021 com o Multissaúde): R$ 19 milhões em 2021; não havia gasto em 2018.",
        PT, ""),
    2: n("Criar o cartão digital aumentaria a despesa (custo pequeno)"),
    3: n("Integrar os sistemas das polícias aumentaria a despesa"),
    4: ("receita_aumenta", None, 1.1, "2020", 1.1, "2020", "nao", "media",
        "Dentro da desestatização, a concessão do Lote Piracicaba–Panorama (rodovias, contrato de mai/2020) rendeu outorga de R$ 1,1 bi, receita única. A extinção de estatais (Codasp, CPOS, Emplasa) reduz a despesa, mas a economia não foi medida; a outorga das Linhas 8 e 9 está na promessa 14.",
        "", "https://monitormercantil.com.br/maior-concessao-rodoviaria-chega-a-r-1-1-bilhao/"),
    5: (DA, 0.686, 0.838, "2021", 0.497, "2019-2021", "nao", "baixa",
        "O Creche Escola é pago pela ação de cooperação com municípios para construções escolares (5810): R$ 152 milhões em 2018, R$ 107 milhões em 2019, R$ 7 milhões em 2020 e R$ 838 milhões em 2021. A ação também paga outras obras escolares municipais, não só creches.",
        SIGEO, ""),
    6: (DA, 0.247, 1.009, "2021", 0.256, "2019-2021", "sim", "baixa",
        "Implementação da educação integral (ação 6136): R$ 762 milhões em 2018, R$ 786 milhões em 2019, R$ 746 milhões em 2020 e R$ 1,01 bi em 2021. Subestima o custo da expansão (364 para mais de 2 mil escolas), porque a maior parte do salário dos professores está nas ações gerais de pessoal.",
        SIGEO, ""),
    7: n("Garantir a alfabetização com programa novo aumentaria a despesa"),
    8: d("A versão estadual do Corujão da Saúde (mutirão de exames com hospitais privados) aumenta a despesa, mas o gasto não aparece em ação própria do orçamento.", conf="baixa"),
    9: d("Os novos AMEs aumentam a despesa (obra e custeio), mas o gasto não aparece em ação própria do orçamento.", conf="baixa"),
    10: d("Houve nomeações, mas o efetivo das polícias caiu; o custo das contratações não é separado no orçamento."),
    11: d("As novas unidades prisionais aumentam a despesa com obra e custeio, mas as obras estão em ações gerais de construção da Secretaria da Administração Penitenciária, sem separação por unidade.", conf="baixa"),
    12: (DA, 0.61, 1.035, "2021", 0.554, "2019-2021", "sim", "media",
         "Produção de moradias da CDHU (ação 16822006), subsídio do Casa Paulista ao crédito imobiliário (2486), fomento ao crédito habitacional (2276) e PPP habitacional (2492): R$ 425 milhões em 2018, R$ 366 milhões em 2019, R$ 429 milhões em 2020 e R$ 1,04 bi em 2021.",
         SIGEO, ""),
    13: n("Criar a força-tarefa de titulação aumentaria a despesa (custo pequeno)"),
    14: ("receita_aumenta", None, 0.98, "2021", 0.98, "2021", "nao", "media",
         "Concessão das Linhas 8 e 9 da CPTM (leilão em abr/2021): outorga de R$ 980 milhões, receita única. A retomada da PPP da Linha 6 está na promessa 17.",
         "", "https://www.poder360.com.br/economia/cptm-arrecada-r-980-milhoes-em-leilao-de-concessao-das-linhas-8-e-9-em-sp/"),
    15: n("Criar a articulação metropolitana é coordenação, sem gasto relevante", SID),
    16: d("A regulação foi delegada à Artesp, agência que já existia, sem gasto novo relevante.", SID),
    17: (DA, 0.606, 0.726, "2021", 0.974, "2019-2021", "nao", "media",
         "Obras do metrô: aportes na PPP da Linha 6 (ação 2475: R$ 1 milhão em 2018, R$ 297 milhões em 2021) e obras da Linha 17 (ação 16952282: R$ 119 milhões em 2018, R$ 167 milhões em 2019, R$ 422 milhões em 2020 e R$ 429 milhões em 2021). Outras linhas (Linhas 5, 15 e 4) estão em ações do Metrô que não foram somadas, o que subestima o gasto.",
         SIGEO, ""),
    18: (DA, None, 0.113, "2019", 0.205, "2019-2020", "nao", "media",
         "Implantação do sistema integrado da Baixada Santista (VLT, ação 16931469): R$ 113 milhões em 2019 e R$ 92 milhões em 2020; não houve empenho em 2018 nem em 2021. A operação do trecho já existente (PPP, ação 2484) não entra, porque é anterior ao mandato.",
         SIGEO, ""),
    19: d("O Trem Intercidades ficou em projeto e consulta pública até a renúncia, sem gasto relevante.", conf="media"),
    20: n("Fazer um plano de trens regionais é planejamento, sem gasto relevante", SID),
    21: d("O BRT-ABC é construído pela concessionária do Corredor ABD em troca da prorrogação da concessão, fora do orçamento do Estado.", "fora_do_orcamento"),
    22: (DA, None, 0.166, "2021", None, "", "sim", "media",
         "Ações Novo Rio Pinheiros (2355) e preservação do Rio Tietê (6157): R$ 116 milhões em 2018, R$ 87 milhões em 2019, R$ 47 milhões em 2020 e R$ 166 milhões em 2021; no mandato o gasto ficou abaixo do de 2018, por isso só o custo total. A maior parte do Novo Rio Pinheiros (coleta de esgoto) foi paga pela Sabesp, fora do orçamento.",
         SIGEO, ""),
    23: n("Implantar o Hidroanel aumentaria a despesa"),
    24: n("Implantar transporte nos rios aumentaria a despesa"),
    25: n("Atualizar o mapeamento cultural teria custo pequeno", SID),
    26: n("Criar o Cidades Criativas aumentaria a despesa"),
    27: d("A digitalização da Junta Comercial tem custo pequeno frente ao orçamento.", SID),
    28: n("Combater a guerra fiscal aumentaria a receita do ICMS", "receita_aumenta"),
    29: ("despesa_reduz", 3.2, None, "2021", 6.4, "2020-2021", "sim", "baixa",
         "Reforma da previdência estadual (EC 49/2020 e LC 1.354/2020): o governo estimou economia de R$ 32 bi em dez anos, cerca de R$ 3,2 bi por ano, com idades mínimas maiores e alíquotas de contribuição mais altas. É estimativa, não economia medida; contada em 2020 e 2021.",
         "", "https://www.moneytimes.com.br/sao-paulo-aprova-reforma-da-previdencia-estadual/"),
}

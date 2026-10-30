# Impacto fiscal das promessas de Eduardo Paes (prefeitura do Rio de Janeiro, 2024) no orçamento do Município.
# Base: 2024. Mandato em curso (2025-2028). Os dados abertos da prefeitura (Data.Rio) só vão até 2019, e os portais
# Contas Rio e Rio Transparente recusam conexões feitas de fora do Brasil; como nos governadores do RJ, os valores
# são os divulgados pela prefeitura e pela imprensa (fonte_comparacao), com confiança média ou baixa. Investimento em
# obra é gasto único (recorrente = "nao"); o acumulado é o valor investido no mandato até agora.
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
FO = "fora_do_orcamento"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


I = {
    1: d("O programa Educação para Cidadania veio de lei de vereador e tem custo pequeno.", SID),
    2: (DA, None, 0.061, "2026", 0.061, "2025-2026", "nao", "media",
        "O Super Centro Carioca de Saúde da Zona Oeste, inaugurado em mar/2026, custou cerca de R$ 61 milhões, incluindo a compra do imóvel; R$ 50 milhões vieram de economia do orçamento da Câmara Municipal repassada à prefeitura. O da Zona Norte (Câmara destinou R$ 75 milhões) ainda está em obra. Gasto único; o custeio da unidade não está somado.",
        "", "https://diariodorio.com/prefeitura-abre-super-centro-carioca-de-saude-da-zona-oeste-com-foco-em-obesidade-e-reabilitacao/"),
    3: d("Os novos centros de referência em autismo aumentam a despesa; o valor não foi localizado.", DA, "baixa"),
    4: d("Ampliar o tempo integral aumenta a despesa com professores e escolas; o valor não foi localizado.", DA, "baixa"),
    5: d("As 2.065 vagas de creche criadas em 2025 aumentam a despesa; o valor não foi localizado.", DA, "baixa"),
    6: d("Os novos Ginásios Educacionais Tecnológicos aumentam a despesa; o valor não foi localizado.", DA, "baixa"),
    7: d("As aulas de programação são dadas na rede, com custo pequeno separado.", DA, "baixa"),
    8: d("Os novos agentes de apoio à educação especial aumentam a folha da educação; o valor não foi localizado.", DA, "baixa"),
    9: n("Climatizar todas as salas aumentaria a despesa"),
    10: n("Trocar o BRT por VLT ou VLP seria feito por concessão, com aportes da prefeitura"),
    11: d("As novas integrações tarifárias com a bilhetagem Jaé tendem a aumentar o subsídio ao transporte; o valor não foi separado.", DA, "baixa"),
    12: d("A faixa azul para motos é sinalização, com custo pequeno.", SID),
    13: d("A PPP de 175 ônibus elétricos (R$ 509 milhões) só começa a operar em 2027.", DA, "baixa"),
    14: d("A plataforma Oportunidades Cariocas reúne cursos já existentes, com custo pequeno.", SID),
    15: n("Um programa de formalização com auxílio financeiro aumentaria a despesa"),
    16: d("O programa de novas rotas aéreas (Decreto 57.057/2025) é pago pelo Fundo Municipal de Turismo, que já existia; o valor repassado às companhias não foi localizado.", DA, "baixa"),
    17: d("A redução do ISS do mercado de capitais de 5% para 2% reduz a receita, mas a bolsa ainda não opera, por isso ainda não há perda de arrecadação.", "receita_reduz", "baixa"),
    18: n("Ampliar as rondas da Guarda aumentaria a despesa"),
    19: n("Expandir o BRT Seguro aumentaria a despesa"),
    20: (DA, 0.038, 0.216, "2026", 0.038, "2025", "sim", "media",
         "Força Municipal, divisão armada da Guarda (LC 282/2025): a prefeitura estimou o impacto orçamentário em R$ 38,2 milhões em 2025, R$ 215,7 milhões em 2026 e R$ 463,2 milhões em 2027, com a formação de novos agentes. É estimativa do governo, não gasto medido.",
         "", "https://monitormercantil.com.br/camara-do-rio-aprova-projeto-que-cria-forca-de-seguranca-armada/"),
    21: (DA, None, 0.18, "2026", None, "", "sim", "baixa",
         "O orçamento da central de inteligência Civitas subiu de R$ 16 milhões para cerca de R$ 180 milhões por ano, pago por aditivo à PPP de iluminação Smart Luz, com a nova sede inaugurada em jan/2026; a expansão para 20 mil câmeras até 2028 está estimada em R$ 600 milhões. Não há valor de 2025 separado.",
         "", "https://governodigital.prefeitura.rio/noticia/prefeitura-inaugura-nova-sede-da-civitas-e-triplica-capacidade-operacional-da-central-de-inteligencia-com-orcamento-anual-de-r-180-milhoes/"),
    22: d("Atrair investimento privado por concessões e PPPs passa o investimento às concessionárias.", FO),
    23: d("O atendimento por WhatsApp tem custo pequeno.", SID),
    24: d("Conquistar o selo de transparência é medida de gestão.", SID),
    25: (DA, None, 0.43, "2026", None, "", "nao", "media",
         "As obras de controle de enchentes do Rio Acari começaram em set/2026, com investimento previsto de R$ 430 milhões (obras e manutenção), financiado em grande parte por empréstimo da Caixa com garantia da União (R$ 350 milhões). Em 2025 houve só a dragagem, de R$ 9 milhões a R$ 14 milhões, sem valor separado.",
         "", "https://tribunadosertao.com.br/rj-em-foco/2026/09/12/977798-prefeitura-inicia-obras-contra-enchentes-no-rio-acari-projeto-de-r-430-milhoes-preve-beneficiar-80-mil-pessoas"),
    26: n("Reassentar ribeirinhos aumentaria a despesa"),
    27: n("Ampliar as sirenes aumentaria a despesa"),
    28: d("As obras do Jardim Maravilha (R$ 340 milhões) são do Novo PAC, pagas sobretudo pela União, e começaram em jun/2026.", FO, "baixa"),
    29: d("O Planta+Rio (90 mil mudas até 2028) tem custo pequeno; o valor não foi localizado.", DA, "baixa"),
    30: (DA, 0.077, 0.077, "2026", None, "", "sim", "baixa",
         "Cartão Primeira Infância Carioca (out/2025): R$ 200 por mês para mais de 32 mil famílias em set/2026, ou cerca de R$ 77 milhões por ano (cálculo a partir dos números divulgados pela prefeitura); em 2025 foram só três meses.",
         "", "https://www.correiodamanha.com.br/rio-de-janeiro/2026/09/321937-cartao-da-primeira-infancia-carioca-amplia-beneficio-para-mais-de-32-mil-familias.html"),
    31: d("As novas cozinhas comunitárias do Prato Feito Carioca aumentam a despesa; o valor não foi localizado.", DA, "baixa"),
    32: d("O acolhimento da população de rua é pago pelas ações gerais de assistência social; o valor não foi separado.", DA, "baixa"),
    33: d("As novas frentes do Morar Carioca e do Bairro Maravilha aumentam o investimento; o valor não foi localizado.", DA, "baixa"),
    34: d("O Casa Carioca teve crédito suplementar em set/2026; o valor gasto não foi localizado.", DA, "baixa"),
    35: d("O HUB Favela Empreendedora apoia projetos por chamamento, com custo pequeno.", SID),
    36: d("A capacitação para o empreendedorismo feminino tem custo pequeno.", SID),
    37: n("Incluir mais famílias no Cartão Carioca aumentaria a despesa"),
    38: n("Ampliar a Ronda Maria da Penha aumentaria a despesa"),
    39: n("Capacitar pessoas com deficiência aumentaria a despesa"),
    40: n("Transporte para pessoas com deficiência aumentaria a despesa"),
    41: d("A formação de jovens no Pacto pela Juventude tem custo pequeno; o valor não foi localizado.", DA, "baixa"),
    42: d("Os Espaços e Casas da Juventude aumentam a despesa; o valor não foi localizado.", DA, "baixa"),
    43: n("Atender jovens no Rio Vestibular aumentaria a despesa"),
    44: n("Ampliar o Jaé Cultural aumentaria a despesa"),
    45: n("Expandir o Oficina Cultural Carioca aumentaria a despesa"),
    46: d("O Museu Olímpico funciona no Velódromo, já existente; o valor das obras do Parque do Legado não foi localizado.", DA, "baixa"),
    47: (DA, None, 0.22, "2026", 0.22, "2025-2026", "nao", "baixa",
         "O complexo do Parque Oeste Ana Gonzaga, com a Vila Olímpica, recebeu investimento total de R$ 220 milhões, com obras concluídas em out/2026; inclui o parque, não só a vila. Os valores das vilas de Rio das Pedras e Sepetiba, em obra, não foram localizados.",
         "", "https://www.correiodamanha.com.br/rio-de-janeiro/2026/10/326462-prefeitura-conclui-obras-do-parque-oeste-ana-gonzaga-em-inhoaiba.html"),
    48: d("Apoiar três atletas a mais no Time Rio tem custo pequeno.", SID),
}

# Impacto fiscal das promessas de Marcelo Crivella (prefeitura do Rio de Janeiro, 2016) no orçamento do Município.
# Base: 2016 (ano anterior ao mandato). Mandato completo 2017-2020, mas os dados abertos da prefeitura (Data.Rio,
# "Execução Orçamentária Despesas", scripts/orcamento_rio.py) só têm 2017 e 2018 completos: 2019 está incompleto
# (última atualização em out/2019) e 2020 não existe, e os portais Contas Rio e Rio Transparente recusam conexões
# de fora do Brasil. O acumulado cobre só 2017-2018. A reforma administrativa de 2018 renumerou muitas ações.
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
FO = "fora_do_orcamento"
RIO = "https://www.data.rio/datasets/PCRJ::execução-orçamentária-despesas"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


def so(total, txt, conf="media"):
    return (DA, None, total, "2018", None, "", "sim", conf, txt, RIO, "")


I = {
    1: d("O Zona Franca Social dá preferência nas compras da prefeitura a pequenos fornecedores das áreas pobres; não criou benefício tributário, sem efeito separado no orçamento.", SID),
    2: d("O Cimento Social municipal (obras emergenciais e coordenadoria criada em 2019) não tem ação própria identificada no orçamento de 2017 e 2018.", DA, "baixa"),
    3: n("Aumentar em R$ 250 milhões por ano os recursos da Saúde e reestruturar a gestão das 14 UPAs e 8 hospitais de emergência aumentaria a despesa"),
    4: n("Criar o programa Clínica de Especialistas, com 20 unidades até 2020 aumentaria a despesa"),
    5: n("Contratar mais ginecologistas e pediatras para as Clínicas da Família aumentaria a despesa"),
    6: n("Implantar CERs junto aos hospitais Rocha Faria, Salgado Filho e Albert Schweitzer até 2017 aumentaria a despesa"),
    7: n("Assumir a gestão das 16 UPAs estaduais no município até 2018 aumentaria a despesa"),
    8: n("Fazer mutirão para zerar filas de cirurgias com risco de vida e aumentar em 20% os leitos dos hospitais municipais até 2018 aumentaria a despesa"),
    9: n("Criar plano de cargos e salários por mérito para os servidores da saúde até 2017 aumentaria a despesa"),
    10: d("Auditar as Organizações Sociais é medida de controle, com custo pequeno.", SID),
    11: so(0.056, "Cegonha Carioca (atividade 2011): R$ 67 milhões em 2016, R$ 58 milhões em 2017 e R$ 56 milhões em 2018; como ficou abaixo de 2016, só o custo de 2018."),
    12: n("Criar maternidade junto ao Hospital Nossa Senhora do Loreto (Ilha do Governador) até 2018 aumentaria a despesa"),
    13: n("Criar 20 mil vagas em creches e 40 mil em pré-escolas até 2020, por PPP aumentaria a despesa"),
    14: (DA, 0.008, 0.008, "2018", 0.008, "2017-2018", "nao", "baixa", "Construção de escolas em tempo integral (projeto 1111): sem gasto em 2016 e 2017 e R$ 8 milhões em 2018. O turno único em escolas existentes é pago pelas ações gerais de pessoal, sem valor separado, por isso subestima o custo.", RIO, ""),
    15: d("A reformulação da Escola de Formação do Professor Carioca usa a estrutura da Secretaria de Educação, sem ação própria separada.", DA, "baixa"),
    16: n("Aumentar em 20% o orçamento de custeio das escolas até 2020 aumentaria a despesa"),
    17: n("Interromper a construção de escolas de ensino fundamental reduziria o investimento", "despesa_reduz"),
    18: d("Os agentes de apoio à educação convocados entram na folha geral da educação, sem valor separado.", DA, "baixa"),
    19: n("Fazer parcerias com o terceiro setor para atividades complementares nos anos finais do ensino fundamental aumentaria a despesa"),
    20: n("Criar em 2017 programa de incentivo à participação dos pais na escola, ampliando o Vale Cultura aumentaria a despesa"),
    21: n("Pôr ao menos 80% da Guarda Municipal em policiamento comunitário e vigilância até 2018 é regra ou parceria, sem gasto próprio relevante", SID),
    22: d("O treinamento de 186 guardas em armas não letais tem custo pequeno.", SID),
    23: n("Ampliar em ao menos 20% as câmeras de vigilância até 2020 aumentaria a despesa"),
    24: n("Recuperar as 10 Unidades de Ordem Pública (UOPs) existentes até 2018 aumentaria a despesa"),
    25: n("Criar 10 novas UOPs nas Zonas Norte e Oeste até 2020 aumentaria a despesa"),
    26: n("Ter ao menos um guarda municipal em cada escola municipal até 2017 aumentaria a despesa"),
    27: n("Criar até 2018 política municipal de incentivos às polícias do estado por metas de segurança por AISP é regra ou parceria, sem gasto próprio relevante", SID),
    28: d("A PPP da iluminação pública só foi assinada em abr/2020 e foi suspensa pela Justiça, depois do período com dados (2017-2018).", DA, "baixa"),
    29: (DA, 0.026, 0.041, "2018", 0.02, "2017-2018", "sim", "baixa", "Urbanização e conservação de praças e áreas ajardinadas e manejo da arborização (3015, 4010 e 4042): R$ 15 milhões em 2016, R$ 9 milhões em 2017 e R$ 41 milhões em 2018.", RIO, ""),
    30: n("Firmar no primeiro ano parceria com o Ministério Público e o Conselho Tutelar contra a exploração de crianças nas ruas é regra ou parceria, sem gasto próprio relevante", SID),
    31: n("Concluir o BRT TransBrasil e pô-lo em operação até 2017 aumentaria a despesa"),
    32: d("A frota do BRT é das concessionárias; exigir mais ônibus não passa pelo orçamento.", FO),
    33: d("Suspender a racionalização das linhas é regra de operação do sistema.", SID),
    34: n("Ampliar o Bilhete Único Carioca aumentaria o subsídio às empresas de transporte"),
    35: n("Licitar o serviço de vans na Zona Oeste ao final de 2017 (um CPF, uma van) é regra ou parceria, sem gasto próprio relevante", SID),
    36: d("O laudo do CREA-RJ foi cooperação técnica, e os reparos da ciclovia foram cobrados do consórcio construtor.", SID),
    37: n("Estacionamentos por PPP teriam o investimento feito pela concessionária", FO),
    38: n("Cobrar o ISS da Uber no Rio aumentaria a receita", "receita_aumenta"),
    39: d("Menos radares reduz a receita de multas; o valor não foi separado.", "receita_reduz", "baixa"),
    40: d("A fusão de secretarias (2018) reduziu cargos, mas o gasto com pessoal subiu de R$ 11,6 bi em 2016 para R$ 12,2 bi em 2019; a economia da fusão não foi medida.", "despesa_reduz", "baixa"),
    41: n("Criar o programa Oficina para o Emprego, com 20 centros e 40 mil vagas até 2019 aumentaria a despesa"),
    42: n("Garantir por lei 1% do orçamento municipal para a cultura já no primeiro ano e reestruturar o Vale Cultura aumentaria a despesa"),
    43: n("A concessão da água e do esgoto da AP 4 seria feita com a Cedae, fora do orçamento municipal", FO),
    44: n("Criar até 2019 um parque entre Bangu e Campo Grande no padrão do Parque de Madureira aumentaria a despesa"),
    45: n("Resolver com Comlurb e Cedae o saneamento, a água e a limpeza das 20 principais comunidades até 2019 é regra ou parceria, sem gasto próprio relevante", SID),
    46: n("Aprovar nova legislação urbanística para a AP 4 (Vargens e Jacarepaguá) com contrapartidas maiores dos empreendedores é regra ou parceria, sem gasto próprio relevante", SID),
    47: n("Ampliar o Acordo de Resultados para premiar os 1.000 servidores com melhor desempenho e conter a descapitalização da previdência aumentaria a despesa"),
    48: n("Criar 4.000 vagas de acolhimento para a população de rua até 2019 aumentaria a despesa"),
}

# Impacto fiscal das promessas de João Doria (prefeitura de São Paulo, 2016) no orçamento do Município de São Paulo.
# Base: 2016 (ano anterior ao mandato). Renunciou em 06/04/2018: único ano completo é 2017.
# Fonte oficial: despesa EMPENHADA (líquida) por projeto/atividade nos dados abertos da Prefeitura
# ("Execução orçamentária", scripts/orcamento_spcapital.py).
NI = "; não implementada."
DA = "despesa_aumenta"
SID = "sem_impacto_direto"
FO = "fora_do_orcamento"
PMSP = "https://dados.prefeitura.sp.gov.br/dataset/execucao-orcamentaria"


def d(txt, cat=DA, conf="media"):
    return (cat, None, None, "", None, "", "", conf, txt, "", "")


def n(oque, cat=DA):
    return d(oque + NI, cat)


def so(total, txt, conf="media"):
    """Gasto de 2017 abaixo de 2016: só o custo de 2017."""
    return (DA, None, total, "2017", None, "", "sim", conf, txt, PMSP, "")


I = {
    1: n("Implantar o prontuário eletrônico integrando todas as unidades de saúde, inclusive as de OS aumentaria a despesa"),
    2: n("Ampliar o uso da telemedicina e monitorar a distância idosos com risco de agravamento aumentaria a despesa"),
    3: n("Implantar unidades móveis de saúde nas periferias aumentaria a despesa"),
    4: d("O Agenda Fácil (app de marcação de consultas) usa a estrutura de tecnologia da saúde, com custo pequeno e sem ação própria.", DA, "baixa"),
    5: n("Criar a agência regulatória de convênios das vagas de 0 a 3 anos é medida administrativa ou de regra, com custo pequeno", SID),
    6: n("Criar programas de habilidades socioemocionais para os alunos da rede municipal aumentaria a despesa"),
    7: so(0.01, "Ações de Educação Integral (atividade 4303): R$ 13,5 milhões em 2016 e R$ 9,8 milhões em 2017. Subestima o custo, porque os professores das escolas integrais são pagos pelas ações gerais de remuneração.", "baixa"),
    8: n("Criar o Centro de Apoio e Inovação para professores e equipes escolares aumentaria a despesa"),
    9: n("Criar Centro Regional de Atendimento a Crianças e Adolescentes vítimas de violação de direitos aumentaria a despesa"),
    10: n("Criar o Centro de Apoio e Valorização da Família aumentaria a despesa"),
    11: d("O Programa Redenção é pago por ações gerais de saúde e assistência social; a ação própria de álcool e drogas teve menos de R$ 1 milhão por ano, sem valor separado.", DA, "baixa"),
    12: n("Implantar unidades do Bom Prato nos distritos mais vulneráveis aumentaria a despesa"),
    13: n("Unificar o cadastro dos beneficiários dos programas de transferência de renda e da assistência é medida administrativa ou de regra, com custo pequeno", SID),
    14: n("Implantar centros de informação ao imigrante e refugiado em rodoviárias, aeroportos e estações aumentaria a despesa"),
    15: n("Transformar os Centros de Convivência de Idosos em Centros de Sabedoria e Conhecimento aumentaria a despesa"),
    16: n("Ampliar o Programa de Assistência Domiciliar ao Idoso aumentaria a despesa"),
    17: n("Ampliar o Programa Acompanhante de Idosos aumentaria a despesa"),
    18: d("A nova Unidade de Referência à Saúde do Idoso, inaugurada em abr/2018, é paga pela manutenção geral da atenção básica, fora do ano completo (2017).", DA, "baixa"),
    19: n("Implantar o Plano Municipal de Ações Afirmativas e Combate ao Racismo é medida administrativa ou de regra, com custo pequeno", SID),
    20: n("Ampliar os Centros de Referência de Combate ao Racismo aumentaria a despesa"),
    21: n("Implantar o Programa Via Rápida Zumbi dos Palmares de trabalho e empreendedorismo afro-brasileiro aumentaria a despesa"),
    22: n("Criar grupo de trabalho intersetorial de combate à intolerância religiosa é medida administrativa ou de regra, com custo pequeno", SID),
    23: n("Criar fundo municipal de políticas para a comunidade negra e núcleos de combate ao racismo nas prefeituras regionais aumentaria a despesa"),
    24: n("Criar conselho de participação e desenvolvimento da comunidade negra é medida administrativa ou de regra, com custo pequeno", SID),
    25: n("Instituir fórum da comunidade negra e premiação de destaques é medida administrativa ou de regra, com custo pequeno", SID),
    26: n("Criar o Centro Cultural Afro aumentaria a despesa"),
    27: n("Ampliar o Programa Transcidadania aumentaria a despesa"),
    28: n("Ampliar o Centro de Referência LGBT aumentaria a despesa"),
    29: n("Criar o Fórum Ecumênico Municipal é medida administrativa ou de regra, com custo pequeno", SID),
    30: n("Criar uma Rede Única de Serviços para a mulher aumentaria a despesa"),
    31: n("Oferecer aulas de educação financeira e vida prática aos jovens nas escolas ou CEUs nos fins de semana aumentaria a despesa"),
    32: n("Criar a Virada Hackathon Jovens Empreendedores aumentaria a despesa"),
    33: n("Implantar na Casa das Retortas o Museu da História da Cidade de São Paulo aumentaria a despesa"),
    34: n("Criar o Centro da Memória da Dramaturgia Brasileira aumentaria a despesa"),
    35: n("Criar o prêmio São Paulo Amiga da Leitura aumentaria a despesa"),
    36: n("Reativar e aumentar os ônibus-biblioteca aumentaria a despesa"),
    37: n("Criar Conselhos de Cultura nas Prefeituras Regionais é medida administrativa ou de regra, com custo pequeno", SID),
    38: n("Elaborar novo Plano Municipal de Esporte é medida administrativa ou de regra, com custo pequeno", SID),
    39: n("Criar Núcleos de Desenvolvimento Regional aumentaria a despesa"),
    40: n("Criar o Empreenda SP em cada Prefeitura Regional aumentaria a despesa"),
    41: n("Aprovar a Lei Municipal de Inovação é medida administrativa ou de regra, com custo pequeno", SID),
    42: d("Mudar o nome e as atribuições das subprefeituras é reorganização administrativa.", SID),
    43: d("A primeira unidade do Descomplica SP abriu em mar/2018 (projeto 1358: R$ 5,8 milhões em 2018), fora do ano completo do mandato (2017).", DA, "baixa"),
    44: n("Criar um Centro de Operações Integrado para o Município aumentaria a despesa"),
    45: n("Implantar um Centro de Controle e Operação da Mobilidade integrando CET e SPTrans aumentaria a despesa"),
    46: n("Integrar a central da GCM (CETEL) ao COPOM da Polícia Militar é medida administrativa ou de regra, com custo pequeno", SID),
    47: n("Levar wi-fi com soluções pedagógicas às EMEFs, aberto às comunidades vizinhas aumentaria a despesa"),
    48: n("Modernizar as cinco Centrais de Tráfego em Área aumentaria a despesa"),
    49: n("Criar observatório de ideias para atrair talentos criativos, instalado nos bairros é medida administrativa ou de regra, com custo pequeno", SID),
    50: n("Instalar um polo criativo na Fábrica do Samba aumentaria a despesa"),
    51: n("Criar polo de capacitação em audiovisual (animação e publicidade) com a iniciativa privada aumentaria a despesa"),
    52: d("O Empreenda Fácil é um sistema de simplificação com custo pequeno.", SID),
    53: d("Reduzir o prazo de abertura de empresas é mudança de procedimento, sem gasto relevante.", SID),
    54: n("Criar frentes de trabalho emergenciais para pessoas em vulnerabilidade aumentaria a despesa"),
    55: n("Implantar o Mutirão do Emprego aumentaria a despesa"),
    56: n("Implantar Ruas 24 Horas de compras, lazer e cultura é medida administrativa ou de regra, com custo pequeno", SID),
    57: n("Criar, com o Estado, um Centro Tecnológico de Pesquisa para Agricultura e uma Escola Técnica Agrícola aumentaria a despesa"),
    58: n("Criar um centro de compostagem em grande escala na Zona Sul aumentaria a despesa"),
    59: n("Criar, com o Estado, um Poupatempo da atividade rural aumentaria a despesa"),
    60: n("Implantar programa de monitoramento de emissões de ônibus e caminhões a diesel aumentaria a despesa"),
    61: d("O Córrego Limpo é feito com a Sabesp, que paga as obras de coleta de esgoto; a parte da Prefeitura não tem ação própria.", FO, "baixa"),
    62: d("O projeto Centro Novo foi doado (via Secovi), e o enterramento de fios é feito pelas concessionárias de energia e telecomunicações, sem valor separado no orçamento da Prefeitura.", SID, "baixa"),
    63: n("Criar uma Unidade de Gestão para o Circuito das Compras (Brás, 25 de Março, Bom Retiro) é medida administrativa ou de regra, com custo pequeno", SID),
    64: n("Transformar o Parque Industrial da Mooca em Parque da Indústria Criativa aumentaria a despesa"),
    65: d("Reduzir o prazo do licenciamento é mudança de procedimento.", SID),
    66: n("Implantar os Polos Tecnológicos do Jaguaré e da Zona Leste aumentaria a despesa"),
    67: d("O Plano de Desenvolvimento Urbano Integrado é conduzido pelo Estado.", SID),
    68: n("Ampliar as linhas de ônibus noturnas nos fins de semana aumentaria a despesa"),
    69: n("Criar as linhas de ônibus interbairros aumentaria a despesa"),
    70: n("Implantar bolsões de estacionamento pagos com Bilhete Único nas pontas das linhas troncais e do metrô é medida administrativa ou de regra, com custo pequeno", SID),
    71: n("Ceder espaços municipais ao Detran para Centros de Treinamento e Exames é medida administrativa ou de regra, com custo pequeno", SID),
    72: d("O compartilhamento de bicicletas é regulamentado e operado por empresas privadas, sem gasto da Prefeitura.", SID),
    73: d("Mudar o limite de velocidade é regra de trânsito; pode reduzir a receita de multas, sem valor medido.", SID, "baixa"),
    74: n("Implantar miniterminais de cargas para pequenos e médios comércios aumentaria a despesa"),
    75: n("Criar comitê multissetorial de cargas é medida administrativa ou de regra, com custo pequeno", SID),
    76: n("Criar Conselhos de Segurança no Trânsito e de Transportes nas regiões operacionais é medida administrativa ou de regra, com custo pequeno", SID),
    77: n("Criar programa de aluguel social em imóveis ociosos aumentaria a despesa"),
    78: d("O PPI 2017 (Lei 16.680/2017) antecipa a cobrança da dívida ativa com descontos de multa e juros; a Prefeitura esperava arrecadar cerca de R$ 1 bi, mas o valor arrecadado não foi localizado.", "receita_aumenta", "baixa"),
    79: n("Recuperar a iluminação oriental da Liberdade aumentaria a despesa"),
    80: n("Implantar luminárias solares com LED em praças e parques aumentaria a despesa"),
    81: d("A rede de sanitários seria uma concessão, com investimento da concessionária; a licitação foi suspensa.", FO),
    82: n("Construir em PPP um crematório na região Sul ou Sudoeste aumentaria a despesa"),
    83: n("Ampliar as centrais de triagem manual de recicláveis aumentaria a despesa"),
    84: n("Implantar rede de usinas de compostagem aumentaria a despesa"),
    85: n("Extinguir uma secretaria reduziria pouco a despesa", "despesa_reduz"),
    86: n("Criar unidade gestora de drenagem urbana e controle de inundações é medida administrativa ou de regra, com custo pequeno", SID),
    87: d("A concessão dos cemitérios só foi feita depois da renúncia; no mandato houve só autorização e estudos.", FO),
    88: n("Contratar zeladoria em microáreas por parceria público-privada aumentaria a despesa"),
    89: d("A concessão do Pacaembu e a venda do Anhembi só geraram receita depois de 2017 (contratos de 2019 em diante); em 2017 houve só as leis.", "receita_aumenta", "media"),
}

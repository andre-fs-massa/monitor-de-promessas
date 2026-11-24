# Classificação do censo de Tarso Genro (RS, 2010). Mandato 2011-2014, encerrado. Entregas posteriores ao mandato
# contam como não cumpridas; sem registro = não cumprida, confiança baixa.
SEM = "Busca nas notícias do governo do Rio Grande do Sul e na imprensa (2011 a 2014) não localizou "
RS = "https://estado.rs.gov.br/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


def C(txt, url, data, conf="alta"):
    return ("cumprida", conf, txt, url, data)


D = {
    1: C("O Conselho de Desenvolvimento Econômico e Social (CDES-RS) foi instalado em 15/03/2011 e funcionou durante todo o governo.", RS + "upload/arquivos/20170701/revista-de-balanco-gestao-2011-2012-cdes-rs.pdf", "2012"),
    2: S("a criação do Conselho de Ética Pública nem do Observatório da Cidadania."),
    3: S("a instituição de comissão permanente de negociação com os servidores."),
    4: ("nao_cumprida", "media", "O CDES elaborou minuta do Conselho Estadual de Comunicação Social em 2012 e o governador disse que enviaria o projeto sem urgência; não se localizou a criação do conselho.", "https://sul21.com.br/?p=113284", "2012-07"),
    5: C("O Ensino Médio Politécnico, reestruturação curricular proposta em 2011, foi implantado em toda a rede estadual a partir de 2012 e concluído em 2014.", "https://www.redalyc.org/pdf/2750/275043450102.pdf", "2014"),
    6: ("nao_cumprida", "alta", "O Estado não pagou o piso nacional do magistério: em 2014 projetava pagar R$ 1.260 até o fim do ano, frente ao piso de R$ 1.451, e em 2012 Tarso aderiu a ação no STF contra o critério de reajuste.", "https://sul21.com.br/?p=117381", "2014"),
    7: C("Documento de 2013 ligado ao governo afirma que a gestão investiu mais de R$ 300 milhões em 1.800 obras escolares e acabou com as escolas de lata (afirmação do próprio governo).", "https://img.claudemirpereira.com.br/2013/09/AQUI1.pdf", "2013-09", "baixa"),
    8: S("programa de computador para cada professor no governo Tarso (o Professor Digital, com notebooks financiados pelo Banrisul, é do governo anterior)."),
    9: S("a criação do ProUni/RS."),
    10: S("a retomada dos cursos de Pedagogia na Uergs."),
    11: C("O governo criou o RS na Paz, Programa de Segurança Pública com Cidadania, para consolidar a metodologia do Pronasci, e renovou o convênio com a União prevendo cinco novos Territórios de Paz.", "https://sul21.com.br/?p=126158", "2012-03", "media"),
    12: S("a criação de observatórios da violência e criminalidade."),
    13: C("O governo elevou gradualmente o gasto em saúde e afirmou ter atingido os 12% constitucionais (a secretaria fala em 7,6% para 12%); o cálculo é contestado por entidades médicas e órgãos de controle.", RS + "mateando-com-o-governador-executivo-deve-destinar-12-dos-recursos-para-a-saude-ainda-em-2013", "2013-08", "baixa"),
    14: S("a criação da Ouvidoria Geral Estadual do SUS."),
    15: S("centrais de interpretação a distância dos exames de imagem."),
    16: ("nao_cumprida", "alta", "Ao fim de 2018, 62 municípios gaúchos ainda não tinham acesso asfáltico, segundo o governo seguinte.", RS + "em-seis-anos-estado-realiza-maior-investimento-da-historia-em-acessos-asfalticos-com-recursos-proprios", "2025-08"),
    17: S("a retomada do Programa Estadual de Pavimentação Poliédrica."),
    18: S("a criação do Conselho Estadual de Energia, Recursos Minerais e Telecomunicações."),
    19: S("o programa Mais e Melhor Energia para Todos."),
    20: S("o Programa Estadual de Incentivo a Fontes Alternativas de Energia."),
    21: S("o Programa Estadual de Produção e Uso de Biodiesel."),
    22: S("a retomada do Programa de Habitação Rural."),
    23: S("a criação do Museu das Águas na orla do Guaíba."),
    24: S("a criação do Fundo Estadual de Abastecimento e Saneamento."),
    25: S("a criação de um Programa de Conectividade Estadual."),
    26: ("nao_cumprida", "media", "O Plano Estadual de Cultura foi rejeitado pela Assembleia Legislativa; não se localizou lei do Sistema Estadual de Cultura no período.", "https://sul21.com.br/?p=127427", "2014"),
    27: S("a criação da Coordenadoria de Direitos Humanos, Diversidade e Dignidade."),
    28: S("a criação do Bolsa Juventude."),
    29: S("linha de microcrédito para mulheres chefes de família."),
    30: S("balanço da capacitação de 40 mil mulheres."),
    31: S("o Pacto pela Educação Infantil com os municípios."),
    32: S("programa estadual pela escola sem homofobia."),
    33: C("Publicação do governo (Secretaria do Esporte e UFRGS) registra que os JIRGS e o ParaJIRGS foram reestruturados e valorizados no governo Tarso.", "https://ludopedio.org.br/wp-content/uploads/Goellner_e_Silva_L_-_Jogos_Intermunicipais_no_RS.pdf", "2014", "baixa"),
    34: C("A Lei 13.924, de 17/01/2012, criou o Pró-Esporte/RS, programa de incentivo fiscal ao esporte.", "https://www.normasbrasil.com.br/norma/lei-13924-2012-rs_155861.html", "2012-01"),
}

# Classificação do censo de Eduardo Leite (RS, 2018). Mandato 2019-2022; Leite renunciou em 31/03/2022 para disputar
# a Presidência e o vice, Ranolfo Vieira Júnior, completou o mandato. Avaliação até a renúncia: o que começou e foi
# concluído depois aparece como interrompida; sem registro = não cumprida, confiança baixa.
SEM = "Busca nas notícias do governo do Rio Grande do Sul e na imprensa (2019 a mar/2022) não localizou "
RS = "https://estado.rs.gov.br/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


def C(txt, url, data, conf="alta"):
    return ("cumprida", conf, txt, url, data)


def I(txt, url, data, conf="media"):
    return ("interrompida", conf, txt, url, data)


D = {
    1: C("A Assembleia aprovou em 2021 a lei do teto de gastos, um dos requisitos para a adesão ao Regime de Recuperação Fiscal (a regra foi endurecida pelo PLC 48 em mai/2022, já no governo Ranolfo).", "https://www.brasildefato.com.br/2021/10/29/eduardo-leite-envia-a-assembleia-legislativa-projeto-que-cria-teto-de-gastos-estadual-no-rs/", "2021", "media"),
    2: C("A reforma da previdência dos servidores civis (PLC 503/2019) foi aprovada em dez/2019 e a PEC 285/2019 em jan/2020.", RS + "reforma-da-previdencia-dos-servidores-civis-do-rs-e-aprovada-na-assembleia", "2019-12"),
    3: ("nao_cumprida", "media", "A Reforma Tributária RS, enviada à Assembleia em ago/2020 com revisão de benefícios fiscais, foi adiada; não se localizou plano plurianual de redução gradual dos incentivos aprovado até a renúncia.", RS + "rs-esta-reduzindo-a-carga-tributaria-em-plena-pandemia-e-de-forma-responsavel-afirma-leite-apos-aprovacao-do-pl-246", "2020-12"),
    4: C("Com autorização da Assembleia (set/2021), o Estado pediu adesão ao Regime de Recuperação Fiscal em dez/2021 e obteve aprovação do Tesouro Nacional em jan/2022, renegociando a dívida com a União (plano homologado em jun/2022).", RS + "adesao-do-rs-ao-regime-de-recuperacao-fiscal-e-aprovada", "2022-01"),
    5: S("contratualização formal de metas com as secretarias."),
    6: S("a criação de fundo garantidor de PPPs."),
    7: S("a atualização do marco regulatório estadual das PPPs."),
    8: I("O edital da concessão do Bloco 3 de rodovias (271,5 km) foi publicado no governo Leite; o leilão ocorreu em 13/04/2022, duas semanas após a renúncia.", RS + "leilao-para-concessao-de-rodovias-no-rs-sera-nesta-quarta-13-na-b3", "2022-04", "alta"),
    9: S("a concessão da dragagem do Porto de Rio Grande."),
    10: S("a conclusão da duplicação da BR-116 (obra federal)."),
    11: C("A Corsan assinou com a Aegea, em 24/03/2020, a PPP de esgotamento sanitário da Região Metropolitana de Porto Alegre (35 anos).", RS + "consorcio-aegea-vence-leilao-da-ppp-do-saneamento-da-corsan", "2020-03"),
    12: C("O novo Código Estadual do Meio Ambiente (Lei 15.434/2020), sancionado em jan/2020, criou a Licença Ambiental por Compromisso (LAC), regulamentada pelo Consema em 2021.", "https://www.estado.rs.gov.br/da-condicoes-de-desenvolvimento-com-devida-protecao-a-natureza-destaca-leite-na-sancao-do-novo-codigo-ambiental-do-rs", "2020-01"),
    13: C("A Lei 15.451/2020 reformulou o plano de carreira do magistério, com remuneração por subsídio alinhada ao piso nacional.", RS + "governador-sanciona-mudancas-na-previdencia-e-carreira-dos-servidores-do-rs", "2020-02"),
    14: S("o SUS Conectado ou o Centro de Informações e Decisões Estratégicas em Saúde."),
    15: C("O Estado firmou com Famurs, Cosems e Defensoria Pública acordo de cooperação para resolver demandas de saúde sem ação judicial.", "https://www.conass.org.br/?p=20409", "2019", "baixa"),
    16: C("O RS Seguro (2019) criou as Áreas Integradas de Segurança Pública nos 18 municípios prioritários, começando por Canoas.", RS + "entrega-de-acoes-estrategicas-marca-120-dias-do-programa-rs-seguro", "2019-05"),
    17: S("a instituição de um Programa de Integridade no Executivo."),
    18: ("parcialmente_cumprida", "media", "A Delegacia Online ganhou novas funcionalidades (como o registro de violência contra a mulher, em 2020) e os registros cresceram 49% no 1º semestre de 2020; o novo sistema de ocorrências não foi localizado.", "https://www.jornaldocomercio.com/_conteudo/geral/2020/07/748379-registro-de-ocorrencias-via-delegacia-online-cresce-49-no-primeiro-semestre.html", "2020-07"),
    19: I("O Estado contratou o BNDES para estruturar a primeira PPP de presídio (Erechim); o leilão só ocorreu em out/2023, e a vencedora foi desclassificada.", RS + "rs-inicia-a-primeira-ppp-de-presidio-e-publica-edital-para-duplicar-a-rsc-287", "2021"),
    20: S("programa de inovação no agronegócio Agro-Tech."),
    21: S("programa estadual de microcrédito habitacional."),
}

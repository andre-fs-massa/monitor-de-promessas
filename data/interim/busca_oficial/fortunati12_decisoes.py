# Classificação do censo de José Fortunati (Porto Alegre, 2012). Mandato 2013-2016, encerrado. Obras concluídas depois
# do mandato = não cumpridas; sem registro = não cumprida, confiança baixa.
SEM = "Busca nas notícias da Prefeitura de Porto Alegre e na imprensa (2013 a 2016) não localizou "
P = "https://prefeitura.poa.br/"
COPA = "https://www.jornaldocomercio.com/_conteudo/economia/2019/03/amp/674227-como-estao-as-obras-da-copa-em-porto-alegre.html"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


def N(txt, url, data, conf="alta"):
    return ("nao_cumprida", conf, txt, url, data)


D = {
    1: N("O metrô de Porto Alegre não saiu do papel.", "https://sul21.com.br/?p=57885", "2016"),
    8: ("cumprida", "media", "A ETE Serraria, principal obra do Pisa, foi inaugurada em abr/2014 e elevou a capacidade de tratamento de esgoto para 80% (o volume efetivamente tratado seguia perto de 57% em 2025).", "https://prefeitura.poa.br/sites/default/files/usu_doc/sites/dmae/ECOS%2034.pdf", "2014-04"),
    9: ("cumprida", "alta", "Entre jan e mar/2016 a Prefeitura duplicou o número de contêineres da coleta automatizada.", P + "dmlu/coleta-conteinerizada", "2016-03"),
    15: N("A revitalização da Orla do Guaíba (trecho 1) só foi inaugurada em 2018, na gestão seguinte.", P + "gp/noticias/prefeito-abre-semana-da-superacao-com-balanco-do-programa-porto-alegre-forte", "2018", "media"),
    18: N("A duplicação da avenida Tronco não foi concluída no mandato: em 2016 o prazo era dez/2017, e a obra só foi entregue na gestão Melo.", P + "gp/noticias/avenida-tronco-e-entregue-e-liberada-para-transito", "2016"),
    19: ("parcialmente_cumprida", "baixa", "A avenida Beira-Rio (Edvaldo Pereira Paiva) teve obras para a Copa, mas o viaduto previsto só foi entregue em 2019.", COPA, "2019-03"),
    20: N("As obras de arte da Terceira Perimetral seguiam inacabadas em 2016; trincheiras e viadutos foram entregues entre 2019 e 2022.", COPA, "2019-03"),
    21: N("A duplicação da Voluntários da Pátria parou e só foi retomada em 2021, após cinco anos.", P + "smoi/noticias/concluida-obra-da-rua-voluntarios-da-patria-no-trecho-1", "2021"),
    22: N("A ampliação da Severo Dullius não foi concluída no mandato; ficou parada e só terminou em 2023.", COPA, "2019-03"),
    23: N("O viaduto junto à Rodoviária só foi entregue em 2019.", COPA, "2019-03", "media"),
    24: N("Os BRTs não foram implantados; em 2016 o TCU recomendou bloquear obras de corredores e parte da verba foi remanejada em 2018.", "https://diariodotransporte.com.br/2018/01/31/porto-alegre-recupera-parte-de-verba-destinada-para-brt-para-realizar-obras-previstas-para-a-copa/", "2018-01"),
    25: S("a duplicação das avenidas Vicente Monteggia, Edgar Pires de Castro e Oscar Pereira e o acesso norte do Porto Seco (que voltaram a ser prometidos em 2020 e 2024)."),
    36: N("No Ideb 2015 a rede municipal teve 4,6 nos anos iniciais e 3,8 nos anos finais, abaixo da trajetória de metas (5,6 e 5,0 para 2019).", P + "smed/noticias/cinco-escolas-de-ensino-fundamental-atingem-metas-no-ideb-2019", "2016", "media"),
    44: N("As UPAs Navegantes, Azenha e Zona Sul não foram construídas: até 2024 a cidade tinha só uma UPA, a da Zona Norte.", P + "sms/noticias/porto-alegre-contara-com-mais-duas-upas-ate-o-final-do-ano", "2024-06"),
    47: ("parcialmente_cumprida", "media", "O hospital veterinário público (Unidade de Saúde Animal Victória), doado pelo empresário Alexandre Grendene, foi inaugurado em nov/2016, mas sem licenças, e só começou a atender em 2018; não se localizou a meta de 100 esterilizações por dia.", "https://forbes.com.br/colunas/2017/10/hospital-veterinario-publico-doado-por-grendene-completa-um-ano-sem-funcionar/", "2017-10"),
    51: N("A cobertura da Saúde da Família era de cerca de 50% em 2018, abaixo dos 70% prometidos para 2016.", P + "gp/noticias/prefeito-entrega-relatorio-de-atividades-de-2018-camara", "2019", "media"),
    53: N("A pré-escola não foi universalizada: a rede tinha 16.661 vagas em 2016, e a meta do Plano Municipal de Educação de universalizar até 2016 seguia em aberto.", "https://www.ufrgs.br/humanista/?p=6589", "2020", "media"),
}
_RESTO = {
    2: "a regulamentação da Lei da Inovação com benefícios fiscais", 3: "a criação do Instituto de Planejamento Urbano e Ambiental",
    4: "a implementação das Regiões de Potencial Tecnológico", 5: "o Banco de Ideias e Projetos",
    6: "operação urbana consorciada no trajeto do metrô", 7: "a reforma dos centros regionais em Centros de Cogestão",
    10: "as 15 novas equipes da coleta seletiva", 11: "as seis novas unidades de triagem do projeto de carroceiros",
    12: "central de tratamento de resíduos orgânicos", 13: "a implantação do Plano Diretor de Drenagem Urbana",
    14: "balanço de ciclovias da gestão", 16: "a reestruturação da Defesa Civil com núcleos regionais",
    17: "o Plano de Contingência e Redução das Áreas de Risco", 26: "a Central de Monitoramento da Frota com wi-fi nos ônibus",
    27: "o programa Tecnojovem", 28: "novos Centros de Referência da Juventude", 29: "as repúblicas para jovens adultos em situação de rua",
    30: "o Escritório de Regularização Fundiária e Urbanização", 31: "a conclusão do Teatro Elis Regina",
    32: "a Escola Municipal de Cultura", 33: "as Casas Comunitárias de Leitura", 34: "a Coordenação de Dança e o Prêmio Açorianos de Dança",
    35: "a universalização do tempo integral", 37: "balanço das 65 escolas prometidas", 38: "monitores para alunos com deficiência",
    39: "o Centro de Referência do Negro", 40: "o Plano Municipal do Idoso", 41: "a informatização plena da regulação",
    42: "balanço dos 1.077 leitos prometidos", 43: "a conclusão da reforma do Hospital de Pronto Socorro",
    45: "saúde bucal em todas as unidades reformadas", 46: "os cinco novos CAPS adultos",
    48: "a unidade móvel do Centro de Referência às Vítimas de Violência", 49: "a ampliação do cercamento eletrônico dos parques",
    50: "paradas seguras em todos os pontos de ônibus", 52: "aprovação digital de projetos de até 800 m²",
}
for _k, _v in _RESTO.items():
    D.setdefault(_k, S(_v + "."))

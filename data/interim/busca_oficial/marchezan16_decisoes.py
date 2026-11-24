# Classificação do censo de Nelson Marchezan Júnior (Porto Alegre, 2016). Mandato 2017-2020, encerrado.
SEM = "Busca nas notícias da Prefeitura de Porto Alegre e na imprensa (2017 a 2020) não localizou "
P = "https://prefeitura.poa.br/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


D = {
    1: ("nao_cumprida", "media", "As assembleias do Orçamento Participativo foram suspensas na gestão Marchezan, sob o argumento de que a Prefeitura não conseguia atender as demandas já aprovadas, e só foram retomadas na gestão seguinte.", "https://www.brasildefato.com.br/2018/01/06/fim-do-orcamento-participativo-e-cerco-a-protesto-conheca-o-prefeito-de-porto-alegre/", "2018-01"),
    2: ("cumprida", "media", "A Prefeitura fechou 2019 com superávit orçamentário de R$ 573,1 milhões, o maior em 20 anos (sexto resultado positivo consecutivo), com redução de 2,4% das despesas.", "https://www.jornaldocomercio.com/politica/2020/01/721606-porto-alegre-tem-superavit-de-r-573-milhoes-em-2019.html", "2020-01"),
    3: S("dados de ampliação das vagas de pré-escola."),
    4: ("nao_cumprida", "alta", "No Ideb 2019 a rede municipal teve 4,9 nos anos iniciais (meta 5,6) e 3,7 nos anos finais (meta 5,0); só cinco escolas atingiram suas metas.", P + "smed/noticias/cinco-escolas-de-ensino-fundamental-atingem-metas-no-ideb-2019", "2020-09"),
    5: S("programa permanente de manutenção das escolas."),
    6: S("a ampliação dos Núcleos de Apoio à Saúde da Família."),
    7: ("cumprida", "alta", "A cobertura da Estratégia Saúde da Família subiu de 50% em 2018 para 61,3% em 2019 (263 equipes), acima da meta anual de 58%.", P + "sms/noticias/resultados-da-saude-sao-apresentados-em-relatorio-de-gestao", "2020"),
    8: S("a criação de rede de proteção às mulheres com o Estado (entidades afirmam que acordo de 2018 para a Casa de Referência não foi cumprido).", "https://sul21.com.br/?p=132639"),
    9: ("nao_cumprida", "media", "Os primeiros ônibus elétricos do transporte público de Porto Alegre só começaram a operar em fev/2024, na gestão seguinte.", P + "gp/noticias/onibus-eletricos-entram-em-operacao-em-porto-alegre", "2024-02"),
    10: ("cumprida", "media", "A gestão entregou cerca de 10 a 11 km de ciclovias, levando a rede a 54 km em 2020 (menos do que nos dois últimos anos da gestão anterior).", P + "eptc/noticias/ciclovias-chegam-aos-54-quilometros-em-porto-alegre", "2020-05"),
}

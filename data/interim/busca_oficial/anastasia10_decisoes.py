# Classificação do censo de Antonio Anastasia (governo de Minas Gerais, 2010). Renunciou em 04/04/2014 para disputar
# o Senado; o vice, Alberto Pinto Coelho, assumiu. Avaliação até a renúncia: iniciadas e não concluídas = interrompida;
# não iniciadas = não cumprida (mesmo critério de Zema 2022, Doria e Alckmin).
# Chave = índice (1-based) em anastasia10_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia) ou None.
SEM = "Busca na imprensa, na Agência Minas e na legislação mineira (API da ALMG, jan/2011 a 04/04/2014) não localizou "


def S(txt, url="", data="2014-04"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


D = {
    1: ("interrompida", "media", "O modelo Estado em Rede, da Gestão para a Cidadania (2011), foi testado em comitês regionais piloto (Rio Doce, Norte e Mata), sem chegar às 66 microrregiões até a renúncia.", "https://www.agenciaminas.mg.gov.br/noticia/comite-regional-da-mata-realiza-primeira-reuniao-em-juiz-de-fora-67876", "2012-02"),
    2: ("interrompida", "media", "Foram instalados comitês regionais com agentes de várias secretarias em cidades-polo como Montes Claros e Juiz de Fora (2012), mas só em parte das regiões.", "https://www.agenciaminas.mg.gov.br/noticia/montes-claros-recebe-6a-reuniao-do-comite-regional-do-norte-73150", "2012"),
    3: S("unificação da base territorial dos órgãos estaduais."),
    4: S("ampliação da escola em tempo integral entre 2011 e 2014."),
    5: S("ampliação da formação profissionalizante estadual entre 2011 e 2014."),
    6: ("cumprida", "baixa", "A extrema pobreza em Minas caiu de 3,78% (2006) para 2,49% (2013), segundo a PNAD; não há dado separado do período de Anastasia, e em 2012-2013 a extrema pobreza subiu no país.", "https://www.ipece.ce.gov.br/wp-content/uploads/sites/45/2012/12/EnfoqueEconomicoN80_04_10_2013.pdf", "2013"),
}
AJUSTES = {}

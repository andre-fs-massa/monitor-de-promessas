# Classificação do censo de Romeu Zema (governo de Minas Gerais, 2018). Mandato 2019-2022, encerrado.
# Chave = índice (1-based) em zema18_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia) ou None.
SEM = "Busca na imprensa, na Agência Minas e na legislação mineira (API da ALMG, jan/2019 a dez/2022) não localizou "
LEG = "https://www.almg.gov.br/legislacao-mineira/texto/"
AG = "https://www.agenciaminas.mg.gov.br/noticia/"


def S(txt, url="", data="2022-12"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


D = {
    1: ("cumprida", "alta", "A reforma administrativa (Lei 23.304/2019) reduziu as secretarias de 21 para 12 e extinguiu cargos.", LEG + "LEI/23304/2019/", "2019-05"),
    2: ("cumprida", "alta", "O programa Transforma Minas (mar/2019) passou a selecionar por mérito e competências os ocupantes de cargos de liderança; mais de 200 foram nomeados assim.", AG + "governador-romeu-zema-recebe-102-aprovados-pelo-programa-transforma-minas", "2019"),
    3: S("auditorias patrimoniais aleatórias; a sindicância patrimonial já existia desde 2015 (Decreto 46.881) e só foi alterada em 2022.", LEG + "DEC/48421/2022/"),
    4: S("exigência de seguro do tipo performance bond nas contratações estaduais."),
    5: ("cumprida", "alta", "O acordo com a AMM (abr/2019) parcelou em 33 vezes os R$ 7 bilhões de ICMS, IPVA e Fundeb atrasados, quitados em jun/2022.", AG + "governo-de-minas-quita-divida-de-r-7-bi-com-municipios-2022-06-02-22-30-00-0300", "2022-06"),
    6: S("avaliação de órgãos e servidores por pesquisa com a população ligada à bonificação."),
    7: ("cumprida", "alta", "O governo concedeu o Aeroporto da Pampulha, o Mineirinho, os lotes 1 e 2 de rodovias (2022) e o Rodoanel, entre outros projetos.", "https://diariodocomercio.com.br/economia/governo-leiloa-3o-lote-de-rodovias-e-grupo-vence-mais-uma-vez/", "2022"),
    8: ("cumprida", "media", "A previdência complementar dos novos servidores já existia (Prevcom-MG, LC 132/2014); a reforma de 2020 abriu a migração dos servidores antigos, como prometido.", "https://tce.mg.gov.br/noticia/Detalhe/1111624726", "2020"),
    9: ("cumprida", "media", "Zema manteve a sede do governo na Cidade Administrativa e não ocupou os palácios.", "https://www.em.com.br/app/noticia/politica/2019/01/24/interna_politica,1024154/zema-articula-parceria-pra-decidir-futuro-do-palacio-das-mangabeiras.shtml", "2019-01"),
    10: ("cumprida", "media", "O Palácio da Liberdade voltou a ser aberto à visitação pública em out/2019.", AG + "governador-romeu-zema-acompanha-a-troca-da-guarda-do-palacio-da-liberdade-em-belo-horizonte", "2019-10"),
    11: S("redução do salário do governador por lei; Zema declarou doar o próprio salário."),
    12: ("cumprida", "alta", "Zema não morou no Palácio das Mangabeiras, que deixou de ser residência oficial (Decreto 47.667/2019) e virou parque público em 2022.", AG + "codemge-assume-gestao-do-palacio-das-mangabeiras-105891", "2019-06"),
    13: ("cumprida", "media", "Não foram criados tributos nem elevadas alíquotas no mandato; o adicional de ICMS sobre supérfluos, anterior a 2019, foi mantido até o fim de 2022.", "https://www.itatiaia.com.br/politica/nao-queremos-aumentar-impostos-mas-manter-o-que-vigorou-ate-2022-diz-zema-sobre-projeto-do-icms/", "2022-12"),
    14: ("nao_cumprida", "alta", "O governo manteve o sigilo da lista de empresas com regimes especiais de ICMS; a divulgação só ocorreu em 2026, após pressão do TCE e da Justiça.", "https://ofator.com.br/informacao/tce-avalia-cobrar-governo-zema-pela-divulgacao-da-lista-de-empresas-beneficiadas-por-incentivos-fiscais/", "2022-12"),
    15: S("norma que permita selos e certificações privadas no lugar da regulação estatal."),
    16: ("cumprida", "alta", "O decreto de liberdade econômica do Minas Livre para Crescer (em vigor em jan/2021) dispensou de alvará 642 atividades de baixo risco e criou a aprovação tácita.", AG + "decreto-de-liberdade-economica-entra-em-vigor-109708", "2021-01"),
    17: ("parcialmente_cumprida", "media", "A Jucemg passou a fazer registro automático de empresas simples (abr/2019), mas a exigência de autenticação de cópias foi só substituída por declaração assinada.", "https://www.agenciaminas.mg.gov.br/news/pdf/115626.pdf", "2022"),
    18: S("abertura das estatais remanescentes ao capital privado com conselhos independentes."),
    19: S("cadastro voluntário de bens duráveis."),
    20: S("monitoramento de indicadores de esclarecimento dos inquéritos de homicídio."),
    21: S("ampliação das penas alternativas com tornozeleiras ou revisão da população carcerária entre 2019 e 2022."),
    22: ("cumprida", "media", "A PM comprou 1.040 câmeras corporais em 2022 e começou a usá-las em projeto-piloto no fim do ano.", "https://tribunademinas.com.br/noticias/minas/06-05-2022/policia-militar-de-minas-quer-comecar-a-usar-cameras-no-uniforme-em-outubro-deste-ano.html?amp=1", "2022-12"),
    23: S("expansão das APACs ou de novas PPPs prisionais."),
    24: S("integração dos sistemas de informação das polícias no modelo do Infocrim."),
    25: S("criação de setor de inteligência para a violência no campo."),
    26: S("cerco eletrônico com câmeras inteligentes nas divisas."),
    27: S("PPP para reformar ou construir escolas; a PPP de 95 escolas só foi leiloada em 2026.", "https://agenciainfra.com/blog/?p=27585"),
    28: S("nova regra de distribuição de recursos priorizando as escolas mais precárias."),
    29: S("premiação de escolas e profissionais pela evolução do desempenho."),
    30: S("cessão de escolas ociosas a escolas privadas em troca de bolsas."),
    31: S("criação de voucher educacional."),
    32: S("parcerias com Senar, Sebrae ou Senai para cursos nas escolas rurais."),
    33: ("nao_cumprida", "media", "O app Conexão Escola (2020) foi feito para alunos e professores; o boletim digital para as famílias só começou depois de 2023.", "https://www.agenciaminas.mg.gov.br/news/pdf/108232.pdf", "2022-12"),
    34: ("cumprida", "media", "O parcelamento dos salários acabou em ago/2021 e os repasses atrasados aos municípios foram quitados até 2022.", "https://tribunademinas.com.br/noticias/minas/16-07-2021/governador-romeu-zema-anuncia-o-fim-do-parcelamento-dos-salarios.html?amp=1", "2021-08"),
    35: ("nao_cumprida", "alta", "Nenhum hospital regional foi entregue no mandato; as obras foram retomadas em out/2022 e o primeiro (Teófilo Otoni) só saiu em dez/2025.", "https://www.itatiaia.com.br/politica/promessa-de-zema-em-2022-nenhum-dos-seis-hospitais-regionais-foi-entregue-ate-agora/", "2022-12"),
    36: ("cumprida", "media", "O SAMU passou de cerca de 550 municípios atendidos em 2019 para quase 830 em 2023, com novas regionais implantadas a partir de 2022.", AG + "governo-de-minas-amplia-cobertura-do-samu-e-garante-atendimento-em-100-do-estado", "2023"),
    37: S("delegação da gestão de unidades estaduais de saúde a OS ou PPP."),
    38: ("cumprida", "alta", "A política Valora Minas (Deliberação CIB-SUS/MG 3.213/2020) passou a remunerar os hospitais por eficiência e resultados.", "https://portal-antigo.saude.mg.gov.br/cib/document/download/22969-resolucao-ses-mg-n-7-830-de-05-de-novembro-de-2021", "2020-09"),
    39: S("implantação estadual de prontuário eletrônico ou centros de telemedicina."),
}
AJUSTES = {}

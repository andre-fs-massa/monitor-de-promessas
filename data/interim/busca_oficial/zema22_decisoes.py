# Classificação do censo de Romeu Zema (governo de Minas Gerais, 2022). Renunciou em 22/03/2026 para disputar a
# Presidência; o vice, Mateus Simões, assumiu. Avaliação até a renúncia: iniciadas e não concluídas = interrompida;
# não iniciadas = não cumprida (mesmo critério de Doria e Alckmin em SP).
# Chave = índice (1-based) em zema22_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia) ou None.
SEM = "Busca na imprensa, na Agência Minas e na legislação mineira (API da ALMG, jan/2023 a mar/2026) não localizou "
LEG = "https://www.almg.gov.br/legislacao-mineira/texto/"
AG = "https://www.agenciaminas.mg.gov.br/noticia/"


def S(txt, url="", data="2026-03"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


D = {
    1: ("interrompida", "alta", "Até a renúncia foram entregues as obras dos hospitais regionais de Teófilo Otoni (dez/2025) e Divinópolis (fev/2026); Governador Valadares (34% em fev/2026), Conselheiro Lafaiete e Juiz de Fora seguiam em obras.", "https://www.agenciaminas.mg.gov.br/news/pdf/128721.pdf", "2026-02"),
    2: ("cumprida", "alta", "Em 2025 o Opera Mais incluiu 51 novos procedimentos (727 no total), com orçamento anual acima de R$ 376 milhões.", AG + "governo-de-minas-investe-mais-de-r-148-milhoes-para-ampliar-cirurgias-eletivas-em-todo-o-estado", "2025"),
    3: ("cumprida", "alta", "A Lei 25.668/2025 instituiu as unidades regionais de saneamento básico e criou o Fundo Estadual de Saneamento.", LEG + "LEI/25668/2025/", "2025-12"),
    4: ("parcialmente_cumprida", "baixa", "A base integrada de segurança pública passou a funcionar no data lake do Estado (Prodemge), usada pela PM; auditoria do TCU ainda apontou falta de integração dos sistemas em Minas.", "https://convergenciadigital.com.br/governo/base-integrada-de-dados-permite-a-pm-de-minas-avancar-com-ia/", "2025"),
    5: S("ampliação do Plantão Digital depois de 2022; em 2023 a OAB-MG pediu sua suspensão por filas de até 30 horas.", "https://www.conjur.com.br/?p=339737"),
    6: ("cumprida", "media", "O Trilhas de Futuro abriu 50 mil vagas em 2024 (ampliadas de 40 mil após recorde de inscrições) e 50 mil em 2025, além de 9.600 vagas do Trilhas nas Escolas.", AG + "governo-de-minas-amplia-vagas-do-trilhas-de-futuro-para-50-mil-apos-recorde-de-inscricoes-123791", "2025-06"),
    7: ("interrompida", "media", "O edital de 2024 para levar o Somar a até 80 escolas foi suspenso pelo TCE-MG e pelo TJMG; o projeto seguiu nas 3 escolas-piloto.", "https://www.gazetadopovo.com.br/vida-e-cidadania/tjmg-sindicato-expansao-gestao-privada-escolas/", "2024-10"),
    8: ("cumprida", "alta", "O ensino médio em tempo integral passou de 591 escolas em 2022 para 798 em 2025, com previsão de 838 em 2026.", AG + "governo-de-minas-anuncia-nova-expansao-do-ensino-medio-em-tempo-integral-emti-na-rede-estadual-de-ensino", "2025-12"),
    9: ("cumprida", "media", "O governo leiloou o lote 3 de rodovias (Varginha-Furnas) e preparou novos lotes (Vetor Norte, Ouro Preto-Mariana, Zona da Mata); a Lei 25.235/2025 criou a agência reguladora de transportes.", "https://diariodocomercio.com.br/economia/governo-leiloa-3o-lote-de-rodovias-e-grupo-vence-mais-uma-vez/", "2025"),
    10: ("parcialmente_cumprida", "media", "Não houve um marco legal único das renováveis, mas foram aprovadas leis setoriais: biogás e biometano (Lei 24.396/2023), energia rural renovável (Lei 24.625/2023) e hidrogênio verde (Lei 24.940/2024).", LEG + "LEI/24625/2023/", "2024-07"),
    11: S("licenciamento automático de empreendimentos de menor impacto; o Decreto 49.013/2025 consolidou normas de liberdade econômica.", LEG + "DEC/49013/2025/"),
    12: ("cumprida", "media", "O Minas Reurb seguiu ampliando a regularização: desde 2019 mais de 80 mil escrituras viabilizadas e 19 mil títulos entregues em 299 municípios.", "https://agenciaminas.mg.gov.br/news/pdf/128004.pdf", "2025-10"),
    13: ("interrompida", "alta", "A Lei 25.664/2025 autorizou a desestatização da Copasa; a oferta de ações só foi concluída em jun/2026, já na gestão Simões.", LEG + "LEI/25664/2025/", "2025-12"),
    14: S("criação de fundo estadual de microcrédito para agricultores familiares."),
    15: S("regulamentação da rastreabilidade e certificação agropecuária com empresas privadas."),
    16: ("cumprida", "alta", "O novo Regulamento do ICMS foi aprovado pelo Decreto 48.589/2023 e entrou em vigor em 01/07/2023.", LEG + "DEC/48589/2023/", "2023-03"),
    17: S("envio de projeto de Lei de Responsabilidade Fiscal estadual."),
    18: ("parcialmente_cumprida", "baixa", "A Lei 24.358/2023 extinguiu e criou cargos em comissão no Executivo; não foi localizado se todos os cargos vagos foram extintos.", LEG + "LEI/24358/2023/", "2023-06"),
    19: ("parcialmente_cumprida", "media", "Houve revisão de 4,62% em 2024 (inflação de 2023, Lei 24.838/2024) e foi anunciada a de 5,4% em mar/2026, mas não houve revisão em 2023 nem em 2025.", AG + "governo-de-minas-sanciona-nesta-quinta-feira-27-6-reajuste-salarial-de-4-62-para-os-servidores-publicos/", "2026-03"),
    20: ("cumprida", "media", "O contrato de concessão dos parques do Ibitipoca e do Itacolomi foi assinado em maio de 2023, e a concessão da Rota das Grutas Peter Lund entrou em consulta pública.", "https://www.agenciaminas.mg.gov.br/news/pdf/113003.pdf", "2023-05"),
    21: S("novo programa de internet e equipamentos para pessoas em vulnerabilidade; o TecPop Minas existe desde 2021."),
    22: ("parcialmente_cumprida", "media", "Não foi criado crédito habitacional, mas o programa Moradas Gerais passou a pagar reformas de até R$ 35 mil em casas de famílias vulneráveis.", "https://www.agenciaminas.mg.gov.br/news/pdf/129563.pdf", "2026-02"),
    23: ("cumprida", "media", "O Minas Forma (mai/2024) oferece cursos gratuitos com bolsa-auxílio para pessoas do CadÚnico.", AG + "governo-de-minas-lanca-programa-de-capacitacao-profissional-gratuita-em-101-cidades-122129", "2024-05"),
}
AJUSTES = {}

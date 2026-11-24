# Classificação do censo de Beto Richa (governo do Paraná, 2014). Mandato 2015-2018 interrompido: Richa renunciou em
# 06/04/2018 para disputar o Senado e a vice, Cida Borghetti, completou o mandato. Avaliação até a renúncia: o que já
# tinha começado fica "interrompida"; o que não tinha começado, "não cumprida". Fontes: arquivo da Agência Estadual de
# Notícias, sites oficiais do Paraná e imprensa. Sem registro = não cumprida, baixa.
# Chave = índice (1-based) em richa14_def.P; valor = (status, confianca, evidencia, fonte_url, data_evidencia).
SEM = "Busca no arquivo da Agência Estadual de Notícias, em páginas oficiais do governo do Paraná e na imprensa (2015 a abr/2018) não localizou "
ARQ = "https://arquivo2011.aen.pr.gov.br/sites/default/arquivos_restritos/files/documento/migrados/"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "baixa", SEM + txt, url, data)


D = {
    1: ("cumprida", "media", "No ajuste fiscal de 2015 o governo extinguiu cinco secretarias, fundiu outras e cortou mil cargos em comissão de uma vez.", "https://www.fazenda.pr.gov.br/Noticia/Governo-propoe-novas-medidas-para-cortar-gastos-e-retomar-investimentos", "2015-02"),
    2: S("balanço de 900 escolas equipadas e mobiliadas pelo Renova Escola até 2015; o programa atendeu 83 unidades a partir de 2016 (cerca de 900 escolas receberam reparos de outro programa, o Escola 1.000)."),
    3: S("plano estadual de logística elaborado pelo governo; o PELT 2035, iniciado em 2015, foi feito pelo Fórum Futuro 10 Paraná, liderado por entidades empresariais (Fiep, Sicepot), e o plano estadual (PELTi-2040) só saiu em 2025."),
    4: ("interrompida", "media", "A faixa de infraestrutura de Pontal do Paraná (rodovia, canal, ramal ferroviário e dutos) teve o EIA/RIMA elaborado e a licença prévia aprovada em 2017-2018, mas as obras não começaram até a renúncia e o licenciamento foi depois contestado na Justiça.", "https://www.gazetadopovo.com.br/parana/licenciamento-faixa-de-infraestrutura-litoral/", "2018"),
    5: S("nova política estadual de mudanças climáticas no mandato; a política estadual é da Lei 17.133/2012 (1º mandato) e o Plano de Ação Climática é posterior."),
    6: ("interrompida", "baixa", "O governo abriu em 2015 um Procedimento de Manifestação de Interesse para o Trem Pé-Vermelho e autorizou três consórcios a fazer estudos em mai/2016, mas o projeto não avançou para obra até a renúncia.", ARQ + "1805_pe_vermelho_e.doc", "2016-05"),
    7: ("interrompida", "media", "Richa assinou e enviou à Assembleia o projeto da Política Estadual do Biogás e Biometano, sancionado como Lei 19.500 em 21/05/2018 pela sucessora, Cida Borghetti.", ARQ + "2105_lei_biogas_e.doc", "2018-05"),
    8: S("a formulação de nova etapa da Política Estadual de Desenvolvimento Científico e Tecnológico."),
    9: S("alteração da Lei Estadual de Inovação (Lei 17.314/2012) no mandato; ela só foi atualizada pela Lei 20.541/2021."),
}

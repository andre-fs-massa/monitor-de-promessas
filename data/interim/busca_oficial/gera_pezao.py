import csv, json, re, runpy, sys
from pathlib import Path

# Pastas relativas a este arquivo (data/interim/busca_oficial/)
AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
P = runpy.run_path(str(AQUI / "pezao_def.py"))["P"]
L = json.load(open(AQUI / "pezao_rj_2014.json", encoding="utf-8"))
MID = "pezao_rj_2014"


def doerj(chave, data, padrao):
    for v in L[chave]["ioerj"].values():
        for i in v.get("itens", []):
            if i["data"] == data and re.search(padrao, i["resumo"]):
                return re.sub(r"&tb=.*", "&tb=", i["link"])
    raise SystemExit(f"link não achado: {chave} {data}")


SR = ("Busca na imprensa, em sites oficiais e no Diário Oficial do RJ (Parte I, 2015–2018) em out/2026 não localizou registro de {}. "
      "O banco de projetos da Alerj de 2015–2019 não respondeu às consultas.")

# chave: (status, confianca, evidencia, fonte_url, data)
C = {
 "upp": ("nao_cumprida", "media", "Nenhuma UPP nova foi criada entre 2015 e 2018; a última (38ª, Vila Kennedy) é de maio/2014.", "https://www.metropoles.com/brasil/policia-br/upp-10-anos-o-que-foi-feito-e-quais-promessas-ficaram-pelo-caminho", "2018-12"),
 "sim_bonus": ("nao_cumprida", "media", SR.format("ampliação do bônus do Sistema Integrado de Metas"), "", "2026-10"),
 "risp": ("nao_cumprida", "media", SR.format("construção de sedes de RISP"), "", "2026-10"),
 "cicc": ("nao_cumprida", "media", "A integração do CICC com o interior e com centrais municipais só ocorreu a partir de 2022 (serviço 190) e 2025 (Baixada); não foi localizada conclusão no período 2015–2018.", "https://www.tupi.fm/rio/pm-da-inicio-a-processo-de-integracao-do-servico-190-para-o-interior-do-estado/", "2026-10"),
 "coe": ("nao_cumprida", "media", "A licitação para implantar o COE em Ramos foi aberta em jul/2015, mas a sede só foi inaugurada em mar/2026.", "https://digital.correiodamanha.com.br/jornalcorreiodamanha/2026/03/24/005031/pdf/2403df_cmanha21.pdf", "2015-07"),
 "portal_seg": ("nao_cumprida", "media", SR.format("ampliação das bases do Portal da Segurança"), "", "2026-10"),
 "radio": ("nao_cumprida", "media", SR.format("modernização integral da radiocomunicação das polícias"), "", "2026-10"),
 "hab_policial": ("nao_cumprida", "media", SR.format("linha de crédito imobiliário especial para policiais"), "", "2026-10"),
 "salas_estab": ("nao_cumprida", "media", SR.format("ampliação do programa de salas de estabilização"), "", "2026-10"),
 "clinica_familia": ("nao_cumprida", "media", SR.format("Clínicas da Família construídas com o Estado"), "", "2026-10"),
 "uae": ("nao_cumprida", "media", SR.format("criação de Unidades Ambulatoriais Especializadas"), "", "2026-10"),
 "samu": ("nao_cumprida", "media", SR.format("implantação do Samu regional no Noroeste, no Norte e na Baixada Litorânea (há registros só do Médio Paraíba)"), "", "2026-10"),
 "riofarmes": ("nao_cumprida", "baixa", "A rede Rio Farmes tem hoje três unidades (Praça XI, Nova Iguaçu e Duque de Caxias); não há registro de seis novos polos no período.", "https://diariodorio.com/rio-farmes-tera-reforco-nos-canais-de-informacao-sobre-medicamentos/", "2026-10"),
 "rioimagem": ("nao_cumprida", "alta", "A obra do Rio Imagem II em Niterói (contrato de 2014) foi paralisada em 2016, 2017 e 2018 por falta de crédito orçamentário.", doerj("rioimagem", "2018-07-12", "Niterói"), "2018-07"),
 "imagem_ni_dc": ("nao_cumprida", "media", "Não houve financiamento de centros municipais em Nova Iguaçu e Duque de Caxias; o Rio Imagem Baixada, estadual, só abriu em 2023.", "https://digital.correiodamanha.com.br/jornalcorreiodamanha/2025/07/18/00168e/pdf/1807cmanha11.pdf", "2026-10"),
 "movel_mamo": ("parcialmente_cumprida", "baixa", "Em fev/2018 o estado contratou unidade móvel de mamografia e ultrassonografia para os municípios; não foi localizado o diagnóstico de câncer de próstata nas unidades móveis.", doerj("movel_mamo", "2018-02-26", "mamografia"), "2018-02"),
 "hosp_medio_paraiba": ("cumprida", "media", "O Hospital Regional do Médio Paraíba Zilda Arns, em Volta Redonda, foi inaugurado no fim de 2016.", "https://www.conass.org.br/?p=49708", "2016-12"),
 "onco_serrana": ("nao_cumprida", "alta", "As obras do Hospital Estadual de Oncologia da Região Serrana (contrato de 2015) pararam em 2016 e só foram retomadas em 2022.", "https://www.tupi.fm/?p=1485700", "2016-07"),
 "santa_maria": ("nao_cumprida", "media", SR.format("reforma e ampliação do Hospital Santa Maria"), "", "2026-10"),
 "eduardo_rabelo": ("nao_cumprida", "media", SR.format("polo de reabilitação no Hospital Eduardo Rabelo"), "", "2026-10"),
 "raquimedular": ("nao_cumprida", "media", SR.format("serviço de trauma raquimedular no Adão Pereira Nunes"), "", "2026-10"),
 "pahi": ("nao_cumprida", "media", "A Resolução SES 1.470/2016 reorganizou o PAHI para hospitais regionais, mas o programa seguiu restrito ao interior; não houve extensão à Região Metropolitana.", doerj("pahi", "2016-12-28", "PAHI"), "2016-12"),
 "trs": ("nao_cumprida", "media", SR.format("ampliação da terapia renal substitutiva em todas as regiões"), "", "2026-10"),
 "radioterapia": ("nao_cumprida", "media", SR.format("ampliação dos serviços estaduais de radioterapia"), "", "2026-10"),
 "dupla_escola": ("parcialmente_cumprida", "media", "Em 2015 o Dupla Escola ganhou novas parcerias e unidades (ex.: C.E. Horácio Macedo, C.E. Jornalista Maurício Azevedo, C.E. São João em Queimados), mas não há registro de cobertura de todas as regiões.", doerj("dupla_escola", "2015-08-13", "Dupla Escola"), "2015-08"),
 "apoio_escolas": ("nao_cumprida", "media", SR.format("equipes pedagógicas especiais para as escolas com piores resultados"), "", "2026-10"),
 "conexao": ("nao_cumprida", "media", SR.format("oferta de conteúdos digitais pelo Conexão Educação"), "", "2026-10"),
 "predios_alugados": ("nao_cumprida", "media", SR.format("transferência das escolas em prédios alugados ou compartilhados"), "", "2026-10"),
 "concurso_prof": ("nao_cumprida", "media", "Não houve concurso para professor efetivo entre 2015 e 2018: o último foi em 2014 e o Diário Oficial mostra só convocações de concursos anteriores.", "https://www.estrategiaconcursos.com.br/blog/concurso-seeduc-rj/", "2018-12"),
 "bu_municipal": ("nao_cumprida", "media", SR.format("integração de novas redes municipais de ônibus ao Bilhete Único"), "", "2026-10"),
 "linha4": ("cumprida", "alta", "A Linha 4 do metrô (General Osório–Jardim Oceânico) foi inaugurada em 30/07/2016.", "https://en.wikipedia.org/wiki/Jardim_Oce%C3%A2nico_Station", "2016-07"),
 "linha4_ext": ("nao_cumprida", "media", "Nenhuma das extensões começou no período; a obra da estação Gávea ficou parada por cerca de uma década e só foi retomada em 2025.", "https://tribunadosertao.com.br/rj-em-foco/2026/07/20/943028-explosoes-diarias-muita-lama-e-maquinas-a-todo-vapor-saiba-como-estao-as-obras-do-metro-da-gavea-video", "2026-07"),
 "linha3": ("nao_cumprida", "media", "As obras da Linha 3 não começaram; em jun/2015 o projeto ainda dependia de PPP sem licitação marcada.", "https://www.jb.com.br/rio/noticias/2015/06/26/amp/governo-muda-projeto-e-interligacao-de-municipios-passa-de-brt-para-linha-3-do-metro.html", "2015-06"),
 "estacoes_trem": ("parcialmente_cumprida", "media", "As seis estações olímpicas foram reformadas pela SuperVia para os Jogos de 2016 (R$ 250 milhões); não foi localizada a extensão do programa às demais estações.", "https://monitormercantil.com.br/apos-obras-estacao-de-trem-do-engenhao-e-entregue-para-os-jogos-rio-2016/", "2016-07"),
 "trens_ar": ("nao_cumprida", "baixa", "No início de 2015 havia 78 trens climatizados e previsão de mais 42; não foi localizado registro de frota 100% climatizada em 2016.", "https://revistaferroviaria.com.br/2015/02/more-two-chinese-trains-began-operating-on-rio-de-janeiro-supervia/", "2015-02"),
 "atp": ("nao_cumprida", "media", SR.format("conclusão do sistema ATP em toda a rede"), "", "2026-10"),
 "barcas": ("parcialmente_cumprida", "baixa", "As sete barcas compradas na China começaram a operar a partir de mar/2015 (a primeira foi a Pão de Açúcar); não foi localizada a conclusão das nove embarcações prometidas.", "https://www.folhavitoria.com.br/geral/novas-barcas-rio-niteroi-nao-cabem-em-pier/", "2015-03"),
 "brt": ("nao_cumprida", "media", SR.format("implantação de corredores metropolitanos de BRT (em 2016 o tema aparece só como possibilidade em estudo)"), "", "2026-10"),
 "bonde": ("parcialmente_cumprida", "baixa", "A reestruturação do bonde seguiu em 2015 e parte da linha voltou a operar, mas os ramais Silvestre e Paula Mattos só foram reabertos em 2024–2026 e não há registro dos 14 novos bondes.", "https://www.tupi.fm/?p=2395141", "2015-11"),
 "telef_rocinha": ("nao_cumprida", "media", "As obras do PAC 2 na Rocinha, que incluíam o teleférico, ficaram paralisadas desde fev/2015 e o teleférico não foi construído.", "https://rioonwatch.org/?p=28887", "2016-06"),
 "acu": ("nao_cumprida", "media", SR.format("implantação de acessos rodoviários e ferroviários ao Porto do Açu"), "", "2026-10"),
 "furado": ("nao_cumprida", "media", "As obras públicas do complexo da Barra do Furado pararam com a recessão de 2014–2016; a retomada só foi anunciada em 2026.", "https://diariodorio.com/porto-e-estaleiro-no-norte-do-rj-voltam-ao-radar-com-investimento-de-r-850-milhoes/", "2026-03"),
 "ef118": ("nao_cumprida", "media", "A ferrovia não foi construída; em ago/2018 havia apenas cooperação para a modelagem da concessão federal.", doerj("ef118", "2018-08-02", "118"), "2018-08"),
 "pac2": ("nao_cumprida", "media", "O PAC 2 da Rocinha ficou paralisado desde fev/2015 e os serviços do PAC 2 no Jacarezinho foram suspensos em 2016 por falta de crédito orçamentário.", doerj("pac2", "2016-08-16", "Jacarezinho"), "2016-08"),
 "reurb": ("nao_cumprida", "media", SR.format("obras de urbanização em Mangueira, Salgueiro, Formiga e Borel"), "", "2026-10"),
 "mcmv": ("nao_cumprida", "media", SR.format("balanço de 190 mil famílias atendidas pelo Minha Casa Minha Vida com apoio do Estado"), "", "2026-10"),
 "vila_idade": ("nao_cumprida", "media", "No Diário Oficial de 2015–2018 aparecem só a manutenção das Vilas da Melhor Idade existentes; não foi localizada nova unidade.", "", "2026-10"),
 "arco": ("nao_cumprida", "media", "O trecho federal (BR-493, Magé–Manilha) não foi concluído em 2016; as obras ficaram suspensas a partir de 2018 e a duplicação só avançou após 2022.", "https://monitormercantil.com.br/tarcisio-inclui-arco-metropolitano-na-concessao-da-br-116/", "2018-12"),
 "vialight": ("nao_cumprida", "media", "A ligação da Via Light à Avenida Brasil não foi concluída; em 2015 o estado advertiu o consórcio da obra por descumprimento do contrato.", doerj("vialight", "2015-08-10", "Via Light"), "2015-08"),
 "transbaixada": ("nao_cumprida", "media", "A Transbaixada não saiu do papel; em 2026 ainda era estudada para concessão.", "https://diariodorio.com/claudio-castro-pretende-levar-adiante-construcao-da-transbaixada/", "2026-10"),
 "transv_oeste": ("nao_cumprida", "media", SR.format("obras da Rodovia Transversal Oeste ou do Anel Viário de Campos Elíseos"), "", "2026-10"),
 "corredores": ("nao_cumprida", "media", SR.format("obras dos corredores Transfluminense, Transnoroeste, Transnorte, Transul e Anel Norte-Sul"), "", "2026-10"),
 "regin": ("nao_cumprida", "media", "Não foi localizada adesão de todos os municípios ao Regin no período; a Jucerja só anunciou os 92 municípios no alvará automatizado em 2024.", "https://www.tupi.fm/?p=1914987", "2026-10"),
 "banda_larga": ("nao_cumprida", "media", SR.format("licitação da PPP da Rede de Banda Larga RJ"), "", "2026-10"),
 "datacenter": ("nao_cumprida", "media", SR.format("construção do Data Center do Governo"), "", "2026-10"),
 "telemedicina": ("nao_cumprida", "media", SR.format("implantação de telemedicina em todo o estado"), "", "2026-10"),
 "acordo_result": ("nao_cumprida", "media", SR.format("Acordos de Resultados com consórcios intermunicipais"), "", "2026-10"),
 "poupatempo": ("nao_cumprida", "media", SR.format("abertura de unidades do Rio Poupa Tempo na Rocinha e em Madureira"), "", "2026-10"),
 "poupatempo_virtual": ("nao_cumprida", "media", SR.format("criação do Rio Poupa Tempo Virtual"), "", "2026-10"),
 "concurso_carreiras": ("nao_cumprida", "media", SR.format("novos concursos para as carreiras de Estado"), "", "2026-10"),
 "gespi": ("nao_cumprida", "media", SR.format("ampliação do Gespi"), "", "2026-10"),
 "pronatec_rsm": ("nao_cumprida", "media", SR.format("bolsas do Pronatec ou microcrédito voltados às famílias do Rio Sem Miséria"), "", "2026-10"),
 "lgbt": ("nao_cumprida", "baixa", "Em 2015 há repasses para estruturar os Centros de Cidadania LGBT existentes, mas não foi localizado centro novo no período; em 2016–2017 os centros enfrentaram falta de recursos.", "https://istoedinheiro.com.br/governo-do-rj-pagara-salarios-de-funcionarios-de-programa-de-combate-a-homofobia", "2017-05"),
 "esgoto80": ("nao_cumprida", "media", "A meta de 80% de esgoto coletado e tratado em 2018 não foi atingida, segundo ex-dirigente da Cedae.", "https://www.nbcnewyork.com/news/national-international/rio-sewage-may-not-be-treated-until-2035/2030863/", "2018-12"),
 "etas": ("nao_cumprida", "media", "A ETA Novo Guandu teve financiamento contratado em 2016 e licitação do projeto executivo em 2017, sem início de obra; não foi localizada a ETA Saracuruna.", doerj("etas", "2017-04-11", "Novo Guandu"), "2017-04"),
 "redes_agua": ("nao_cumprida", "media", SR.format("balanço de 1.200 km de redes de água e 360 mil ligações"), "", "2026-10"),
 "lagunar": ("nao_cumprida", "media", "Os trabalhos de despoluição do complexo lagunar estavam estagnados em 2016, após intervenções do Ministério Público e com a crise fiscal.", "https://www.lance.com.br/rio2016/esgoto-lama-ate-moveis-degradam-aguas-vizinhas-coracao-rio-2016.html", "2016-08"),
 "sena_limpa": ("nao_cumprida", "baixa", "No Diário Oficial aparece só o aditivo de 2015 ao convênio da primeira fase do Sena Limpa; não foi localizada a segunda fase.", doerj("sena_limpa", "2015-07-23", "Sena Limpa"), "2015-07"),
 "zona_oeste_agua": ("nao_cumprida", "baixa", "As obras de ampliação do abastecimento da Zona Oeste (Santa Cruz, Guaratiba e outros) foram contratadas em 2014–2015, mas não foi localizado registro de conclusão até 2018.", doerj("zona_oeste_agua", "2015-05-13", "Zona Oeste"), "2015-05"),
 "lixoes": ("nao_cumprida", "baixa", SR.format("erradicação de todos os lixões do estado (em 2014 eram 62 dos 92 municípios com destinação adequada)"), "", "2026-10"),
 "metano": ("nao_cumprida", "media", SR.format("usinas estaduais de aproveitamento do gás de lixo"), "", "2026-10"),
 "taxi_eletrico": ("nao_cumprida", "media", SR.format("frota de táxis elétricos"), "", "2026-10"),
 "bib_parque": ("nao_cumprida", "alta", "Nenhuma Biblioteca-Parque nova foi aberta; as existentes fecharam em dez/2016 com a crise e só reabriram em parte em 2018.", "https://agenciabrasil.ebc.com.br/cultura/noticia/2016-12/bibliotecas-parque-fecham-no-rio-secretaria-promete-retorno-rapido", "2016-12"),
 "rio_criativo": ("cumprida", "media", "Em nov/2015 o estado contratou a gestão da incubadora e dos núcleos de conhecimento e negócios do Rio Criativo e lançou o LAB Rio Criativo.", doerj("rio_criativo", "2015-11-25", "Rio Criativo"), "2015-11"),
 "mis": ("nao_cumprida", "alta", "A obra do MIS em Copacabana ficou paralisada entre 2016 e 2021; o museu só abriu em mai/2026.", "https://www.correiodamanha.com.br/cultura/exposicao/2026/05/283244-enfim-o-mis.html", "2026-05"),
 "sist_cultura": ("cumprida", "alta", "A Lei 7.035, de 07/07/2015, instituiu o Sistema Estadual de Cultura.", doerj("sist_cultura", "2015-07-08", "Sistema Estadual de Cultura"), "2015-07"),
 "esporte_rj": ("nao_cumprida", "media", SR.format("300 mil pessoas atendidas nos núcleos do Esporte RJ"), "", "2026-10"),
}
assert set(C) == {p[0] for p in P}, set(C) ^ {p[0] for p in P}
campos = ["id", "mandato_id", "paragrafo", "trecho_literal", "promessa", "area", "tipo", "depende_legislativo",
          "outro_ente", "status", "confianca", "evidencia", "fonte_url", "data_evidencia"]
with open(RAIZ / "data" / "promessas" / "pezao_rj_2014.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(campos)
    for n, (k, sec, tre, pro, area, tipo, leg, ente) in enumerate(P, 1):
        w.writerow([f"{MID}-{n:02d}", MID, sec, tre, pro, area, tipo, leg, ente, *C[k]])
print(len(P))

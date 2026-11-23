# Classificação do censo de ACM Neto (prefeitura de Salvador, 2012). Mandato 2013-2016 encerrado; avaliado até
# 31/12/2016 (entregas de 2017 em diante não contam). Fontes: Relatórios de Atividades anuais 2013-2016 da Casa Civil
# (por eixo, inclusive o balanço "Realizações 2013-2016"; cópia em ssa_relatorios_2013_2016/), o Diário Oficial do
# Município (scripts/busca_ssa.py; resultados em acmneto_ssa_2012.json) e a imprensa.
# Como o Diário Oficial foi consultado, "sem registro" = não cumprida com confiança média.
SEM = "Busca no Diário Oficial do Município (2013-2016), nos Relatórios de Atividades anuais 2013-2016 da Prefeitura e na imprensa não localizou "
U = "https://casacivil.salvador.ba.gov.br/wp-content/uploads/2024/11/"
INST = U + "2-Relatoriodeatividades-Institucional.pdf"
EDU = U + "3-Relatoriodeatividades-Educacao.pdf"
EDU15 = U + "2-Relatorio-de-atividades-EDUCACAO.pdf"
SAU = U + "4-Relatoriodeatividades-Saude.pdf"
JUS = U + "5-Relatoriodeatividades-JusticaSocial.pdf"
NEG = U + "6-Relatoriodeatividades-Negocios.pdf"
MOB = U + "7-Relatoriodeatividades-Mobilidade.pdf"
MOB14 = U + "7-RELATORIO-ATIVIDADES-MOBILIDADE.pdf"
ORD = U + "8-Relatoriodeatividades-OrdemPublica.pdf"
GES = U + "10-Relatoriodeatividades-Gestao.pdf"
GES14 = U + "11-RELATORIO-ATIVIDADES-GESTAO.pdf"


def S(txt, url="", data="2026-11"):
    return ("nao_cumprida", "media", SEM + txt, url, data)


def C(txt, url, data="2016-12", conf="alta"):
    return ("cumprida", conf, txt, url, data)


def P_(txt, url, data="2016-12", conf="media"):
    return ("parcialmente_cumprida", conf, txt, url, data)


def NC(txt, url, data="2016-12", conf="media"):
    return ("nao_cumprida", conf, txt, url, data)


D = {
    1: C("Com o nome de Prefeituras-Bairro: as dez unidades previstas foram implantadas até 2016 (a décima, em Valéria, abriu em 2016) e fizeram 884 mil atendimentos naquele ano.", INST),
    2: C("No primeiro dia do mandato o prefeito assinou decretos de austeridade que aplicaram a Lei da Ficha Limpa à ocupação de cargos municipais; no discurso de posse, ser ficha limpa foi apresentado como pré-requisito para integrar a gestão.", "https://dom.salvador.ba.gov.br/diario/arquivo/01KYGSWFZDA25Y66DHPZGXC5K7", "2013-01", "media"),
    3: S("a criação de um conselho permanente de prefeitos da Região Metropolitana."),
    4: C("Com outro nome: o programa Ouvindo Nosso Bairro (2015) fez consultas nos bairros para a população eleger as obras e ações prioritárias, executadas depois pelo Salvador Bairro a Bairro.", INST, conf="media"),
    5: C("Entre 2013 e 2016 foram construídas, reconstruídas e reformadas 50 unidades de educação infantil, chegando a 32,1 mil vagas, cerca de 90% a mais que em 2012.", EDU),
    6: P_("Com outro nome: o projeto dos Centros de Educação Integral foi reformulado em 2016 como Escolab, e só a unidade do Subúrbio estava em funcionamento no fim do mandato.", EDU),
    7: C("A Secretaria de Educação elaborou em 2015 o projeto pedagógico Nossa Rede, com conteúdos por disciplina para a rede municipal, e em 2016 fez capacitações para o seu uso.", EDU, conf="media"),
    8: C("O Plano de Carreira e Remuneração dos Servidores da Educação foi sancionado em dez/2014 (Lei 8.722/2014) e regulamentado em jun/2015, com regras de progressão funcional.", EDU15, "2015-06"),
    9: S("um programa de implantação de centros de informática com banda larga nas escolas municipais; só há registro de conectividade de alta velocidade na Escolab do Subúrbio."),
    10: S("a municipalização das séries finais do Ensino Fundamental; os relatórios só registram a cobrança de repasses de convênios antigos de municipalização."),
    11: S("a criação do Gabinete Municipal de Gestão Integrada."),
    12: P_("A Guarda foi reorganizada (Lei 9.070/2016), reequipada e capacitada, e ganhou um Grupo Especial Ambiental para os parques; não há registro de aumento do efetivo nem de grupo para áreas turísticas.", ORD),
    13: C("O projeto Nova Codesal reestruturou a Defesa Civil (Lei 8.969/2016, com autonomia e poder de polícia), alterou o Conselho Municipal de Defesa Civil e criou núcleos comunitários; o Programa de Voluntariado foi instituído em 2015.", GES),
    14: S("um programa de combate à violência juvenil com aulas nas escolas."),
    15: P_("O videomonitoramento da Prefeitura chegou a 41 câmeras na Infovia Municipal, mais as usadas no Carnaval; não chega a ser um programa extenso.", GES14, "2014-12", "baixa"),
    16: S("um Programa Municipal de Controle e Redução da Violência."),
    17: S("um Observatório da Violência para coleta de informações e planejamento; os observatórios que existiam eram o da Discriminação Racial e LGBT (no Carnaval) e o da Sustentabilidade."),
    18: P_("A cobertura da Atenção Básica subiu de 18,6% em 2012 para 61% em 2016 (dado preliminar), longe dos 100% prometidos.", SAU),
    19: P_("Quatro Multicentros de Saúde foram inaugurados entre 2014 e 2016, mas não um em cada um dos 12 distritos sanitários.", SAU, conf="alta"),
    20: S("a criação de centrais de regulação em cada distrito sanitário; a regulação seguiu centralizada na Central Municipal de Regulação."),
    21: NC("A maternidade municipal não foi construída no mandato; a primeira maternidade municipal de Salvador só foi inaugurada em 2026, na Federação, e a maternidade do Subúrbio (2021) é do Governo do Estado.", "https://www.bahianoticias.com.br/noticia/235820-prefeitura-estuda-construir-maternidade-mas-esbarra-na-limitacao-orcamentaria", "2019", "alta"),
    22: S("um plano de cargos próprio da Saúde; os relatórios registram só a reestruturação do Plano de Cargos e Vencimentos geral dos servidores e o plano da Educação."),
    23: C("O Programa Morar Melhor, de reforma de moradias da população de baixa renda, foi lançado em jun/2015; 18 mil imóveis foram cadastrados e as obras começaram em out/2015.", JUS),
    24: S("a implantação do Conselho Municipal de Transporte e dos Comitês Regionais de Mobilidade."),
    25: P_("Foram implantadas vias e faixas exclusivas de ônibus na Paulo VI (2013), na Vasco da Gama e na ACM, muito abaixo dos 40 km; o BRT Lapa-Iguatemi só teve o financiamento e a licitação no mandato.", MOB, conf="baixa"),
    26: C("Segundo a Transalvador, as mortes no trânsito caíram mais de 50% em relação a 2010 (266); foram 247 em 2012, 182 em 2015 e 83 até out/2016.", MOB, conf="baixa"),
    27: C("Foram construídas passarelas nos corredores citados, como a do Sumaré (Tancredo Neves), Detran, Imbuí e Mussurunga (Paralela), além de outras recuperadas.", MOB14, "2014-12", "media"),
    28: P_("Pelo programa Eu Curto Meu Passeio, 105,76 km de calçadas foram regularizados até out/2016, pouco mais da metade dos 200 km.", MOB),
    29: S("o Programa Travessia Escolar."),
    30: P_("A Transalvador implantou em out/2015 o Núcleo de Operação Assistida, com 400 smartphones para gerir as operações, mas a central de semáforos com monitoramento em tempo real ainda estava em implantação no fim de 2016.", MOB, conf="baixa"),
    31: P_("O projeto de semáforos inteligentes (36 interseções) estava em implantação: até o fim de 2016 só dois controladores tinham sido instalados, nos Barris, com conclusão prevista para mar/2017.", MOB),
    32: S("a instalação de painéis de mensagem variável fixos; os registros são de painéis exigidos de empresas em eventos que interferem na via."),
    33: S("o controle eletrônico da Zona Azul; no mandato as vagas passaram de 4.559 para 10.002, ainda com o sistema de talões."),
    34: C("Os planos inclinados Pilar (2015), Liberdade-Calçada (2015) e Gonçalves (jun/2016) foram reformados e reabertos, com mais de R$ 9 milhões investidos nos ascensores.", MOB),
    35: C("Foram 145 km de ciclovias, ciclofaixas e ciclorrotas implantados no mandato, acima dos 45 km prometidos.", MOB),
    36: C("A orla foi requalificada em vários trechos, como Barra (2014-2015), Rio Vermelho, Jardim de Alah e Itapuã/Piatã.", INST),
    37: NC("No fim de 2016 os instrumentos normativos da Política de Economia Criativa ainda estavam em elaboração; a política não foi implementada no mandato.", NEG),
    38: C("O Parque da Cidade foi entregue totalmente requalificado em jun/2016, e outros parques e lagoas foram requalificados; o PDDU de 2016 prevê 16 novos parques.", MOB, conf="media"),
    39: P_("A Prefeitura ampliou a Infovia e instalou pontos de internet pública, mas o projeto da Cidade Digital ficou na fase de captação de recursos.", GES, conf="baixa"),
    40: C("O Programa de Coleta Seletiva foi lançado em ago/2015, com 150 Pontos de Entrega Voluntária, e a Limpurb deu apoio a duas redes e seis cooperativas de catadores.", MOB, conf="media"),
    41: S("uma estrutura ligada ao gabinete do prefeito para coordenar as ações para grupos vulneráveis em todas as secretarias."),
    42: S("a Agenda da Família nem a visita a todas as famílias vulneráveis do CadÚnico."),
    43: S("o Mapa da Exclusão Social."),
    44: C("A rede passou de 26 CRAS em 2015 para 28 em 2016.", JUS, conf="media"),
    45: C("De 2013 a 2016 o número de CREAS em funcionamento subiu de dois para sete.", JUS),
}
AJUSTES = {}

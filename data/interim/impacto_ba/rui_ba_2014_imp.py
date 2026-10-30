# Impacto fiscal das promessas de Rui Costa (governo da Bahia, 2014) no orçamento do Estado da Bahia.
# Base: 2014 (ano anterior ao mandato). Mandato completo: 2015-2018 (ano de referência 2018).
# Fonte oficial: despesa empenhada por ação, dados abertos do Estado (FIPLAN) — ver ba_comum.py.
import csv
from pathlib import Path
from ba_comum import *

MID = "rui_ba_2014"
P = list(csv.DictReader(open(Path(__file__).resolve().parents[2] / "promessas" / f"{MID}.csv", encoding="utf-8")))
B, F = 2014, 2018

CATS = {1: SID, 9: SID, 12: SID, 25: SID, 26: SID, 42: RR, 47: SID, 52: SID, 54: SID, 58: SID, 71: SID, 72: SID,
        73: SID, 74: SID, 76: SID, 77: SID, 79: SID, 87: SID, 89: SIP, 132: SID, 134: SID, 137: SID, 139: SID,
        140: SIP, 141: SID, 144: SID, 154: SID, 157: SID, 160: SID, 161: SID}
I = padrao(P, CATS)

SVP_AGUA = "Incluída no valor da promessa sobre os sistemas de abastecimento de água listados (ações gerais de sistemas de abastecimento e adutoras)."
I.update({
    2: d("A educação integral não tinha ação própria relevante no período (R$ 7 milhões em 2014 na ação 2698, quase nada depois); o custo das escolas em tempo integral fica nas ações gerais de pessoal e funcionamento. Sem valor.", DA, "baixa"),
    3: v(["3904", "4449", "3906", "5432", "6992", "7860"], B, F, "Ações do TOPA (bolsas de alfabetizadores, alimentação, material didático e diagnóstico) e de alfabetização de jovens e adultos."),
    16: v(["7529"], B, F, "Apoio ao Programa de Permanência Estudantil na Educação Superior (Mais Futuro), que começou a pagar em 2017."),
    19: v(["4178"], B, F, "Gerenciamento das parcerias público-privadas em saúde: inclui a PPP de diagnóstico por imagem (desde nov/2015), mas também o Hospital do Subúrbio e o novo Couto Maia, que não dá para separar.", "baixa"),
    21: v(["3997", "3996", "5607"], B, F, "Construção, ampliação e aparelhamento de unidades de saúde (ações gerais, que incluem os hospitais entregues em Seabra e Ilhéus).", "baixa", rec="nao"),
    39: d("A construção e a ampliação de unidades prisionais (ações 5401 e 5428) somaram R$ 23 milhões em 2016-2017, sem gasto em 2014 nem em 2018; o custeio das novas vagas está na ação geral de funcionamento das unidades prisionais. Sem valor a mais no último ano.", DA, "baixa"),
    48: v(["7496", "1177", "7671", "7673", "7494"], B, F, "Requalificação de vias e imóveis, revitalização urbanística, fiscalização de obras e preservação do Centro Antigo de Salvador.", rec="nao"),
    51: v(["7955"], B, F, "Requalificação do Complexo Teatro Castro Alves.", rec="nao"),
    59: v(["3564", "4028"], B, F, "Implantação da infraestrutura do metrô (aportes à concessionária na obra das Linhas 1 e 2) e gerenciamento da parceria público-privada; o Estado não teve gasto com o metrô em 2014.", rec="nao"),
    61: v(["7224", "7238"], B, F, "Implantação dos Corredores de Transporte Transversais I (Lobato–Pirajá / Linha Azul) e II (Av. Orlando Gomes / Linha Vermelha).", rec="nao"),
    62: d("A Via Barradão foi paga em ação geral de infraestrutura viária urbana, junto com outras obras; sem valor próprio.", SVP, "baixa"),
    88: v(["6672", "7721", "6584"], B, F, "Implantação e funcionamento das Unidades de Inclusão Socioprodutiva (Vida Melhor urbano).", "baixa"),
    94: v(["7901"], B, F, "Ação geral de construção de barragens (inclui a Barragem do Rio Colônia, inaugurada em 2018).", "baixa", rec="nao"),
    95: d(SVP_AGUA, SVP, "baixa"),
    96: d("A construção de cisternas pelo Estado (ação 5136) teve R$ 42 milhões em 2014 e nenhum gasto de 2015 a 2018; as cisternas do período vieram sobretudo de programas federais. Sem valor.", DA, "baixa"),
    101: v(["7887", "1240", "5743", "1709", "3826"], B, F, "Implantação e ampliação de sistemas de abastecimento de água (simplificados, convencionais e integrados).", "baixa", rec="nao"),
    102: v(["1243", "1254"], B, F, "Implantação e ampliação de sistemas de esgotamento sanitário pelo Estado (as ligações da Embasa, empresa estatal, ficam fora do orçamento).", "baixa", rec="nao"),
    106: d("Os perímetros do Salitre e do Baixio de Irecê são obras federais (Codevasf); sem efeito direto no orçamento do Estado.", SID),
    110: d("A Ferrovia de Integração Oeste-Leste é obra federal (Valec, depois concessão); sem efeito direto no orçamento do Estado.", SID),
    115: v(["2868", "7911", "3980"], B, F, "Conservação da malha estadual e implantação e recuperação de acessos rodoviários. Subestima o custo, porque as pavimentações e restaurações de trechos específicos têm ações próprias por rodovia, que não foram somadas.", "baixa"),
    138: v(["6943", "5230", "4055", "1065"], B, F, "Assistência técnica e extensão rural (Ater) aos agricultores familiares, pela Bahiater e por projetos com entidades.", "baixa"),
})

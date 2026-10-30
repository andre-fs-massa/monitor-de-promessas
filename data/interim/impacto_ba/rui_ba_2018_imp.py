# Impacto fiscal das promessas de Rui Costa (governo da Bahia, 2018) no orçamento do Estado da Bahia.
# Base: 2018 (ano anterior ao mandato). Mandato completo: 2019-2022 (ano de referência 2022).
# Fonte oficial: despesa empenhada por ação, dados abertos do Estado (FIPLAN) — ver ba_comum.py.
import csv
from pathlib import Path
from ba_comum import *

MID = "rui_ba_2018"
P = list(csv.DictReader(open(Path(__file__).resolve().parents[2] / "promessas" / f"{MID}.csv", encoding="utf-8")))
B, F = 2018, 2022

CATS = {21: SID, 38: SID, 85: SID, 106: SID, 107: SID, 109: SID, 125: SID, 158: SID, 159: SID, 167: SID, 168: SID,
        170: SID, 171: SID, 173: SID, 190: SID, 191: SID, 192: SID, 193: SID, 194: SID, 198: SID}
I = padrao(P, CATS)

SVP_ESC = "Incluída no valor da promessa de construir 60 novas escolas (ações gerais de construção e ampliação de escolas)."
SVP_HOSP = "Incluída no valor da promessa de reformar ou ampliar 11 hospitais (ações gerais de construção, ampliação e aparelhamento de unidades de saúde)."
SVP_AGUA = "Incluída no valor da promessa de implantar ou ampliar 25 sistemas integrados (ações gerais de sistemas de abastecimento de água e adutoras)."
I.update({
    10: d(SVP_ESC, SVP, "baixa"),
    28: v(["7527", "7531"], B, F, "Construção e ampliação de unidades escolares da educação básica (inclui as escolas novas, os complexos integrados e as quadras; o grosso do gasto foi em 2022).", "baixa", rec="nao"),
    29: d(SVP_ESC, SVP, "baixa"),
    45: v(["3997", "3996", "5607"], B, F, "Construção, ampliação e aparelhamento de unidades de saúde (ações gerais, que incluem os hospitais e maternidades prometidos).", "baixa", rec="nao"),
    47: d(SVP_HOSP, SVP, "baixa"), 48: d(SVP_HOSP, SVP, "baixa"), 49: d(SVP_HOSP, SVP, "baixa"),
    52: d(SVP_HOSP, SVP, "baixa"), 54: d(SVP_HOSP, SVP, "baixa"), 57: d(SVP_HOSP, SVP, "baixa"),
    58: d(SVP_HOSP, SVP, "baixa"), 60: d(SVP_HOSP, SVP, "baixa"),
    62: v(["4873"], B, F, "Apoio ao funcionamento dos consórcios interfederativos de saúde, que administram as policlínicas regionais (custeio estadual). A construção e o aparelhamento das policlínicas (ações 7511, 7735 e 7938) foram maiores em 2018 do que em 2022 e não entram."),
    79: v(["5359"], B, F, "Implantação do Vídeo-Polícia (videomonitoramento com reconhecimento facial e de placas)."),
    91: v(["7529", "7809", "4131", "3051", "3050"], B, F, "Mais Futuro (permanência estudantil), Primeiro Emprego (iniciação profissional de egressos) e Partiu Estágio.", "baixa"),
    96: d("A construção de unidade socioeducativa teve R$ 20 milhões em 2019 (ação 1168), mas o gasto de 2022 ficou abaixo de 2018; sem valor a mais.", DA, "baixa"),
    123: v(["7224"], B, F, "Implantação do Corredor Transversal I (Lobato–Pirajá / Linha Azul).", rec="nao"),
    124: v(["7238"], B, F, "Implantação do Corredor Transversal II (Av. Orlando Gomes / Linha Vermelha).", rec="nao"),
    127: v(["7911", "2868"], B, F, "Recuperação de acessos rodoviários e conservação da malha estadual. Subestima o custo, porque as pavimentações e restaurações de trechos específicos têm ações próprias por rodovia, que não foram somadas.", "baixa"),
    136: v(["3979"], B, F, "Ação geral de construção de pontes (inclui a Ponte Ilhéus–Pontal e outras).", "baixa", rec="nao"),
    137: d("A ponte Xique-Xique–Barra foi feita por parceria público-privada; o valor está incluído na ação geral de construção de pontes ou na contraprestação, não localizada. Sem valor próprio.", SVP, "baixa"),
    141: v(["5340"], B, F, "Implantação do Porto Sul (acessos e desapropriações a cargo do Estado; o porto é privado).", rec="nao"),
    143: v(["6283", "5244", "5347"], B, F, "Funcionamento e requalificação do Parque Tecnológico da Bahia."),
    180: d(SVP_AGUA, SVP, "baixa"),
    181: v(["5743", "3057", "1240", "1709"], B, F, "Implantação e ampliação de sistemas de abastecimento de água e adutoras (ações gerais, que incluem os sistemas integrados prometidos).", "baixa", rec="nao"),
    184: d(SVP_AGUA, SVP, "baixa"),
    187: v(["1243", "1254"], B, F, "Implantação e ampliação de sistemas de esgotamento sanitário pelo Estado (as obras da Embasa, empresa estatal, ficam fora do orçamento).", "baixa", rec="nao"),
    189: v(["7466"], B, F, "Implantação de sistemas de manejo de águas pluviais (macrodrenagem) em áreas urbanas.", rec="nao"),
})

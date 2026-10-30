# Impacto fiscal das promessas de Jerônimo Rodrigues (governo da Bahia, 2022) no orçamento do Estado da Bahia.
# Base: 2022 (ano anterior ao mandato). Mandato em curso: anos completos 2023-2025 (ano de referência 2025).
# Fonte oficial: despesa empenhada por ação, dados abertos do Estado (FIPLAN) — ver ba_comum.py.
import csv
from pathlib import Path
from ba_comum import *

MID = "jeronimo_ba_2022"
P = list(csv.DictReader(open(Path(__file__).resolve().parents[2] / "promessas" / f"{MID}.csv", encoding="utf-8")))
B, F = 2022, 2025

CATS = {1: RR, 3: NEU, 4: RR, 5: SID, 20: SID, 22: SID, 23: SIP, 25: SID, 26: SID, 29: SID, 32: SID, 34: SID,
        35: SID, 38: SID, 40: SID, 65: SID, 73: SID, 114: SID, 119: SID, 131: SID, 139: SID, 146: SID, 157: RA,
        162: SID, 169: SIP, 178: SID, 182: SID, 185: SID, 186: SID, 191: SID, 193: SID, 194: SID, 196: SID,
        200: SID, 201: SID, 202: SID, 207: SID, 208: SID, 214: SID, 215: SID}
I = padrao(P, CATS)

I.update({
    4: d("A isenção de IPVA para carros 100% elétricos de até R$ 300 mil (Lei 14.638/2023) reduz a receita; a renúncia estimada não foi localizada. Sem valor.", RR, "baixa"),
    9: v(["5578"], B, F, "Ponte Salvador–Itaparica: só o gerenciamento do projeto, porque a obra é feita por parceria público-privada. A contraprestação da PPP (ação 3410) começou em 2026, ano ainda incompleto (R$ 160 milhões empenhados até out/2026), e fica fora do acumulado.", "baixa"),
    13: v(["7911", "2868"], B, F, "Recuperação de acessos rodoviários e conservação da malha estadual. Subestima o custo, porque as pavimentações e restaurações de trechos específicos têm ações próprias por rodovia, que não foram somadas.", "baixa"),
    14: v(["7420"], B, F, "Ampliação da infraestrutura do metrô (novas linhas e estações).", rec="nao"),
    15: d("A nova rodoviária de Salvador foi feita por concessão, com investimento privado; a contrapartida do Estado não foi localizada. Sem valor.", DA, "baixa"),
    16: v(["7421"], B, F, "Implantação do VLT do Subúrbio (obra em andamento, gasto de investimento).", rec="nao"),
    19: v(["5220"], B, F, "Contenção de encostas em áreas de risco."),
    30: v(["1765"], B, F, "Implantação de sistemas de energia renovável em prédios e equipamentos públicos.", "baixa"),
    43: v(["7894"], B, F, "Perfuração de poços."),
    47: v(["7887"], B, F, "Implantação de sistemas simplificados de abastecimento de água."),
    51: d("Incluída no valor da promessa sobre as barragens do Catolé e de Baraúnas (ação geral de construção de barragens).", SVP, "baixa"),
    52: v(["7901"], B, F, "Ação geral de construção de barragens, que inclui Catolé, Baraúnas e outras obras.", "baixa", rec="nao"),
    53: d("Incluída no valor da promessa sobre as barragens do Catolé e de Baraúnas (ação geral de construção de barragens).", SVP, "baixa"),
    57: d("O Bahia Sem Fome reúne ações de várias secretarias (cozinhas comunitárias, compra e distribuição de alimentos) e não tem ação orçamentária própria; o governo divulgou R$ 5 bilhões somados até jun/2026, número que inclui programas que já existiam. Sem valor.", DA, "baixa"),
    58: d("Incluída na promessa de implantar o Bahia Sem Fome.", SVP, "baixa"),
    64: v(["6943", "5230"], B, F, "Assistência técnica e extensão rural (Ater) aos agricultores familiares, inclusive a do semiárido.", "baixa"),
    71: v(["7125", "7130"], B, F, "Projeto de desenvolvimento rural sustentável com o Banco Mundial (Bahia Mais Produtiva). A ação é a mesma do projeto anterior (Bahia Produtiva), que gastou mais em 2022.", "baixa"),
    100: v(["4172"], B, F, "Incentivo financeiro estadual a unidades hospitalares municipais."),
    102: v(["4873"], B, F, "Apoio ao funcionamento dos consórcios interfederativos de saúde, que administram as policlínicas."),
    112: v(["6991"], B, F, "Gestão das ações de educação integral. Subestima o custo, porque o salário dos professores das horas a mais fica nas ações gerais de pessoal."),
    115: v(["3101"], B, F, "Promoção da conectividade ao estudante e ao profissional da educação (tablets e chips).", "baixa"),
    117: v(["3236", "5254"], B, F, "Instalação e melhoria da rede de internet nas escolas estaduais."),
    158: d("Incluída na promessa de expandir o Vídeo-Polícia (câmeras e monitoramento).", SVP, "baixa"),
    164: v(["5357"], B, F, "Implantação do serviço de comunicação crítica móvel (radiocomunicação digital)."),
    165: v(["5359"], B, F, "Expansão do Vídeo-Polícia (câmeras e reconhecimento facial)."),
    187: v(["5215"], B, F, "Apoio à realização do Programa Ouro Negro."),
    210: d("Concursos aumentam a despesa com pessoal, que fica nas ações gerais de pessoal de cada órgão; sem valor.", DA, "baixa"),
})

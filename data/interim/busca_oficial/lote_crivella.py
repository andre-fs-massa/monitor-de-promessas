"""Lote de buscas no DO Rio para o censo do Crivella 2016 (mandato 2017-2020).

python -I data/interim/busca_oficial/lote_crivella.py [chave ...]   -> grava/atualiza crivella_rio_2016.json
"""
import json, runpy, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
dorio = runpy.run_path(str(AQUI.parents[2] / "scripts" / "busca_rj.py"))["dorio"]
SAIDA = AQUI / "crivella_rio_2016.json"

# chave: [(frase exata, palavras que a página também precisa conter), ...]
Q = {
 "zona_franca": [('"Zona Franca Social"', "")],
 "cimento_social": [('"Cimento Social"', "")],
 "saude_250mi": [('"Fundo Municipal de Saúde"', "suplementa;crédito"), ('"reestruturação"', "UPA;emergência")],
 "clinicas_especialistas": [('"Clínica de Especialistas"', ""), ('"Clínicas de Especialidades"', ""), ('"Policlínica"', "inaugura")],
 "cf_ginecologistas": [('"ginecologista"', "Clínica da Família;contrata"), ('"pediatra"', "Clínica da Família;contrata")],
 "cers": [('"Coordenação de Emergência Regional"', ""), ('"CER"', "Rocha Faria"), ('"CER"', "Salgado Filho"), ('"CER"', "Albert Schweitzer")],
 "upas_estaduais": [('"UPA"', "municipalização"), ('"Unidades de Pronto Atendimento"', "Estado;gestão;transferência")],
 "mutirao_leitos": [('"mutirão"', "cirurgias"), ('"novos leitos"', "hospital")],
 "pccs_saude": [('"plano de cargos"', "saúde;meritocracia"), ('"plano de cargos, carreiras"', "Saúde")],
 "auditoria_oss": [('"auditoria"', "Organizações Sociais;saúde"), ('"Organização Social"', "auditoria")],
 "cegonha": [('"Cegonha Carioca"', "")],
 "maternidade_ilha": [('"Nossa Senhora do Loreto"', "maternidade"), ('"maternidade"', "Ilha do Governador")],
 "creches_ppp": [('"Espaço de Desenvolvimento Infantil"', "parceria público-privada"), ('"PPP"', "creche"), ('"novas vagas"', "creche")],
 "integral_50": [('"turno único"', "ampliação"), ('"horário integral"', "anos iniciais")],
 "qualif_professores": [('"formação continuada"', "professores;programa"), ('"Escola de Formação do Professor Carioca"', "")],
 "custeio_escolas": [('"SDP"', "escolas;custeio"), ('"Sistema Descentralizado de Pagamento"', "unidades escolares")],
 "sem_novas_escolas": [('"construção de escola"', "ensino fundamental"), ('"construção da Escola Municipal"', "")],
 "agentes_ed_especial": [('"Agente de Apoio à Educação Especial"', "nomeação;convocação"), ('"Agente de Apoio à Educação Especial"', "")],
 "contraturno": [('"contraturno"', "parceria"), ('"atividades complementares"', "ensino fundamental;parceria")],
 "pais_vale_cultura": [('"Vale Cultura"', "pais"), ('"responsáveis"', "programa;escola;incentivo;participação")],
 "gm_80": [('"policiamento comunitário"', "Guarda Municipal"), ('"Guarda Municipal"', "efetivo;vigilância ostensiva")],
 "gm_requalificacao": [('"Força Nacional"', "Guarda Municipal;capacitação"), ('"armas não letais"', "Guarda Municipal")],
 "cameras_20": [('"câmeras"', "Centro de Operações;videomonitoramento"), ('"videomonitoramento"', "ampliação")],
 "uops_recuperar": [('"Unidade de Ordem Pública"', ""), ('"UOP"', "Guarda Municipal")],
 "uops_novas": [('"Unidade de Ordem Pública"', "nova;implantação"), ('"UOP"', "Madureira;Bangu")],
 "gm_escolas": [('"Ronda Escolar"', "Guarda Municipal"), ('"guarda municipal"', "unidades escolares;presença")],
 "incentivo_policias": [('"Área Integrada de Segurança Pública"', "metas;incentivo"), ('"PROEIS"', "")],
 "ppp_iluminacao": [('"iluminação pública"', "parceria público-privada"), ('"PPP"', "iluminação")],
 "pracas_poda": [('"inventário"', "poda;praças"), ('"poda"', "praças;mutirão")],
 "parceria_mp_criancas": [('"Conselho Tutelar"', "Ministério Público;termo de cooperação;crianças")],
 "transbrasil": [('"TransBrasil"', "conclusão;operação"), ('"Transbrasil"', "obras")],
 "brt_frota": [('"BRT"', "frota;ampliação;concessionárias"), ('"BRT"', "multa;ar-condicionado")],
 "racionalizacao": [('"racionalização"', "linhas de ônibus"), ('"reimplantação"', "linhas de ônibus")],
 "bilhete_unico": [('"Bilhete Único Carioca"', "três horas"), ('"Bilhete Único Carioca"', "metrô;integração")],
 "vans_zo": [('"Serviço de Transporte Público Local"', "licitação"), ('"STPL"', "licitação;vans")],
 "ciclovia_tim_maia": [('"Tim Maia"', "ciclovia;CREA"), ('"ciclovia Tim Maia"', "")],
 "estacionamentos": [('"estacionamentos subterrâneos"', ""), ('"estacionamento subterrâneo"', "PPP")],
 "iss_uber_taxi": [('"Uber"', "ISS"), ('"táxi"', "subsídio;frota")],
 "radares": [('"radares"', "redução;equipamentos"), ('"fiscalização eletrônica"', "redução")],
 "secretarias": [('"estrutura organizacional"', "secretarias;Poder Executivo"), ('"extingue"', "Secretaria Municipal")],
 "ope": [('"Oficina para o Emprego"', ""), ('"OPE"', "capacitação;jovens")],
 "cultura_1pct": [('"1% do orçamento"', "cultura"), ('"um por cento"', "cultura;orçamento"), ('"Vale Cultura"', "reestruturação")],
 "lagoas_ap4": [('"AP 4"', "concessão;esgotamento sanitário"), ('"Área de Planejamento 4"', "esgotamento sanitário;concessão")],
 "parque_bangu_cg": [('"Parque"', "Bangu;Campo Grande;implantação"), ('"Parque de Madureira"', "Bangu")],
 "comunidades_20": [('"Comlurb"', "Cedae;comunidades;saneamento")],
 "adensamento_ap4": [('"Vargens"', "contrapartida;Projeto de Lei Complementar"), ('"PEU das Vargens"', "")],
 "acordo_1000": [('"Acordo de Resultados"', "prêmio;servidores"), ('"Acordo de Resultados"', "")],
 "acolhimento_4000": [('"acolhimento"', "população de rua;vagas"), ('"Centro de Acolhimento"', "vagas;inauguração")],
}


def consulta(frase, filtro):
    try:
        total, itens = dorio(frase, "2017-01-01", "2020-12-31", 3 if filtro else 2, [f for f in filtro.split(";") if f])
        return {"total": total, "itens": itens}
    except Exception as e:  # noqa: BLE001 - registra e segue o lote
        return {"erro": str(e)}


if __name__ == "__main__":
    # consultas em paralelo; mantém o que já foi gravado sem erro e grava a cada consulta concluída
    from concurrent.futures import ThreadPoolExecutor, as_completed
    sys.stdout.reconfigure(encoding="utf-8")
    dados = json.loads(SAIDA.read_text(encoding="utf-8")) if SAIDA.exists() else {}
    pedidas = sys.argv[1:] or list(Q)
    tarefas = {}
    with ThreadPoolExecutor(max_workers=1) as ex:
        for chave in pedidas:
            dados.setdefault(chave, {})
            for frase, filtro in Q[chave]:
                q = frase + (f" | {filtro}" if filtro else "")
                if sys.argv[1:] or "itens" not in dados[chave].get(q, {}):
                    tarefas[ex.submit(consulta, frase, filtro)] = (chave, q)
        for fut in as_completed(tarefas):
            chave, q = tarefas[fut]
            r = dados[chave][q] = fut.result()
            print(chave, "|", q, "|", r.get("erro") or f"{r['total']} -> {len(r['itens'])}", flush=True)
            SAIDA.write_text(json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")

"""Lote de buscas no DO Rio para o censo do Paes 2024 (mandato desde 01/01/2025).

python -I data/interim/busca_oficial/lote_paes.py [chave ...]   -> grava/atualiza paes_rio_2024.json
"""
import json, runpy, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
dorio = runpy.run_path(str(AQUI.parents[2] / "scripts" / "busca_rj.py"))["dorio"]
SAIDA = AQUI / "paes_rio_2024.json"

# chave: [(frase exata, palavras que a página também precisa conter), ...]
Q = {
 "conscientizacao": [('"Educação para Cidadania"', ""), ('"Cidadania Carioca"', "escola")],
 "super_centros": [('"Super Centro"', "Realengo"), ('"Super Centro"', "Jacarepaguá"), ('"Super Centro Carioca de Saúde da Criança"', "")],
 "autismo": [('"Espectro Autista"', "centro;referência"), ('"Espectro Autista"', "programa;famílias")],
 "tempo_integral": [('"tempo integral"', "matrículas;%")],
 "creches": [('"vagas em creche"', ""), ('"Espaço de Desenvolvimento Infantil"', "inaugura")],
 "programacao": [('"pensamento computacional"', ""), ('"programação"', "alunos;rede municipal;computa")],
 "educ_especial": [('"Agente de Apoio à Educação Especial"', "contrata")],
 "climatizacao": [('"climatização"', "salas de aula"), ('"climatização das escolas"', "")],
 "brt_vlt": [('"VLP"', "BRT"), ('"Lei Complementar nº 289"', "")],
 "jae_tarifa": [('"integração tarifária"', "Jaé"), ('"política tarifária"', "")],
 "faixa_azul": [('"motofaixa"', "")],
 "eletrificacao": [('"ônibus elétricos"', ""), ('"transição energética"', "ônibus")],
 "qualificacao": [('"Oportunidades Cariocas"', "")],
 "formalizacao": [('"formalização"', "programa;auxílio financeiro"), ('"formalização"', "trabalhadores;incentivo")],
 "fundo_turismo": [('"Fundo Municipal de Turismo"', ""), ('"Rotas Aéreas Internacionais"', "")],
 "bolsa_valores": [('"Bolsa de Valores"', "")],
 "rondas_gm": [('"Ronda Escolar"', ""), ('"Guarda Municipal"', "praças;parques;efetivo")],
 "brt_seguro": [('"BRT Seguro"', "")],
 "gm_armada": [('"Força Municipal"', "arma de fogo")],
 "iluminacao_cameras": [('"Civitas"', "câmeras"), ('"iluminação pública"', "LED;novos pontos")],
 "ppps": [('"Parceria Público-Privada"', "contrato"), ('"leilão"', "concessão;B3")],
 "whatsapp_wifi": [('"Wi-Fi"', "público"), ('"WhatsApp"', "1746")],
 "selo_diamante": [('"Selo Diamante"', "")],
 "acari": [('"Rio Acari"', "")],
 "reassentamento": [('"reassentamento"', "inunda"), ('"reassentamento"', "ribeirinh")],
 "sirenes": [('"sirenes"', "inunda"), ('"sirenes"', "enchente")],
 "jardim_maravilha": [('"Jardim Maravilha"', "drenagem")],
 "zn_verde": [('"ZN Verde"', ""), ('"Planta+Rio"', ""), ('"Planta Mais Rio"', "")],
 "carioquinha": [('"Cartão Primeira Infância Carioca"', ""), ('"Carioquinha"', "renda")],
 "prato_feito": [('"Restaurante Popular Carioca"', ""), ('"Prato Feito Carioca"', "")],
 "pop_rua": [('"Seguir em Frente"', "acolhid"), ('"situação de rua"', "acolhimento;meta")],
 "morar_carioca": [('"Morar Carioca"', ""), ('"Bairro Maravilha"', "")],
 "casa_carioca": [('"Casa Carioca"', "")],
 "hub_favela": [('"Favela Empreendedora"', "")],
 "empreend_feminino": [('"Rede Empreendedora Carioca"', ""), ('"empreendedorismo feminino"', "capacita")],
 "cartao_mulheres": [('"Cartão Família Carioca"', "mulheres"), ('"Cartão Carioca"', "chefes de família")],
 "maria_penha": [('"Ronda Maria da Penha"', "")],
 "pcd_capacitacao": [('"pessoas com deficiência"', "capacitação;familiares"), ('"pessoa com deficiência"', "capacitação;15")],
 "pcd_transporte": [('"pessoa com deficiência"', "transporte;consultas;exames"), ('"pessoas com deficiência"', "transporte;cirurgias")],
 "pacto_juventude": [('"Pacto pela Juventude"', "")],
 "espacos_juventude": [('"Espaço da Juventude"', ""), ('"Casa da Juventude"', "")],
 "rio_vestibular": [('"Rio Vestibular"', "")],
 "jae_cultural": [('"Jaé Cultural"', "")],
 "oficina_cultural": [('"Oficina Cultural Carioca"', ""), ('"Oficinas Culturais"', "Carioca")],
 "museu_olimpico": [('"Museu Olímpico"', ""), ('"Parque Imagine"', ""), ('"Parque do Legado"', "")],
 "vilas_olimpicas": [('"Vila Olímpica"', "Sepetiba"), ('"Vila Olímpica"', "Rio das Pedras"), ('"Vila Olímpica"', "Cidade de Deus")],
 "time_rio": [('"Time Rio"', "")],
}

def consulta(frase, filtro):
    try:
        total, itens = dorio(frase, "2025-01-01", "2026-10-14", 10 if filtro else 3, [f for f in filtro.split(";") if f])
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
    with ThreadPoolExecutor(max_workers=8) as ex:
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

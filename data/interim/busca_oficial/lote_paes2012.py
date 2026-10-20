"""Lote de buscas no DO Rio para o censo do Paes 2012 (mandato 2013-2016).

python -I data/interim/busca_oficial/lote_paes2012.py [chave ...]   -> grava/atualiza paes_rio_2012.json
"""
import json, runpy, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
dorio = runpy.run_path(str(AQUI.parents[2] / "scripts" / "busca_rj.py"))["dorio"]
SAIDA = AQUI / "paes_rio_2012.json"

# chave: [(frase exata, palavras que a página também precisa conter), ...]
Q = {
 "ideb": [('"IDEB"', "anos iniciais;2015")], "alfabetizacao": [('"alfabetizados"', "7 anos")], "analf_funcional": [('"analfabetismo funcional"', "")],
 "tempo_integral": [('"turno único"', "alunos;percentual")], "segundo_segmento": [('"16 anos"', "segundo segmento")], "vagas_infantil": [('"Espaço de Desenvolvimento Infantil"', "inauguração")],
 "ingles": [('"Rio Criança Global"', "9º ano")], "clinicas_familia": [('"Clínica da Família"', "inaugura")], "psf_70": [('"cobertura"', "Saúde da Família;70%")],
 "padi": [('"PADI"', "equipes")], "medicos_2mil": [('"médicos"', "contratação;2.000")], "consultas_eletivas": [('"consultas eletivas"', "tempo de espera")],
 "cer_espera": [('"CER"', "tempo de espera")], "leitos_cnes": [('"leitos"', "CNES;cadastrados")], "mortalidade_infantil": [('"mortalidade infantil"', "1.000 nascidos")],
 "mortalidade_materna": [('"mortalidade materna"', "")], "saude_inteligente": [('"prontuário eletrônico"', "")], "esgoto_ap5": [('"AP 5"', "esgotamento sanitário;cobertura")],
 "reflorestamento": [('"reflorestamento"', "hectares")], "arvores": [('"mudas"', "plantio;árvores")], "ciclovias": [('"malha cicloviária"', "km")],
 "reciclavel": [('"coleta seletiva"', "percentual")], "gee": [('"emissões"', "inventário;efeito estufa")], "macrodrenagem": [('"Cação Vermelho"', ""), ('"macrodrenagem"', "Jacarepaguá")],
 "plano_clima": [('"adaptação"', "mudanças climáticas;plano")], "pracas_15min": [('"15 Minutos Verdes"', "")], "morar_carioca": [('"Morar Carioca"', "domicílios")],
 "mcmv_50mil": [('"Minha Casa Minha Vida"', "unidades contratadas")], "risco_zero": [('"alto risco"', "famílias;encostas")], "favelas_5pct": [('"áreas ocupadas por favelas"', "")],
 "bairro_maravilha": [('"Bairro Maravilha"', "km")], "porto_maravilha": [('"Porto Maravilha"', "conclusão;obras")], "upp_social": [('"UPP Social"', "")],
 "parque_olimpico": [('"Parque Olímpico"', "concessão")], "rio_branco": [('"Avenida Rio Branco"', "fechamento;pedestres")], "cidade_nova": [('"Cidade Nova"', "Operação Urbana Consorciada")],
 "brt_tempo": [('"tempo de viagem"', "BRT;redução")], "acidentes": [('"acidentes"', "vítimas;redução")], "bilhete_unico": [('"Bilhete Único Carioca"', "barcas;metrô")],
 "alta_capacidade": [('"alta capacidade"', "usuários;percentual")], "brts": [('"TransOlímpica"', "inauguração"), ('"TransBrasil"', "obras")], "frota_onibus": [('"ar-condicionado"', "frota;ônibus")],
 "taxis": [('"Rio Boa Praça"', "táxi")], "vlt": [('"VLT"', "inauguração;operação")], "racionalizacao": [('"racionalização"', "linhas de ônibus")],
 "plano_mobilidade": [('"Plano de Mobilidade Urbana Sustentável"', "")], "zn_zo": [('"Zonas Norte e Oeste"', "investimentos;recursos")], "investir_34bi": [('"investimentos"', "bilhões;2013-2016")],
 "producoes_350": [('"fomento"', "editais;produções culturais")], "frequencia_cultura": [('"equipamentos culturais"', "frequência;público")], "porto_cultura": [('"Porto Maravilha"', "cultural;Museu")],
 "imoveis_tiradentes": [('"Praça Tiradentes"', "imóveis;recuperação")], "polo_portuario": [('"José Bonifácio"', "Centro Cultural"), ('"Cidade do Teatro"', ""), ('"Cais do Valongo"', "")],
 "escritorio_cultura": [('"escritório"', "projetos culturais")], "pobreza_50": [('"linha de pobreza"', "redução")], "pobreza_beneficiarios": [('"Cartão Família Carioca"', "pobreza;superação")],
 "caps": [('"CAPS"', "inauguração"), ('"residências terapêuticas"', "")], "cfc_saude": [('"Cartão Família Carioca"', "Saúde da Família")], "rio_em_forma": [('"Rio em Forma"', "Escolas do Amanhã")],
 "uops": [('"Unidade de Ordem Pública"', "inauguração;implantação")], "recapeamento": [('"Asfalto Liso"', "km")], "calcadas": [('"Rio Acessível"', "calçadas;rampas")],
 "apagamento": [('"índice de apagamento"', "")], "plano_iluminacao": [('"Plano Diretor de Iluminação"', "")], "investimento_15": [('"investimentos"', "receita corrente;percentual")],
 "central_1746": [('"1746"', "atendimentos;satisfação")], "compras_10": [('"compras"', "economia;redução;preço")], "receita_15": [('"receita tributária"', "crescimento")],
 "rede_datacenter": [('"datacenter"', ""), ('"Datacenter"', "")], "regionais_33": [('"Regiões Administrativas"', "atendimento ao cidadão;presencial")], "smgpm": [('"Sistema Municipal de Gerenciamento de Projetos"', "")],
 "nota_carioca": [('"Nota Carioca"', "sorteio;premiados")], "codigo_tributario": [('"Consolidação da Legislação Tributária"', ""), ('"consolidação"', "legislação tributária")],
 "alvaras": [('"Alvará Já"', ""), ('"licenciamento"', "eletrônico;alvará")], "energia_1bi": [('"Rio Capital da Energia"', "investimentos")], "hotel_7mil": [('"quartos"', "rede hoteleira;novos")],
 "economia_criativa": [('"economia criativa"', "empregos")], "condominio_industrial": [('"condomínio industrial"', "Zona Oeste")], "centro_convencoes": [('"centro de convenções"', "Zona Portuária")],
 "agencia_criativa": [('"agência"', "economia criativa;indústria criativa")],
}


def consulta(frase, filtro):
    try:
        total, itens = dorio(frase, "2013-01-01", "2016-12-31", 2 if filtro else 1, [f for f in filtro.split(";") if f])
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

"""Lote de buscas no DO Rio para o censo do Paes 2020 (mandato 2021-2024).

python -I data/interim/busca_oficial/lote_paes2020.py [chave ...]   -> grava/atualiza paes_rio_2020.json
"""
import json, runpy, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
dorio = runpy.run_path(str(AQUI.parents[2] / "scripts" / "busca_rj.py"))["dorio"]
SAIDA = AQUI / "paes_rio_2020.json"

# chave: [(frase exata, palavras que a página também precisa conter), ...]
Q = {
 "avenida_brasil": [('"Avenida Brasil"', "revitaliza;investimento"), ('"Transbrasil"', "concluí")],
 "convenios_etica": [('"Transparência Internacional"', ""), ('"Ministério Público"', "convênio;integridade"), ('"Tribunal de Contas"', "acordo de cooperação;integridade")],
 "salarios_em_dia": [('"calendário de pagamento"', "servidores"), ('"décimo terceiro"', "pagamento;servidores")],
 "acordo_resultados": [('"Acordo de Resultados"', "decreto")],
 "cartao_familia": [('"Cartão Família Carioca"', "valor"), ('"Família Carioca"', "benefício;reajuste")],
 "restaurantes_populares": [('"restaurante popular"', "inaugura"), ('"farmácia popular"', ""), ('"Restaurante Popular"', "")],
 "frentes_trabalho": [('"frente de trabalho"', ""), ('"frentes de trabalho"', "")],
 "conscientizacao": [('"Cidadania Carioca"', ""), ('"educação para a cidadania"', "escolas"), ('"conscientização"', "cidadania;programa")],
 "plano_100_dias": [('"100 dias"', "plano;BRT"), ('"cem dias"', "plano"), ('"intervenção"', "BRT;Mobi")],
}

def consulta(frase, filtro):
    try:
        total, itens = dorio(frase, "2021-01-01", "2024-12-31", 10 if filtro else 3, [f for f in filtro.split(";") if f])
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
    with ThreadPoolExecutor(max_workers=2) as ex:
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

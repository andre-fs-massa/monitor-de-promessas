# Crivella 2016 (crivella_rio_2016) — notas do censo (15/10/2026)

- SQ 190000017952, PRB, coligação "Por um Rio mais humano" (PRB/PTN/PR). Mandato 2017-2020, encerrado (preso em 22/12/2020; Jorge Felippe assumiu até 31/12).
- O plano **não está** no zip de dados abertos `proposta_governo_2016_RJ.zip` (10 dos 11 candidatos do Rio estão; o do Crivella não, nem com outro SQ). DivulgaCandContas bloqueia script e Chrome headless (403); Wayback não tem cópia. O usuário baixou o PDF no navegador (`data/raw/tse/2016/proposta_governo1471038889100.PDF`, copiado para `pdf_rj_crivella/2016RJ190000017952.pdf`). 8 páginas, "As 50 principais propostas".
- Arquivos: `crivella_def.py` (48 promessas), `crivella_decisoes.py`, `gera_crivella.py`, `lote_crivella.py` (DO Rio 2017–2020; o servidor recusou conexões com 3 workers — está com 1), `crivella_rio_2016.json`, `ver_crivella.py`.
- Fontes principais: Aos Fatos, checagens de dez/2017 (14 promessas com prazo em 2017) e set/2020 (as 50).
- Lote do DO incompleto: as promessas já fechadas com a imprensa/Aos Fatos não tiveram todas as consultas concluídas (para rodar o resto: `python -I lote_crivella.py`).

## Fora do censo
Itens 14 (autonomia dos diretores, vago), 17 (manter meritocracia), 40 (estação Gávea, cobrança ao Estado), 44 (manter apoio às escolas de samba); estudo do BRT para a Ilha (parte do item 31).

## Casos duvidosos (levar ao usuário)
1. Zona Franca Social = parcial: programa criado (preferência nas compras), sem os benefícios tributários prometidos. Alternativa: cumprida.
2. Cimento Social = cumprida baixa: a prefeitura criou coordenadoria e fez obras pontuais (Salgueiro), sem balanço.
3. Clínicas da Família (contratar ginecologistas e pediatras) = não cumprida, com corte de 239 equipes em 2018. O Aos Fatos deu "cumprida" (13 clínicas inauguradas), olhando o "manter".
4. Não construir novas escolas = não cumprida baixa (escola Marielle Franco na Maré, 2018). Pode ter sido obra iniciada na gestão anterior.
5. PPP da iluminação = parcial (assinada abr/2020, prazo era concluir investimentos até 2019). Aos Fatos: cumprida.
6. Radares = parcial (redução de 17% em 2017; dinheiro das multas não exclusivo).
7. Adensamento da AP 4 = não cumprida baixa (LC 192/2018 libera acréscimos com contrapartida). Aos Fatos: cumprida.
8. Guarda 80% em policiamento = não cumprida baixa (PPA com índice de referência 74%, sem resultado).
9. Frota do BRT = parcial baixa (327 → 413 ônibus até 2020, mas 360 de 420 em 2019 e intervenção).
10. Agentes de educação especial = parcial (chamados até out/2018, prazo era 2017).

## Revisão de padronização dos prefeitos (15/10/2026)
- Regra sem registro: com Diário Oficial consultado a confiança passou a média (16 casos no Paes 2012, 2 no Crivella).
- Critério para metas de indicador não atingidas: parcial se avançou ao menos metade do caminho entre o ponto de partida e a meta (ou ficou a menos de 1 ponto dela); senão, não cumprida. Dado intermediário que já bate a meta final = cumprida; abaixo dela, sem dado final = parcial se houve avanço relevante.
- Mudanças: Paes 2012 CAPS cumprida->parcial; Paes 2012 conclusão até 16 anos (95,7/96) não->parcial; Crivella tempo integral (19,4%->35,5% de 50%) não->parcial.
- Áreas: obras de drenagem/enchentes = Saneamento (Paes 2012 macrodrenagem, Paes 2024 Acari); poda/praças = Meio ambiente (Crivella); investimento total = Política fiscal (Paes 2012).
- Mantido para o usuário decidir: alfabetização 95% (90,7% em 2014, sem ponto de partida) segue não cumprida.

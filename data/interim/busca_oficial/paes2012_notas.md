# Paes 2012 (paes_rio_2012) — notas do censo (15/10/2026)

- SQ 190000004018, PMDB, coligação "Somos um Rio". Mandato 2013-2016, encerrado. Plano no zip de dados abertos (87 páginas).
- Censo: 80 promessas = todas as "Metas" (5.x.3) + itens do Sumário fora das metas + compromissos concretos dos Projetos. Fora: diretrizes, continuidade de programas, estudo de viabilidade (aquaviário), frases vagas. Detalhes no cabeçalho de `paes2012_def.py`.
- Divergências internas do plano: Clínicas (62 x 79), UOPs (14 no total x mais 9), reflorestamento (600 x 1.100 ha), Zonas Norte/Oeste (2/3 x 70%) — valeu Sumário/Metas.
- Resultado: 22% cumpridas, 31% parciais, 46% não cumpridas; confiança 13 alta / 32 média / 35 baixa.

## Fontes principais
- **Acordo de Resultados 2015 — resultados por secretaria**: Diário Oficial de 11/04/2016, págs. 6 a 11 (`doweb.rio.rj.gov.br/portal/edicoes/download/3075/6` a `/11`). Recortes em imagem em `paes2012_docs/c3075_*.png` (tabelas com meta 2015, referência e resultado). É a melhor fonte oficial: as metas do Plano Estratégico 2013-2016 são quase as mesmas do plano de governo.
- **Acordo de Resultados 2016 — metas e valores de referência**: DO de 20/04/2016, págs. 10 a 12 (`3083/10` a `/12`). Não foi localizada a apuração final de 2016 (a gestão seguinte não publicou).
- Relatório Anual de Gestão 2016 da Saúde (`paes2012_docs/RAG-2016.pdf`).
- Ata do Conselho do IPP de 14/09/2016 (tempo integral).
- Lote do DO Rio 2013–2016: `lote_paes2012.py` → `paes_rio_2012.json` (ainda rodando ao fim da sessão; as consultas que faltavam não mudaram a classificação).

## Casos duvidosos (levar ao usuário)
1. Muitas metas foram julgadas pelo resultado de 2015 (último publicado): CER, consultas eletivas, leitos CNES, acidentes, BRT, apagamento = cumpridas; UOPs, 1746, alvarás, rede = parciais.
2. Saúde da Família 70% = parcial (68,62% em dez/2016 pelo Ministério da Saúde; 70% só em jan/2017). Alternativa: cumprida.
3. Tempo integral 35% = parcial baixa (19,4% dos alunos em 2015; 36% das escolas em set/2016).
4. Clínicas da Família = parcial (~45 novas contra 62; 14 de 54 reformas até 2015).
5. MCMV 50 mil = parcial baixa (77.365 desde 2009 até 2015; não se sabe quanto em 2013–2016).
6. Investimento 15% = cumprida baixa (só número da própria prefeitura: 16,1%).
7. SMGPM = cumprida baixa (monitoramento por Acordos de Resultados; não achei ato com esse nome).
8. CAPS 60% = cumprida baixa (meta de 58% aprovada em 2015).
9. UPP Social = cumprida (Rio+Social em 208 comunidades), embora o programa tenha sido esvaziado depois.
10. Promessas de indicador sem dado localizado (pobreza, favelas, alta capacidade, ZN/ZO, R$ 34,3 bi, economia criativa, energia) = não cumpridas com confiança baixa, pela regra "sem registro".

## Revisão de padronização dos prefeitos (15/10/2026)
- Regra sem registro: com Diário Oficial consultado a confiança passou a média (16 casos no Paes 2012, 2 no Crivella).
- Critério para metas de indicador não atingidas: parcial se avançou ao menos metade do caminho entre o ponto de partida e a meta (ou ficou a menos de 1 ponto dela); senão, não cumprida. Dado intermediário que já bate a meta final = cumprida; abaixo dela, sem dado final = parcial se houve avanço relevante.
- Mudanças: Paes 2012 CAPS cumprida->parcial; Paes 2012 conclusão até 16 anos (95,7/96) não->parcial; Crivella tempo integral (19,4%->35,5% de 50%) não->parcial.
- Áreas: obras de drenagem/enchentes = Saneamento (Paes 2012 macrodrenagem, Paes 2024 Acari); poda/praças = Meio ambiente (Crivella); investimento total = Política fiscal (Paes 2012).
- Mantido para o usuário decidir: alfabetização 95% (90,7% em 2014, sem ponto de partida) segue não cumprida.

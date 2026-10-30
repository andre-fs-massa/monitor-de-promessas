# Livro de códigos — promessas de governo (presidentes e governadores)

Baseado no método do Comparative Party Pledges Group (Thomson, Royed, Naurin et al., AJPS 2017).

## Unidade de análise

Uma **promessa** é uma frase do plano de governo registrado no TSE que compromete o futuro governo com uma **ação** ou um **resultado** cuja realização pode ser verificada.

- Entra: "Retomaremos a política de valorização do salário mínimo", "Opomo-nos à privatização dos Correios".
- Não entra: diretrizes e diagnósticos sem objeto verificável ("fortalecer a educação pública universal", "o Brasil merece mudar para melhor").
- Um parágrafo pode conter mais de uma promessa; cada uma vira uma linha.
- Toda promessa testável do plano entra na base, tenha ou não evidência encontrada. Testável é o compromisso com objeto concreto: criar, extinguir, construir, implantar, revisar um contrato ou ato específico, ou atingir uma meta numérica.
- Ficam fora: verbos sem objeto verificável ("apoiar", "estimular", "fortalecer", "valorizar", "melhorar", "buscar", "promover"), estudos de viabilidade, cobranças a outro ente ("cobrar do Governo Federal"), manutenção de estrutura já existente e itens repetidos de outra seção.
- O `trecho_literal` deve existir no texto extraído do PDF. `scripts/build.py` confere isso.

## Campos

| Campo | Descrição |
| --- | --- |
| `id` | `<mandato_id>-<nn>` |
| `mandato_id` | Mandato ao qual a promessa pertence (ver `data/mandatos.csv`) |
| `paragrafo` | Número do parágrafo ou da seção no plano, quando o plano os numera (vazio caso contrário) |
| `pagina` | Página do PDF onde o trecho começa; calculada por `scripts/build.py`, não preenchida à mão |
| `trecho_literal` | Citação exata do plano |
| `promessa` | Reescrita curta e neutra da promessa |
| `area` | Área temática |
| `tipo` | `acao` (o governo fará algo) ou `resultado` (um indicador chegará a um nível) |
| `depende_legislativo` | `sim` quando a promessa só pode ser cumprida com aprovação do Legislativo (Congresso para presidentes, Assembleia Legislativa para governadores): lei, emenda constitucional ou conversão de medida provisória; `nao` quando o Executivo pode cumpri-la sozinho (decreto, portaria, gestão). A lei orçamentária anual não conta. |
| `outro_ente` | Vazio quando a execução cabe a quem prometeu. Preenchido (`União`, `Estados`, `Municípios`, `Estados e municípios`) quando a execução cabe por lei a outro ente federativo e quem prometeu só pode financiar, induzir ou cooperar. Programas que o próprio governo cria e aos quais outros entes aderem contam como competência própria |
| `status` | Ver abaixo |
| `confianca` | `alta` (ato oficial inequívoco), `media` (evidência indireta ou interpretação), `baixa` (evidência fraca ou parcial, ou nenhum registro encontrado em busca só na imprensa e em sites) |
| `evidencia` | Fato que sustenta o status, com data |
| `fonte_url` | Link para a fonte; obrigatório para toda promessa avaliada |
| `data_evidencia` | Data (AAAA-MM ou AAAA) do fato; quando nenhum registro foi encontrado, o mês da busca |

## Status

| Status | Regra |
| --- | --- |
| `cumprida` | Ação realizada ou resultado alcançado integralmente |
| `parcialmente_cumprida` | Parte relevante realizada, ou realizada com escopo menor que o prometido |
| `nao_cumprida` | Mandato encerrado sem realização, ação contrária à promessa, ou abandono declarado pelo governo durante o mandato. Também quando a busca (imprensa, sites oficiais, Diário Oficial, Assembleia) não encontra nenhum registro de execução: nesse caso a confiança é `baixa` se a busca foi só na imprensa e em sites, e `media` se também foi consultado o Diário Oficial ou o Legislativo — Assembleia, Câmara Municipal ou, para presidentes, a Câmara dos Deputados (ex.: com `scripts/busca_rj.py` e `scripts/busca_br.py`); `fonte_url` pode ficar vazio e `evidencia` descreve a busca feita |
| `em_andamento` | Mandato em curso, com medidas concretas iniciadas, mas sem conclusão. Sem nenhum registro de início, a promessa segue a regra de `nao_cumprida` por falta de registro e é reavaliada a cada nova `data_corte` |
| `interrompida` | Mandato encerrado antes do prazo (impeachment, renúncia) com a promessa já iniciada (obra, contrato, projeto enviado, programa criado) e com prazo posterior à data de saída. Sem nenhum início até a saída, a promessa é `nao_cumprida`. Promessas com prazo próprio vencido antes da saída são julgadas normalmente |
| `nao_avaliada` | Busca ainda não feita; fica fora do denominador das taxas |

**Metas numéricas não atingidas** (indicador ou quantidade): `parcialmente_cumprida` quando o governo percorreu pelo menos metade do caminho entre o ponto de partida e a meta, ou ficou a menos de 1 ponto dela; abaixo disso, `nao_cumprida`. Se só há dado intermediário, ele vale como `cumprida` quando já alcança a meta final e segue o mesmo critério quando não alcança. Com execução comprovada mas sem total localizado, `parcialmente_cumprida` com confiança `baixa`.

**Áreas padronizadas:** rodovias e vias expressas = Mobilidade; drenagem, controle de enchentes, lixo e reciclagem = Saneamento; poda e praças = Meio ambiente; volume de investimento = Política fiscal.

As taxas são calculadas sobre as promessas avaliadas (`total − nao_avaliada`). Para mandatos em curso, o status reflete a `data_corte` de `mandatos.csv`. Para mandatos interrompidos, a avaliação vai até `mandato_fim_efetivo` (data do afastamento ou da renúncia; o motivo fica em `motivo_interrupcao`); fatos posteriores podem aparecer na evidência, mas não mudam o status.

## Impacto fiscal (presidentes, governadores do RJ, de SP e de MG e prefeitos de SP)

Arquivo `data/impacto_fiscal/<mandato>.csv` (uma linha por promessa do mandato), validado pelo `build.py` e publicado em `data/base_aberta/impacto_fiscal.csv`.

| Campo | Regra |
| --- | --- |
| `impacto_fiscal` | `despesa_aumenta`, `despesa_reduz`, `receita_aumenta`, `receita_reduz`, `neutro` (efeitos se compensam por desenho) ou sem impacto direto: `sem_impacto_direto` (regulatória), `regra_fiscal`, `fora_do_orcamento` (estatais, fundos como CDE e FGTS), `sem_impacto_primario` (privatização, fundos garantidores), `indireto_estatal` (via dividendos), `sem_valor_proprio` (resultado de outros programas, sem dupla contagem). Promessa não implementada recebe a direção, sem valor |
| `valor_incremental_rs_bi` | Despesa ou receita a mais (ou a menos, nas categorias `_reduz`) por ano com o que foi implementado, comparada com o ano anterior ao mandato (2010 para Dilma 2010, 2014 para Dilma 2014, 2018 para Bolsonaro, 2022 para Lula), em R$ bi nominais. Usa o último ano completo de governo com dado oficial (2014 para Dilma 2010; 2015 para Dilma 2014, afastada em mai/2016; 2022 para Bolsonaro; 2025 para Lula). Quando o programa já existia e o gasto caiu em relação ao ano anterior ao mandato, não há despesa a mais: fica só o custo total |
| `valor_total_rs_bi` | Custo total do programa no `ano_ref` |
| `valor_acumulado_rs_bi` | Soma, ano a ano, da diferença em relação ao ano anterior ao mandato, nos anos em que a medida vigorou (receitas únicas entram uma vez); só anos completos, em R$ bi nominais |
| `periodo_acumulado` | Anos somados no acumulado (ex.: `2023-2025`); se a medida só vale depois, o texto diz quando começa |
| `recorrente` | `nao` para receitas ou gastos únicos (bônus de privatização, outorgas de concessão, curso pontual); a interface mostra o resultado também sem eles |
| `compensacao_rs_bi` | Perda de receita aprovada junto com a receita prometida (ex.: isenção do IR até R$ 5 mil) |
| `fonte_oficial` / `fonte_comparacao` | Primeiro fonte oficial (execução por ação no Portal da Transparência/CGU via `scripts/orcamento_federal.py`, ministérios, Planalto, consultorias de orçamento do Congresso); imprensa só para comparar |

Despesa = empenhada (na Dilma 2010 usa-se o valor PAGO do Tesouro Transparente, "Despesas da União mensais desde 2008", em todos os anos, porque o Portal da Transparência só tem o empenhado a partir de 2014); empréstimos reembolsáveis (Finep, Fundo Social) são financeiros e ficam fora. A interface soma os incrementais por grupo e calcula o resultado (déficit ou superávit) = receitas a mais − receitas a menos − compensações atreladas − despesas a mais + despesas cortadas, com a ressalva de que os anos variam e não há correção pela inflação.


Governadores do RJ: o orçamento de referência é o do Estado. Como os portais oficiais do Estado (Transparência, SEFAZ, TCE, Alerj) recusam conexões feitas de fora do Brasil, os valores vêm de investimentos anunciados pelo governo e publicados na imprensa (`fonte_comparacao`), com confiança média ou baixa. Obra ou equipamento é gasto único (`recorrente` = `nao`) e o acumulado é o valor investido no mandato, com o período da obra; custeio não divulgado fica sem valor.

Governadores de SP: o orçamento de referência é o do Estado de São Paulo. A despesa é a empenhada por ação no Portal da Transparência do Estado (`scripts/orcamento_sp.py`, base desde 2020; para anos anteriores, consulta por ação no SIGEO da Secretaria da Fazenda). Quando o PPA reagrupa ações e a ação nova não é comparável à do ano anterior ao mandato, não há valor a mais; quando um programa substitui outro (ex.: Tabela SUS Paulista no lugar do Santas Casas SUStentáveis), as duas ações são somadas nos dois lados da comparação. Aporte em concessão ou PPP para obra é gasto único (`recorrente` = `nao`).

Governadores de MG: o orçamento de referência é o do Estado de Minas Gerais. A despesa é a empenhada por ação nos dados abertos da Controladoria-Geral do Estado (conjunto "Despesa pública", desde 2002; `scripts/orcamento_mg.py`). Quando o PPAG renumera uma ação, a nova é somada à que ela substituiu; quando o gasto do mandato fica abaixo do ano anterior ao mandato, fica só o custo do último ano.

Prefeitos de São Paulo: o orçamento de referência é o do Município de São Paulo. A despesa é a empenhada (líquida) por projeto/atividade nos dados abertos da Prefeitura (conjunto "Execução orçamentária", desde 2003; `scripts/orcamento_spcapital.py`). Mesmo método dos governadores: diferença de cada ano completo do mandato para o ano anterior ao mandato; quando o gasto do mandato fica abaixo desse ano, fica só o custo do último ano completo.

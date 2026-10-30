# Monitor de Promessas

**Quantas promessas dos planos de governo foram cumpridas?**

O Monitor de Promessas lê o plano de governo que cada presidente, governador e prefeito registrou no Tribunal Superior Eleitoral (TSE), separa as promessas que podem ser verificadas e confere, uma por uma, se foram cumpridas. Cada veredito traz o trecho exato do plano, a evidência encontrada e o link para a fonte.

🌐 **Site:** <https://promessas.afsm.me>
📦 **Base de dados:** [`promessas.csv`](docs/dados/promessas.csv) · [`promessas.json`](docs/dados/promessas.json) · [`impacto_fiscal.csv`](docs/dados/impacto_fiscal.csv)

> **Versão preliminar.** As classificações e os valores de impacto fiscal ainda estão em revisão e podem mudar. Encontrou um erro? [Abra uma issue](../../issues/new/choose) — veja [como colaborar](CONTRIBUTING.md).

---

## O que tem na base

32 mandatos e 2.121 promessas (atualizado em outubro de 2026):

| Cargo | Mandato | Situação | Promessas |
|---|---|---|---:|
| Presidente | Lula (2022) | em curso | 46 |
| Presidente | Bolsonaro (2018) | encerrado | 48 |
| Presidente | Dilma Rousseff (2014) | interrompido (impeachment) | 33 |
| Presidente | Dilma Rousseff (2010) | encerrado | 37 |
| Governador (RJ) | Cláudio Castro (2022) | interrompido (renúncia) | 49 |
| Governador (RJ) | Wilson Witzel (2018) | interrompido (afastamento) | 87 |
| Governador (RJ) | Luiz Fernando Pezão (2014) | encerrado | 77 |
| Governador (RJ) | Sérgio Cabral (2010) | interrompido (renúncia) | 137 |
| Governador (SP) | Tarcísio de Freitas (2022) | em curso | 77 |
| Governador (SP) | João Doria (2018) | interrompido (renúncia) | 29 |
| Governador (SP) | Geraldo Alckmin (2014) | interrompido (renúncia) | 125 |
| Governador (SP) | Geraldo Alckmin (2010) | encerrado | 68 |
| Governador (MG) | Romeu Zema (2022) | interrompido (renúncia) | 23 |
| Governador (MG) | Romeu Zema (2018) | encerrado | 39 |
| Governador (MG) | Fernando Pimentel (2014) | encerrado | 12 |
| Governador (MG) | Antonio Anastasia (2010) | interrompido (renúncia) | 6 |
| Governador (BA) | Jerônimo Rodrigues (2022) | em curso | 219 |
| Governador (BA) | Rui Costa (2018) | encerrado | 198 |
| Governador (BA) | Rui Costa (2014) | encerrado | 163 |
| Governador (BA) | Jaques Wagner (2010) | encerrado | 20 |
| Prefeito (Rio) | Eduardo Paes (2024) | em curso | 48 |
| Prefeito (Rio) | Eduardo Paes (2020) | encerrado | 9 |
| Prefeito (Rio) | Marcelo Crivella (2016) | encerrado | 48 |
| Prefeito (Rio) | Eduardo Paes (2012) | encerrado | 80 |
| Prefeito (São Paulo) | Ricardo Nunes (2024) | em curso | 92 |
| Prefeito (São Paulo) | Bruno Covas (2020) | encerrado (completado pelo vice, Ricardo Nunes) | 48 |
| Prefeito (São Paulo) | João Doria (2016) | interrompido (renúncia) | 89 |
| Prefeito (São Paulo) | Fernando Haddad (2012) | encerrado | 60 |
| Prefeito (Belo Horizonte) | Fuad Noman (2024) | em curso (com Álvaro Damião) | 27 |
| Prefeito (Belo Horizonte) | Alexandre Kalil (2020) | interrompido (renúncia) | 94 |
| Prefeito (Belo Horizonte) | Alexandre Kalil (2016) | encerrado | 16 |
| Prefeito (Belo Horizonte) | Marcio Lacerda (2012) | encerrado | 17 |

Os planos de governo só passaram a ser registrados no TSE a partir das eleições de 2010, por isso a base começa nelas.

## Como funciona

1. **Fonte das promessas.** Só o plano de governo registrado no TSE ([portal de dados abertos](https://dadosabertos.tse.jus.br/)). Discursos, debates e entrevistas ficam de fora.
2. **Censo completo.** Entram *todas* as frases do plano que comprometem o governo com uma ação ou um resultado verificável (criar, extinguir, construir, implantar, meta com número), tenham ou não evidência encontrada. Diretrizes genéricas ("valorizar", "fortalecer", "apoiar") ficam de fora. O critério segue o método do Comparative Party Pledges Group (CPPG), grupo internacional de pesquisadores que estuda o cumprimento de promessas eleitorais.
3. **Classificação.** Cada promessa recebe um status:
   - `cumprida`, `parcialmente_cumprida` ou `nao_cumprida`;
   - `em_andamento`, enquanto o mandato ainda está em curso;
   - `interrompida`, quando o mandato acabou antes do prazo (impeachment, renúncia, afastamento) com a promessa já iniciada.
4. **Evidência.** Cada veredito tem fonte e nível de confiança (alta, média, baixa). A busca começa por fontes oficiais (Diário Oficial, Assembleias, Câmara dos Deputados, Portal da Transparência) e usa a imprensa como complemento. Quando nada é encontrado, a promessa conta como não cumprida e a busca feita fica descrita na evidência.
5. **Outros marcadores.** Se a promessa depende do Legislativo (lei, emenda, conversão de medida provisória) e se a execução cabe por lei a outro ente federativo.
6. **Impacto fiscal (presidentes, governadores do RJ, de SP e de MG e prefeitos de SP, BH e Rio).** Efeito no orçamento federal, estadual ou municipal de cada promessa implementada: quanto aumentou ou reduziu despesas e receitas, por ano e acumulado no mandato, com dados oficiais.

As regras completas, com os casos de fronteira, estão no **[livro de códigos](data/codebook.md)**. Presidentes, governadores e prefeitos não são somados num mesmo consolidado, porque têm poderes e orçamentos de escala diferente.

## Como verificar

Cada promessa pode ser conferida de ponta a ponta:

- o **trecho literal** do plano está na coluna `trecho_literal`, com página e parágrafo; o texto completo de cada plano está em [`data/interim/`](data/interim/) e o PDF original, no link `url_tse` de [`data/mandatos.csv`](data/mandatos.csv);
- o script de validação confere que todo trecho literal aparece mesmo no plano;
- a **evidência** e o **link da fonte** estão nas colunas `evidencia` e `fonte_url`;
- as buscas em fontes oficiais (Diário Oficial do RJ, Alerj, Alesp, Câmara dos Deputados) e as decisões de classificação de cada mandato estão em [`data/interim/busca_oficial/`](data/interim/busca_oficial/).

## Estrutura do repositório

```
data/
  mandatos.csv                cadastro dos mandatos (cargo, local, datas, situação, link do plano no TSE)
  promessas/<mandato>.csv     promessas de cada mandato, uma por linha — a fonte da verdade
  impacto_fiscal/<mandato>.csv impacto fiscal das promessas (presidentes, governadores do RJ, de SP e de MG e prefeitos de SP, BH e Rio)
  codebook.md                 livro de códigos: regras de seleção e classificação
  base_aberta/                base consolidada gerada (CSV e JSON)
  interim/<mandato>.txt       texto extraído de cada plano de governo
  interim/busca_oficial/      buscas em fontes oficiais, notas e decisões por mandato
  historico/                  versões anteriores da base
scripts/
  fetch_tse.py                baixa os planos do TSE e extrai o texto de um candidato
  build.py                    valida a base e gera base_aberta/ e web/data.js
  censo_add.py                acrescenta promessas novas ao CSV de um mandato
  busca_rj.py                 busca no Diário Oficial do RJ, no Diário Oficial do Rio e na Alerj
  busca_sp.py                 busca nas leis, decretos e projetos do governador (dados abertos da Alesp)
  busca_br.py                 busca projetos do Executivo na Câmara dos Deputados (API de dados abertos)
  orcamento_federal.py        agrega a execução do orçamento federal por ação (Portal da Transparência e Tesouro)
  orcamento_sp.py             baixa a despesa do Estado de SP por programa e ação (Portal da Transparência de SP)
  orcamento_mg.py             baixa a despesa do Estado de MG por ação (dados abertos da CGE-MG)
  publicar.sh                 gera e publica o site em docs/
web/                          código da interface (HTML, CSS e JavaScript, sem dependências)
docs/                         site publicado no GitHub Pages (gerado; não edite à mão)
```

## Como rodar

Requer Python 3.11 ou mais novo (só biblioteca padrão) e, para extrair texto de PDFs, o `pdftotext` do [Poppler](https://poppler.freedesktop.org/).

```bash
# validar a base e gerar os dados da interface
python -I scripts/build.py
python -I scripts/build.py --links     # também testa se os links das fontes respondem

# ver o site localmente
cd web && python -m http.server 8765   # abra http://127.0.0.1:8765

# baixar um plano do TSE e extrair o texto
python -I scripts/fetch_tse.py 2022 BR 280001607829 lula_2022

# buscar em fontes oficiais
python -I scripts/busca_rj.py ioerj "Telessaúde" --anos 2019,2020
python -I scripts/busca_sp.py normas "saneamento" --de 2023-01-01
python -I scripts/busca_br.py camara "reforma tributária" --anos 2023 --executivo
```

Os arquivos brutos (zips do TSE, planilhas do Portal da Transparência e do Tesouro, documentos oficiais em PDF) somam vários gigabytes e não estão no repositório; os scripts baixam tudo de novo das fontes públicas. O plano de Marcelo Crivella (2016) não está nos dados abertos do TSE e foi baixado do [DivulgaCandContas](https://divulgacandcontas.tse.jus.br/).

## Como colaborar

Correções são muito bem-vindas, principalmente com fonte. Você pode:

- **apontar um erro de classificação** (status, evidência, fonte) ou **uma promessa que ficou de fora**: [abra uma issue](../../issues/new/choose) com o link da evidência;
- **propor mudanças diretamente** nos CSVs de `data/promessas/` por pull request, seguindo o livro de códigos e rodando `python -I scripts/build.py` antes de enviar.

Detalhes em [CONTRIBUTING.md](CONTRIBUTING.md). O princípio que guia a revisão é o mesmo critério para casos iguais em todos os mandatos, de qualquer partido.

## Licença

Uso livre **para fins não comerciais**, com crédito:

- **código** (scripts e interface): [PolyForm Noncommercial 1.0.0](LICENSE-CODIGO.md);
- **dados e textos** (base de promessas, impacto fiscal, livro de códigos, documentação): [Creative Commons BY-NC 4.0](LICENSE-DADOS.txt).

Resumo em [LICENSE](LICENSE). Os planos de governo são documentos públicos do TSE. Para uso comercial, fale com o autor.

## Como citar

> Massa, André. *Monitor de Promessas: cumprimento das promessas dos planos de governo registrados no TSE*. 2026. Disponível em: <https://promessas.afsm.me>. Código e dados: <https://github.com/andre-fs-massa/monitor-de-promessas>.

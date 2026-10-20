# Como colaborar

Obrigado por ajudar a melhorar o Monitor de Promessas! O projeto só é confiável se qualquer pessoa puder conferir e corrigir o que está aqui.

## O princípio

**O mesmo critério para casos iguais, em todos os mandatos e partidos.** Toda correção é avaliada por uma pergunta: a regra do [livro de códigos](data/codebook.md) foi aplicada aqui do mesmo jeito que em casos parecidos de outros mandatos? Argumentos sobre se um governo foi bom ou ruim não mudam uma classificação; evidências mudam.

## Jeitos de colaborar

### 1. Apontar um erro (não precisa saber programar)

[Abra uma issue](../../issues/new/choose) escolhendo o modelo **Correção de classificação**. Informe:

- o **id** da promessa (ex.: `lula_2022-07`; aparece no CSV e na base aberta);
- o que está errado (status, evidência, fonte, área, se depende do Legislativo etc.);
- o que você acha que deveria ser, **com o link da fonte**. Fontes oficiais (Diário Oficial, leis, decretos, portais de transparência, relatórios de órgãos públicos) pesam mais que reportagens.

### 2. Sugerir uma promessa que ficou de fora

Use o modelo **Promessa que ficou de fora** e cole o trecho literal do plano de governo, com a página. Lembre que só entram promessas verificáveis (uma ação ou um resultado concreto), não diretrizes genéricas.

### 3. Propor a mudança diretamente (pull request)

1. Edite o CSV do mandato em `data/promessas/<mandato>.csv` (ou `data/impacto_fiscal/<mandato>.csv`). Não edite `data/base_aberta/`, `web/data.js` nem `docs/`: eles são gerados.
2. Siga os campos e valores do [livro de códigos](data/codebook.md). O `trecho_literal` precisa ser copiado exatamente do texto do plano em `data/interim/<mandato>.txt`.
3. Rode a validação, que confere colunas, status e se o trecho existe no plano:

   ```bash
   python -I scripts/build.py
   ```

4. Explique no pull request o que mudou e por quê, com as fontes.

Para acrescentar promessas novas a um mandato, use `scripts/censo_add.py` (instruções no início do arquivo), que mantém os ids existentes.

### 4. Melhorar o código ou a interface

A interface (`web/`) é HTML, CSS e JavaScript puros, sem dependências nem etapa de build. Os scripts usam só a biblioteca padrão do Python. Para ver o site com suas mudanças:

```bash
python -I scripts/build.py
cd web && python -m http.server 8765
```

## O que acontece depois

Toda sugestão é revisada antes de entrar na base. Se for aceita, a mudança aparece no site na próxima publicação. Se não for, explicamos o motivo na própria issue ou no pull request.

## Licença das contribuições

Ao contribuir, você concorda que sua contribuição seja distribuída sob as mesmas licenças do projeto: [PolyForm Noncommercial 1.0.0](LICENSE-CODIGO.md) para código e [CC BY-NC 4.0](LICENSE-DADOS.txt) para dados e textos.

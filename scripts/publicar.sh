#!/usr/bin/env bash
# Publica o site no GitHub Pages (pasta docs/ do repositório): roda o build, copia web/ e a base
# aberta para docs/, faz commit de tudo o que mudou no projeto e envia.
#   bash scripts/publicar.sh "mensagem do commit"
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
PUB="$RAIZ/docs"
python -I "$RAIZ/scripts/build.py"
mkdir -p "$PUB/dados"
cp "$RAIZ"/web/index.html "$RAIZ"/web/app.js "$RAIZ"/web/data.js "$RAIZ"/web/style.css "$PUB/"
# Arquivos para buscadores e domínio próprio (promessas.afsm.me)
cp "$RAIZ"/web/robots.txt "$RAIZ"/web/sitemap.xml "$RAIZ"/web/compartilhar.png "$RAIZ"/web/CNAME "$PUB/"
cp "$RAIZ"/web/favicon.ico "$RAIZ"/web/favicon.svg "$RAIZ"/web/apple-touch-icon.png "$PUB/"
cp "$RAIZ"/data/base_aberta/* "$PUB/dados/"
touch "$PUB/.nojekyll"
cd "$RAIZ"
git add -A
git diff --cached --quiet && { echo "Nada mudou."; exit 0; }
git commit -q -m "${1:-Atualiza o site}" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q origin main
echo "Publicado."

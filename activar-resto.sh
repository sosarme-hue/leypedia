#!/bin/bash
# Filopedia: diseno Ensayo en toda la web (bloque al final de assets/estilo.css). 10-11-2026.
R=/home/u235595016/domains/filopedia.com/public_html
C=/home/u235595016/domains/filopedia.com/copias-diseno/2026-11-10-resto
cd "$R" || exit 1
if [ ! -f "$C/estilo.css" ]; then mkdir -p "$C"; cp -p assets/estilo.css "$C/estilo.css"; fi
sed -i '/=== diseno Ensayo para toda la web/,/=== fin diseno Ensayo ===/d' assets/estilo.css
cat _diseno/bloque-ensayo.css >> assets/estilo.css
date > _diseno/hecho-resto.txt
wc -c assets/estilo.css "$C/estilo.css" >> _diseno/hecho-resto.txt
grep -c 'diseno Ensayo' assets/estilo.css >> _diseno/hecho-resto.txt

#!/bin/bash
# Pinacopedia: diseno "Sala de museo" (portada + toda la web). Uso unico, 10-11-2026.
R=/home/u235595016/domains/pinacopedia.com/public_html
C=/home/u235595016/domains/pinacopedia.com/copias-diseno/2026-11-10
cd "$R" || exit 1
if [ ! -f "$C/index.html" ]; then
  mkdir -p "$C/en" "$C/assets"
  cp -p index.html "$C/index.html"
  cp -p en/index.html "$C/en/index.html"
  cp -p assets/estilo.css "$C/assets/estilo.css"
fi
cp _diseno/pina-portada.css assets/pina-portada.css
grep -q 'pina-portada.css' index.html || sed -i 's#<link rel="stylesheet" href="assets/estilo.css">#&\n<link rel="stylesheet" href="assets/pina-portada.css?v=1">#' index.html
grep -q 'pina-portada.css' en/index.html || sed -i 's#<link rel="stylesheet" href="../assets/estilo.css">#&\n<link rel="stylesheet" href="../assets/pina-portada.css?v=1">#' en/index.html
sed -i '/=== diseno Sala de museo para toda la web/,/=== fin diseno Sala ===/d' assets/estilo.css
cat _diseno/bloque-sala.css >> assets/estilo.css
date > _diseno/hecho.txt
grep -c 'pina-portada.css' index.html en/index.html >> _diseno/hecho.txt
wc -c assets/estilo.css "$C/assets/estilo.css" assets/pina-portada.css index.html en/index.html >> _diseno/hecho.txt
grep -c 'diseno Sala' assets/estilo.css >> _diseno/hecho.txt

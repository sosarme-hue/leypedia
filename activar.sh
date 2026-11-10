#!/bin/bash
# Filopedia: activa el diseno C "Ensayo" en la portada (ES y EN). Uso unico, 10-11-2026.
R=/home/u235595016/domains/filopedia.com/public_html
C=/home/u235595016/domains/filopedia.com/copias-diseno/2026-11-10
cd "$R" || exit 1
if [ ! -f "$C/index.html" ]; then
  mkdir -p "$C/en" "$C/assets"
  cp -p index.html "$C/index.html"
  cp -p en/index.html "$C/en/index.html"
  [ -f assets/filo-portada.css ] && cp -p assets/filo-portada.css "$C/assets/filo-portada.css"
fi
cp _diseno/filo-portada.css assets/filo-portada.css
grep -q 'filo-portada.css' index.html || sed -i 's#<link rel="stylesheet" href="assets/filo2.css?v=2">#&\n<link rel="stylesheet" href="assets/filo-portada.css?v=1">#' index.html
grep -q 'filo-portada.css' en/index.html || sed -i 's#<link rel="stylesheet" href="../assets/filo2.css?v=2">#&\n<link rel="stylesheet" href="../assets/filo-portada.css?v=1">#' en/index.html
date > _diseno/hecho.txt
grep -c 'filo-portada.css' index.html en/index.html >> _diseno/hecho.txt
# version del estilo (para que los navegadores bajen el nuevo)
sed -i 's#filo-portada.css?v=[0-9]*#filo-portada.css?v=2#' index.html en/index.html
grep -o 'filo-portada.css?v=[0-9]*' index.html en/index.html >> _diseno/hecho.txt

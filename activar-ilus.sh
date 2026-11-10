R=/home/u235595016/domains/filopedia.com/public_html
C=/home/u235595016/domains/filopedia.com/copias-diseno/2026-11-10-ilus
cd "$R" || exit 1
if [ ! -f "$C/estilo.css" ]; then mkdir -p "$C"; cp -p assets/estilo.css "$C/estilo.css"; fi
mkdir -p img/ilus
cp -p _diseno/ilus/*.jpg img/ilus/
sed -i '/=== ilustraciones por seccion/,/=== fin ilustraciones ===/d' assets/estilo.css
cat _diseno/bloque-ilus.css >> assets/estilo.css
{ date; ls img/ilus | wc -l; wc -c assets/estilo.css; } > _diseno/hecho-ilus.txt

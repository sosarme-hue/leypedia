# Classicapedia · limpieza para AdSense (rama de subida, no fusionar)

AdSense rechazó classicapedia.com por «contenido de poco valor» (18-11-2026). La causa principal son los posts de /p/
que solo tienen un título y el botón de Patreon, o un vídeo de YouTube y una línea.

Se despliega en Hostinger en la carpeta `_limpieza/` de classicapedia.com (hosting_git_deploy-website-repository).
La carpeta no es accesible desde la web (`.htaccess`). Se ejecuta desde una tarea programada (`/usr/bin/php .../_limpieza/aplicar.php <modo>`).

- `aplicar.php prueba`: no toca la web. Escribe `informe-prueba.json` y `lista-noindex.txt`.
- `aplicar.php aplicar`: añade `<meta name="robots" content="noindex, follow">` a los posts de /p/ y /en/p/ con menos de 100 palabras
  propias (sin contar el botón de Patreon, la foto ni el vídeo) y a las biografías de /b/ y /en/b/ con menos de 80; quita esas URL
  de `sitemap-auto-1.xml`, `sitemap-auto-2.xml`, `sitemap-es.xml` y `sitemap-en.xml`; convierte los «<h3>* …</h3>» seguidos en listas.
  No borra ninguna página. Copia de cada archivo cambiado en `copias/`, resumen en `hecho.txt` e `informe-aplicado.json`.
- `deshacer.php`: copia `copias/` sobre la raíz.
- Si algún día se regenera la web con el generador original, hay que volver a ejecutar `aplicar.php aplicar` (borrando antes `hecho.txt`).

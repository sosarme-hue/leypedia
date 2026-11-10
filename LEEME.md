# Classicapedia · blog (rama de subida, no fusionar)

Se despliega en Hostinger en la carpeta `_blog/` de classicapedia.com (hosting_git_deploy-website-repository).
La carpeta no es accesible desde la web (`.htaccess`).

- `payload/blog/` y `payload/en/blog/`: el blog en español e inglés (3 artículos + portada en cada idioma). Se generan con `gen.py` a partir de `contenido/`.
- `aplicar.php`: se ejecuta una vez desde una tarea programada (`php .../_blog/aplicar.php`). Copia el blog a `/blog/` y `/en/blog/`,
  añade al final de `assets/ga.js` y `en/assets/ga.js` el código de `menu-blog.js` (enlace «Blog» en el menú de todas las páginas)
  y añade las URL del blog a `sitemap-es.xml` y `sitemap-en.xml`. Guarda copias en `copias/` y el resultado en `hecho.txt`.
- Para deshacer: copiar `copias/` sobre la raíz y borrar `/blog/` y `/en/blog/`.

## Publicación programada (desde el 10-11-2026)

- `publicar.php` lo ejecuta cada día a las 06:05 una tarea programada de Hostinger (`/usr/bin/php .../_blog/publicar.php`).
- Lee `manifiesto.json` y publica en `/blog/` y `/en/blog/` los artículos cuya fecha ya ha llegado (uno cada martes, del 17-11-2026 al 05-01-2027).
  Nunca sobrescribe un artículo publicado. Cambia la portada del blog por la de `payload/indices/<idioma>/<fecha>.html` y añade las URL a los sitemaps.
- Copias de lo que cambia en `copias/<fecha>/` y registro en `publicaciones.log`.
- Para añadir artículos: escribir `contenido/es|en/<clave>.html`, darlos de alta en `gen.py` (ART, ORDEN, FECHAS), ejecutar `python3 gen.py`, subir y volver a desplegar `_blog`.

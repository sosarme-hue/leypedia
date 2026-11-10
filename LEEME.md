# Classicapedia · blog (rama de subida, no fusionar)

Se despliega en Hostinger en la carpeta `_blog/` de classicapedia.com (hosting_git_deploy-website-repository).
La carpeta no es accesible desde la web (`.htaccess`).

- `payload/blog/` y `payload/en/blog/`: el blog en español e inglés (3 artículos + portada en cada idioma). Se generan con `gen.py` a partir de `contenido/`.
- `aplicar.php`: se ejecuta una vez desde una tarea programada (`php .../_blog/aplicar.php`). Copia el blog a `/blog/` y `/en/blog/`,
  añade al final de `assets/ga.js` y `en/assets/ga.js` el código de `menu-blog.js` (enlace «Blog» en el menú de todas las páginas)
  y añade las URL del blog a `sitemap-es.xml` y `sitemap-en.xml`. Guarda copias en `copias/` y el resultado en `hecho.txt`.
- Para deshacer: copiar `copias/` sobre la raíz y borrar `/blog/` y `/en/blog/`.

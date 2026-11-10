# Blog de CatDogPedia (rama de despliegue)

Esta rama solo contiene la carpeta `_blog` de catdogpedia.com. Hostinger la despliega por Git en `public_html/_blog` y nada más.
La carpeta está protegida con `.htaccess` (Require all denied).

- `aplicar.php` (una sola vez, tarea programada): añade «Blog» al menú de todas las páginas y ejecuta `publicar.php`.
- `publicar.php` (cada día, tarea programada): publica los artículos cuya fecha ha llegado (nunca sobrescribe uno ya publicado),
  pone la portada del blog, la portada de la web y el buscador de esa fecha (una sola vez por versión) y añade las URL a `sitemap.xml`.
- Generado con `gen_web.py` de CatDogPedia (`BLOG_PAQUETE=… python3 -I gen_web.py datos salida`).

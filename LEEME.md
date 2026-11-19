# Blogs de Pinacopedia y Culinapedia (rama de subida, no fusionar)

Se despliega con hosting_git_deploy-website-repository en la carpeta `_blog/` de pinacopedia.com y de culinapedia.com.
La carpeta no es accesible desde la web (`.htaccess`). Cada web usa solo su subcarpeta: `_blog/pinacopedia/` o `_blog/culinapedia/`.

- `<web>/payload/`: artículos (blog/ y en/blog/), portadas por fecha (indices/es|en/<fecha>.html) e imágenes propias (blog/img/).
- `<web>/manifiesto.json`: fecha de cada artículo, archivos, URL y JS común donde va el enlace «Blog».
- `<web>/publicar.php`: lo ejecuta cada hora una tarea programada de Hostinger. Es idempotente. Publica los artículos cuya fecha ha llegado
  (3 el 19-11-2026 y uno cada martes del 24-11-2026 al 12-01-2027), cambia la portada del blog, añade una vez el enlace «Blog»
  al final de `assets/busca.js` (Pinacopedia) o `assets/familia.js` (Culinapedia), escribe `sitemap-blog.xml` y lo añade al índice `sitemap.xml`.
  Nunca sobrescribe un artículo publicado ni borra nada. Copias en `copias/<fecha>/`, registro en `publicaciones.log`.
- `fuente/`: textos (`<web>/contenido/es|en/<clave>.html`), configuración (`sitios.py`) y generador (`gen.py <web>`, `vista.py`).
  Para añadir artículos: escribir los textos, darlos de alta en `sitios.py`, `python3 gen.py <web>`, copiar payload y manifiesto (con `js_menu`) y volver a desplegar.
- Para deshacer: restaurar desde `copias/` el JS y `sitemap.xml`, y borrar `/blog/`, `/en/blog/` y `sitemap-blog.xml`.

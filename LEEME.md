# Classicapedia · nuevo diseño de la portada (rama de subida, no fusionar)

Se despliega en Hostinger en la carpeta `_portada/` de classicapedia.com (hosting_git_deploy-website-repository).
La carpeta no es accesible desde la web (`.htaccess`).

- `portada-c.css`: estilo «Contrapunto» (solo CSS). Fuentes Fraunces alojadas en el propio servidor.
- `aplicar.php`: se ejecuta una vez desde una tarea programada (`php .../_portada/aplicar.php`). Copia el CSS y las fuentes
  a `assets/` y `en/assets/` y añade una línea `<link>` en `index.html` y `en/index.html`. Copias en `copias/`, resultado en `hecho.txt`.
- Para deshacer: ejecutar `deshacer.php` (quita la línea `<link>`), o copiar `copias/` sobre la raíz.
- `aplicar2.php`: quita la numeración de las secciones de la portada (copia portada-c.css y pasa ?v=1 a ?v=2).
- `aplicar3.php`: diseño «Ficha» para las biografías; añade `bio-c.css` al final de `assets/estilo.css` y `en/assets/estilo.css`
  (copias en `copias/`). Para deshacer: copiar `copias/assets/estilo.css` y `copias/en/assets/estilo.css` a su sitio.
- `aplicar-23.php`: ejecuta los dos anteriores seguidos.

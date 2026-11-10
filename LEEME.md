# Classicapedia · alta en Google AdSense (rama de subida, no fusionar)

Se despliega en Hostinger en la carpeta `_adsense/` de classicapedia.com (hosting_git_deploy-website-repository).

- `payload/`: archivos que se copian a la raíz de la web: código de AdSense en `index.html` y `en/index.html`,
  `assets/ga.js` y `en/assets/ga.js` (AdSense en todas las páginas, Analytics según el aviso de consentimiento de Google,
  «Configurar cookies» abre ese aviso, enlace a Contacto en el pie), `ads.txt`, `contacto.html` y textos de privacidad,
  cookies, aviso legal y «Quién soy».
- `aplicar.php?k=…`: copia `payload/` sobre la raíz solo si los archivos no han cambiado desde que se prepararon
  (huellas en `originales.json`). Guarda una copia de cada archivo sustituido en `copias/`. Se borra a sí mismo al terminar.
- Para deshacer: copiar `copias/` sobre la raíz.

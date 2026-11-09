# Leypedia: código fuente

La web publicada son los archivos de la raíz. Se generan con:

    python3 _fuente/build.py <carpeta_salida>

- `content.py` y `pages2.py`: textos de cada página en castellano y catalán.
- `app.js`: generador de contratos (solo en el navegador) y lectura del BOE.
- `boe.php`: lee la API de datos abiertos del BOE y guarda una copia diaria en `api/cache`.
- `htaccess`: cabeceras de seguridad y redirección a https.

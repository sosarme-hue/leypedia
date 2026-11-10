<?php
// Ejecuta los cambios 2 (portada sin numeración) y 3 (biografías «Ficha») en una sola pasada.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
if (!file_exists(__DIR__ . '/hecho3.txt')) {
  if (!file_exists(__DIR__ . '/hecho2.txt')) { (function () { require __DIR__ . '/aplicar2.php'; })(); }
  (function () { require __DIR__ . '/aplicar3.php'; })();
} else echo "Ya se aplico antes.\n";

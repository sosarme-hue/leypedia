<?php
// Ejecuta los cambios 2 (portada sin numeración) y 3 (biografías «Ficha») en una sola pasada.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
foreach (['aplicar2.php', 'aplicar3.php'] as $s) passthru(PHP_BINARY . ' ' . escapeshellarg(__DIR__ . "/$s"));

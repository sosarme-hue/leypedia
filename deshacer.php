<?php
// Vuelve a la portada anterior: quita la línea de portada-c.css de index.html y en/index.html. No borra nada más.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$raiz = dirname(__DIR__); $log = [];
foreach (['index.html', 'en/index.html'] as $p) {
  $t = "$raiz/$p"; $c = file_get_contents($t);
  $n = preg_replace('#\n<link rel="stylesheet" href="assets/portada-c\.css[^"]*">#', '', $c);
  if ($n !== $c && file_put_contents($t, $n) !== false) $log[] = "quitado de $p"; else $log[] = "$p sin cambios";
}
$r = date('c') . "\n" . implode("\n", $log) . "\n"; file_put_contents(__DIR__ . '/deshecho.txt', $r); echo $r;

<?php
// Cambio 2 (10-11-2026): quita la numeración de las secciones. Copia portada-c.css a assets/ y en/assets/
// y cambia ?v=1 por ?v=2 en index.html y en/index.html para que los navegadores carguen la versión nueva.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$aqui = __DIR__; $raiz = dirname($aqui);
if (file_exists("$aqui/hecho2.txt")) exit("Ya se aplico antes.\n");
$log = []; $err = [];
foreach (['assets', 'en/assets'] as $d) {
  if (@copy("$aqui/portada-c.css", "$raiz/$d/portada-c.css")) $log[] = "copiado $d/portada-c.css"; else $err[] = "no se pudo copiar $d/portada-c.css";
}
foreach (['index.html', 'en/index.html'] as $p) {
  $t = "$raiz/$p"; $c = file_get_contents($t);
  $n = str_replace('assets/portada-c.css?v=1', 'assets/portada-c.css?v=2', $c);
  if ($n === $c) { $log[] = "$p sin cambios"; continue; }
  if (file_put_contents($t, $n) !== false) $log[] = "version actualizada en $p"; else $err[] = "no se pudo escribir $p";
}
$r = date('c') . "\nHECHO:\n" . implode("\n", $log) . "\nERRORES:\n" . implode("\n", $err) . "\n";
file_put_contents("$aqui/hecho2.txt", $r); echo $r;

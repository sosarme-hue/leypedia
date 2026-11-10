<?php
// Cambio 4: corrige el bloque «diseño Ficha» de estilo.css (la primera regla estaba rota). Sustituye solo lo que hay entre las marcas.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$aqui = __DIR__; $raiz = dirname($aqui);
if (file_exists("$aqui/hecho4.txt")) exit("Ya se aplico antes.\n");
$ini = "/* === diseño Ficha para biografías (nov 2026) === */"; $fin = "/* === fin diseño Ficha === */";
$nuevo = $ini . "\n" . file_get_contents("$aqui/bio-c.css") . "\n" . $fin;
$log = []; $err = [];
foreach (['assets/estilo.css', 'en/assets/estilo.css'] as $p) {
  $t = "$raiz/$p"; $c = file_get_contents($t);
  $a = strpos($c, $ini); $b = strpos($c, $fin);
  if ($a === false || $b === false) { $err[] = "$p: no encuentro las marcas"; continue; }
  $c2 = substr($c, 0, $a) . $nuevo . substr($c, $b + strlen($fin));
  if (file_put_contents($t, $c2) !== false) $log[] = "corregido $p"; else $err[] = "no se pudo escribir $p";
}
$r = date('c') . "\nHECHO:\n" . implode("\n", $log) . "\nERRORES:\n" . implode("\n", $err) . "\n";
file_put_contents("$aqui/hecho4.txt", $r); echo $r;

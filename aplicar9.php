<?php
// Cambio 8: añade (o sustituye) el bloque «diseño resto de páginas» al final de estilo.css (ES y EN). Copia de seguridad en copias/.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$aqui = __DIR__; $raiz = dirname($aqui);
if (file_exists("$aqui/hecho9.txt")) exit("Ya se aplico antes.\n");
$ini = "/* === diseño Comunidad, Comparador, Quiz y Blog (nov 2026) === */"; $fin = "/* === fin diseño Comunidad, Comparador, Quiz y Blog === */";
$nuevo = trim(file_get_contents("$aqui/extra-c.css"));
if (strpos($nuevo, $ini) !== 0) exit("extra-c.css no empieza por la marca\n");
@mkdir("$aqui/copias");
$log = []; $err = [];
foreach (['assets/estilo.css', 'en/assets/estilo.css'] as $p) {
  $t = "$raiz/$p"; $c = file_get_contents($t);
  if ($c === false) { $err[] = "$p: no se puede leer"; continue; }
  copy($t, "$aqui/copias/" . str_replace('/', '_', $p) . ".antes9");
  $a = strpos($c, $ini); $b = strpos($c, $fin);
  if ($a !== false && $b !== false) $c2 = substr($c, 0, $a) . $nuevo . substr($c, $b + strlen($fin));
  else $c2 = rtrim($c) . "\n" . $nuevo . "\n";
  if (file_put_contents($t, $c2) !== false) $log[] = "actualizado $p (" . strlen($c2) . " bytes)"; else $err[] = "no se pudo escribir $p";
}
$r = date('c') . "\nHECHO:\n" . implode("\n", $log) . "\nERRORES:\n" . implode("\n", $err) . "\n";
file_put_contents("$aqui/hecho9.txt", $r); echo $r;

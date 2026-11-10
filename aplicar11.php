<?php
// Cambio 11: deshace el cambio 10 (títulos en Bodoni). Vuelve a «font-family:Fraunces» y quita el bloque Bodoni de estilo.css (ES y EN).
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$aqui = __DIR__; $raiz = dirname($aqui);
if (file_exists("$aqui/hecho11.txt")) exit("Ya se aplico antes.\n");
$ini = "/* === tipografía Bodoni en títulos (nov 2026) === */"; $fin = "/* === fin tipografía Bodoni === */";
@mkdir("$aqui/copias");
$log = []; $err = [];
foreach (['assets/estilo.css', 'en/assets/estilo.css'] as $p) {
  $t = "$raiz/$p"; $c = file_get_contents($t);
  if ($c === false) { $err[] = "$p: no se puede leer"; continue; }
  copy($t, "$aqui/copias/" . str_replace('/', '_', $p) . ".antes11");
  $c = str_replace("font-family:'Bodoni Moda',Fraunces", 'font-family:Fraunces', $c, $n);
  $a = strpos($c, $ini); $b = strpos($c, $fin);
  if ($a !== false && $b !== false) $c = rtrim(substr($c, 0, $a)) . "\n" . ltrim(substr($c, $b + strlen($fin)));
  else $err[] = "$p: no encuentro el bloque Bodoni";
  if (file_put_contents($t, $c) !== false) $log[] = "actualizado $p ($n cambios, " . strlen($c) . " bytes)"; else $err[] = "no se pudo escribir $p";
}
$r = date('c') . "\nHECHO:\n" . implode("\n", $log) . "\nERRORES:\n" . implode("\n", $err) . "\n";
file_put_contents("$aqui/hecho11.txt", $r); echo $r;

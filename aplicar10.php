<?php
// Cambio 10: títulos en Bodoni Moda. Copia las fuentes a assets/ y en/assets/, cambia «font-family:Fraunces» por
// «font-family:'Bodoni Moda',Fraunces» en estilo.css (ES y EN) y añade el bloque bodoni-c.css (fuentes + texto y logo en Fraunces).
// Solo CSS. Copia de seguridad en copias/ (.antes10). Para deshacer: restaurar esas copias.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$aqui = __DIR__; $raiz = dirname($aqui);
if (file_exists("$aqui/hecho10.txt")) exit("Ya se aplico antes.\n");
$ini = "/* === tipografía Bodoni en títulos (nov 2026) === */"; $fin = "/* === fin tipografía Bodoni === */";
$nuevo = trim(file_get_contents("$aqui/bodoni-c.css"));
if (strpos($nuevo, $ini) !== 0) exit("bodoni-c.css no empieza por la marca\n");
@mkdir("$aqui/copias");
$log = []; $err = [];
foreach (['assets', 'en/assets'] as $d) foreach (['bodoni-latin.woff2', 'bodoni-latin-ext.woff2'] as $a) {
  if (@copy("$aqui/$a", "$raiz/$d/$a")) $log[] = "copiado $d/$a"; else $err[] = "no se pudo copiar $d/$a";
}
foreach (['assets/estilo.css', 'en/assets/estilo.css'] as $p) {
  $t = "$raiz/$p"; $c = file_get_contents($t);
  if ($c === false) { $err[] = "$p: no se puede leer"; continue; }
  copy($t, "$aqui/copias/" . str_replace('/', '_', $p) . ".antes10");
  $n = 0;
  if (strpos($c, "'Bodoni Moda',Fraunces") === false) $c = str_replace('font-family:Fraunces', "font-family:'Bodoni Moda',Fraunces", $c, $n);
  $a = strpos($c, $ini); $b = strpos($c, $fin);
  if ($a !== false && $b !== false) $c2 = substr($c, 0, $a) . $nuevo . substr($c, $b + strlen($fin));
  else $c2 = rtrim($c) . "\n" . $nuevo . "\n";
  if (file_put_contents($t, $c2) !== false) $log[] = "actualizado $p ($n cambios, " . strlen($c2) . " bytes)"; else $err[] = "no se pudo escribir $p";
}
$r = date('c') . "\nHECHO:\n" . implode("\n", $log) . "\nERRORES:\n" . implode("\n", $err) . "\n";
file_put_contents("$aqui/hecho10.txt", $r); echo $r;

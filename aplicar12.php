<?php
// Cambio 12: títulos en Cormorant Garamond (sustituye a Bodoni). Copia las fuentes, cambia la familia en estilo.css (ES y EN)
// y sustituye el bloque Bodoni por cormorant-c.css. Solo CSS. Copia en copias/ (.antes12).
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$aqui = __DIR__; $raiz = dirname($aqui);
if (file_exists("$aqui/hecho12.txt")) exit("Ya se aplico antes.\n");
$bloques = [["/* === tipografía Bodoni en títulos (nov 2026) === */", "/* === fin tipografía Bodoni === */"], ["/* === tipografía de títulos (nov 2026) === */", "/* === fin tipografía de títulos === */"]];
$nuevo = trim(file_get_contents("$aqui/cormorant-c.css"));
if (strpos($nuevo, $bloques[1][0]) !== 0) exit("cormorant-c.css no empieza por la marca\n");
@mkdir("$aqui/copias");
$log = []; $err = [];
foreach (['assets', 'en/assets'] as $d) foreach (['cormorant-latin.woff2', 'cormorant-latin-ext.woff2'] as $a) {
  if (@copy("$aqui/$a", "$raiz/$d/$a")) $log[] = "copiado $d/$a"; else $err[] = "no se pudo copiar $d/$a";
}
foreach (['assets/estilo.css', 'en/assets/estilo.css'] as $p) {
  $t = "$raiz/$p"; $c = file_get_contents($t);
  if ($c === false) { $err[] = "$p: no se puede leer"; continue; }
  copy($t, "$aqui/copias/" . str_replace('/', '_', $p) . ".antes12");
  $c = str_replace("font-family:'Bodoni Moda',Fraunces", 'font-family:Fraunces', $c);
  $c = str_replace('font-family:Fraunces', "font-family:'Cormorant Garamond',Fraunces", $c, $n);
  foreach ($bloques as $bl) { $a = strpos($c, $bl[0]); $b = strpos($c, $bl[1]);
    if ($a !== false && $b !== false) $c = rtrim(substr($c, 0, $a)) . "\n" . ltrim(substr($c, $b + strlen($bl[1]))); }
  $c = rtrim($c) . "\n" . $nuevo . "\n";
  if (file_put_contents($t, $c) !== false) $log[] = "actualizado $p ($n cambios, " . strlen($c) . " bytes)"; else $err[] = "no se pudo escribir $p";
}
$r = date('c') . "\nHECHO:\n" . implode("\n", $log) . "\nERRORES:\n" . implode("\n", $err) . "\n";
file_put_contents("$aqui/hecho12.txt", $r); echo $r;

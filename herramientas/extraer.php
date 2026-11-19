<?php
// Copia la cabecera y el pie de algunas páginas a _blog/extraido/ sin claves (para hacer la plantilla del blog).
// Uso: php extraer.php ruta1 ruta2 ...  (rutas relativas a public_html)
$raiz = dirname(__DIR__, 2); $out = dirname(__DIR__) . '/extraido'; @mkdir($out);
foreach (array_slice($argv, 1) as $rel) {
  $c = @file_get_contents("$raiz/$rel"); if ($c === false) { echo "no existe $rel\n"; continue; }
  $m = strpos($c, '<main'); $f = strrpos($c, '<footer');
  $t = substr($c, 0, $m === false ? 6000 : $m) . "\n<!-- ===== MAIN (" . strlen($c) . " bytes) ===== -->\n" . substr($c, $m, 1500) . "\n<!-- ===== PIE ===== -->\n" . ($f === false ? substr($c, -6000) : substr($c, $f));
  $t = preg_replace('/AIza[0-9A-Za-z_\-]{30,}/', 'CLAVE_QUITADA', $t);
  $t = preg_replace('/(GK\s*=\s*)["\'][^"\']*["\']/', '$1"CLAVE_QUITADA"', $t);
  $t = preg_replace('/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}/', 'correo@quitado', $t);
  $t = preg_replace('/\+?\d[\d \-]{7,}\d/', 'TEL', $t);
  file_put_contents("$out/" . str_replace('/', '_', $rel) . '.txt', $t); echo "ok $rel\n";
}

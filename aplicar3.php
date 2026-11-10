<?php
// Cambio 3 (10-11-2026): diseño «Ficha» para las biografías (b/ y en/b/).
// Añade al final de assets/estilo.css y en/assets/estilo.css el contenido de bio-c.css. Todas sus reglas empiezan por
// body:has(article.ficha[class*=" p-"]), así que solo afectan a las páginas de biografía. Copia previa en copias/.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$aqui = __DIR__; $raiz = dirname($aqui);
if (file_exists("$aqui/hecho3.txt")) exit("Ya se aplico antes.\n");
$marca = "/* === diseño Ficha para biografías (nov 2026) === */";
$add = "\n$marca\n" . file_get_contents("$aqui/bio-c.css") . "\n/* === fin diseño Ficha === */\n";
$log = []; $err = [];
foreach (['assets/estilo.css', 'en/assets/estilo.css'] as $p) {
  $t = "$raiz/$p"; if (!file_exists($t)) { $err[] = "falta $p"; continue; }
  $c = file_get_contents($t);
  if (strpos($c, $marca) !== false) { $log[] = "$p ya lo tenia"; continue; }
  @mkdir(dirname("$aqui/copias/$p"), 0755, true); copy($t, "$aqui/copias/$p");
  if (file_put_contents($t, rtrim($c) . "\n" . $add) !== false) $log[] = "añadido en $p"; else $err[] = "no se pudo escribir $p";
}
$r = date('c') . "\nHECHO:\n" . implode("\n", $log) . "\nERRORES:\n" . implode("\n", $err) . "\n";
file_put_contents("$aqui/hecho3.txt", $r); echo $r;

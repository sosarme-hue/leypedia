<?php
// Classicapedia · nuevo diseño de la portada («Contrapunto»). Solo se ejecuta desde la línea de comandos (tarea programada).
// 1) Copia portada-c.css y las fuentes Fraunces a assets/ y en/assets/ (archivos nuevos).
// 2) En index.html y en/index.html añade UNA línea <link> a portada-c.css justo después de la de estilo.css.
// No cambia textos, URLs, metadatos, AdSense, cookies ni sitemaps. Guarda copia de index.html en copias/ antes de tocarlo.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$aqui = __DIR__; $raiz = dirname($aqui);
if (file_exists("$aqui/hecho.txt")) exit("Ya se aplico antes. No se ha tocado nada.\n");
$log = []; $err = [];
$archivos = ['portada-c.css', 'fraunces-latin.woff2', 'fraunces-latin-ext.woff2'];
foreach (['assets', 'en/assets'] as $d) {
  if (!is_dir("$raiz/$d")) { $err[] = "falta $d"; continue; }
  foreach ($archivos as $a) {
    if (@copy("$aqui/$a", "$raiz/$d/$a")) $log[] = "copiado $d/$a"; else $err[] = "no se pudo copiar $d/$a";
  }
}
$linea = '<link rel="stylesheet" href="assets/estilo.css">';
$nueva = $linea . "\n" . '<link rel="stylesheet" href="assets/portada-c.css?v=1">';
foreach (['index.html', 'en/index.html'] as $p) {
  $t = "$raiz/$p"; if (!file_exists($t)) { $err[] = "falta $p"; continue; }
  $c = file_get_contents($t);
  if (strpos($c, 'portada-c.css') !== false) { $log[] = "$p ya tenia el enlace"; continue; }
  if (substr_count($c, $linea) !== 1) { $err[] = "$p: no encuentro la linea de estilo.css (no se toca)"; continue; }
  @mkdir(dirname("$aqui/copias/$p"), 0755, true); copy($t, "$aqui/copias/$p");
  if (file_put_contents($t, str_replace($linea, $nueva, $c)) !== false) $log[] = "enlace añadido en $p"; else $err[] = "no se pudo escribir $p";
}
$r = date('c') . "\nHECHO:\n" . implode("\n", $log) . "\nERRORES:\n" . implode("\n", $err) . "\n";
file_put_contents("$aqui/hecho.txt", $r);
echo $r;

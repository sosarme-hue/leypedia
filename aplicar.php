<?php
// Classicapedia · limpieza para AdSense («contenido de poco valor»). Solo desde la línea de comandos (tarea programada).
//   php aplicar.php prueba   -> no toca la web: escribe informe-prueba.json y lista-noindex.txt
//   php aplicar.php aplicar  -> añade <meta name="robots" content="noindex, follow"> a las páginas sin texto propio,
//                               quita esas URL de los sitemaps y convierte los «<h3>* …</h3>» en listas.
// Guarda una copia de cada archivo antes de cambiarlo en copias/. No borra ninguna página.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
set_time_limit(0); ini_set('memory_limit', '1024M');
const P_MIN = 100;  // posts (/p/): menos palabras propias que esto -> noindex
const B_MIN = 80;   // biografías (/b/): menos palabras que esto -> noindex
const META = '<meta name="robots" content="noindex, follow">';
$modo = $argv[1] ?? 'prueba';
$aqui = __DIR__; $raiz = getenv('LIMPIEZA_RAIZ') ?: dirname($aqui);
if ($modo === 'prueba' && file_exists("$aqui/informe-prueba.json")) exit("prueba ya hecha\n");
if ($modo === 'aplicar' && file_exists("$aqui/hecho.txt")) exit("ya aplicado\n");
if (!in_array($modo, ['prueba', 'aplicar'])) exit("modo desconocido\n");

function palabras($html) {
  $t = html_entity_decode(strip_tags(preg_replace('~<(br|/p|/li|/h\d)[^>]*>~i', ' $0', $html)), ENT_QUOTES | ENT_HTML5, 'UTF-8');
  return preg_match_all('~[\p{L}\p{N}]+~u', $t);
}
function texto_propio($html, $tipo) {
  $a = strpos($html, '<div class="texto">'); if ($a === false) return '';
  $b = strpos($html, '</article>', $a); $t = substr($html, $a, $b === false ? null : $b - $a);
  $t = preg_replace('~<p class="patreon">.*?</p>~s', '', $t);
  $t = preg_replace('~<figure.*?</figure>~s', '', $t);
  $t = preg_replace('~<div class="video".*?</button></div>~s', '', $t);
  if ($tipo === 'b') $t = preg_replace('~<section id="maestros".*?</section>~s', '', $t);
  return $t;
}
function arreglar_h3($html, &$n) {
  return preg_replace_callback('~(?:<h3>\*\s*(?:(?!</h3>).)*</h3>\s*)+~su', function ($m) use (&$n) {
    preg_match_all('~<h3>\*\s*((?:(?!</h3>).)*)</h3>~su', $m[0], $it); $n++;
    return '<ul>' . implode('', array_map(fn($x) => '<li>' . trim($x) . '</li>', $it[1])) . '</ul>';
  }, $html);
}
$copia = function ($rel) use ($aqui, $raiz) {
  $c = "$aqui/copias/$rel"; @mkdir(dirname($c), 0755, true);
  if (!file_exists($c)) copy("$raiz/$rel", $c);
};

$inf = ['modo' => $modo, 'fecha' => date('c'), 'umbral' => ['p' => P_MIN, 'b' => B_MIN], 'carpetas' => [], 'h3_paginas' => 0, 'h3_listas' => 0, 'ya_noindex' => 0, 'errores' => []];
$noindex = []; $muestras = [];
foreach (['p', 'b', 'en/p', 'en/b'] as $dir) {
  $tipo = substr($dir, -1); $min = $tipo === 'p' ? P_MIN : B_MIN;
  $hist = ['0' => 0, '1-49' => 0, '50-99' => 0, '100-199' => 0, '200+' => 0]; $tot = 0; $oc = 0;
  foreach (glob("$raiz/$dir/*.html") as $f) {
    $rel = "$dir/" . basename($f); $html = file_get_contents($f); $tot++;
    $w = palabras(texto_propio($html, $tipo));
    $hist[$w == 0 ? '0' : ($w < 50 ? '1-49' : ($w < 100 ? '50-99' : ($w < 200 ? '100-199' : '200+')))]++;
    $nuevo = $html; $nh = 0;
    if ($tipo === 'p') $nuevo = arreglar_h3($nuevo, $nh);
    $poner = $w < $min;
    if (stripos($html, 'name="robots"') !== false) { $inf['ya_noindex']++; $poner = false; }
    if ($poner) {
      $noindex[] = $rel; $oc++;
      if (count($muestras[$dir] ?? []) < 15) $muestras[$dir][] = "$rel ($w palabras)";
      $nuevo = preg_replace('~(<meta name="viewport"[^>]*>)~', "$1\n" . META, $nuevo, 1);
    }
    if ($nh) { $inf['h3_paginas']++; $inf['h3_listas'] += $nh; if (count($muestras['h3'] ?? []) < 15) $muestras['h3'][] = $rel; }
    if ($modo === 'aplicar' && $nuevo !== $html) {
      $copia($rel);
      if (file_put_contents($f, $nuevo) === false) $inf['errores'][] = "no se pudo escribir $rel";
    }
  }
  $inf['carpetas'][$dir] = ['paginas' => $tot, 'noindex' => $oc, 'palabras' => $hist];
}
// sitemaps
$fuera = array_flip(array_map(fn($r) => "https://classicapedia.com/$r", $noindex));
foreach (['sitemap-auto-1.xml', 'sitemap-auto-2.xml', 'sitemap-es.xml', 'sitemap-en.xml'] as $s) {
  $t = "$raiz/$s"; if (!file_exists($t)) continue;
  $lin = explode("\n", file_get_contents($t)); $quedan = []; $q = 0;
  foreach ($lin as $l) {
    if (preg_match('~<loc>([^<]+)</loc>~', $l, $m) && isset($fuera[$m[1]])) { $q++; continue; }
    $quedan[] = $l;
  }
  $inf['sitemaps'][$s] = ['quitadas' => $q, 'quedan' => substr_count(implode("\n", $quedan), '<loc>')];
  if ($modo === 'aplicar' && $q) { $copia($s); if (file_put_contents($t, implode("\n", $quedan)) === false) $inf['errores'][] = "no se pudo escribir $s"; }
}
$inf['total_noindex'] = count($noindex); $inf['muestras'] = $muestras;
file_put_contents("$aqui/lista-noindex.txt", implode("\n", $noindex) . "\n");
file_put_contents("$aqui/" . ($modo === 'aplicar' ? 'informe-aplicado.json' : 'informe-prueba.json'), json_encode($inf, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES));
if ($modo === 'aplicar') file_put_contents("$aqui/hecho.txt", date('c') . ' · noindex: ' . count($noindex) . ' · errores: ' . count($inf['errores']) . "\n");
echo "$modo: noindex " . count($noindex) . ", h3 " . $inf['h3_paginas'] . ", errores " . count($inf['errores']) . "\n";

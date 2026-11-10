<?php
// Classicapedia · publicador semanal del blog. Solo desde la línea de comandos (tarea programada de Hostinger, los martes).
// Publica los artículos de manifiesto.json cuya fecha ya ha llegado: los copia a /blog/ y /en/blog/ si todavía no existen
// (nunca sobrescribe un artículo publicado), pone la portada del blog que corresponde a la fecha y añade las URL nuevas a los sitemaps.
// Guarda una copia de cada portada y sitemap antes de cambiarlos (copias/AAAA-MM-DD/) y anota todo en publicaciones.log. No borra nada.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
date_default_timezone_set('Europe/Madrid');
$aqui = __DIR__; $raiz = dirname($aqui); $hoy = getenv('BLOG_HOY') ?: date('Y-m-d');
$m = json_decode(file_get_contents("$aqui/manifiesto.json"), true);
$log = []; $err = []; $nuevas = [];
$copia = function ($rel) use ($aqui, $raiz, $hoy) {
  $c = "$aqui/copias/$hoy/$rel"; @mkdir(dirname($c), 0755, true);
  if (!file_exists($c)) copy("$raiz/$rel", $c);
};
// 1) artículos
foreach ($m['articulos'] as $a) {
  if ($a['fecha'] > $hoy) continue;
  foreach ($a['archivos'] as $i => $rel) {
    $t = "$raiz/$rel";
    if (file_exists($t)) continue;
    @mkdir(dirname($t), 0755, true);
    if (@copy("$aqui/payload/$rel", $t)) { $log[] = "publicado $rel"; $nuevas[] = $a['urls'][$i]; }
    else $err[] = "no se pudo copiar $rel";
  }
}
// 2) portada del blog
$f = null; foreach ($m['indices'] as $x) if ($x <= $hoy) $f = $x;
if ($f) foreach (['es' => 'blog/index.html', 'en' => 'en/blog/index.html'] as $l => $rel) {
  $src = "$aqui/payload/indices/$l/$f.html"; $t = "$raiz/$rel";
  if (file_exists($t) && md5_file($t) === md5_file($src)) continue;
  if (file_exists($t)) $copia($rel);
  if (@copy($src, $t)) $log[] = "portada $rel actualizada ($f)"; else $err[] = "no se pudo escribir $rel";
}
// 3) sitemaps
foreach (['sitemap-es.xml' => 'https://classicapedia.com/blog/', 'sitemap-en.xml' => 'https://classicapedia.com/en/blog/'] as $s => $pre) {
  $t = "$raiz/$s"; if (!file_exists($t)) { $err[] = "falta $s"; continue; }
  $c = file_get_contents($t); $add = '';
  foreach ($m['articulos'] as $a) {
    if ($a['fecha'] > $hoy) continue;
    foreach ($a['urls'] as $u) if (strpos($u, $pre) === 0 && strpos($c, "<loc>$u</loc>") === false) $add .= "<url><loc>$u</loc><lastmod>{$a['fecha']}</lastmod></url>\n";
  }
  if ($add === '') continue;
  $p = strrpos($c, '</urlset>'); if ($p === false) { $err[] = "$s sin </urlset>"; continue; }
  $copia($s);
  if (file_put_contents($t, substr($c, 0, $p) . $add . substr($c, $p)) !== false) $log[] = "sitemap actualizado: $s"; else $err[] = "no se pudo escribir $s";
}
$r = date('c') . ' · ' . ($log ? implode('; ', $log) : 'nada nuevo') . ($err ? ' · ERRORES: ' . implode('; ', $err) : '') . "\n";
file_put_contents("$aqui/publicaciones.log", $r, FILE_APPEND);
echo $r;

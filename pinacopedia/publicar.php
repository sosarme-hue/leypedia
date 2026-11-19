<?php
// Blog · publicador. Solo desde la línea de comandos (tarea programada de Hostinger, cada hora).
// Vive en public_html/_blog/<web>/. Es idempotente: si no hay nada nuevo, no toca nada.
// 1) Copia las imágenes del blog y los artículos de manifiesto.json cuya fecha ya ha llegado (nunca sobrescribe un artículo publicado).
// 2) Pone la portada del blog que corresponde a la fecha.
// 3) Añade una vez el enlace «Blog» al menú (al final del JS común de la web), con copia previa.
// 4) Escribe sitemap-blog.xml y lo añade una vez al índice sitemap.xml, con copia previa.
// Copias en copias/<fecha>/ y registro en publicaciones.log. No borra nada.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
date_default_timezone_set('Europe/Madrid');
$aqui = __DIR__; $raiz = dirname(__DIR__, 2); $hoy = getenv('BLOG_HOY') ?: date('Y-m-d');
$m = json_decode(file_get_contents("$aqui/manifiesto.json"), true);
$dom = $m['dominio']; $js = $m['js_menu'];
if (!file_exists("$raiz/$js") || !file_exists("$raiz/sitemap.xml")) exit("Raíz inesperada: $raiz\n");
$log = []; $err = [];
$copia = function ($rel) use ($aqui, $raiz, $hoy) {
  $c = "$aqui/copias/$hoy/$rel"; @mkdir(dirname($c), 0755, true);
  if (!file_exists($c) && file_exists("$raiz/$rel")) copy("$raiz/$rel", $c);
};
// 1) imágenes y artículos
foreach (($m['imagenes'] ?? []) as $rel) {
  $t = "$raiz/$rel"; if (file_exists($t)) continue;
  @mkdir(dirname($t), 0755, true);
  if (@copy("$aqui/payload/$rel", $t)) $log[] = "imagen $rel"; else $err[] = "no se pudo copiar $rel";
}
$pub = [];
foreach ($m['articulos'] as $a) {
  if ($a['fecha'] > $hoy) continue;
  foreach ($a['archivos'] as $i => $rel) {
    $pub[] = [$a['urls'][$i], $a['fecha']];
    $t = "$raiz/$rel"; if (file_exists($t)) continue;
    @mkdir(dirname($t), 0755, true);
    if (@copy("$aqui/payload/$rel", $t)) $log[] = "publicado $rel"; else $err[] = "no se pudo copiar $rel";
  }
}
// 2) portada del blog
$f = null; foreach ($m['indices'] as $x) if ($x <= $hoy) $f = $x;
if ($f) foreach (['es' => 'blog/index.html', 'en' => 'en/blog/index.html'] as $l => $rel) {
  $src = "$aqui/payload/indices/$l/$f.html"; $t = "$raiz/$rel";
  if (file_exists($t) && md5_file($t) === md5_file($src)) continue;
  $copia($rel); @mkdir(dirname($t), 0755, true);
  if (@copy($src, $t)) $log[] = "portada $rel ($f)"; else $err[] = "no se pudo escribir $rel";
}
// 3) enlace en el menú
$c = file_get_contents("$raiz/$js");
if (strpos($c, 'enlace Blog en el menu') === false) {
  $copia($js);
  if (file_put_contents("$raiz/$js", rtrim($c) . "\n" . file_get_contents("$aqui/menu-blog.js")) !== false) $log[] = "menú añadido en $js"; else $err[] = "no se pudo escribir $js";
}
// 4) sitemaps
if ($f) {
  $x = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n";
  $x .= "<url><loc>https://$dom/blog/</loc><lastmod>$f</lastmod></url>\n<url><loc>https://$dom/en/blog/</loc><lastmod>$f</lastmod></url>\n";
  foreach ($pub as [$u, $d]) $x .= "<url><loc>$u</loc><lastmod>$d</lastmod></url>\n";
  $x .= "</urlset>\n";
  $t = "$raiz/sitemap-blog.xml";
  if (!file_exists($t) || file_get_contents($t) !== $x) {
    if (file_put_contents($t, $x) !== false) $log[] = 'sitemap-blog.xml'; else $err[] = 'no se pudo escribir sitemap-blog.xml';
  }
  $c = file_get_contents("$raiz/sitemap.xml"); $loc = "https://$dom/sitemap-blog.xml";
  if (strpos($c, $loc) === false) {
    $p = strrpos($c, '</sitemapindex>');
    if ($p === false) $err[] = 'sitemap.xml no es un índice';
    else {
      $copia('sitemap.xml');
      if (file_put_contents("$raiz/sitemap.xml", substr($c, 0, $p) . "<sitemap><loc>$loc</loc></sitemap>\n" . substr($c, $p)) !== false) $log[] = 'sitemap.xml: añadido sitemap-blog.xml';
      else $err[] = 'no se pudo escribir sitemap.xml';
    }
  }
}
if ($log || $err) {
  $r = date('c') . ' · ' . ($log ? implode('; ', $log) : '') . ($err ? ' · ERRORES: ' . implode('; ', $err) : '') . "\n";
  file_put_contents("$aqui/publicaciones.log", $r, FILE_APPEND);
  echo $r;
} else echo date('c') . " · nada nuevo\n";

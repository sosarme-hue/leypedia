<?php
// Blog · publicador. Solo desde la línea de comandos (tarea programada de Hostinger, cada hora).
// Vive en public_html/_blog/<web>/. Es idempotente: si no hay nada nuevo, no toca nada.
// 1) Copia las imágenes del blog y los artículos de manifiesto.json cuya fecha ya ha llegado (nunca sobrescribe un artículo publicado).
// 2) Pone la portada del blog que corresponde a la fecha.
// 3) Añade una vez el enlace «Blog» al menú (al final del JS común de la web), con copia previa. Opcional (js_menu).
// Opciones del manifiesto: idiomas (por defecto es y en) y no_tocar_web (no modifica JS, robots.txt ni sitemap.xml).
// 4) Escribe sitemap-blog.xml y lo añade una vez al índice sitemap.xml, con copia previa.
// Copias en copias/<fecha>/ y registro en publicaciones.log. No borra nada.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
date_default_timezone_set('Europe/Madrid');
$aqui = __DIR__; $raiz = dirname(__DIR__, 2); $hoy = getenv('BLOG_HOY') ?: date('Y-m-d');
$m = json_decode(file_get_contents("$aqui/manifiesto.json"), true);
$dom = $m['dominio']; $js = $m['js_menu'] ?? ''; $langs = $m['idiomas'] ?? ['es', 'en']; $tocar = empty($m['no_tocar_web']);
if (!file_exists("$raiz/index.html") || ($js !== '' && !file_exists("$raiz/$js")) || ($tocar && !file_exists("$raiz/sitemap.xml"))) exit("Raíz inesperada: $raiz\n");
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
if ($f) foreach (['es' => 'blog/index.html', 'en' => 'en/blog/index.html'] as $l => $rel) if (in_array($l, $langs)) {
  $src = "$aqui/payload/indices/$l/$f.html"; $t = "$raiz/$rel";
  if (file_exists($t) && md5_file($t) === md5_file($src)) continue;
  $copia($rel); @mkdir(dirname($t), 0755, true);
  if (@copy($src, $t)) $log[] = "portada $rel ($f)"; else $err[] = "no se pudo escribir $rel";
}
// 3) enlace en el menú
$c = $js !== '' ? file_get_contents("$raiz/$js") : 'enlace Blog en el menu';
if (strpos($c, 'enlace Blog en el menu') === false) {
  $copia($js);
  if (file_put_contents("$raiz/$js", rtrim($c) . "\n" . file_get_contents("$aqui/menu-blog.js")) !== false) $log[] = "menú añadido en $js"; else $err[] = "no se pudo escribir $js";
}
// 4) sitemaps
if ($f) {
  $x = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n";
  foreach (['es' => 'blog/', 'en' => 'en/blog/'] as $l => $b) if (in_array($l, $langs)) $x .= "<url><loc>https://$dom/$b</loc><lastmod>$f</lastmod></url>\n";
  foreach ($pub as [$u, $d]) $x .= "<url><loc>$u</loc><lastmod>$d</lastmod></url>\n";
  $x .= "</urlset>\n";
  $t = "$raiz/sitemap-blog.xml";
  if (!file_exists($t) || file_get_contents($t) !== $x) {
    if (file_put_contents($t, $x) !== false) $log[] = 'sitemap-blog.xml'; else $err[] = 'no se pudo escribir sitemap-blog.xml';
  }
  $c = $tocar ? file_get_contents("$raiz/sitemap.xml") : ''; $loc = "https://$dom/sitemap-blog.xml";
  $p = strrpos($c, '</sitemapindex>');
  if (!$tocar) {
    // la web se despliega desde Git: no se tocan sus archivos (menú, robots.txt y sitemap.xml van en el repositorio)
  } elseif ($p === false) {
    // sitemap.xml es una lista de URL (no un índice): se anuncia sitemap-blog.xml en robots.txt
    $rb = file_exists("$raiz/robots.txt") ? file_get_contents("$raiz/robots.txt") : '';
    if (strpos($rb, $loc) === false) {
      if ($rb !== '') $copia('robots.txt');
      if (file_put_contents("$raiz/robots.txt", rtrim($rb) . ($rb === '' ? '' : "\n") . "Sitemap: $loc\n") !== false) $log[] = 'robots.txt: añadido sitemap-blog.xml';
      else $err[] = 'no se pudo escribir robots.txt';
    }
  } elseif (strpos($c, $loc) === false) {
    {
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

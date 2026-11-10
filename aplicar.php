<?php
// Classicapedia · instala el blog. Solo se ejecuta desde la línea de comandos (tarea programada de Hostinger).
// Copia payload/blog y payload/en/blog (archivos nuevos, no sobrescribe nada que ya exista con otro contenido),
// añade el enlace «Blog» al menú al final de assets/ga.js y en/assets/ga.js, y añade las URL del blog a los sitemaps.
// Antes de tocar ga.js o los sitemaps guarda una copia en copias/. No borra nada de la web.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$aqui = __DIR__; $raiz = dirname($aqui);
if (file_exists("$aqui/hecho.txt")) exit("Ya se aplico antes. No se ha tocado nada.\n");
$log = []; $err = [];
// 1) páginas del blog
foreach (['blog', 'en/blog'] as $d) {
  foreach (glob("$aqui/payload/$d/*.html") as $f) {
    $t = "$raiz/$d/" . basename($f);
    if (file_exists($t) && md5_file($t) !== md5_file($f)) { $err[] = "existe y es distinto: $d/" . basename($f); continue; }
    @mkdir(dirname($t), 0755, true);
    if (@copy($f, $t)) $log[] = "copiado $d/" . basename($f); else $err[] = "no se pudo copiar $d/" . basename($f);
  }
}
// 2) enlace en el menú
$snip = file_get_contents("$aqui/menu-blog.js");
foreach (['assets/ga.js', 'en/assets/ga.js'] as $g) {
  $t = "$raiz/$g"; if (!file_exists($t)) { $err[] = "falta $g"; continue; }
  $c = file_get_contents($t);
  if (strpos($c, 'enlace «Blog» en el menú') !== false) { $log[] = "$g ya tenía el enlace"; continue; }
  @mkdir(dirname("$aqui/copias/$g"), 0755, true); copy($t, "$aqui/copias/$g");
  if (file_put_contents($t, rtrim($c) . "\n" . $snip) !== false) $log[] = "menú añadido en $g"; else $err[] = "no se pudo escribir $g";
}
// 3) sitemaps
$urls = json_decode(file_get_contents("$aqui/urls.json"), true);
foreach (['sitemap-es.xml' => 'https://classicapedia.com/blog/', 'sitemap-en.xml' => 'https://classicapedia.com/en/blog/'] as $s => $pre) {
  $t = "$raiz/$s"; if (!file_exists($t)) { $err[] = "falta $s"; continue; }
  $c = file_get_contents($t);
  if (strpos($c, "<loc>$pre</loc>") !== false) { $log[] = "$s ya tenía el blog"; continue; }
  $add = '';
  foreach ($urls as $u) if (strpos($u, $pre) === 0) $add .= "<url><loc>$u</loc><lastmod>2026-11-10</lastmod></url>\n";
  $p = strrpos($c, '</urlset>'); if ($p === false) { $err[] = "$s sin </urlset>"; continue; }
  @mkdir("$aqui/copias", 0755, true); copy($t, "$aqui/copias/$s");
  if (file_put_contents($t, substr($c, 0, $p) . $add . substr($c, $p)) !== false) $log[] = "sitemap actualizado: $s"; else $err[] = "no se pudo escribir $s";
}
$r = date('c') . "\nHECHO:\n" . implode("\n", $log) . "\nERRORES:\n" . implode("\n", $err) . "\n";
file_put_contents("$aqui/hecho.txt", $r);
echo $r;

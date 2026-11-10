<?php
// Instalación de un solo uso del blog de CatDogPedia. Solo desde la línea de comandos (tarea programada de Hostinger).
// 1) añade «Blog» al final del menú de todas las páginas .html (solo cambia ese trozo exacto del menú);
// 2) ejecuta publicar.php, que pone los artículos ya fechados, la portada, el buscador y el mapa del sitio.
// Deja hecho.txt y no se repite. Para quitar el enlace del menú: BLOG_DESHACER=1 php aplicar.php. No borra nada.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
date_default_timezone_set('Europe/Madrid');
$aqui = __DIR__; $pub = getenv('BLOG_RAIZ') ?: dirname($aqui);
$deshacer = getenv('BLOG_DESHACER') === '1';
if (!$deshacer && file_exists("$aqui/hecho.txt")) exit("Ya aplicado: " . file_get_contents("$aqui/hecho.txt"));
if (!is_file("$pub/index.html") || !is_dir("$pub/perros")) exit("No parece la raíz de CatDogPedia: $pub\n");
$cambios = [
  '<a href="/curiosidades/">Curiosidades</a></nav>' => '<a href="/curiosidades/">Curiosidades</a><a href="/blog/">Blog</a></nav>',
  '<a href="/en/did-you-know/">Did you know?</a></nav>' => '<a href="/en/did-you-know/">Did you know?</a><a href="/en/blog/">Blog</a></nav>',
];
if ($deshacer) $cambios = array_flip($cambios);
$n = 0; $vistos = 0; $err = 0;
$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($pub, FilesystemIterator::SKIP_DOTS));
foreach ($it as $f) {
  $p = $f->getPathname();
  if (substr($p, -5) !== '.html') continue;
  $rel = substr($p, strlen($pub) + 1);
  if (preg_match('#^(_og/|_blog/|_copia)#', $rel)) continue;
  $vistos++;
  $t = file_get_contents($p); if ($t === false) continue;
  $t2 = strtr($t, $cambios);
  if ($t2 !== $t) { if (file_put_contents($p, $t2, LOCK_EX) !== false) $n++; else $err++; }
}
$r = date('c') . " menú: $n de $vistos páginas " . ($deshacer ? 'sin Blog' : 'con Blog') . ($err ? ", $err errores" : '') . "\n";
file_put_contents("$aqui/publicaciones.log", $r, FILE_APPEND); echo $r;
if ($deshacer) exit;
file_put_contents("$aqui/hecho.txt", $r);
require "$aqui/publicar.php";

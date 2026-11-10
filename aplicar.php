<?php
// Classicapedia · alta en AdSense: copia payload/ sobre la raíz de la web.
// Antes de sobrescribir cada archivo comprueba que no ha cambiado desde que se preparó (huella en originales.json)
// y guarda una copia en copias/. ads.txt y contacto.html son nuevos. No borra nada de la web.
header('Content-Type: text/html; charset=utf-8');
if (($_GET['k'] ?? '') !== '0bc3c0a589a49cb2f033fa6b') { http_response_code(403); exit('No autorizado'); }
if (file_exists(__DIR__ . '/hecho.txt')) exit('<p style="font:20px sans-serif;text-align:center;margin-top:20vh">Ya se aplicó antes. No se ha tocado nada.</p>');
$src = __DIR__ . '/payload'; $dst = dirname(__DIR__);
$orig = json_decode(file_get_contents(__DIR__ . '/originales.json'), true);
$ok = []; $saltados = []; $err = [];
$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($src, FilesystemIterator::SKIP_DOTS));
$lista = [];
foreach ($it as $f) $lista[] = substr($f->getPathname(), strlen($src) + 1);
// 1) comprobar todo antes de tocar nada
foreach ($lista as $rel) {
  $t = "$dst/$rel";
  if (isset($orig[$rel])) {
    if (!file_exists($t) || md5(rtrim(file_get_contents($t))) !== $orig[$rel]) $saltados[] = $rel;
  } elseif (file_exists($t) && $rel !== 'ads.txt') $saltados[] = $rel;
}
if ($saltados) { echo '<p style="font:18px sans-serif;margin:10vh 5vw">No se ha tocado nada: estos archivos han cambiado desde que Claude preparó la subida. Avisa a Claude.<br>' . htmlspecialchars(implode(', ', $saltados)) . '</p>'; exit; }
// 2) copias y escritura
foreach ($lista as $rel) {
  $t = "$dst/$rel"; $s = "$src/$rel";
  if (file_exists($t)) { $c = __DIR__ . "/copias/$rel"; @mkdir(dirname($c), 0755, true); @copy($t, $c); }
  if ($rel === 'ads.txt' && file_exists($t)) {
    $linea = trim(file_get_contents($s)); $actual = file_get_contents($t);
    if (strpos($actual, $linea) === false) $res = file_put_contents($t, rtrim($actual) . "\n" . $linea . "\n"); else $res = true;
  } else { @mkdir(dirname($t), 0755, true); $res = @copy($s, $t); }
  if ($res === false) $err[] = $rel; else $ok[] = $rel;
}
file_put_contents(__DIR__ . '/hecho.txt', date('c') . "\ncopiados: " . implode(', ', $ok) . "\nerrores: " . implode(', ', $err) . "\n");
@unlink(__FILE__);
echo '<div style="font:20px sans-serif;text-align:center;margin-top:20vh">';
echo $err ? 'Copiados ' . count($ok) . ' archivos, ' . count($err) . ' con error. Avisa a Claude.' : '✅ ¡Listo! Classicapedia ya tiene AdSense. Puedes cerrar esta página.';
echo '</div>';

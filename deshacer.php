<?php
// Copia copias/ sobre la raíz de la web (deja todo como estaba antes de aplicar.php). Solo línea de comandos.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$src = __DIR__ . '/copias'; $dst = dirname(__DIR__); $n = 0;
$it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($src, FilesystemIterator::SKIP_DOTS));
foreach ($it as $f) { $rel = substr($f->getPathname(), strlen($src) + 1); if (copy($f->getPathname(), "$dst/$rel")) $n++; }
@rename(__DIR__ . '/hecho.txt', __DIR__ . '/hecho-deshecho.txt');
echo "restaurados $n archivos\n";

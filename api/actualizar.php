<?php
// Leypedia: actualización diaria de BOE, DOGC y EUR-Lex.
// Se ejecuta con una tarea programada (cron) del hosting, por ejemplo cada día a las 8:30:
//   php /home/USUARIO/domains/leypedia.com/public_html/api/actualizar.php
// Solo funciona desde la línea de comandos, no desde el navegador.
if (php_sapi_name() !== 'cli') { http_response_code(404); exit; }
$_SERVER['SCRIPT_FILENAME'] = __FILE__;
require __DIR__ . '/feed.php';
foreach ($FUENTES as $id => $F) {
    $r = feed_actualiza($id, $F, true);
    echo $id . ': ' . ($r ? count($r['items']) . ' elementos (' . $r['canal'] . ')' : 'sin respuesta') . "\n";
}
ob_start(); include __DIR__ . '/boe.php'; $b = json_decode(ob_get_clean(), true);
echo 'boe: ' . (isset($b['total']) ? $b['total'] . ' disposiciones del ' . $b['fecha'] : 'sin respuesta') . "\n";

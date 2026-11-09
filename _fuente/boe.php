<?php
// Leypedia: resumen del último BOE a partir de la API de datos abiertos del BOE.
// Guarda una copia por día en api/cache para no consultar el BOE en cada visita.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=1800');
header('X-Content-Type-Options: nosniff');

$cacheDir = __DIR__ . '/cache';
if (!is_dir($cacheDir)) { @mkdir($cacheDir, 0755, true); }

function boe_get($fecha) {
    $url = 'https://www.boe.es/datosabiertos/api/boe/sumario/' . $fecha;
    $ctx = stream_context_create(['http' => [
        'header' => "Accept: application/json\r\nUser-Agent: Leypedia/1.0 (+https://leypedia.com)\r\n",
        'timeout' => 15, 'ignore_errors' => true]]);
    $raw = @file_get_contents($url, false, $ctx);
    if ($raw === false && function_exists('curl_init')) {
        $c = curl_init($url);
        curl_setopt_array($c, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 15,
            CURLOPT_HTTPHEADER => ['Accept: application/json'], CURLOPT_USERAGENT => 'Leypedia/1.0 (+https://leypedia.com)']);
        $raw = curl_exec($c); curl_close($c);
    }
    if (!$raw) return null;
    $j = json_decode($raw, true);
    return (is_array($j) && isset($j['data'])) ? $j : null;
}

function boe_walk($node, $ctx, &$out) {
    if (!is_array($node)) return;
    if (isset($node['identificador']) && isset($node['titulo'])) {
        $u = $node['url_html'] ?? '';
        if (is_array($u)) $u = $u['texto'] ?? '';
        $out[] = ['seccion' => $ctx['sec'] ?? '', 'seccion_nombre' => $ctx['secn'] ?? '',
                  'departamento' => $ctx['dep'] ?? '', 'id' => (string)$node['identificador'],
                  'titulo' => (string)$node['titulo'], 'url' => (string)$u];
        return;
    }
    if (isset($node['codigo']) && isset($node['departamento'])) {
        $ctx['sec'] = (string)$node['codigo']; $ctx['secn'] = (string)($node['nombre'] ?? '');
    } elseif (isset($node['nombre']) && (isset($node['epigrafe']) || isset($node['item']))) {
        $ctx['dep'] = (string)$node['nombre'];
    }
    foreach ($node as $v) { if (is_array($v)) boe_walk($v, $ctx, $out); }
}

$tz = new DateTimeZone('Europe/Madrid');
$day = new DateTime('now', $tz);
$result = null;
for ($i = 0; $i < 7 && !$result; $i++) {
    $f = $day->format('Ymd');
    $file = "$cacheDir/$f.json";
    if (is_file($file)) { $result = json_decode(file_get_contents($file), true); break; }
    $j = boe_get($f);
    if ($j) {
        $items = [];
        boe_walk($j['data'], [], $items);
        if ($items) {
            $secs = [];
            foreach ($items as $it) {
                $k = $it['seccion'];
                if (!isset($secs[$k])) $secs[$k] = ['codigo' => $k, 'nombre' => $it['seccion_nombre'], 'n' => 0];
                $secs[$k]['n']++;
            }
            $gen = array_values(array_filter($items, function ($it) { return $it['seccion'] === '1'; }));
            $result = ['fecha' => $f, 'total' => count($items), 'secciones' => array_values($secs),
                       'items' => array_map(function ($it) { unset($it['seccion'], $it['seccion_nombre']); return $it; }, $gen)];
            @file_put_contents($file, json_encode($result, JSON_UNESCAPED_UNICODE));
        }
    }
    $day->modify('-1 day');
}
if (!$result) { http_response_code(503); echo json_encode(['error' => 'BOE no disponible']); exit; }
echo json_encode($result, JSON_UNESCAPED_UNICODE);

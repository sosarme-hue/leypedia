<?php
// Leypedia: últimas publicaciones del DOGC y de EUR-Lex (Diario Oficial de la UE).
// Lee el canal RSS/Atom oficial y guarda una copia por día en api/cache.
// Las direcciones de cada canal están en $FUENTES: si una cambia, basta con editarla aquí.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=1800');
header('X-Content-Type-Options: nosniff');

$FUENTES = [
  'dogc' => ['nombre' => 'Diari Oficial de la Generalitat de Catalunya', 'hosts' => ['gencat.cat'], 'urls' => [
      'https://dogc.gencat.cat/ca/inici/rss/darrer-dogc.xml',
      'https://portaldogc.gencat.cat/utilsEADOP/AppJava/RssDogc.do?lang=ca',
      'https://web.gencat.cat/ca/actualitat/rss/dogc.xml',
  ], 'socrata' => 'https://analisi.transparenciacatalunya.cat/api/views/n6hn-rmy7'],
  'ue' => ['nombre' => 'EUR-Lex · Diario Oficial de la Unión Europea, serie L', 'hosts' => ['europa.eu'], 'urls' => [
      'https://eur-lex.europa.eu/ES/display-feed.rss?rssId=165',
      'https://eur-lex.europa.eu/EN/display-feed.rss?rssId=165',
  ]],
];

function feed_get($url) {
    $ua = 'Leypedia/1.0 (+https://leypedia.com)';
    $raw = false;
    if (function_exists('curl_init')) {
        $c = curl_init($url);
        curl_setopt_array($c, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 15, CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_MAXREDIRS => 3, CURLOPT_USERAGENT => $ua, CURLOPT_HTTPHEADER => ['Accept: application/rss+xml, application/atom+xml, application/xml, text/xml']]);
        $raw = curl_exec($c);
        $code = curl_getinfo($c, CURLINFO_HTTP_CODE);
        curl_close($c);
        if ($code >= 400) $raw = false;
    }
    if ($raw === false) {
        $ctx = stream_context_create(['http' => ['header' => "User-Agent: $ua\r\n", 'timeout' => 15]]);
        $raw = @file_get_contents($url, false, $ctx);
    }
    return $raw ?: null;
}

function feed_parse($raw, $hosts) {
    $prev = libxml_use_internal_errors(true);
    $x = simplexml_load_string($raw, 'SimpleXMLElement', LIBXML_NOCDATA | LIBXML_NONET);
    libxml_use_internal_errors($prev);
    if (!$x) return [];
    $out = [];
    $nodes = isset($x->channel->item) ? $x->channel->item : (isset($x->item) ? $x->item : $x->entry);
    foreach ($nodes as $n) {
        $t = trim(preg_replace('/\s+/u', ' ', strip_tags((string)$n->title)));
        $l = (string)$n->link;
        if (!$l && isset($n->link['href'])) $l = (string)$n->link['href'];
        $d = (string)($n->pubDate ?: ($n->updated ?: $n->children('http://purl.org/dc/elements/1.1/')->date));
        $h = parse_url($l, PHP_URL_HOST);
        $ok = false;
        foreach ($hosts as $hh) { if ($h && ($h === $hh || substr($h, -strlen('.' . $hh)) === '.' . $hh)) $ok = true; }
        if (!$t || !$ok || parse_url($l, PHP_URL_SCHEME) !== 'https') continue;
        $out[] = ['titulo' => $t, 'url' => $l, 'fecha' => $d ? date('Y-m-d', strtotime($d)) : ''];
        if (count($out) >= 30) break;
    }
    return $out;
}

// Dades obertes de la Generalitat (Socrata): normativa publicada al DOGC, actualitzada cada dia.
// Es llegeixen les columnes del conjunt de dades per trobar el títol, l'enllaç i la data.
function feed_socrata($base, $hosts) {
    $meta = json_decode((string)feed_get($base . '.json'), true);
    if (!$meta || empty($meta['columns'])) return [];
    $tit = $url = $dat = null;
    foreach ($meta['columns'] as $c) {
        $f = $c['fieldName'] ?? ''; $n = mb_strtolower(($c['name'] ?? '') . ' ' . $f); $ty = $c['dataTypeName'] ?? '';
        if (!$dat && $ty === 'calendar_date' && preg_match('/publica|dogc|data/u', $n)) $dat = $f;
        if (!$url && ($ty === 'url' || preg_match('/url|enlla|link/u', $n))) $url = $f;
        if (!$tit && $ty === 'text' && preg_match('/t[ií]tol|titulo|title/u', $n)) $tit = $f;
    }
    if (!$tit || !$url) return [];
    $id = basename($base);
    $dom = substr($base, 0, strpos($base, '/api/views/'));
    $q = '$limit=30' . ($dat ? '&$order=' . rawurlencode("$dat DESC") : '');
    $rows = json_decode((string)feed_get("$dom/resource/$id.json?$q"), true);
    if (!is_array($rows)) return [];
    $out = [];
    foreach ($rows as $r) {
        $t = trim(preg_replace('/\s+/u', ' ', strip_tags((string)($r[$tit] ?? ''))));
        $l = $r[$url] ?? '';
        if (is_array($l)) $l = $l['url'] ?? '';
        $h = parse_url($l, PHP_URL_HOST); $ok = false;
        foreach ($hosts as $hh) { if ($h && ($h === $hh || substr($h, -strlen('.' . $hh)) === '.' . $hh)) $ok = true; }
        if (!$t || !$ok) continue;
        if (parse_url($l, PHP_URL_SCHEME) === 'http') $l = 'https' . substr($l, 4);
        $d = $dat && !empty($r[$dat]) ? date('Y-m-d', strtotime($r[$dat])) : '';
        $out[] = ['titulo' => mb_strlen($t) > 220 ? mb_substr($t, 0, 217) . '…' : $t, 'url' => $l, 'fecha' => $d];
    }
    return $out;
}

function feed_actualiza($id, $F, $forzar = false) {
    $cacheDir = __DIR__ . '/cache';
    if (!is_dir($cacheDir)) { @mkdir($cacheDir, 0755, true); }
    $hoy = (new DateTime('now', new DateTimeZone('Europe/Madrid')))->format('Ymd');
    $file = "$cacheDir/$id-$hoy.json";
    if (!$forzar && is_file($file)) return json_decode(file_get_contents($file), true);
    if (!empty($F['socrata'])) {
        $items = feed_socrata($F['socrata'], $F['hosts']);
        if ($items) {
            $r = ['fuente' => $F['nombre'], 'canal' => $F['socrata'], 'actualizado' => $hoy, 'items' => $items];
            @file_put_contents($file, json_encode($r, JSON_UNESCAPED_UNICODE));
            return $r;
        }
    }
    foreach ($F['urls'] as $u) {
        $raw = feed_get($u);
        if (!$raw) continue;
        $items = feed_parse($raw, $F['hosts']);
        if ($items) {
            $r = ['fuente' => $F['nombre'], 'canal' => $u, 'actualizado' => $hoy, 'items' => $items];
            @file_put_contents($file, json_encode($r, JSON_UNESCAPED_UNICODE));
            foreach (glob("$cacheDir/$id-*.json") as $old) { if ($old !== $file && filemtime($old) < time() - 86400 * 8) @unlink($old); }
            return $r;
        }
    }
    // Si hoy no responde, se sirve la última copia disponible
    $prev = glob("$cacheDir/$id-*.json");
    if ($prev) { rsort($prev); return json_decode(file_get_contents($prev[0]), true); }
    return null;
}

if (basename($_SERVER['SCRIPT_FILENAME'] ?? '') === 'feed.php') {
    $id = $_GET['f'] ?? '';
    if (!isset($FUENTES[$id])) { http_response_code(400); echo json_encode(['error' => 'fuente desconocida']); exit; }
    $r = feed_actualiza($id, $FUENTES[$id]);
    if (!$r) { http_response_code(503); echo json_encode(['error' => 'no disponible']); exit; }
    echo json_encode($r, JSON_UNESCAPED_UNICODE);
}

<?php
// Cambio 13: tema «Atril» (fondo crema, granate, líneas finas) sobre los diseños actuales. Solo CSS.
// Sustituye colores y grosores de borde en estilo.css (ES y EN) y en portada-c.css si existe, y añade el bloque atril-c.css.
// Copia de seguridad en copias/ (.antes13). Para deshacer: restaurar esas copias.
if (php_sapi_name() !== 'cli') { http_response_code(403); exit('No autorizado'); }
$aqui = __DIR__; $raiz = dirname($aqui);
if (file_exists("$aqui/hecho13.txt")) exit("Ya se aplico antes.\n");
$ini = "/* === tema Atril (nov 2026) === */"; $fin = "/* === fin tema Atril === */";
$nuevo = trim(file_get_contents("$aqui/atril-c.css"));
if (strpos($nuevo, $ini) !== 0) exit("atril-c.css no empieza por la marca\n");
$pares = [
  ['--papel:#ffffff;--tinta:#111111;--suave:#5c5c5c;--linea:#e6e6e6;--oro:#e8452c;--blanco:#f4f2ee;--marca:#e8452c;', '--papel:#f5efe3;--tinta:#1c1712;--suave:#6b5f50;--linea:#d9cdb8;--oro:#7b1e2e;--blanco:#fbf8f1;--marca:#a8823a;'],
  ['--medieval:#6b3fa0;--renacimiento:#0f8a6a;--barroco:#e08a00;--clasicismo:#2357d8;--romanticismo:#d6283c;--siglo-xx:#222222;--contemporaneo:#00a3b4', '--medieval:#7a4b8c;--renacimiento:#2f6f5e;--barroco:#9a5b1f;--clasicismo:#2d5d8f;--romanticismo:#a3333d;--siglo-xx:#4a4a4a;--contemporaneo:#1d7f8c'],
  ['{background:#fff;color:var(--tinta)', '{background:var(--papel);color:var(--tinta)'],
  ['background:#fff', 'background:var(--blanco)'],
  ['#e8452c', '#7b1e2e'],
  ['rgba(232,69,44', 'rgba(123,30,46'],
  ['3px solid var(--tinta)', '1px solid var(--tinta)'],
  ['2px solid var(--tinta)', '1px solid var(--linea)'],
  ['px 0 var(--tinta)', 'px 0 var(--linea)'],
  ['#ffd84a', 'var(--blanco)']
];
@mkdir("$aqui/copias");
$log = []; $err = [];
foreach (['assets/estilo.css', 'en/assets/estilo.css', 'assets/portada-c.css', 'en/assets/portada-c.css'] as $p) {
  $t = "$raiz/$p"; if (!file_exists($t)) { $log[] = "$p no existe (se salta)"; continue; }
  $c = file_get_contents($t); if ($c === false) { $err[] = "$p: no se puede leer"; continue; }
  copy($t, "$aqui/copias/" . str_replace('/', '_', $p) . ".antes13");
  $tot = 0; foreach ($pares as $pr) { $c = str_replace($pr[0], $pr[1], $c, $n); $tot += $n; }
  if (substr($p, -9) === 'estilo.css') {
    $a = strpos($c, $ini); $b = strpos($c, $fin);
    if ($a !== false && $b !== false) $c = substr($c, 0, $a) . $nuevo . substr($c, $b + strlen($fin));
    else $c = rtrim($c) . "\n" . $nuevo . "\n";
  }
  if (file_put_contents($t, $c) !== false) $log[] = "actualizado $p ($tot cambios, " . strlen($c) . " bytes)"; else $err[] = "no se pudo escribir $p";
}
$r = date('c') . "\nHECHO:\n" . implode("\n", $log) . "\nERRORES:\n" . implode("\n", $err) . "\n";
file_put_contents("$aqui/hecho13.txt", $r); echo $r;

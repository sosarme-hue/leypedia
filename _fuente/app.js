(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var lang = document.documentElement.lang === 'ca' ? 'ca' : 'es';

  // ---------- Generador de contrato (todo en el navegador) ----------
  var doc = $('doc');
  if (doc) {
    var f = $('f');
    var val = function (id) { return $(id).value; };
    var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };
    var HUECO = '______________________________';
    var nombre = function (id) { var v = val(id).trim(); return ($('bl').checked || !v) ? HUECO : esc(v); };
    var loc = lang === 'ca' ? 'ca-ES' : 'es-ES';
    var eur = function (n) { return Number(n || 0).toLocaleString(loc, { style: 'currency', currency: 'EUR' }); };

    var render = function () {
      var im = Number(val('im')) || 0, pl = Math.max(1, Number(val('pl')) || 1), ti = Number(val('in')) || 0;
      var ciudad = esc(val('ci').trim() || '__________');
      var fecha = new Date().toLocaleDateString(loc, { day: 'numeric', month: 'long', year: 'numeric' });
      var r = ti / 100 / 12, cuota = r ? im * r / (1 - Math.pow(1 + r, -pl)) : im / pl;
      var unico = im * (1 + ti / 100 * pl / 12);
      var mensual = val('pa') === 'm';
      var h;
      if (lang === 'ca') {
        h = '<h3>CONTRACTE DE PRÉSTEC ENTRE PARTICULARS</h3>' +
          '<p>A ' + ciudad + ', ' + fecha + '.</p>' +
          '<p><b>REUNITS</b>: d\'una banda, ' + nombre('pr') + ', major d\'edat, amb DNI ____________, d\'ara endavant «la part prestadora»; i de l\'altra, ' + nombre('pt') + ', major d\'edat, amb DNI ____________, d\'ara endavant «la part prestatària».</p>' +
          '<p><b>Primera. Objecte.</b> La part prestadora lliura en aquest acte a la part prestatària la quantitat de ' + eur(im) + ', que aquesta declara rebre.</p>' +
          '<p><b>Segona. Interès.</b> ' + (ti ? 'El préstec merita un interès fix del ' + ti.toLocaleString(loc) + ' % anual.' : 'El préstec és gratuït i no merita interessos.') + '</p>' +
          '<p><b>Tercera. Devolució.</b> La part prestatària retornarà el capital ' + (mensual ? 'mitjançant ' + pl + ' quotes mensuals de ' + eur(cuota) + ', pagadores el dia 5 de cada mes per transferència bancària' : 'en un únic pagament de ' + eur(unico) + ' al venciment del termini de ' + pl + ' mesos') + '.</p>' +
          '<p><b>Quarta. Amortització anticipada.</b> La part prestatària podrà retornar total o parcialment el préstec abans del termini, sense penalització.</p>' +
          '<p><b>Cinquena. Impostos.</b> Aquest préstec està exempt de l\'Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados, però cal presentar el model 600 davant l\'administració tributària de la comunitat autònoma (a Catalunya, l\'Agència Tributària de Catalunya) en els 30 dies hàbils següents a la signatura.</p>' +
          '<p>I, en prova de conformitat, les parts signen aquest contracte per duplicat.</p>' +
          '<div class="firma"><div>La part prestadora</div><div>La part prestatària</div></div>';
      } else {
        h = '<h3>CONTRATO DE PRÉSTAMO ENTRE PARTICULARES</h3>' +
          '<p>En ' + ciudad + ', a ' + fecha + '.</p>' +
          '<p><b>REUNIDOS</b>: de una parte, ' + nombre('pr') + ', mayor de edad, con DNI ____________, en adelante «la parte prestamista»; y de otra, ' + nombre('pt') + ', mayor de edad, con DNI ____________, en adelante «la parte prestataria».</p>' +
          '<p><b>Primera. Objeto.</b> La parte prestamista entrega en este acto a la parte prestataria la cantidad de ' + eur(im) + ', que esta declara recibir.</p>' +
          '<p><b>Segunda. Interés.</b> ' + (ti ? 'El préstamo devenga un interés fijo del ' + ti.toLocaleString(loc) + ' % anual.' : 'El préstamo es gratuito y no devenga intereses.') + '</p>' +
          '<p><b>Tercera. Devolución.</b> La parte prestataria devolverá el capital ' + (mensual ? 'mediante ' + pl + ' cuotas mensuales de ' + eur(cuota) + ', pagaderas el día 5 de cada mes por transferencia bancaria' : 'en un único pago de ' + eur(unico) + ' al vencimiento del plazo de ' + pl + ' meses') + '.</p>' +
          '<p><b>Cuarta. Amortización anticipada.</b> La parte prestataria podrá devolver total o parcialmente el préstamo antes del plazo, sin penalización.</p>' +
          '<p><b>Quinta. Impuestos.</b> Este préstamo está exento del Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados, pero debe presentarse el modelo 600 ante la administración tributaria de la comunidad autónoma (en Catalunya, la Agència Tributària de Catalunya) en los 30 días hábiles siguientes a la firma.</p>' +
          '<p>Y en prueba de conformidad, las partes firman el presente contrato por duplicado.</p>' +
          '<div class="firma"><div>La parte prestamista</div><div>La parte prestataria</div></div>';
      }
      doc.innerHTML = h;
    };
    f.addEventListener('input', render);
    f.addEventListener('change', render);
    f.addEventListener('submit', function (e) { e.preventDefault(); });
    render();

    var msg = $('cmsg');
    $('copiar').addEventListener('click', function () {
      var ok = lang === 'ca' ? 'Contracte copiat.' : 'Contrato copiado.';
      var sel = function () {
        var r = document.createRange(); r.selectNodeContents(doc);
        var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
        msg.textContent = lang === 'ca' ? 'Text seleccionat: prem Ctrl+C.' : 'Texto seleccionado: pulsa Ctrl+C.';
      };
      try { navigator.clipboard.writeText(doc.innerText).then(function () { msg.textContent = ok; }, sel); } catch (e) { sel(); }
    });
    $('borrar').addEventListener('click', function () {
      ['pr', 'pt', 'ci'].forEach(function (id) { $(id).value = ''; });
      $('im').value = 6000; $('pl').value = 24; $('in').value = 0; $('bl').checked = false;
      render();
      msg.textContent = lang === 'ca' ? 'Dades esborrades.' : 'Datos borrados.';
    });
    // Al salir de la página no queda nada: los campos se vacían.
    window.addEventListener('pagehide', function () { ['pr', 'pt', 'ci'].forEach(function (id) { $(id).value = ''; }); });
  }

  // ---------- BOE (lo sirve api/boe.php en el propio servidor) ----------
  var list = $('boe-list'), panel = $('boe-panel');
  if (!list && !panel) return;
  var api = (document.querySelector('link[rel=stylesheet]').getAttribute('href') || '').replace('assets/style.css', 'api/boe.php');
  var fmt = function (d) { return new Date(d.slice(0, 4) + '-' + d.slice(4, 6) + '-' + d.slice(6, 8) + 'T12:00:00').toLocaleDateString(lang === 'ca' ? 'ca-ES' : 'es-ES', { day: 'numeric', month: 'long', year: 'numeric' }); };
  fetch(api, { headers: { Accept: 'application/json' } }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (j) {
    if (!j || !j.fecha) throw new Error('vacío');
    if (panel) {
      $('boe-fecha').textContent = fmt(j.fecha);
      $('boe-total').textContent = j.total;
      $('boe-secs').innerHTML = (j.secciones || []).map(function (s) { return '<li><span>' + s.nombre.replace(/[<>&]/g, '') + '</span><span class="num">' + s.n + '</span></li>'; }).join('');
    }
    if (list) {
      $('boe-info').textContent = (lang === 'ca' ? 'BOE del ' : 'BOE del ') + fmt(j.fecha) + ' · ' + j.items.length + (lang === 'ca' ? ' disposicions generals' : ' disposiciones generales');
      list.innerHTML = j.items.map(function (it) {
        var t = it.titulo.replace(/[<>&]/g, ''), d = (it.departamento || '').replace(/[<>&]/g, '');
        return '<li><span class="dep">' + d + '</span><a href="' + it.url + '" target="_blank" rel="noopener">' + t + '</a><span class="mono">' + it.id + '</span></li>';
      }).join('');
    }
  }).catch(function () {
    var t = lang === 'ca' ? 'Ara mateix no es pot connectar amb el BOE. Consulta-ho a boe.es.' : 'Ahora mismo no se puede conectar con el BOE. Consúltalo en boe.es.';
    if (list) $('boe-info').textContent = t;
    if (panel) $('boe-secs').innerHTML = '<li><span>' + t + '</span></li>';
  });
})();

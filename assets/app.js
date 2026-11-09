(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var lang = document.documentElement.lang === 'ca' ? 'ca' : 'es';

  var BASE = (document.querySelector('link[rel=stylesheet]').getAttribute('href') || '').split('?')[0].replace('assets/style.css', '');
  var PREVIEW = document.documentElement.hasAttribute('data-preview');
  var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); };

  // ---------- Buscador (índice estático en assets/buscar-xx.json) ----------
  if (PREVIEW) {
    Array.prototype.forEach.call(document.querySelectorAll('form.search'), function (fm) {
      fm.addEventListener('submit', function (e) {
        e.preventDefault();
        var q = fm.querySelector('input[name=q]').value, a = fm.querySelector('input[name=a]:checked');
        location.href = fm.getAttribute('action') + '#q=' + encodeURIComponent(q) + (a && a.value ? '&a=' + a.value : '');
      });
    });
  }
  // ---------- Sugerencias al escribir (desde 3 letras) ----------
  var IDX = null, idxP = null;
  var loadIdx = function () { if (!idxP) idxP = fetch(BASE + 'assets/buscar-' + lang + '.json').then(function (r) { return r.json(); }).then(function (j) { IDX = j; return j; }); return idxP; };
  var normS = function (s) { return String(s).toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, ''); };
  var SECN = lang === 'ca' ? { contratos: 'Contracte', contractes: 'Contracte', historia: 'Història', materias: 'Matèries', materies: 'Matèries', etica: 'Ètica', moral: 'Moral', novedades: 'Novetats', novetats: 'Novetats', catalunya: 'Catalunya', 'ue-i-internacional': 'UE', biografies: 'Història', judicis: 'Història', preguntes: 'Pregunta', canvis: 'Canvi' }
    : { contratos: 'Contrato', historia: 'Historia', materias: 'Materias', etica: 'Ética', moral: 'Moral', novedades: 'Novedades', catalunya: 'Catalunya', 'ue-e-internacional': 'UE', biografias: 'Historia', juicios: 'Historia', preguntas: 'Pregunta', cambios: 'Cambio' };
  var SYN = (lang === 'ca' ? [
    ['pis', 'habitatge', 'lloguer', 'arrendament', 'llogater', 'propietari', 'habitacio', 'casa'],
    ['cotxe', 'vehicle', 'moto', 'automobil'],
    ['acomiadament', 'feina', 'treball', 'nomina', 'sou', 'salari', 'empresa', 'treballador'],
    ['pensio', 'jubilacio', 'jubilar', 'retir', 'jubilat'],
    ['herencia', 'testament', 'successio', 'heretar', 'llegitima', 'hereu'],
    ['divorci', 'separacio', 'custodia', 'parella', 'matrimoni'],
    ['deute', 'prestec', 'diners', 'pagament', 'terminis', 'rebut'],
    ['multa', 'sancio', 'recurs', 'reclamacio', 'queixa'],
    ['compra', 'compravenda', 'vendre', 'venda', 'devolucio', 'garantia', 'consumidor', 'botiga'],
    ['dades', 'rgpd', 'privacitat', 'galetes'],
    ['autonom', 'factura', 'socis', 'negoci'],
    ['llei', 'norma', 'boe', 'dogc', 'novetats'],
    ['historia', 'personatge', 'epoca', 'curiositat', 'anecdota']
  ] : [
    ['piso', 'vivienda', 'alquiler', 'arrendamiento', 'inquilino', 'casero', 'propietario', 'habitacion', 'casa'],
    ['coche', 'vehiculo', 'moto', 'automovil'],
    ['despido', 'trabajo', 'nomina', 'sueldo', 'salario', 'empresa', 'trabajador', 'empleo'],
    ['pension', 'jubilacion', 'jubilarse', 'jubilar', 'retiro', 'jubilado'],
    ['herencia', 'testamento', 'sucesion', 'heredar', 'legitima', 'heredero'],
    ['divorcio', 'separacion', 'custodia', 'pareja', 'matrimonio'],
    ['deuda', 'prestamo', 'dinero', 'pago', 'plazos', 'recibo'],
    ['multa', 'sancion', 'recurso', 'reclamacion', 'queja'],
    ['compra', 'compraventa', 'vender', 'venta', 'devolucion', 'garantia', 'consumidor', 'tienda'],
    ['datos', 'rgpd', 'privacidad', 'cookies'],
    ['autonomo', 'factura', 'socios', 'negocio'],
    ['ley', 'norma', 'boe', 'dogc', 'novedades'],
    ['historia', 'personaje', 'epoca', 'curiosidad', 'anecdota']
  ]);
  var lev1 = function (a, b) { // distancia de edición <= 1
    if (Math.abs(a.length - b.length) > 1) return false;
    var i = 0, j = 0, d = 0;
    while (i < a.length && j < b.length) {
      if (a[i] === b[j]) { i++; j++; continue; }
      if (++d > 1) return false;
      if (a.length > b.length) i++; else if (b.length > a.length) j++; else { i++; j++; }
    }
    return d + (a.length - i) + (b.length - j) <= 1;
  };
  var prep = function (p) {
    if (p._t === undefined) { p._t = normS(p.t); p._d = normS(p.d); p._x = normS(p.x); p._w = (p._t + ' ' + p._d).split(/[^a-z0-9]+/).filter(function (w) { return w.length > 3; }); }
  };
  var expand = function (w) {
    var out = [w];
    if (w.length >= 3) SYN.forEach(function (g) { if (g.some(function (m) { return m.indexOf(w) === 0 || (w.length >= 5 && w.indexOf(m) === 0); })) g.forEach(function (m) { if (out.indexOf(m) < 0) out.push(m); }); });
    return out;
  };
  var termScore = function (p, w, syn) {
    var s = 0, t = p._t;
    if (t.indexOf(w) === 0) s = 22; else if (t.indexOf(' ' + w) >= 0) s = 16; else if (t.indexOf(w) >= 0) s = 10;
    if (p._d.indexOf(w) >= 0) s += 5;
    var c = p._x.split(w).length - 1; s += Math.min(c, 6);
    return syn ? s * 0.6 : s;
  };
  var engine = function (q, amb) {
    if (!IDX) return { res: [], terms: [] };
    var terms = normS(q).split(/[^a-z0-9·]+/).filter(function (x) { return x.length > 1 || /\d/.test(x); });
    if (!terms.length) return { res: [], terms: [] };
    var groups = terms.map(expand), all = [], any = [];
    IDX.forEach(function (p) {
      if (amb && p.a.indexOf(amb) < 0) return;
      prep(p);
      var sc = 0, hit = 0;
      groups.forEach(function (g, gi) {
        var best = 0;
        g.forEach(function (w, wi) { var s = termScore(p, w, wi > 0); if (s > best) best = s; });
        if (!best && terms[gi].length >= 4) { var fz = function (x) { return lev1(terms[gi], x) || (x.length > terms[gi].length && lev1(terms[gi], x.slice(0, terms[gi].length))); };
          if (p._t.split(/[^a-z0-9]+/).some(fz)) best = 14; else if (p._w.some(fz)) best = 6; }
        if (best) hit++; sc += best;
      });
      if (hit === groups.length) all.push([sc, p]); else if (hit) any.push([sc * hit / groups.length, p]);
    });
    var res = all.length >= 3 ? all : all.concat(any.sort(function (a, b) { return b[0] - a[0]; }).slice(0, 20));
    res.sort(function (a, b) { return b[0] - a[0]; });
    var flat = [].concat.apply([], groups);
    return { res: res.map(function (r) { return r[1]; }), terms: flat };
  };
  window.__lp = { engine: engine, load: function () { return loadIdx(); } };
  Array.prototype.forEach.call(document.querySelectorAll('form.search'), function (fm) {
    var inp = fm.querySelector('input[name=q]');
    if (!inp || (fm.classList.contains('big') && $('sres'))) return;
    fm.classList.add('ac');
    var box = document.createElement('div'); box.className = 'sugg'; box.hidden = true; box.setAttribute('role', 'listbox');
    fm.querySelector('.sbar').appendChild(box);
    var cur = -1, items = [];
    var hl = function (t, q) { var n = normS(t), w = normS(q.trim().split(/\s+/)[0] || ''), i = w ? n.indexOf(w) : -1; return i < 0 ? esc(t) : esc(t.slice(0, i)) + '<mark>' + esc(t.slice(i, i + w.length)) + '</mark>' + esc(t.slice(i + w.length)); };
    var close = function () { box.hidden = true; cur = -1; };
    var show = function () {
      var q = inp.value.trim();
      if (q.length < 3) { close(); return; }
      loadIdx().then(function () {
        items = engine(q).res.slice(0, 8);
        var all = fm.getAttribute('action') + (PREVIEW ? '#q=' : '?q=') + encodeURIComponent(q);
        box.innerHTML = (items.length ? items.map(function (p, i) {
          var sec = SECN[p.u.replace(/^ca\//, '').split('/')[0]] || '';
          return '<a role="option" href="' + BASE + p.u + (PREVIEW ? 'index.html' : '') + '" data-i="' + i + '"><span class="sx"><span class="st">' + hl(p.t, q) + '</span><span class="sd">' + esc(p.d.length > 90 ? p.d.slice(0, 88) + '…' : p.d) + '</span></span>' + (sec ? '<span class="ss">' + esc(sec) + '</span>' : '') + '</a>';
        }).join('') : '<p class="none">' + (lang === 'ca' ? 'Cap resultat' : 'Sin resultados') + '</p>')
          + '<a class="all" href="' + all + '">' + (lang === 'ca' ? 'Veure tots els resultats' : 'Ver todos los resultados') + ' ›</a>';
        box.hidden = false; cur = -1;
      });
    };
    inp.addEventListener('input', show);
    inp.addEventListener('focus', function () { loadIdx(); if (inp.value.trim().length >= 3) show(); });
    inp.addEventListener('keydown', function (e) {
      var links = box.querySelectorAll('a');
      if (box.hidden || !links.length) return;
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        e.preventDefault();
        cur = (cur + (e.key === 'ArrowDown' ? 1 : -1) + links.length) % links.length;
        Array.prototype.forEach.call(links, function (l, i) { l.classList.toggle('on', i === cur); });
      } else if (e.key === 'Enter' && cur >= 0) { e.preventDefault(); location.href = links[cur].href; }
      else if (e.key === 'Escape') close();
    });
    document.addEventListener('click', function (e) { if (!fm.contains(e.target)) close(); });
  });

  var sres = $('sres');
  if (sres) {
    var norm = function (s) { return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/·/g, '.'); };
    var params = new URLSearchParams((location.search || '').slice(1) || (location.hash || '').slice(1));
    var q0 = params.get('q') || '', a0 = params.get('a') || '';
    var qi = $('qb'); qi.value = q0;
    Array.prototype.forEach.call(document.querySelectorAll('form.search.big input[name=a]'), function (r) { if (r.value === a0) r.checked = true; });
    var AMBN = lang === 'ca' ? { es: 'Espanya', cat: 'Catalunya', ue: 'Europa', hist: 'Història' } : { es: 'España', cat: 'Catalunya', ue: 'Europa', hist: 'Historia' };
    var info = $('sinfo'), idx = null;
    var mark = function (text, terms) {
      var t = esc(text), n = norm(t);
      var out = '', i = 0;
      // marca respetando acentos: se busca en el texto normalizado (misma longitud)
      var re = new RegExp(terms.map(function (x) { return x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('|'), 'g'), m;
      while ((m = re.exec(n))) { out += t.slice(i, m.index) + '<mark>' + t.slice(m.index, m.index + m[0].length) + '</mark>'; i = m.index + m[0].length; if (!m[0].length) re.lastIndex++; }
      return out + t.slice(i);
    };
    var run = function () {
      var q = norm(qi.value.trim()), a = (document.querySelector('form.search.big input[name=a]:checked') || {}).value || '';
      if (!q) { info.textContent = lang === 'ca' ? 'Escriu el que vols cercar.' : 'Escribe lo que quieres buscar.'; sres.innerHTML = ''; return; }
      IDX = idx; var E = engine(qi.value.trim(), a), terms = E.terms.length ? E.terms : [q];
      var res = E.res.map(function (p) { return [0, p]; });
      info.textContent = res.length ? (res.length + (lang === 'ca' ? (res.length === 1 ? ' resultat' : ' resultats') : (res.length === 1 ? ' resultado' : ' resultados'))) : (lang === 'ca' ? 'No hi ha resultats. Prova amb altres paraules.' : 'No hay resultados. Prueba con otras palabras.');
      sres.innerHTML = res.slice(0, 40).map(function (r) {
        var p = r[1], x = norm(p.x), pos = -1;
        terms.some(function (w) { pos = x.indexOf(w); return pos >= 0; });
        var snip = pos >= 0 ? (pos > 60 ? '…' : '') + p.x.slice(Math.max(0, pos - 60), pos + 160) + '…' : p.d;
        var href = BASE + p.u + (PREVIEW ? 'index.html' : '');
        return '<li><a href="' + href + '">' + mark(p.t, terms) + '</a>' + p.a.map(function (z) { return '<span class="amb">' + AMBN[z] + '</span>'; }).join('') + '<p>' + mark(snip, terms) + '</p></li>';
      }).join('');
    };
    fetch(BASE + 'assets/buscar-' + lang + '.json').then(function (r) { return r.json(); }).then(function (j) {
      idx = j; run();
      qi.addEventListener('input', run);
      Array.prototype.forEach.call(document.querySelectorAll('form.search.big input[name=a]'), function (r) { r.addEventListener('change', run); });
      qi.form.addEventListener('submit', function (e) { e.preventDefault(); run(); });
    }).catch(function () { info.textContent = lang === 'ca' ? 'No s’ha pogut carregar el cercador.' : 'No se ha podido cargar el buscador.'; });
  }

  // ---------- Contratos (todo en el navegador) ----------
  var doc = $('doc');
  if (doc) {
    var f = $('f'), tipo = doc.getAttribute('data-tipo') || 'prestamo';
    var HUECO = '______________________________', CORTO = '__________';
    var val = function (id) { var e = $(id); return e ? e.value : ''; };
    var txt = function (id, h) { var v = val(id).trim(); return v ? esc(v) : (h || CORTO); };
    var nom = function (id) { var v = val(id).trim(); return ($('bl').checked || !v) ? HUECO : esc(v); };
    var num = function (id) { return Number(val(id)) || 0; };
    var loc = lang === 'ca' ? 'ca-ES' : 'es-ES';
    var eur = function (n) { return Number(n || 0).toLocaleString(loc, { style: 'currency', currency: 'EUR' }); };
    var fecha = function () { return new Date().toLocaleDateString(loc, { day: 'numeric', month: 'long', year: 'numeric' }); };
    var P = function (b, t) { return '<p><b>' + b + '</b> ' + t + '</p>'; };
    var firma = function (a, b) { return '<div class="firma"><div>' + a + '</div><div>' + b + '</div></div>'; };
    var CA = lang === 'ca';
    var T = {
      prestamo: function () {
        var im = num('im'), pl = Math.max(1, num('pl')), ti = num('in');
        var r = ti / 100 / 12, cuota = r ? im * r / (1 - Math.pow(1 + r, -pl)) : im / pl, unico = im * (1 + ti / 100 * pl / 12), mensual = val('pa') === 'm';
        if (CA) return '<h3>CONTRACTE DE PRÉSTEC ENTRE PARTICULARS</h3><p>A ' + txt('ci') + ', ' + fecha() + '.</p>' +
          '<p><b>REUNITS</b>: d\'una banda, ' + nom('pr') + ', major d\'edat, amb DNI ____________, d\'ara endavant «la part prestadora»; i de l\'altra, ' + nom('pt') + ', major d\'edat, amb DNI ____________, d\'ara endavant «la part prestatària».</p>' +
          P('Primera. Objecte.', 'La part prestadora lliura en aquest acte a la part prestatària la quantitat de ' + eur(im) + ', que aquesta declara rebre.') +
          P('Segona. Interès.', ti ? 'El préstec merita un interès fix del ' + ti.toLocaleString(loc) + ' % anual.' : 'El préstec és gratuït i no merita interessos.') +
          P('Tercera. Devolució.', 'La part prestatària retornarà el capital ' + (mensual ? 'mitjançant ' + pl + ' quotes mensuals de ' + eur(cuota) + ', pagadores el dia 5 de cada mes per transferència bancària' : 'en un únic pagament de ' + eur(unico) + ' al venciment del termini de ' + pl + ' mesos') + '.') +
          P('Quarta. Amortització anticipada.', 'La part prestatària podrà retornar total o parcialment el préstec abans del termini, sense penalització.') +
          P('Cinquena. Impostos.', 'Aquest préstec està exempt de l\'Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados, però cal presentar el model 600 davant l\'administració tributària de la comunitat autònoma (a Catalunya, l\'Agència Tributària de Catalunya) en els 30 dies hàbils següents a la signatura.') +
          '<p>I, en prova de conformitat, les parts signen aquest contracte per duplicat.</p>' + firma('La part prestadora', 'La part prestatària');
        return '<h3>CONTRATO DE PRÉSTAMO ENTRE PARTICULARES</h3><p>En ' + txt('ci') + ', a ' + fecha() + '.</p>' +
          '<p><b>REUNIDOS</b>: de una parte, ' + nom('pr') + ', mayor de edad, con DNI ____________, en adelante «la parte prestamista»; y de otra, ' + nom('pt') + ', mayor de edad, con DNI ____________, en adelante «la parte prestataria».</p>' +
          P('Primera. Objeto.', 'La parte prestamista entrega en este acto a la parte prestataria la cantidad de ' + eur(im) + ', que esta declara recibir.') +
          P('Segunda. Interés.', ti ? 'El préstamo devenga un interés fijo del ' + ti.toLocaleString(loc) + ' % anual.' : 'El préstamo es gratuito y no devenga intereses.') +
          P('Tercera. Devolución.', 'La parte prestataria devolverá el capital ' + (mensual ? 'mediante ' + pl + ' cuotas mensuales de ' + eur(cuota) + ', pagaderas el día 5 de cada mes por transferencia bancaria' : 'en un único pago de ' + eur(unico) + ' al vencimiento del plazo de ' + pl + ' meses') + '.') +
          P('Cuarta. Amortización anticipada.', 'La parte prestataria podrá devolver total o parcialmente el préstamo antes del plazo, sin penalización.') +
          P('Quinta. Impuestos.', 'Este préstamo está exento del Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados, pero debe presentarse el modelo 600 ante la administración tributaria de la comunidad autónoma (en Catalunya, la Agència Tributària de Catalunya) en los 30 días hábiles siguientes a la firma.') +
          '<p>Y en prueba de conformidad, las partes firman el presente contrato por duplicado.</p>' + firma('La parte prestamista', 'La parte prestataria');
      },
      alquiler: function () {
        var re = num('re'), du = Math.max(1, num('du')), ga = Math.min(2, Math.max(0, num('ga'))), dp = Math.min(7, Math.max(1, num('dp') || 5)), pj = $('pj').checked, min = pj ? 7 : 5;
        if (CA) return '<h3>CONTRACTE DE LLOGUER D\'HABITATGE</h3><p>A ' + txt('ci') + ', ' + fecha() + '.</p>' +
          '<p><b>REUNITS</b>: d\'una banda, ' + nom('ar') + ', amb DNI/NIF ____________, com a part arrendadora; i de l\'altra, ' + nom('at') + ', amb DNI/NIE ____________, com a part arrendatària. Totes dues parts es reconeixen capacitat per signar aquest contracte.</p>' +
          P('Primera. Objecte.', 'La part arrendadora lloga a la part arrendatària l\'habitatge situat a ' + txt('di', HUECO) + ', perquè hi visqui de manera permanent com a habitatge habitual.') +
          P('Segona. Durada.', 'El contracte té una durada de ' + du + (du === 1 ? ' any' : ' anys') + ' a comptar d\'avui. Si la durada és inferior a ' + min + ' anys, es prorrogarà any rere any fins arribar a ' + min + ' anys, llevat que la part arrendatària comuniqui, amb 30 dies d\'antelació, que no el vol renovar. Després, si cap part no l\'ha denunciat, es prorrogarà anualment fins a 3 anys més.') +
          P('Tercera. Renda.', 'La renda és de ' + eur(re) + ' al mes, que la part arrendatària pagarà dins dels ' + dp + ' primers dies de cada mes per transferència al compte que indiqui la part arrendadora.') +
          P('Quarta. Actualització.', 'La renda s\'actualitzarà cada any, en la data en què es compleixi cada any de contracte, d\'acord amb l\'índex que estableixi la normativa vigent en cada moment.') +
          P('Cinquena. Fiança i garanties.', 'La part arrendatària lliura en aquest acte ' + eur(re) + ' en concepte de fiança legal, equivalent a una mensualitat de renda' + (ga ? ', i ' + eur(re * ga) + ' com a garantia addicional' : '') + '. La fiança es retornarà en acabar el contracte, descomptant-hi els danys o deutes que hi pugui haver. A Catalunya, la part arrendadora l\'ha de dipositar a l\'INCASÒL.') +
          P('Sisena. Despeses.', 'Les despeses de gestió immobiliària i de formalització del contracte són a càrrec de la part arrendadora. Els subministraments que es mesuren amb comptador (llum, aigua, gas) són a càrrec de la part arrendatària.') +
          P('Setena. Conservació.', 'La part arrendadora farà les reparacions necessàries per mantenir l\'habitatge en condicions d\'habitabilitat. Les petites reparacions pel desgast de l\'ús ordinari són a càrrec de la part arrendatària.') +
          P('Vuitena. Desistiment.', 'La part arrendatària pot deixar l\'habitatge quan hagin passat almenys 6 mesos, avisant per escrit amb 30 dies d\'antelació. En aquest cas indemnitzarà la part arrendadora amb una mensualitat de renda per cada any que quedi per complir; els períodes inferiors a un any donaran lloc a la part proporcional.') +
          P('Novena. Cessió i sotsarrendament.', 'La part arrendatària no pot cedir el contracte ni sotsarrendar l\'habitatge sense el consentiment per escrit de la part arrendadora.') +
          P('Desena. Documentació.', 'La part arrendadora lliura el certificat d\'eficiència energètica i, a Catalunya, la cèdula d\'habitabilitat.') +
          P('Onzena. Llei aplicable.', 'Aquest contracte es regeix per la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos.') +
          '<p>I, en prova de conformitat, les parts signen aquest contracte per duplicat.</p>' + firma('La part arrendadora', 'La part arrendatària');
        return '<h3>CONTRATO DE ARRENDAMIENTO DE VIVIENDA</h3><p>En ' + txt('ci') + ', a ' + fecha() + '.</p>' +
          '<p><b>REUNIDOS</b>: de una parte, ' + nom('ar') + ', con DNI/NIF ____________, como parte arrendadora; y de otra, ' + nom('at') + ', con DNI/NIE ____________, como parte arrendataria. Ambas partes se reconocen capacidad para firmar este contrato.</p>' +
          P('Primera. Objeto.', 'La parte arrendadora alquila a la parte arrendataria la vivienda situada en ' + txt('di', HUECO) + ', para que viva en ella de forma permanente como vivienda habitual.') +
          P('Segunda. Duración.', 'El contrato tiene una duración de ' + du + (du === 1 ? ' año' : ' años') + ' desde hoy. Si la duración es inferior a ' + min + ' años, se prorrogará año a año hasta alcanzar ' + min + ' años, salvo que la parte arrendataria comunique con 30 días de antelación que no desea renovarlo. Después, si ninguna parte lo ha denunciado, se prorrogará por años hasta 3 años más.') +
          P('Tercera. Renta.', 'La renta es de ' + eur(re) + ' al mes, que la parte arrendataria pagará dentro de los ' + dp + ' primeros días de cada mes por transferencia a la cuenta que indique la parte arrendadora.') +
          P('Cuarta. Actualización.', 'La renta se actualizará cada año, en la fecha en que se cumpla cada año de contrato, conforme al índice que establezca la normativa vigente en cada momento.') +
          P('Quinta. Fianza y garantías.', 'La parte arrendataria entrega en este acto ' + eur(re) + ' en concepto de fianza legal, equivalente a una mensualidad de renta' + (ga ? ', y ' + eur(re * ga) + ' como garantía adicional' : '') + '. La fianza se devolverá al terminar el contrato, descontando los daños o deudas que pudiera haber. En Catalunya, la parte arrendadora debe depositarla en el INCASÒL.') +
          P('Sexta. Gastos.', 'Los gastos de gestión inmobiliaria y de formalización del contrato son a cargo de la parte arrendadora. Los suministros que se miden por contador (luz, agua, gas) son a cargo de la parte arrendataria.') +
          P('Séptima. Conservación.', 'La parte arrendadora realizará las reparaciones necesarias para conservar la vivienda en condiciones de habitabilidad. Las pequeñas reparaciones por el desgaste del uso ordinario son a cargo de la parte arrendataria.') +
          P('Octava. Desistimiento.', 'La parte arrendataria puede dejar la vivienda cuando hayan pasado al menos 6 meses, avisando por escrito con 30 días de antelación. En ese caso indemnizará a la parte arrendadora con una mensualidad de renta por cada año que quede por cumplir; los periodos inferiores al año darán lugar a la parte proporcional.') +
          P('Novena. Cesión y subarriendo.', 'La parte arrendataria no puede ceder el contrato ni subarrendar la vivienda sin el consentimiento por escrito de la parte arrendadora.') +
          P('Décima. Documentación.', 'La parte arrendadora entrega el certificado de eficiencia energética y, en Catalunya, la cédula de habitabilidad.') +
          P('Undécima. Ley aplicable.', 'Este contrato se rige por la Ley 29/1994, de 24 de noviembre, de Arrendamientos Urbanos.') +
          '<p>Y en prueba de conformidad, las partes firman el presente contrato por duplicado.</p>' + firma('La parte arrendadora', 'La parte arrendataria');
      },
      habitacion: function () {
        var re = num('re'), du = Math.max(1, num('du')), fi = num('fi'), pv = num('pv') || 30, inc = val('gs') === 'i';
        if (CA) return '<h3>CONTRACTE DE LLOGUER D\'HABITACIÓ</h3><p>A ' + txt('ci') + ', ' + fecha() + '.</p>' +
          '<p><b>REUNITS</b>: d\'una banda, ' + nom('ar') + ', amb DNI/NIF ____________, com a part arrendadora; i de l\'altra, ' + nom('at') + ', amb DNI/NIE ____________, com a part arrendatària.</p>' +
          P('Primera. Objecte.', 'La part arrendadora lloga a la part arrendatària una habitació (' + txt('hb', HUECO) + ') del pis situat a ' + txt('di', HUECO) + ', amb dret a utilitzar la cuina, el bany i les zones comunes.') +
          P('Segona. Durada.', 'El contracte dura ' + du + (du === 1 ? ' mes' : ' mesos') + ' a comptar d\'avui. Es podrà renovar si totes dues parts hi estan d\'acord per escrit.') +
          P('Tercera. Preu.', 'El preu és de ' + eur(re) + ' al mes, que es pagarà dins dels 5 primers dies de cada mes.') +
          P('Quarta. Despeses.', inc ? 'El preu inclou les despeses de llum, aigua, gas i internet.' : 'Les despeses de llum, aigua, gas i internet es repartiran a parts iguals entre els ocupants del pis, segons les factures.') +
          P('Cinquena. Fiança.', fi ? 'La part arrendatària lliura ' + eur(re * fi) + ' com a fiança, que es retornarà en acabar el contracte si no hi ha danys ni deutes.' : 'No es lliura fiança.') +
          P('Sisena. Convivència.', 'La part arrendatària farà un ús adequat de l\'habitació i de les zones comunes, respectarà el descans dels altres ocupants i les normes de la comunitat, i no podrà allotjar altres persones de manera estable sense acord.') +
          P('Setena. Sortida anticipada.', 'Qualsevol de les parts pot posar fi al contracte avisant l\'altra per escrit amb ' + pv + ' dies d\'antelació.') +
          P('Vuitena. Llei aplicable.', 'Aquest contracte es regeix pel que s\'hi ha pactat i, en el que no s\'hi prevegi, pel Código Civil, sense perjudici de les normes imperatives que siguin aplicables.') +
          '<p>I, en prova de conformitat, les parts signen aquest contracte per duplicat.</p>' + firma('La part arrendadora', 'La part arrendatària');
        return '<h3>CONTRATO DE ALQUILER DE HABITACIÓN</h3><p>En ' + txt('ci') + ', a ' + fecha() + '.</p>' +
          '<p><b>REUNIDOS</b>: de una parte, ' + nom('ar') + ', con DNI/NIF ____________, como parte arrendadora; y de otra, ' + nom('at') + ', con DNI/NIE ____________, como parte arrendataria.</p>' +
          P('Primera. Objeto.', 'La parte arrendadora alquila a la parte arrendataria una habitación (' + txt('hb', HUECO) + ') del piso situado en ' + txt('di', HUECO) + ', con derecho a usar la cocina, el baño y las zonas comunes.') +
          P('Segunda. Duración.', 'El contrato dura ' + du + (du === 1 ? ' mes' : ' meses') + ' desde hoy. Podrá renovarse si ambas partes lo acuerdan por escrito.') +
          P('Tercera. Precio.', 'El precio es de ' + eur(re) + ' al mes, que se pagará dentro de los 5 primeros días de cada mes.') +
          P('Cuarta. Gastos.', inc ? 'El precio incluye los gastos de luz, agua, gas e internet.' : 'Los gastos de luz, agua, gas e internet se repartirán a partes iguales entre los ocupantes del piso, según las facturas.') +
          P('Quinta. Fianza.', fi ? 'La parte arrendataria entrega ' + eur(re * fi) + ' como fianza, que se devolverá al terminar el contrato si no hay daños ni deudas.' : 'No se entrega fianza.') +
          P('Sexta. Convivencia.', 'La parte arrendataria hará un uso adecuado de la habitación y de las zonas comunes, respetará el descanso de los demás ocupantes y las normas de la comunidad, y no podrá alojar a otras personas de forma estable sin acuerdo.') +
          P('Séptima. Salida anticipada.', 'Cualquiera de las partes puede poner fin al contrato avisando a la otra por escrito con ' + pv + ' días de antelación.') +
          P('Octava. Ley aplicable.', 'Este contrato se rige por lo pactado y, en lo no previsto, por el Código Civil, sin perjuicio de las normas imperativas que resulten aplicables.') +
          '<p>Y en prueba de conformidad, las partes firman el presente contrato por duplicado.</p>' + firma('La parte arrendadora', 'La parte arrendataria');
      },
      coche: function () {
        var pr = num('pr'), km = num('km');
        var hora = '____ : ____';
        if (CA) return '<h3>CONTRACTE DE COMPRAVENDA DE VEHICLE USAT</h3><p>A ' + txt('ci') + ', ' + fecha() + ', a les ' + hora + ' hores.</p>' +
          '<p><b>REUNITS</b>: d\'una banda, ' + nom('ve') + ', amb DNI ____________, com a part venedora; i de l\'altra, ' + nom('co') + ', amb DNI ____________, com a part compradora.</p>' +
          P('Primera. Objecte.', 'La part venedora ven a la part compradora el vehicle ' + txt('mm', HUECO) + ', amb matrícula ' + txt('mt') + ', número de bastidor ' + txt('bt', HUECO) + ' i ' + km.toLocaleString(loc) + ' quilòmetres.') +
          P('Segona. Preu.', 'El preu és de ' + eur(pr) + ', que la part venedora declara haver rebut en aquest acte.') +
          P('Tercera. Estat del vehicle.', 'La part compradora ha examinat el vehicle i l\'accepta en l\'estat en què es troba. La part venedora declara que el vehicle està lliure de càrregues, embargaments i multes pendents, i que no té cap defecte ocult que conegui.') +
          P('Quarta. Documentació.', 'La part venedora lliura el permís de circulació, la fitxa tècnica amb la ITV en vigor, l\'últim rebut de l\'impost de circulació i les claus.') +
          P('Cinquena. Canvi de titular.', 'La part compradora sol·licitarà a la Dirección General de Tráfico el canvi de titularitat en el termini legal. La part venedora podrà notificar la venda a Tráfico.') +
          P('Sisena. Impostos.', 'L\'Impuesto sobre Transmisiones Patrimoniales és a càrrec de la part compradora, que presentarà el model 620 davant l\'administració tributària de la comunitat autònoma (a Catalunya, l\'Agència Tributària de Catalunya).') +
          P('Setena. Responsabilitat.', 'A partir de la data i l\'hora d\'aquest contracte, la part compradora és responsable de les sancions, els danys i les despeses del vehicle.') +
          P('Vuitena. Defectes ocults.', 'La part venedora respon dels defectes ocults d\'acord amb la legislació civil aplicable (a Catalunya, el Codi civil de Catalunya).') +
          '<p>I, en prova de conformitat, les parts signen aquest contracte per duplicat.</p>' + firma('La part venedora', 'La part compradora');
        return '<h3>CONTRATO DE COMPRAVENTA DE VEHÍCULO USADO</h3><p>En ' + txt('ci') + ', a ' + fecha() + ', a las ' + hora + ' horas.</p>' +
          '<p><b>REUNIDOS</b>: de una parte, ' + nom('ve') + ', con DNI ____________, como parte vendedora; y de otra, ' + nom('co') + ', con DNI ____________, como parte compradora.</p>' +
          P('Primera. Objeto.', 'La parte vendedora vende a la parte compradora el vehículo ' + txt('mm', HUECO) + ', con matrícula ' + txt('mt') + ', número de bastidor ' + txt('bt', HUECO) + ' y ' + km.toLocaleString(loc) + ' kilómetros.') +
          P('Segunda. Precio.', 'El precio es de ' + eur(pr) + ', que la parte vendedora declara haber recibido en este acto.') +
          P('Tercera. Estado del vehículo.', 'La parte compradora ha examinado el vehículo y lo acepta en el estado en que se encuentra. La parte vendedora declara que el vehículo está libre de cargas, embargos y multas pendientes, y que no tiene ningún defecto oculto que conozca.') +
          P('Cuarta. Documentación.', 'La parte vendedora entrega el permiso de circulación, la ficha técnica con la ITV en vigor, el último recibo del impuesto de circulación y las llaves.') +
          P('Quinta. Cambio de titular.', 'La parte compradora solicitará a la Dirección General de Tráfico el cambio de titularidad en el plazo legal. La parte vendedora podrá notificar la venta a Tráfico.') +
          P('Sexta. Impuestos.', 'El Impuesto sobre Transmisiones Patrimoniales es a cargo de la parte compradora, que presentará el modelo 620 ante la administración tributaria de la comunidad autónoma (en Catalunya, la Agència Tributària de Catalunya).') +
          P('Séptima. Responsabilidad.', 'Desde la fecha y hora de este contrato, la parte compradora es responsable de las sanciones, daños y gastos del vehículo.') +
          P('Octava. Defectos ocultos.', 'La parte vendedora responde de los defectos ocultos conforme a la legislación civil aplicable (en Catalunya, el Codi civil de Catalunya).') +
          '<p>Y en prueba de conformidad, las partes firman el presente contrato por duplicado.</p>' + firma('La parte vendedora', 'La parte compradora');
      },
      garaje: function () {
        var re = num('re'), fi = num('fi'), du = Math.max(1, num('du'));
        if (CA) return '<h3>CONTRACTE DE LLOGUER DE PLAÇA DE GARATGE</h3><p>A ' + txt('ci') + ', ' + fecha() + '.</p>' +
          '<p><b>REUNITS</b>: d\'una banda, ' + nom('ar') + ', amb DNI/NIF ____________, com a part arrendadora; i de l\'altra, ' + nom('at') + ', amb DNI/NIE ____________, com a part arrendatària.</p>' +
          P('Primera. Objecte.', 'La part arrendadora lloga a la part arrendatària la plaça d\'aparcament situada a ' + txt('di', HUECO) + ', només per aparcar-hi un vehicle.') +
          P('Segona. Durada.', 'El contracte dura ' + du + (du === 1 ? ' mes' : ' mesos') + ' a comptar d\'avui i es prorrogarà per mesos si cap part no el denuncia amb 30 dies d\'antelació.') +
          P('Tercera. Renda.', 'La renda és de ' + eur(re) + ' al mes, que es pagarà dins dels 5 primers dies de cada mes.') +
          P('Quarta. Fiança.', fi ? 'La part arrendatària lliura ' + eur(re * fi) + ' com a fiança, que es retornarà en acabar el contracte si no hi ha danys ni deutes.' : 'No es lliura fiança.') +
          P('Cinquena. Ús.', 'No es poden guardar a la plaça materials inflamables ni objectes que no siguin el vehicle. La part arrendatària respectarà les normes de la comunitat.') +
          P('Sisena. Accés.', 'La part arrendadora lliura el comandament o la clau d\'accés, que la part arrendatària retornarà en acabar el contracte.') +
          P('Setena. Llei aplicable.', 'Aquest contracte es regeix pel que s\'hi ha pactat i, en el que no s\'hi prevegi, pel Código Civil.') +
          '<p>I, en prova de conformitat, les parts signen aquest contracte per duplicat.</p>' + firma('La part arrendadora', 'La part arrendatària');
        return '<h3>CONTRATO DE ALQUILER DE PLAZA DE GARAJE</h3><p>En ' + txt('ci') + ', a ' + fecha() + '.</p>' +
          '<p><b>REUNIDOS</b>: de una parte, ' + nom('ar') + ', con DNI/NIF ____________, como parte arrendadora; y de otra, ' + nom('at') + ', con DNI/NIE ____________, como parte arrendataria.</p>' +
          P('Primera. Objeto.', 'La parte arrendadora alquila a la parte arrendataria la plaza de aparcamiento situada en ' + txt('di', HUECO) + ', solo para aparcar un vehículo.') +
          P('Segunda. Duración.', 'El contrato dura ' + du + (du === 1 ? ' mes' : ' meses') + ' desde hoy y se prorrogará por meses si ninguna parte lo denuncia con 30 días de antelación.') +
          P('Tercera. Renta.', 'La renta es de ' + eur(re) + ' al mes, que se pagará dentro de los 5 primeros días de cada mes.') +
          P('Cuarta. Fianza.', fi ? 'La parte arrendataria entrega ' + eur(re * fi) + ' como fianza, que se devolverá al terminar el contrato si no hay daños ni deudas.' : 'No se entrega fianza.') +
          P('Quinta. Uso.', 'No se pueden guardar en la plaza materiales inflamables ni objetos distintos del vehículo. La parte arrendataria respetará las normas de la comunidad.') +
          P('Sexta. Acceso.', 'La parte arrendadora entrega el mando o la llave de acceso, que la parte arrendataria devolverá al terminar el contrato.') +
          P('Séptima. Ley aplicable.', 'Este contrato se rige por lo pactado y, en lo no previsto, por el Código Civil.') +
          '<p>Y en prueba de conformidad, las partes firman el presente contrato por duplicado.</p>' + firma('La parte arrendadora', 'La parte arrendataria');
      }
    };
    var cd = $('cdata');
    if (cd) {
      var D = JSON.parse(cd.textContent);
      T.gen = function () {
        var sel = function (id) { var e = $(id); return e && e.selectedIndex >= 0 ? esc(e.options[e.selectedIndex].text) : ''; };
        var fill = function (s) {
          return s.replace(/\{fecha\}/g, fecha()).replace(/\{(n|t|T|e|d|s|a):(\w+)\}/g, function (m, k, id) {
            if (k === 'n') return nom(id);
            if (k === 't') return txt(id);
            if (k === 'T') return txt(id, HUECO);
            if (k === 'e') return eur(num(id));
            if (k === 'd') return num(id).toLocaleString(loc);
            if (k === 's') return sel(id);
            if (k === 'a') { var v = val(id).trim(); return v ? esc(v).replace(/\n/g, '<br>') : HUECO + '<br>' + HUECO; }
            return m;
          });
        };
        return '<h3>' + D.t + '</h3><p>' + fill(D.i) + '</p>' + D.c.map(function (c) { return '<p>' + (c[0] ? '<b>' + c[0] + '</b> ' : '') + fill(c[1]) + '</p>'; }).join('') +
          (D.f ? '<p>' + D.f + '</p>' : '') + '<div class="firma' + (D.s.length === 1 ? ' one' : D.s.length === 3 ? ' three' : '') + '">' + D.s.map(function (x) { return '<div>' + x + '</div>'; }).join('') + '</div>';
      };
    }
    var render = function () { doc.innerHTML = (T[tipo] || T.prestamo)(); };
    f.addEventListener('input', render);
    f.addEventListener('change', render);
    f.addEventListener('submit', function (e) { e.preventDefault(); });
    render();
    var msg = $('cmsg');
    $('copiar').addEventListener('click', function () {
      var ok = CA ? 'Contracte copiat.' : 'Contrato copiado.';
      var sel = function () {
        var r = document.createRange(); r.selectNodeContents(doc);
        var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
        msg.textContent = CA ? 'Text seleccionat: prem Ctrl+C.' : 'Texto seleccionado: pulsa Ctrl+C.';
      };
      try { navigator.clipboard.writeText(doc.innerText).then(function () { msg.textContent = ok; }, sel); } catch (e) { sel(); }
    });
    var pb = $('imprimir'); if (pb) pb.addEventListener('click', function () { window.print(); });
    $('borrar').addEventListener('click', function () { f.reset(); render(); msg.textContent = CA ? 'Dades esborrades.' : 'Datos borrados.'; });
    // Al salir de la página no queda nada: el formulario se vacía.
    window.addEventListener('pagehide', function () { f.reset(); });
  }

  // ---------- DOGC y EUR-Lex (los sirve api/feed.php en el propio servidor) ----------
  Array.prototype.forEach.call(document.querySelectorAll('[data-feed]'), function (ul) {
    var id = ul.getAttribute('data-feed'), info = $(ul.getAttribute('data-info'));
    var fmtd = function (d) { return d ? new Date(d + 'T12:00:00').toLocaleDateString(lang === 'ca' ? 'ca-ES' : 'es-ES', { day: 'numeric', month: 'short', year: 'numeric' }) : ''; };
    fetch(BASE + 'api/feed.php?f=' + id, { headers: { Accept: 'application/json' } }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (j) {
      if (!j || !j.items || !j.items.length) throw new Error('vacío');
      info.textContent = j.fuente + ' · ' + j.items.length + (lang === 'ca' ? ' publicacions recents' : ' publicaciones recientes');
      ul.innerHTML = j.items.map(function (it) {
        if (!/^https:\/\//.test(it.url)) return '';
        return '<li><span class="dep">' + esc(fmtd(it.fecha)) + '</span><a href="' + esc(it.url) + '" target="_blank" rel="noopener">' + esc(it.titulo) + '</a></li>';
      }).join('');
    }).catch(function () {
      info.textContent = lang === 'ca' ? 'Ara mateix no es pot connectar amb la font oficial. Consulta-la directament.' : 'Ahora mismo no se puede conectar con la fuente oficial. Consúltala directamente.';
    });
  });

  // ---------- Portada: resumen de DOGC y EUR-Lex ----------
  ['dogc', 'ue'].forEach(function (id) {
    var n = $(id + '-n'), f = $(id + '-fecha');
    if (!n) return;
    fetch(BASE + 'api/feed.php?f=' + id, { headers: { Accept: 'application/json' } }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (j) {
      if (!j || !j.items || !j.items.length) throw new Error('vacío');
      n.textContent = j.items.length + (lang === 'ca' ? ' publicacions recents' : ' publicaciones recientes');
      var d = j.items[0].fecha;
      if (d) f.textContent = new Date(d + 'T12:00:00').toLocaleDateString(lang === 'ca' ? 'ca-ES' : 'es-ES', { day: 'numeric', month: 'long', year: 'numeric' });
    }).catch(function () {});
  });

  // ---------- BOE (lo sirve api/boe.php en el propio servidor) ----------
  var list = $('boe-list'), panel = $('boe-panel');
  if (!list && !panel) return;
  var api = BASE + 'api/boe.php';
  var fmt = function (d) { return new Date(d.slice(0, 4) + '-' + d.slice(4, 6) + '-' + d.slice(6, 8) + 'T12:00:00').toLocaleDateString(lang === 'ca' ? 'ca-ES' : 'es-ES', { day: 'numeric', month: 'long', year: 'numeric' }); };
  fetch(api, { headers: { Accept: 'application/json' } }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }).then(function (j) {
    if (!j || !j.fecha) throw new Error('vacío');
    if (panel) {
      $('boe-fecha').textContent = fmt(j.fecha);
      $('boe-total').textContent = j.total;
      if ($('boe-secs')) $('boe-secs').innerHTML = (j.secciones || []).map(function (s) { return '<li><span>' + s.nombre.replace(/[<>&]/g, '') + '</span><span class="num">' + s.n + '</span></li>'; }).join('');
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
    if (panel) { $('boe-total').parentNode.textContent = 'Boletín Oficial del Estado'; $('boe-fecha').textContent = lang === 'ca' ? 'Consulta-ho a boe.es' : 'Consúltalo en boe.es'; }
  });
})();

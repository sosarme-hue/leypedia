(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var lang = document.documentElement.lang === 'ca' ? 'ca' : 'es';

  var BASE = (document.querySelector('link[rel=stylesheet]').getAttribute('href') || '').replace('assets/style.css', '');
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
      var terms = q.split(/\s+/).filter(function (x) { return x.length > 1 || /\d/.test(x); });
      if (!terms.length) terms = [q];
      var res = [];
      idx.forEach(function (p) {
        if (a && p.a.indexOf(a) < 0) return;
        var t = norm(p.t), d = norm(p.d), x = norm(p.x), sc = 0, ok = true;
        terms.forEach(function (w) {
          var s = 0;
          if (t.indexOf(w) >= 0) s += 12;
          if (d.indexOf(w) >= 0) s += 5;
          var c = x.split(w).length - 1; s += Math.min(c, 8);
          if (!s) ok = false; sc += s;
        });
        if (ok) res.push([sc, p]);
      });
      res.sort(function (u, v) { return v[0] - u[0]; });
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

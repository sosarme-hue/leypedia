/* Classicapedia · consentimiento, analítica y publicidad (nov 2026)
   - El aviso de cookies es el de Google (CMP certificado, TCF v2.2), configurado en AdSense > Privacidad y mensajes.
   - Google Analytics solo se carga si el visitante lo acepta en ese aviso (finalidad 1 y proveedor Google, 755).
   - AdSense (anuncios automáticos) se carga en todas las páginas; Google respeta la elección del aviso. */
window.dataLayer = window.dataLayer || []; function gtag() { dataLayer.push(arguments); }
gtag('consent', 'default', {analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'});
window.GA_ID = 'G-GXF84YCY44';
window.ADS_ID = 'ca-pub-6250668607782976';
window.cargarGA = function () {
  if (window.gaCargado) return; window.gaCargado = true;
  gtag('consent', 'update', {analytics_storage: 'granted'});
  var s = document.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID; document.head.appendChild(s);
  gtag('js', new Date()); gtag('config', GA_ID);
};
(function () {
  /* AdSense: si la página no lo trae ya en el <head>, se añade aquí */
  if (!document.querySelector('script[src*="adsbygoogle.js"]')) {
    var a = document.createElement('script'); a.async = true; a.crossOrigin = 'anonymous';
    a.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + ADS_ID;
    document.head.appendChild(a);
  }
  /* Analytics según la elección en el aviso de Google */
  var n = 0;
  (function esperar() {
    if (typeof window.__tcfapi === 'function') {
      window.__tcfapi('addEventListener', 2, function (d, ok) {
        if (!ok || !d) return;
        if (d.gdprApplies === false) { cargarGA(); return; }
        if (d.eventStatus !== 'tcloaded' && d.eventStatus !== 'useractioncomplete') return;
        if (d.purpose && d.purpose.consents && d.purpose.consents[1] && d.vendor && d.vendor.consents && d.vendor.consents[755]) cargarGA();
      });
    } else if (n++ < 50) setTimeout(esperar, 200);
  })();
  /* el aviso propio antiguo ya no se usa: lo sustituye el de Google */
  var css = document.createElement('style'); css.textContent = '#aviso-cookies{display:none!important}'; document.head.appendChild(css);
  /* «Configurar cookies» abre de nuevo el aviso de Google */
  window.addEventListener('click', function (e) {
    var l = e.target.closest && e.target.closest('[data-cookies]'); if (!l) return;
    e.preventDefault(); e.stopImmediatePropagation();
    window.googlefc = window.googlefc || {}; googlefc.callbackQueue = googlefc.callbackQueue || [];
    googlefc.callbackQueue.push(function () { googlefc.showRevocationMessage(); });
  }, true);
  /* enlace a Contacto en el pie */
  function contacto() {
    var p = document.querySelector('footer .legales'); if (!p || p.querySelector('a[href$="contacto.html"]')) return;
    var en = (document.documentElement.lang || 'es').slice(0, 2) === 'en';
    var al = p.querySelector('a[href*="aviso-legal.html"]');
    var a = document.createElement('a'); a.href = al ? al.getAttribute('href').replace('aviso-legal.html', 'contacto.html') : (window.RAIZ || '') + 'contacto.html'; a.textContent = en ? 'Contact' : 'Contacto';
    p.insertBefore(document.createTextNode(' · '), p.firstChild); p.insertBefore(a, p.firstChild);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', contacto); else contacto();
})();

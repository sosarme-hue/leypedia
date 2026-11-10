
/* enlace «Blog» en el menú, después de Posts (nov 2026) */
(function () {
  function blog() {
    var m = document.querySelector('.cab .menu'); if (!m || m.querySelector('a[href$="blog/"]')) return;
    var p = m.querySelector('a[href$="posts.html"]'); if (!p) return;
    var a = document.createElement('a'); a.href = p.getAttribute('href').replace('posts.html', 'blog/'); a.textContent = 'Blog';
    p.parentNode.insertBefore(a, p.nextSibling);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', blog); else blog();
})();

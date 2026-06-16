/* ═══════════════════════════════════════════════════════
   CRS GROWTH — main.js v3
   Nav · Reveal · Ticker · Hamburger
═══════════════════════════════════════════════════════ */

(function() {

  // ── LOAD NAV & FOOTER ──────────────────────────────────
  function loadComponent(id, url, cb) {
    var el = document.getElementById(id);
    if (!el) return;
    fetch(url)
      .then(function(r) { return r.text(); })
      .then(function(html) {
        el.innerHTML = html;
        if (cb) cb();
      })
      .catch(function() {});
  }

  function initNav() {
    // Active link
    var links = document.querySelectorAll('.nav-links a, .nav-drawer-links a');
    var path = window.location.pathname;
    links.forEach(function(a) {
      if (a.getAttribute('href') === path || (path !== '/' && a.getAttribute('href') !== '/' && path.startsWith(a.getAttribute('href')))) {
        a.classList.add('active');
      }
    });

    // Scroll shadow
    var nav = document.getElementById('site-nav');
    if (nav) {
      window.addEventListener('scroll', function() {
        nav.classList.toggle('scrolled', window.scrollY > 10);
      }, { passive: true });
    }

    // Hamburger
    var btn = document.getElementById('nav-hamburger');
    var drawer = document.getElementById('nav-drawer');
    if (btn && drawer) {
      btn.addEventListener('click', function() {
        var open = drawer.classList.toggle('open');
        btn.classList.toggle('open', open);
        btn.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
      });
      // Close on link click
      drawer.querySelectorAll('a').forEach(function(a) {
        a.addEventListener('click', function() {
          drawer.classList.remove('open');
          btn.classList.remove('open');
        });
      });
    }
  }

  // ── REVEAL ON SCROLL ──────────────────────────────────
  function initReveal() {
    var els = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
    if (!els.length) return;
    var io = new IntersectionObserver(function(entries) {
      entries.forEach(function(e) {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function(el) { io.observe(el); });
  }

  // ── TICKER DUPLICATE ─────────────────────────────────
  function initTicker() {
    var inner = document.querySelector('.ticker-inner');
    if (!inner) return;
    // Already doubled in HTML for seamless loop
  }

  // ── SMOOTH ANCHOR SCROLL ─────────────────────────────
  document.addEventListener('click', function(e) {
    var a = e.target.closest('a[href^="#"]');
    if (!a) return;
    var target = document.querySelector(a.getAttribute('href'));
    if (!target) return;
    e.preventDefault();
    var navH = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-h')) || 64;
    window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - navH - 16, behavior: 'smooth' });
  });

  // ── INIT ─────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', function() {
    loadComponent('nav-placeholder', '/components/nav.html', initNav);
    loadComponent('footer-placeholder', '/components/footer.html', null);
    initReveal();
    initTicker();
  });

})();

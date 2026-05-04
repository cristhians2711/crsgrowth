/* ═══════════════════════════════════════════════
   CRS GROWTH — main.js
   Carga nav y footer dinámicamente + utilidades
═══════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ── 1. INJECT COMPONENTS ── */
  async function loadComponent(url, targetId) {
    try {
      const res = await fetch(url);
      if (!res.ok) throw new Error('fetch failed');
      const html = await res.text();
      const el = document.getElementById(targetId);
      if (el) {
        el.innerHTML = html;
        // Run any inline scripts inside the injected HTML
        el.querySelectorAll('script').forEach((s) => {
          const ns = document.createElement('script');
          ns.textContent = s.textContent;
          document.body.appendChild(ns);
        });
      }
    } catch (e) {
      console.warn('Could not load component:', url, e);
    }
  }

  async function initComponents() {
    const base = '/components/';
    await Promise.all([
      loadComponent(base + 'nav.html', 'nav-placeholder'),
      loadComponent(base + 'footer.html', 'footer-placeholder'),
    ]);
    initNav();
    markActiveLink();
  }

  /* ── 2. NAV BEHAVIOUR ── */
  function initNav() {
    const header = document.getElementById('site-nav');
    if (!header) return;

    // Scroll effect
    const onScroll = () => {
      if (window.scrollY > 24) {
        header.classList.add('nav-scrolled');
      } else {
        header.classList.remove('nav-scrolled');
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // Hamburger
    const btn = document.getElementById('nav-hamburger');
    const drawer = document.getElementById('nav-drawer');
    if (btn && drawer) {
      btn.addEventListener('click', () => {
        const isOpen = drawer.classList.toggle('open');
        btn.classList.toggle('open', isOpen);
        document.body.style.overflow = isOpen ? 'hidden' : '';
      });
      // Close on link click
      drawer.querySelectorAll('a').forEach((a) => {
        a.addEventListener('click', () => {
          drawer.classList.remove('open');
          btn.classList.remove('open');
          document.body.style.overflow = '';
        });
      });
    }
  }

  /* ── 3. MARK ACTIVE LINK ── */
  function markActiveLink() {
    const path = window.location.pathname;
    document.querySelectorAll('.nav-links a, .nav-drawer-links a').forEach((a) => {
      try {
        const url = new URL(a.href);
        if (url.pathname === path || (path !== '/' && url.pathname.startsWith(path))) {
          a.classList.add('active');
        }
      } catch (_) {}
    });
  }

  /* ── 4. SCROLL REVEAL ── */
  function initReveal() {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add('visible');
            observer.unobserve(e.target); // fire once
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -48px 0px' }
    );

    document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale').forEach((el) => {
      observer.observe(el);
    });
  }

  /* ── 5. SMOOTH SCROLL (native fallback) ── */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach((a) => {
      a.addEventListener('click', (e) => {
        const id = a.getAttribute('href').slice(1);
        const target = document.getElementById(id);
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  /* ── 6. TICKER ── */
  function initTicker() {
    const ticker = document.querySelector('.ticker-inner');
    if (!ticker) return;
    // Already animated via CSS; just ensure items are duplicated if not
    if (ticker.children.length < 6) {
      const clone = ticker.innerHTML;
      ticker.innerHTML = clone + clone;
    }
  }

  /* ── 7. COUNTER ANIMATION ── */
  function animateCounters() {
    document.querySelectorAll('[data-count]').forEach((el) => {
      const target = parseFloat(el.dataset.count);
      const prefix = el.dataset.prefix || '';
      const suffix = el.dataset.suffix || '';
      const duration = 1600;
      const start = performance.now();

      function step(now) {
        const progress = Math.min((now - start) / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 3);
        const current = Math.round(target * ease);
        el.textContent = prefix + current + suffix;
        if (progress < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
  }

  // Trigger counters when visible
  function initCounters() {
    const els = document.querySelectorAll('[data-count]');
    if (!els.length) return;
    const obs = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          animateCounters();
          obs.disconnect();
        }
      });
    }, { threshold: 0.3 });
    els.forEach((el) => obs.observe(el));
  }

  /* ── INIT ── */
  document.addEventListener('DOMContentLoaded', () => {
    initComponents().then(() => {
      initReveal();
      initSmoothScroll();
      initTicker();
      initCounters();
    });
  });

})();

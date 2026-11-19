/* CRS Growth v6 */
(function () {
  var nav = document.querySelector('.nav');
  var menu = document.querySelector('.nav-menu');
  if (nav && menu) {
    menu.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menu.setAttribute('aria-expanded', open ? 'true' : 'false');
      menu.textContent = open ? 'Cerrar' : 'Menú';
    });
  }

  // La hoja de ruta se rellena una vez: empieza en "Hoy" y, al verla, pasa a "Con CRS" y se sella.
  // Sin script o con movimiento reducido se muestra directamente el estado final.
  var route = document.querySelector('.route[data-play]');
  if (route && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var hoy = route.querySelector('.hoy-input');
    var go = route.querySelector('.go');
    var touched = false;
    route.addEventListener('pointerdown', function () { touched = true; });
    route.addEventListener('keydown', function () { touched = true; });
    hoy.checked = true;
    var play = function () { setTimeout(function () { if (!touched) go.checked = true; }, 1800); };
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (e) { if (e[0].isIntersecting) { play(); io.disconnect(); } }, { threshold: 0.3 });
      io.observe(route);
    } else { play(); }
  }

  // Formularios: envío real a Web3Forms
  document.querySelectorAll('form[data-endpoint]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var box = form.closest('.form');
      var status = form.querySelector('.status');
      var btn = form.querySelector('[type=submit]');
      var label = btn.textContent;
      status.textContent = '';
      btn.disabled = true; btn.setAttribute('aria-busy', 'true'); btn.textContent = 'Enviando';
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = data[k] ? data[k] + ', ' + v : v; });
      var stage = form.querySelector('input[name="momento"]:checked');
      if (stage && stage.dataset.tipo) data.clasificacion_lead = stage.dataset.tipo;
      data.subject = (form.dataset.subject || 'Web') + ': ' + (data.nombre || 'sin nombre') + (data.clasificacion_lead ? ' [' + data.clasificacion_lead + ']' : '');
      fetch(form.dataset.endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { return r.json().then(function (j) { if (!r.ok || !j.success) throw new Error(j.message); }); })
        .then(function () { box.classList.add('sent'); box.querySelector('.done').focus(); })
        .catch(function () {
          status.textContent = 'No se ha podido enviar. Inténtalo de nuevo o escríbenos por WhatsApp.';
          btn.disabled = false; btn.removeAttribute('aria-busy'); btn.textContent = label;
        });
    });
  });
})();

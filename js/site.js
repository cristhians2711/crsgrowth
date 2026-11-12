/* CRS Growth — site.js v4 */
(function () {
  // Menú móvil
  var toggle = document.querySelector('.nav-toggle');
  var links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var abierto = links.classList.toggle('abierto');
      toggle.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { links.classList.remove('abierto'); toggle.setAttribute('aria-expanded', 'false'); }
    });
  }

  // Diagrama: antes (todo pasa por ti) → después (la empresa fluye, tú diriges)
  var flujo = document.querySelector('.flujo');
  if (flujo) {
    var boton = flujo.querySelector('[data-alternar]');
    var estado = flujo.querySelector('[data-estado]');
    var textos = {
      antes: '<strong>Antes:</strong> todo pasa por ti',
      despues: '<strong>Después:</strong> la empresa fluye, tú diriges'
    };
    var poner = function (ordenado) {
      flujo.classList.toggle('ordenado', ordenado);
      estado.innerHTML = ordenado ? textos.despues : textos.antes;
      boton.textContent = ordenado ? 'Ver el antes' : 'Ver el después';
    };
    var reducido = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reducido) { poner(true); }
    else {
      poner(false);
      var arrancar = function () { setTimeout(function () { poner(true); }, 1600); };
      if ('IntersectionObserver' in window) {
        var io = new IntersectionObserver(function (entradas) {
          if (entradas[0].isIntersecting) { arrancar(); io.disconnect(); }
        }, { threshold: 0.4 });
        io.observe(flujo);
      } else { arrancar(); }
    }
    boton.addEventListener('click', function () { poner(!flujo.classList.contains('ordenado')); });
  }

  // Formularios → Web3Forms (llegan por email)
  document.querySelectorAll('form[data-web3]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var caja = form.closest('.formulario');
      var estadoEl = form.querySelector('.estado');
      var btn = form.querySelector('[type=submit]');
      var original = btn.textContent;
      estadoEl.textContent = '';
      btn.disabled = true; btn.textContent = 'Enviando…';

      var datos = new FormData(form);
      var payload = {};
      datos.forEach(function (valor, clave) {
        payload[clave] = payload[clave] ? payload[clave] + ' · ' + valor : valor;
      });
      var etapa = form.querySelector('input[name="momento"]:checked');
      if (etapa && etapa.dataset.clasificacion) {
        payload.clasificacion_lead = etapa.dataset.clasificacion;
      }
      if (form.dataset.asunto) {
        payload.subject = form.dataset.asunto + ' — ' + (payload.nombre || 'Sin nombre') +
          (payload.clasificacion_lead ? ' [' + payload.clasificacion_lead + ']' : '');
      }

      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(payload)
      })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || !res.j.success) throw new Error(res.j.message || 'Error');
          caja.classList.add('enviado');
          caja.scrollIntoView({ behavior: 'smooth', block: 'center' });
        })
        .catch(function () {
          estadoEl.textContent = 'No se ha podido enviar. Revisa tu conexión e inténtalo de nuevo, o escríbenos por WhatsApp.';
          btn.disabled = false; btn.textContent = original;
        });
    });
  });
})();

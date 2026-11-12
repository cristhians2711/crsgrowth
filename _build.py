# Genera las páginas del sitio con la misma cabecera, navegación y pie.
# Uso: python3 _build.py   (no se publica; GitHub Pages ignora archivos que empiezan por _)
import os, textwrap

DOM = "https://www.crsgrowth.com"
WA = "https://wa.me/34697293677"
CAL = "https://calendly.com/cristhiam-silva-crsgrowth/30min"
MAIL = "cristhiam.silva@crsgrowth.com"
KEY = "3a2696c7-20c0-42bf-ba11-cfabf5933296"  # Web3Forms (ya existente)

def head(title, desc, path, body_class="", noindex=False):
    robots = '<meta name="robots" content="noindex">' if noindex else ''
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{DOM}{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOM}{path}">
<meta property="og:image" content="{DOM}/img/icono-512.png">
<meta name="theme-color" content="#16171B">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preload" href="/fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/site.css">
</head>
<body class="{body_class}">
<a class="sr-only" href="#contenido">Saltar al contenido</a>
'''

def nav(actual):
    items = [
        ("/#que-hacemos", "Qué hacemos", "inicio"),
        ("/#como-trabajamos", "Cómo trabajamos", "inicio2"),
        ("/constitucion/", "Constitución", "constitucion"),
        ("/cristhiamsilva/", "Cristhiam Silva", "personal"),
    ]
    lis = "".join(
        f'<li><a href="{h}"{' aria-current="page"' if k == actual else ''}>{t}</a></li>' for h, t, k in items)
    return f'''<header class="nav">
  <div class="wrap">
    <a class="marca" href="/" aria-label="CRS Growth, inicio"><img src="/img/crs-escudo.png" alt="" width="34" height="33">CRS <span>Growth</span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="menu" aria-label="Abrir menú">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 7h18M3 12h18M3 17h18"/></svg>
    </button>
    <ul class="nav-links" id="menu">{lis}<li><a class="btn btn-oro" href="/contacto/">Hablemos</a></li></ul>
  </div>
</header>
<main id="contenido">
'''

FOOT = f'''</main>
<footer class="pie">
  <div class="wrap">
    <div class="pie-grid">
      <div>
        <a class="marca" href="/"><img src="/img/crs-escudo.png" alt="" width="34" height="33">CRS <span>Growth</span></a>
        <p style="margin-top:16px">Dirección y gestión de empresas. Ordenamos cómo funciona tu empresa para que deje de depender de ti.</p>
      </div>
      <div>
        <h4>Sitio</h4>
        <ul>
          <li><a href="/#que-hacemos">Qué hacemos</a></li>
          <li><a href="/constitucion/">Constitución de empresas</a></li>
          <li><a href="/cristhiamsilva/">Acompañamiento personal</a></li>
          <li><a href="/contacto/">Contacto</a></li>
        </ul>
      </div>
      <div>
        <h4>Contacto</h4>
        <ul>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp +34 697 293 677</a></li>
          <li><a href="https://www.linkedin.com/company/crsgrowth" target="_blank" rel="noopener">LinkedIn</a></li>
          <li>Sevilla, España · también en remoto</li>
        </ul>
      </div>
    </div>
    <div class="pie-legal">
      <p>© 2026 CRS Growth es una marca comercial de Novaryn OÜ (Estonia, código de registro 17556049).</p>
      <p><a href="/aviso-legal/">Aviso legal</a> &nbsp; <a href="/privacidad/">Privacidad</a> &nbsp; <a href="/cookies/">Cookies</a></p>
    </div>
  </div>
</footer>
<script src="/js/site.js"></script>
</body>
</html>
'''

def page(path, title, desc, actual, body, body_class="", noindex=False):
    out = head(title, desc, path, body_class, noindex) + nav(actual) + body + FOOT
    f = path.strip("/")
    f = os.path.join(f, "index.html") if f else "index.html"
    os.makedirs(os.path.dirname(f) or ".", exist_ok=True)
    open(f, "w", encoding="utf-8").write(out)
    print("ok", f)

def redirect(path, to):
    f = os.path.join(path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(
        f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="robots" content="noindex">'
        f'<meta http-equiv="refresh" content="0;url={to}"><link rel="canonical" href="{DOM}{to}"><title>CRS Growth</title></head>'
        f'<body><a href="{to}">Continuar</a></body></html>')
    print("redir", f, "->", to)

def hidden(asunto):
    return (f'<input type="hidden" name="access_key" value="{KEY}">'
            f'<input type="hidden" name="from_name" value="Web CRS Growth">'
            f'<input type="checkbox" name="botcheck" class="trampa" tabindex="-1" autocomplete="off">')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
exec(open("_paginas.py", encoding="utf-8").read())

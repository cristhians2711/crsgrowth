# Genera el sitio CRS Growth v6 (tema Coral). Uso: python3 _build.py
# GitHub Pages no publica archivos que empiezan por "_".
import os

DOM = "https://www.crsgrowth.com"
WA = "https://wa.me/34697293677"
CAL = "https://calendly.com/cristhiam-silva-crsgrowth/30min"
MAIL = "cristhiam.silva@crsgrowth.com"
KEY = "3a2696c7-20c0-42bf-ba11-cfabf5933296"
ENDPOINT = "https://api.web3forms.com/submit"
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Filtro del sello: la tinta entra irregular en el papel
PRESS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><filter id="prensa" x="-10%" y="-20%" width="120%" height="140%">
<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="4" result="n"/>
<feColorMatrix in="n" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1.5 1.45" result="m"/>
<feComposite in="SourceGraphic" in2="m" operator="in"/></filter></svg>'''


def head(title, desc, path, cls="", noindex=False):
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{DOM}{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOM}{path}">
<meta property="og:image" content="{DOM}/img/icono-512.png">
<meta name="theme-color" content="#EEE9E4">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preload" href="/fonts/figtree.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/site.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body class="{cls}">
<a class="skip" href="#main">Saltar al contenido</a>
{PRESS}
'''


def nav(cur):
    def a(href, text, key):
        c = ' aria-current="page"' if key == cur else ""
        return f'<li><a href="{href}"{c}>{text}</a></li>'
    return f'''<header class="nav">
  <div class="container">
    <a class="mark" href="/">CRS <span>Growth</span></a>
    <div class="nav-links">
      <ul>
        {a("/#que-llevamos", "Qué llevamos", "x")}
        {a("/constitucion/", "Constitución", "constitucion")}
        {a("/cristhiamsilva/", "Cristhiam Silva", "personal")}
        {a("/contacto/", "Contacto", "contacto")}
      </ul>
      <a class="btn btn--ink btn--small" href="{CAL}" target="_blank" rel="noopener">Reservar llamada</a>
      <button class="btn btn--card btn--small nav-menu" type="button" aria-expanded="false">Menú</button>
    </div>
  </div>
</header>
<main id="main">
'''


FOOT = f'''</main>
<footer class="foot">
  <div class="container">
    <a class="mark" href="/">CRS <span>Growth</span></a>
    <nav aria-label="Pie"><ul>
      <li><a href="/#que-llevamos">Qué llevamos</a></li>
      <li><a href="/constitucion/">Constitución de empresas</a></li>
      <li><a href="/cristhiamsilva/">Acompañamiento personal</a></li>
      <li><a href="/contacto/">Contacto</a></li>
      <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
    </ul></nav>
    <p class="fine">Marca de Novaryn OÜ, Estonia, registro 17556049. <a class="link" href="/aviso-legal/">Aviso legal</a>, <a class="link" href="/privacidad/">privacidad</a>, <a class="link" href="/cookies/">cookies</a>.</p>
  </div>
</footer>
<script src="/js/site.js"></script>
</body>
</html>
'''


def page(path, title, desc, cur, body, cls="", noindex=False):
    f = path.strip("/")
    f = os.path.join(f, "index.html") if f else "index.html"
    os.makedirs(os.path.dirname(f) or ".", exist_ok=True)
    open(f, "w", encoding="utf-8").write(head(title, desc, path, cls, noindex) + nav(cur) + body + FOOT)
    print("ok", f)


def redirect(path, to):
    f = os.path.join(path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(
        f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="robots" content="noindex">'
        f'<meta http-equiv="refresh" content="0;url={to}"><link rel="canonical" href="{DOM}{to}"><title>CRS Growth</title></head>'
        f'<body><a href="{to}">Continuar</a></body></html>')


def hidden():
    return (f'<input type="hidden" name="access_key" value="{KEY}">'
            f'<input type="hidden" name="from_name" value="Web CRS Growth">'
            f'<input type="checkbox" name="botcheck" class="trap" tabindex="-1" autocomplete="off" aria-hidden="true">')


def done(title, text, stamp="Recibido"):
    return f'<div class="done" tabindex="-1"><h2>{title}</h2><p>{text}</p><p class="stamp" aria-hidden="true">{stamp}</p></div>'


# ───────────── INICIO ─────────────
ROUTE = [
    ("Entrada de clientes", "Llegan por mil sitios y se pierden", "Un registro y un responsable"),
    ("Venta", "Cada presupuesto pasa por ti", "Proceso escrito, precios claros"),
    ("Entrega", "Producción se entera tarde", "Traspaso con ficha, sin sorpresas"),
    ("Facturación", "Facturas sin emitir a fin de mes", "Se factura al entregar"),
    ("Contabilidad y gestoría", "Papeles a última hora", "Al día, la llevamos nosotros"),
]
rows = "".join(f'<li><span class="n">0{i+1}</span><strong>{n}</strong><span class="v"><span class="hoy">{h}</span><span class="crs">{c}</span></span></li>'
               for i, (n, h, c) in enumerate(ROUTE))

FRENTES = [
    ("f1", "c1", "Operación", "Cómo fluye el trabajo dentro de tu empresa y dónde se para.",
     ["Flujos de trabajo y cuellos de botella", "Departamentos y responsables", "Comunicación entre áreas", "Procesos y manuales escritos"]),
    ("f2", "c2", "Comercial", "El recorrido del cliente, de la primera llamada al cobro.",
     ["Entrada y registro de clientes", "Proceso de venta y presupuestos", "Gestión y seguimiento", "Entrega del producto o servicio"]),
    ("f3", "c3", "Administración", "Los números al día, para decidir con datos.",
     ["Contabilidad", "Facturación", "Gestoría y asesoría", "Documentación"]),
]
inputs = "".join(f'<input type="radio" name="frente" id="{i}"{" checked" if k == 0 else ""}>' for k, (i, *_ ) in enumerate(FRENTES))
tabs = "".join(f'<label for="{i}">{t}</label>' for i, _, t, *_ in FRENTES)
cards = "".join(
    f'<div class="stock" id="{c}"><h3>{t}</h3><p>{d}</p><ul>' + "".join(f'<li><span>0{n+1}</span>{x}</li>' for n, x in enumerate(items)) + '</ul></div>'
    for i, c, t, d, items in FRENTES)

INICIO = f'''
<section class="hero desk">
  <div class="container">
    <div class="hero-text">
      <h1>Tu empresa funciona. Tú diriges.</h1>
      <p class="lead">Ordenamos y llevamos la operación diaria de tu empresa, contigo.</p>
      <div class="actions">
        <a class="btn btn--ink" href="{CAL}" target="_blank" rel="noopener">Reservar una llamada</a>
        <a class="btn btn--card" href="{WA}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
      </div>
    </div>
    <div class="hero-object">
      <div class="stock envelope" aria-hidden="true"><span class="addr">Tu empresa<br>Sevilla</span></div>
      <div class="stock route" data-play aria-label="Hoja de ruta de una empresa, hoy y con CRS">
        <div class="route-head">
          <div><p class="doc">Documento 01</p><h2>Hoja de ruta de tu empresa</h2></div>
          <fieldset class="groove"><legend>Ver la empresa</legend>
            <input type="radio" name="vista" id="v-hoy" class="hoy-input"><label for="v-hoy">Hoy</label>
            <input type="radio" name="vista" id="v-crs" class="go" checked><label for="v-crs">Con CRS</label>
          </fieldset>
        </div>
        <ol>{rows}</ol>
        <p class="holder"><span>Quién lo sostiene</span><b class="hoy">Tú, todo</b><b class="crs">El sistema. Tú decides.</b></p>
        <p class="stamp" aria-hidden="true">En orden</p>
      </div>
    </div>
  </div>
</section>

<section class="section plain">
  <div class="container grid">
    <p class="statement">Casi nunca falla el producto. Falla el recorrido.</p>
    <p class="wall">Entra un cliente, se vende, se entrega, se factura y se contabiliza. Cuando un tramo se atasca, acaba en tu mesa. Lo encontramos, lo ordenamos y lo llevamos.</p>
  </div>
</section>

<section class="section plain-2" id="que-llevamos">
  <div class="container index">
    <div class="index-intro"><h2>Qué llevamos</h2><p>Tres frentes. Empieza por uno.</p></div>
    <fieldset class="cards"><legend>Frentes de trabajo</legend>
      {inputs}
      <div class="tabs">{tabs}</div>
      <div class="deck"><div class="stock back" aria-hidden="true"></div>{cards}</div>
    </fieldset>
  </div>
</section>

<section class="section plain">
  <div class="container">
    <div class="head"><h2>Cómo trabajamos</h2><p>El último paso no termina: es el día a día.</p></div>
    <table class="ledger">
      <thead><tr><th scope="col"><span class="visually-hidden">Número</span></th><th scope="col">Paso</th><th scope="col">Qué hacemos</th><th scope="col">Qué te queda</th></tr></thead>
      <tbody>
        <tr><td>01</td><td>Llamada</td><td>Nos cuentas cómo funciona hoy.</td><td>Saber si encajamos</td></tr>
        <tr><td>02</td><td>Radiografía</td><td>Recorremos tu empresa y marcamos dónde se para.</td><td>Un mapa real de tu empresa</td></tr>
        <tr><td>03</td><td>Orden</td><td>Responsables, procesos y herramientas.</td><td>Una forma de trabajar escrita</td></tr>
        <tr><td>04</td><td>Implantación</td><td>Lo ponemos en marcha con tu equipo.</td><td>Tu equipo trabajando así</td></tr>
        <tr><td>05</td><td>Gestión</td><td>Nos quedamos llevando lo acordado.</td><td>Revisión periódica contigo</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="section board">
  <div class="container grid">
    <div class="board-text">
      <h2>Tu administración, al día.</h2>
      <p>Facturación, contabilidad, gestoría y documentación. La llevamos nosotros, cada mes.</p>
    </div>
    <div class="board-object">
      <div class="stock under" aria-hidden="true"></div>
      <div class="stock invoice">
        <p class="small">Factura del mes</p>
        <p class="who">Cliente de construcción</p>
        <ul>
          <li><span>Emitida</span><span class="fig">al entregar</span></li>
          <li><span>Contabilizada</span><span class="fig">mismo mes</span></li>
          <li><span>Gestoría</span><span class="fig">sin papeles pendientes</span></li>
        </ul>
        <p class="stamp" aria-hidden="true">Al día</p>
      </div>
    </div>
  </div>
</section>

<section class="section plain">
  <div class="container">
    <div class="head"><h2>Con quién trabajamos hoy</h2><p>Sin nombres, por confidencialidad. En la llamada te contamos cada caso.</p></div>
    <ul class="roster">
      <li><h3>Agencia de marketing</h3><p>Sus cuentas, sus redes, su web y el contenido.</p></li>
      <li><h3>Empresa de construcción</h3><p>Gestoría, asesoría, contabilidad, clientes y facturación.</p></li>
      <li><h3>Empresa de servicios</h3><p>Sus procesos internos, ordenados y gestionados.</p></li>
    </ul>
  </div>
</section>

<section class="section--s plain-2 band">
  <div class="container grid">
    <h2>¿Vas a crear tu empresa? Empezamos el primer día.</h2>
    <div class="band-side"><p>Constituimos tu sociedad de principio a fin. Tú solo firmas.</p>
      <div class="actions"><a class="btn btn--card" href="/constitucion/">Ver constitución</a></div></div>
  </div>
</section>

<section class="section desk">
  <div class="container grid">
    <div class="stock letter">
      <h2>Hablemos de tu empresa.</h2>
      <div class="body">
        <p>Una llamada de 30 minutos, sin coste. Si no encajamos, te lo decimos. El presupuesto llega después de conocer tu empresa, nunca antes.</p>
        <div class="actions"><a class="btn btn--ink" href="{CAL}" target="_blank" rel="noopener">Reservar una llamada</a></div>
      </div>
      <div class="sign">
        <p><b>Cristhiam Silva</b>Dirección estratégica y comercial</p>
        <p><b>Aaron García</b>Operaciones y entrega</p>
      </div>
    </div>
  </div>
</section>
'''
page("/", "CRS Growth, dirección y gestión de empresas",
     "Ordenamos y llevamos la operación de tu empresa: procesos, ventas, facturación, contabilidad y gestoría. Para que deje de depender de ti.",
     "inicio", INICIO)

# ───────────── CONSTITUCIÓN ─────────────
TRAMITES = ["Denominación social", "Estudio de la capitalización del paro", "Tramitación por CIRCE", "Notaría y escrituras",
            "Alta en Hacienda", "Alta en la Seguridad Social", "Registro Mercantil", "Acta de titularidad real",
            "Orientación para la cuenta bancaria", "Certificado digital de la empresa"]
tram = "".join(f"<li>{t}</li>" for t in TRAMITES)

CONST = f'''
<section class="hero desk">
  <div class="container">
    <div class="hero-text">
      <h1>Tu empresa, constituida sin ventanillas.</h1>
      <p class="lead">Hacemos cada trámite por ti. Tú solo firmas.</p>
      <div class="actions">
        <a class="btn btn--ink" href="#presupuesto">Pedir presupuesto</a>
        <a class="btn btn--card" href="{WA}?text=Hola%2C%20quiero%20constituir%20una%20empresa." target="_blank" rel="noopener">Escribir por WhatsApp</a>
      </div>
    </div>
    <div class="hero-object">
      <div class="stock envelope" aria-hidden="true"><span class="addr">Registro Mercantil<br>Sevilla</span></div>
      <div class="stock sheet-list">
        <p class="doc">Expediente, de 15 a 45 días</p>
        <h2>Constitución de tu sociedad</h2>
        <ol class="checklist">{tram}</ol>
        <p class="stamp" aria-hidden="true">Tú solo firmas</p>
      </div>
    </div>
  </div>
</section>

<section class="section plain">
  <div class="container">
    <div class="head"><h2>Cómo funciona</h2><p>Una sola persona de contacto, de la primera llamada a la firma.</p></div>
    <table class="ledger">
      <thead><tr><th scope="col"><span class="visually-hidden">Número</span></th><th scope="col">Paso</th><th scope="col">Qué pasa</th><th scope="col">Qué haces tú</th></tr></thead>
      <tbody>
        <tr><td>01</td><td>Nos cuentas</td><td>Tu proyecto, los socios y tu situación laboral.</td><td>Una conversación</td></tr>
        <tr><td>02</td><td>Te proponemos</td><td>La estructura que te conviene y un presupuesto cerrado.</td><td>Decidir</td></tr>
        <tr><td>03</td><td>Tramitamos</td><td>Cada organismo, con nuestro equipo y colaboradores.</td><td>Firmar cuando toca</td></tr>
        <tr><td>04</td><td>Empiezas</td><td>NIF, escrituras y certificado digital listos.</td><td>Facturar</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="section plain-2">
  <div class="container split">
    <div><h2>Para quién es</h2><p class="after">Y después, si quieres, seguimos llevando tu contabilidad, facturación y gestoría desde el primer mes.</p></div>
    <ul class="roster">
      <li><h3>Primera sociedad</h3><p>Vas a montar tu primera empresa.</p></li>
      <li><h3>Desde el paro</h3><p>Quieres valorar la capitalización.</p></li>
      <li><h3>De autónomo a sociedad</h3><p>Tu actividad ya pide estructura.</p></li>
      <li><h3>Varios socios</h3><p>Vais a emprender juntos.</p></li>
    </ul>
  </div>
</section>

<section class="section desk" id="presupuesto">
  <div class="container split">
    <div><h2>Pide tu presupuesto</h2><p class="after">Te respondemos en menos de 24 horas laborables con los pasos y el precio.</p></div>
    <div class="stock form">
      <form data-endpoint="{ENDPOINT}" data-subject="Constitución">
        {hidden()}
        <div class="field"><label for="c-n">Nombre</label><input id="c-n" name="nombre" autocomplete="name" required></div>
        <div class="field"><label for="c-e">Email</label><input id="c-e" name="email" type="email" autocomplete="email" required></div>
        <div class="field"><label for="c-t">Teléfono o WhatsApp</label><input id="c-t" name="telefono" type="tel" autocomplete="tel" required></div>
        <fieldset><legend>Tu situación</legend><div class="chips">
          <input type="radio" name="situacion" id="cs1" value="Primera empresa" required><label for="cs1">Primera empresa</label>
          <input type="radio" name="situacion" id="cs2" value="Capitalizar el paro"><label for="cs2">Capitalizar el paro</label>
          <input type="radio" name="situacion" id="cs3" value="De autónomo a sociedad"><label for="cs3">De autónomo a sociedad</label>
          <input type="radio" name="situacion" id="cs4" value="Otra"><label for="cs4">Otra</label>
        </div></fieldset>
        <div class="field"><label for="c-m">Tu proyecto <span class="hint">Opcional. A qué te vas a dedicar y cuántos socios seréis.</span></label><textarea id="c-m" name="mensaje"></textarea></div>
        <button class="btn btn--ink" type="submit">Enviar solicitud</button>
        <p class="status" role="status"></p>
        <p class="note">Usamos tus datos solo para responderte. <a class="link" href="/privacidad/">Privacidad</a>.</p>
      </form>
      {done("Solicitud enviada.", "Te escribimos en menos de 24 horas laborables.")}
    </div>
  </div>
</section>
'''
page("/constitucion/", "Constitución de empresas, CRS Growth",
     "Constituimos tu empresa de principio a fin: denominación, capitalización del paro, CIRCE, notaría, Hacienda, Seguridad Social, Registro Mercantil y certificado digital.",
     "constitucion", CONST)

# ───────────── CRISTHIAM SILVA ─────────────
PERSONAL = f'''
<section class="hero desk">
  <div class="container">
    <div class="hero-text">
      <h1>Sabes que algo tiene que cambiar.</h1>
      <p class="lead">Te acompaño a ordenar lo que tienes delante y decidir.</p>
      <div class="actions">
        <a class="btn btn--ink" href="/cristhiamsilva/confiaenti/">Hacer el cuestionario</a>
        <a class="btn btn--card" href="{WA}?text=Hola%20Cristhiam%2C%20quiero%20saber%20m%C3%A1s." target="_blank" rel="noopener">Escribirme por WhatsApp</a>
      </div>
    </div>
    <div class="hero-object">
      <figure class="stock print">
        <div class="frame"><img src="/cristhiamsilva/cristhiam-silva.jpg" alt="Cristhiam Silva, en la calle, con camiseta negra" width="900" height="1600" fetchpriority="high"></div>
      </figure>
      <div class="stock tag"><b>Cristhiam Silva</b><span>Acompañamiento personal, Sevilla</span></div>
    </div>
  </div>
</section>

<section class="section plain">
  <div class="container grid">
    <p class="statement">Más información no siempre trae más claridad.</p>
    <p class="wall">No te falta capacidad. Te falta alguien que mire contigo sin estar atrapado en el mismo ruido. No decido por ti: te ayudo a ver lo que ahora no ves y te acompaño mientras lo conviertes en movimiento.</p>
  </div>
</section>

<section class="section plain-2">
  <div class="container">
    <div class="head"><h2>Cómo trabajo</h2><p>Cada conversación tiene que quitar ruido, no darte más tareas.</p></div>
    <table class="ledger">
      <thead><tr><th scope="col"><span class="visually-hidden">Número</span></th><th scope="col">Momento</th><th scope="col">Qué pasa</th><th scope="col">Con qué sales</th></tr></thead>
      <tbody>
        <tr><td>01</td><td>Entender</td><td>Qué decisión no consigues cerrar.</td><td>El problema bien dicho</td></tr>
        <tr><td>02</td><td>Cuestionar</td><td>Lo que desde dentro no se ve.</td><td>Otra forma de mirarlo</td></tr>
        <tr><td>03</td><td>Mover</td><td>Lo que toca esta semana.</td><td>Acciones concretas</td></tr>
      </tbody>
    </table>
  </div>
</section>

<section class="section board price-board">
  <div class="container grid">
    <div class="board-text">
      <h2>Acompañamiento</h2>
      <p class="price">500 €<small>al mes</small></p>
      <p class="terms">Desde, según el caso. Mínimo tres meses.</p>
      <ul><li>Sesiones sobre decisiones reales</li><li>WhatsApp directo conmigo</li></ul>
    </div>
    <div class="board-object">
      <div class="stock card-first">
        <h3>Primera conversación</h3>
        <p class="zero">0 €</p>
        <ul class="checklist"><li>Cinco preguntas antes de vernos</li><li>Una reunión, en persona o por vídeo</li></ul>
        <div class="actions"><a class="btn btn--ink" href="/cristhiamsilva/confiaenti/">Hacer el cuestionario</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section plain">
  <div class="container split">
    <h2>Preguntas habituales</h2>
    <div class="faq">
      <details><summary>¿Tengo que saber qué necesito?</summary><p>No. El cuestionario hace ese trabajo. Respóndelo con honestidad.</p></details>
      <details><summary>¿Trabajas online?</summary><p>Sí, por videollamada. Y en persona cuando tiene sentido.</p></details>
      <details><summary>¿Por qué un mínimo de tres meses?</summary><p>Aclarar una decisión puede ser cosa de una conversación. Sostener otra forma de decidir exige verla funcionar y ajustarla.</p></details>
      <details><summary>¿Para quién no es?</summary><p>Para quien busca una fórmula rápida, prefiere que alguien decida por él o espera resultados garantizados.</p></details>
    </div>
  </div>
</section>
'''
page("/cristhiamsilva/", "Cristhiam Silva, acompañamiento personal",
     "Acompañamiento personal y para emprendedores con Cristhiam Silva. Primera conversación sin coste.",
     "personal", PERSONAL, "personal")

# ───────────── CUESTIONARIO ─────────────
def q(n, name, text):
    return f'<div class="field"><label for="{name}">{n}. {text}</label><textarea id="{name}" name="{name}" required></textarea></div>'

objetivos = ["Claridad para decidir", "Un cambio importante", "Empezar un proyecto", "Hacer crecer mi negocio",
             "Marca personal", "Más clientes y ventas", "Crecimiento personal"]
momentos = [("Ya tengo mi negocio", "Empresario"), ("Estoy empezando mi proyecto", "Emprendedor inicial"),
            ("Quiero emprender más adelante", "Futuro emprendedor"), ("No pienso emprender", "Crecimiento personal")]
obj = "".join(f'<input type="checkbox" name="objetivos" id="o{i}" value="{o}"><label for="o{i}">{o}</label>' for i, o in enumerate(objetivos))
mom = "".join(f'<input type="radio" name="momento" id="m{i}" value="{t}" data-tipo="{c}" required><label for="m{i}">{t}</label>' for i, (t, c) in enumerate(momentos))

CUEST = f'''
<section class="page-hero desk">
  <div class="container">
    <h1>Antes de nada, confía en ti.</h1>
    <p class="lead">Cinco preguntas, con calma. No busco respuestas perfectas.</p>
  </div>
</section>
<section class="section desk" style="padding-top: 0">
  <div class="container split">
    <div><p>Cuanto más real sea lo que escribas, mejor aprovecharemos la primera conversación. Lo leo yo, con calma, y te escribo para fijarla.</p><p class="after"><a class="link" href="/cristhiamsilva/">Volver</a></p></div>
    <div class="stock form">
      <form data-endpoint="{ENDPOINT}" data-subject="Confía en ti">
        {hidden()}
        <div class="field"><label for="q-n">Nombre</label><input id="q-n" name="nombre" autocomplete="name" required></div>
        <div class="field"><label for="q-t">Teléfono o WhatsApp</label><input id="q-t" name="telefono" type="tel" autocomplete="tel" required></div>
        <div class="field"><label for="q-e">Email</label><input id="q-e" name="email" type="email" autocomplete="email" required></div>
        <fieldset><legend>¿Qué te gustaría trabajar? <span class="hint">Marca las que encajen.</span></legend><div class="chips">{obj}</div></fieldset>
        <fieldset><legend>¿En qué punto estás?</legend><div class="chips">{mom}</div></fieldset>
        {q(1, "pregunta_01", "¿Dónde estás ahora y dónde quieres estar dentro de seis meses?")}
        {q(2, "pregunta_02", "¿Qué es lo que más te está frenando?")}
        {q(3, "pregunta_03", "¿En qué se te va el tiempo cada día?")}
        {q(4, "pregunta_04", "Tres cosas que cambiarías de ti y tres de las que estés orgulloso.")}
        {q(5, "pregunta_05", "Si nos sentamos mañana, ¿qué querrías resolver primero?")}
        <button class="btn btn--ink" type="submit">Enviar mis respuestas</button>
        <p class="status" role="status"></p>
        <p class="note">Uso estos datos solo para preparar nuestra conversación. <a class="link" href="/privacidad/">Privacidad</a>.</p>
      </form>
      {done("Gracias por confiar en mí.", "Ya tengo tus respuestas. Las leo con calma y te escribo para fijar nuestra conversación.", "Leído pronto")}
    </div>
  </div>
</section>
'''
page("/cristhiamsilva/confiaenti/", "Confía en ti, Cristhiam Silva",
     "Cuestionario previo a la primera conversación con Cristhiam Silva.", "personal", CUEST, "personal", noindex=True)

# ───────────── CONTACTO ─────────────
CONTACTO = f'''
<section class="page-hero desk">
  <div class="container">
    <h1>Hablemos de tu empresa.</h1>
    <p class="lead">Reserva una llamada o cuéntanos tu situación por escrito.</p>
    <div class="actions"><a class="btn btn--ink" href="{CAL}" target="_blank" rel="noopener">Reservar una llamada</a><a class="btn btn--card" href="{WA}" target="_blank" rel="noopener">Escribir por WhatsApp</a></div>
  </div>
</section>
<section class="section plain">
  <div class="container split">
    <div><h2>O escríbenos</h2>
      <ul class="checklist plain after"><li><a class="link" href="mailto:{MAIL}">{MAIL}</a></li><li><a class="link" href="tel:+34697293677">+34 697 293 677</a></li><li>Sevilla, y en remoto</li></ul></div>
    <div class="stock form">
      <form data-endpoint="{ENDPOINT}" data-subject="Contacto web">
        {hidden()}
        <div class="field"><label for="k-n">Nombre</label><input id="k-n" name="nombre" autocomplete="name" required></div>
        <div class="field"><label for="k-c">Empresa <span class="hint">Opcional</span></label><input id="k-c" name="empresa" autocomplete="organization"></div>
        <div class="field"><label for="k-e">Email</label><input id="k-e" name="email" type="email" autocomplete="email" required></div>
        <fieldset><legend>¿Sobre qué?</legend><div class="chips">
          <input type="radio" name="motivo" id="k1" value="Dirección y gestión" required><label for="k1">Dirección y gestión</label>
          <input type="radio" name="motivo" id="k2" value="Constitución"><label for="k2">Constitución</label>
          <input type="radio" name="motivo" id="k3" value="Acompañamiento personal"><label for="k3">Acompañamiento personal</label>
          <input type="radio" name="motivo" id="k4" value="Otro"><label for="k4">Otro</label>
        </div></fieldset>
        <div class="field"><label for="k-m">Tu situación</label><textarea id="k-m" name="mensaje" required></textarea></div>
        <button class="btn btn--ink" type="submit">Enviar mensaje</button>
        <p class="status" role="status"></p>
        <p class="note">Usamos tus datos solo para responderte. <a class="link" href="/privacidad/">Privacidad</a>.</p>
      </form>
      {done("Mensaje enviado.", "Te respondemos en menos de 24 horas laborables.")}
    </div>
  </div>
</section>
'''
page("/contacto/", "Contacto, CRS Growth", "Reserva una llamada o escríbenos. Respondemos en menos de 24 horas laborables.", "contacto", CONTACTO)

exec(open("_legal.py", encoding="utf-8").read())
print("listo")

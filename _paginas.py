# Contenido de las páginas. Lo ejecuta _build.py.

# ───────────────────────── INICIO ─────────────────────────
DIAGRAMA = '''
<div class="flujo" aria-label="Diagrama: antes, todo el trabajo de la empresa pasa por el dueño; después, los departamentos se conectan entre sí y el dueño dirige desde arriba.">
  <svg viewBox="0 0 560 460" role="img" aria-hidden="true">
    <g class="radios">
      <path d="M209 132 L232 210"/><path d="M209 268 L232 232"/>
      <path d="M280 377 L280 243"/><path d="M351 268 L328 232"/><path d="M351 132 L328 210"/>
    </g>
    <g class="cadena">
      <path d="M115 143 L115 257"/>
      <path d="M115 303 Q115 400 186 400"/>
      <path d="M374 400 Q445 400 445 303"/>
      <path d="M445 257 L445 143"/>
    </g>
    <g class="supervision">
      <path d="M232 70 L150 97"/><path d="M328 70 L410 97"/><path d="M280 81 L280 377"/>
    </g>
    <g class="pulsos">
      <circle r="5"><animateMotion dur="5s" repeatCount="indefinite" path="M115 143 L115 303 Q115 400 186 400 L374 400 Q445 400 445 303 L445 143"/></circle>
      <circle r="5"><animateMotion dur="5s" begin="1.66s" repeatCount="indefinite" path="M115 143 L115 303 Q115 400 186 400 L374 400 Q445 400 445 303 L445 143"/></circle>
      <circle r="5"><animateMotion dur="5s" begin="3.33s" repeatCount="indefinite" path="M115 143 L115 303 Q115 400 186 400 L374 400 Q445 400 445 303 L445 143"/></circle>
    </g>
    <g class="nodo"><rect x="21" y="97" width="188" height="46" rx="23"/><text x="115" y="126">Entrada de clientes</text></g>
    <g class="nodo"><rect x="21" y="257" width="188" height="46" rx="23"/><text x="115" y="285">Ventas</text></g>
    <g class="nodo"><rect x="186" y="377" width="188" height="46" rx="23"/><text x="280" y="405">Producción y entrega</text></g>
    <g class="nodo"><rect x="351" y="257" width="188" height="46" rx="23"/><text x="445" y="285">Facturación</text></g>
    <g class="nodo"><rect x="351" y="97" width="188" height="46" rx="23"/><text x="445" y="126">Contabilidad y gestoría</text></g>
    <g class="nodo nodo-tu"><rect x="232" y="197" width="96" height="46" rx="23"/><text x="280" y="226">Tú</text></g>
    <g class="cola"><rect x="312" y="184" width="40" height="22" rx="11"/><text x="332" y="199">+14</text></g>
  </svg>
  <div class="flujo-pie"><span data-estado aria-live="polite"></span><button type="button" data-alternar>Ver el antes</button></div>
</div>'''

INICIO = f'''
<section class="hero oscuro">
  <div class="wrap hero-grid">
    <div>
      <h1>Tu empresa funciona.<br>Tú diriges.</h1>
      <p class="lead">Dirigimos y gestionamos la operación de tu empresa: procesos, departamentos, ventas, administración y documentación. Encontramos dónde se atasca y lo llevamos nosotros, para que deje de pasar todo por ti.</p>
      <div class="botones">
        <a class="btn btn-oro" href="{CAL}" target="_blank" rel="noopener">Reservar una llamada</a>
        <a class="btn btn-linea" href="{WA}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
      </div>
      <p style="margin-top:18px;font-size:15px;color:var(--plata-2)">Primera llamada de 30 minutos, sin coste.</p>
    </div>
    {DIAGRAMA}
  </div>
</section>

<section class="seccion papel">
  <div class="wrap">
    <div class="cabecera">
      <h2>Casi nunca falla el producto. Falla el recorrido.</h2>
      <p class="lead">Una empresa es un flujo: entra un cliente, se vende, se produce o se presta el servicio, se factura y se contabiliza. Cuando algo se atasca en ese recorrido, acaba aterrizando en la mesa del dueño.</p>
    </div>
    <ul class="atascos">
      <li><strong>Todo pasa por ti</strong><span>Presupuestos, decisiones, incidencias. Si un día no estás, la empresa se para.</span></li>
      <li><strong>Departamentos que no se hablan</strong><span>Ventas promete lo que producción no sabe. Nadie tiene la foto completa.</span></li>
      <li><strong>Clientes que entran y se pierden</strong><span>Llegan contactos, pero no hay un camino claro desde la primera llamada hasta el cobro.</span></li>
      <li><strong>Procesos que viven en la cabeza de alguien</strong><span>Cada persona trabaja a su manera y nada está escrito.</span></li>
      <li><strong>Administración que va por detrás</strong><span>Facturas sin emitir, contabilidad atrasada y la gestoría pidiendo papeles a última hora.</span></li>
      <li><strong>Documentación por todas partes</strong><span>Contratos, albaranes y archivos repartidos entre correos, móviles y carpetas.</span></li>
    </ul>
  </div>
</section>

<section class="seccion" id="que-hacemos">
  <div class="wrap">
    <div class="cabecera">
      <h2>Qué llevamos nosotros</h2>
      <p class="lead">No entregamos un informe y desaparecemos. Entramos en la operación, la ordenamos y nos quedamos llevándola contigo. Trabajamos en tres frentes.</p>
    </div>
    <div class="areas">
      <div class="area">
        <h3>Operación</h3>
        <div>
          <p>Mapeamos el flujo de trabajo real, localizamos los cuellos de botella entre procesos y departamentos, y definimos quién hace qué, cuándo y cómo se comunica con el resto.</p>
          <ul><li>Flujos de trabajo</li><li>Cuellos de botella</li><li>Departamentos y responsables</li><li>Comunicación interna</li><li>Protocolos y manuales</li></ul>
        </div>
      </div>
      <div class="area">
        <h3>Comercial</h3>
        <div>
          <p>Ordenamos el recorrido completo del cliente: cómo entra, cómo se le vende, cómo se le entrega el producto o servicio y cómo se le hace seguimiento después.</p>
          <ul><li>Entrada de clientes</li><li>Proceso de venta</li><li>Gestión de clientes</li><li>Entrega y seguimiento</li></ul>
        </div>
      </div>
      <div class="area">
        <h3>Administración</h3>
        <div>
          <p>Llevamos o coordinamos la contabilidad, la facturación, la gestoría, la asesoría y la documentación, para que dirijas con datos reales y sin sustos.</p>
          <ul><li>Contabilidad</li><li>Facturación</li><li>Gestoría y asesoría</li><li>Documentación</li></ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="seccion oscuro" id="como-trabajamos">
  <div class="wrap">
    <div class="cabecera">
      <h2>Cómo trabajamos</h2>
      <p class="lead">Cuatro pasos. El último no termina: es la gestión del día a día.</p>
    </div>
    <ol class="pasos">
      <li><h3>Entender</h3><p>Una primera conversación y una radiografía de cómo funciona hoy tu empresa: qué entra, qué sale y dónde se para.</p></li>
      <li><h3>Ordenar</h3><p>Diseñamos el flujo correcto: responsables, procesos, herramientas y cómo se comunican los departamentos.</p></li>
      <li><h3>Implantar</h3><p>Lo ponemos en marcha con tu equipo. No dejamos un documento, dejamos una forma de trabajar funcionando.</p></li>
      <li><h3>Llevar</h3><p>Nos quedamos gestionando lo acordado, con seguimiento periódico contigo para decidir con datos.</p></li>
    </ol>
  </div>
</section>

<section class="seccion papel">
  <div class="wrap">
    <div class="cabecera">
      <h2>Con quién trabajamos hoy</h2>
      <p class="lead">Sin cifras de escaparate. Esto es lo que llevamos ahora mismo a nuestros clientes.</p>
    </div>
    <ul class="clientes">
      <li class="cliente"><h3>Agencia de marketing</h3><p>Llevamos el control de sus cuentas, sus redes, su web y la creación de contenido.</p></li>
      <li class="cliente"><h3>Empresa de construcción</h3><p>Llevamos su gestoría, asesoría y contabilidad, la gestión de clientes y la facturación.</p></li>
      <li class="cliente"><h3>Empresa de servicios</h3><p>Ordenamos y gestionamos sus procesos internos.</p></li>
    </ul>
    <p class="nota">Por confidencialidad no publicamos nombres. En la llamada te contamos cada caso.</p>
  </div>
</section>

<section class="seccion" style="padding-bottom:0">
  <div class="wrap">
    <div class="banda">
      <div>
        <h2 style="font-size:clamp(1.8rem,3.4vw,2.6rem)">¿Vas a crear tu empresa? Empezamos desde el primer día.</h2>
        <p>Nos encargamos de la constitución completa: denominación, notaría, Hacienda, Seguridad Social, Registro Mercantil y certificado digital. Tú solo firmas.</p>
      </div>
      <div class="botones"><a class="btn btn-oro" href="/constitucion/">Ver constitución de empresas</a></div>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="wrap">
    <div class="cabecera"><h2>Quién está detrás</h2><p class="lead">Dos socios, un mismo criterio: lo que se promete, se entrega.</p></div>
    <div class="equipo">
      <div class="persona">
        <h3>Cristhiam Silva</h3>
        <p class="rol">Dirección estratégica y comercial</p>
        <p>Lleva la relación con cada cliente, el diagnóstico y las decisiones de estructura y venta.</p>
        <p><a href="/cristhiamsilva/">También acompaña a personas y emprendedores</a></p>
      </div>
      <div class="persona">
        <h3>Aaron García</h3>
        <p class="rol">Operaciones y entrega</p>
        <p>Responsable de que lo acordado se ejecute: coordina la implantación y la gestión diaria de cada cliente.</p>
      </div>
    </div>
  </div>
</section>

<section class="seccion oscuro cierre">
  <div class="wrap">
    <h2>Hablemos de tu empresa.</h2>
    <p class="lead">30 minutos para entender cómo funciona hoy y ver si podemos ayudarte. Si no encajamos, te lo decimos. El presupuesto se define siempre después de conocer tu empresa.</p>
    <div class="botones">
      <a class="btn btn-oro" href="{CAL}" target="_blank" rel="noopener">Reservar una llamada</a>
      <a class="btn btn-linea" href="/contacto/">Escribirnos</a>
    </div>
  </div>
</section>
'''
page("/", "CRS Growth — Dirección y gestión de empresas",
     "Dirigimos y gestionamos la operación de tu empresa: procesos, departamentos, ventas, contabilidad, gestoría y documentación. Para que deje de pasar todo por ti.",
     "", INICIO)

# ───────────────────────── CONSTITUCIÓN ─────────────────────────
CONST = f'''
<section class="pagina-hero oscuro">
  <div class="wrap">
    <h1>Constituye tu empresa sin pisar una ventanilla.</h1>
    <p class="lead">Gestionamos todos los trámites de principio a fin, con nuestro equipo y colaboradores de confianza. Tú decides y firmas. Del resto nos encargamos nosotros.</p>
    <div class="botones">
      <a class="btn btn-oro" href="#formulario">Pedir presupuesto</a>
      <a class="btn btn-linea" href="{WA}?text=Hola%2C%20quiero%20informaci%C3%B3n%20para%20constituir%20una%20empresa." target="_blank" rel="noopener">Escribir por WhatsApp</a>
    </div>
    <div class="datos">
      <div><strong>15 a 45 días</strong>plazo habitual, según notaría y registro</div>
      <div><strong>Un interlocutor</strong>de principio a fin</div>
      <div><strong>Presupuesto previo</strong>sabes lo que cuesta antes de empezar</div>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="wrap dos-col">
    <div>
      <h2>Qué gestionamos</h2>
      <p class="lead" style="margin-top:20px">Cada trámite, en orden y sin que tengas que perseguir a nadie.</p>
    </div>
    <ul class="checks">
      <li>Búsqueda y reserva de la denominación social</li>
      <li>Estudio de la capitalización del paro</li>
      <li>Tramitación telemática por CIRCE</li>
      <li>Coordinación con notaría y firma de escrituras</li>
      <li>Alta en Hacienda: NIF y declaraciones censales</li>
      <li>Alta en la Seguridad Social</li>
      <li>Inscripción en el Registro Mercantil</li>
      <li>Acta de titularidad real</li>
      <li>Orientación para la cuenta bancaria</li>
      <li>Certificado digital de la empresa</li>
    </ul>
  </div>
</section>

<section class="seccion oscuro">
  <div class="wrap">
    <div class="cabecera"><h2>Cómo funciona</h2><p class="lead">Cuatro pasos y una sola persona de contacto.</p></div>
    <ol class="pasos">
      <li><h3>Nos cuentas</h3><p>Tu proyecto, los socios, tu situación laboral y lo que quieres montar.</p></li>
      <li><h3>Te proponemos</h3><p>La estructura que te conviene y un presupuesto cerrado antes de empezar.</p></li>
      <li><h3>Tramitamos</h3><p>Nos encargamos de cada organismo y te avisamos solo cuando tienes que firmar.</p></li>
      <li><h3>Empiezas</h3><p>Recibes tu empresa operativa, con NIF, escrituras y certificado digital.</p></li>
    </ol>
  </div>
</section>

<section class="seccion papel">
  <div class="wrap dos-col">
    <div>
      <h2>Para quién es</h2>
      <ul class="checks" style="margin-top:28px">
        <li>Vas a montar tu primera sociedad</li>
        <li>Estás en paro y quieres valorar la capitalización</li>
        <li>Eres autónomo y quieres pasar a sociedad</li>
        <li>Vais a emprender varios socios</li>
      </ul>
    </div>
    <div>
      <h2>Y después</h2>
      <p class="lead" style="margin-top:28px">Una empresa bien constituida es solo el principio. Si quieres, seguimos llevando tu contabilidad, facturación, gestoría y documentación desde el primer mes.</p>
      <p><a href="/#que-hacemos" style="font-weight:600">Ver qué llevamos en el día a día</a></p>
    </div>
  </div>
</section>

<section class="seccion" id="formulario">
  <div class="wrap dos-col">
    <div>
      <h2>Pide tu presupuesto</h2>
      <p class="lead" style="margin-top:20px">Cuéntanos tu situación y te respondemos en menos de 24 horas laborables con los pasos y el presupuesto.</p>
    </div>
    <div class="formulario">
      <form data-web3 data-asunto="Constitución de empresa">
        {hidden("")}
        <div class="campo"><label for="c-nombre">Nombre</label><input id="c-nombre" name="nombre" autocomplete="name" required></div>
        <div class="campo"><label for="c-email">Email</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
        <div class="campo"><label for="c-tel">Teléfono o WhatsApp</label><input id="c-tel" name="telefono" type="tel" autocomplete="tel" required></div>
        <div class="campo"><label for="c-sit">Tu situación</label>
          <select id="c-sit" name="situacion" required>
            <option value="">Elige una opción</option>
            <option>Tengo una idea y quiero montar mi primera empresa</option>
            <option>Estoy en paro y quiero capitalizarlo</option>
            <option>Soy autónomo y quiero pasar a sociedad</option>
            <option>Otra situación</option>
          </select></div>
        <div class="campo"><label for="c-socios">¿Cuántos socios seréis?</label>
          <select id="c-socios" name="socios"><option>Solo yo</option><option>Dos</option><option>Tres o más</option></select></div>
        <div class="campo"><label for="c-msg">Cuéntanos tu proyecto <span class="ayuda">Opcional. A qué te vas a dedicar y cuándo quieres empezar.</span></label><textarea id="c-msg" name="mensaje"></textarea></div>
        <button class="btn btn-tinta" type="submit" style="width:100%">Enviar solicitud</button>
        <p class="estado" role="status"></p>
        <p class="legal-form">Usamos tus datos solo para responder a tu solicitud. Más información en la <a href="/privacidad/">política de privacidad</a>.</p>
      </form>
      <div class="gracias"><h3>Solicitud enviada.</h3><p>Te escribimos en menos de 24 horas laborables. Si es urgente, escríbenos por <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a>.</p></div>
    </div>
  </div>
</section>
'''
page("/constitucion/", "Constitución de empresas — CRS Growth",
     "Constituimos tu empresa de principio a fin: denominación, capitalización del paro, CIRCE, notaría, Hacienda, Seguridad Social, Registro Mercantil y certificado digital.",
     "constitucion", CONST)

# ───────────────────────── CRISTHIAM SILVA ─────────────────────────
PERSONAL = f'''
<section class="hero personal-hero">
  <div class="wrap hero-grid">
    <div>
      <h1>Sabes que algo tiene que cambiar.</h1>
      <p class="lead">Pero llevas demasiado tiempo dentro del problema. Te acompaño a ordenar lo que tienes delante y a tomar decisiones que puedas sostener, en tu vida y en tu negocio.</p>
      <div class="botones">
        <a class="btn btn-acento" href="/cristhiamsilva/confiaenti/">Empezar por el cuestionario</a>
        <a class="btn btn-linea" href="{WA}?text=Hola%20Cristhiam%2C%20quiero%20saber%20m%C3%A1s%20sobre%20tu%20acompa%C3%B1amiento." target="_blank" rel="noopener">Escribirme por WhatsApp</a>
      </div>
      <p style="margin-top:18px;font-size:15px;color:var(--gris)">La primera conversación no tiene coste.</p>
    </div>
    <figure class="foto" style="margin:0">
      <img src="/cristhiamsilva/cristhiam-silva.jpg" alt="Cristhiam Silva" width="900" height="1600">
      <figcaption>Cristhiam Silva</figcaption>
    </figure>
  </div>
</section>

<section class="seccion">
  <div class="wrap dos-col">
    <p class="frase">Más información no siempre trae más claridad.</p>
    <div>
      <p>Cuando llevas tiempo resolviéndolo todo por tu cuenta, acumulas ideas, consejos y opiniones. Llega un punto en el que todo eso compite dentro de tu cabeza: revisas una decisión diez veces, cambias de dirección demasiado pronto o pospones lo que sabes que tienes que afrontar.</p>
      <p>No te falta capacidad. Te falta alguien que mire contigo sin estar atrapado en el mismo ruido. Mi trabajo no es decidir por ti: es ayudarte a ver lo que ahora no ves y acompañarte mientras lo conviertes en movimiento, hasta que vuelvas a confiar en tu criterio.</p>
    </div>
  </div>
</section>

<section class="seccion oscuro">
  <div class="wrap">
    <div class="cabecera"><h2>Cómo trabajo</h2><p class="lead">Cada conversación tiene que reducir ruido, no darte más tareas.</p></div>
    <ol class="pasos" style="grid-template-columns:repeat(3,1fr)">
      <li><h3>Entender</h3><p>Me cuentas qué ocurre, qué has intentado y qué decisión no consigues cerrar.</p></li>
      <li><h3>Cuestionar</h3><p>Pregunto, confronto supuestos y conecto puntos que desde dentro pasan desapercibidos.</p></li>
      <li><h3>Mover</h3><p>Sales con lo que hay que hacer esta semana. Si seguimos, revisamos lo que pasa en la realidad y ajustamos.</p></li>
    </ol>
  </div>
</section>

<section class="seccion">
  <div class="wrap">
    <div class="cabecera"><h2>Qué trabajamos</h2><p class="lead">Empezamos por ti. Todo lo demás sale de ahí. No separo la persona del negocio, porque casi nunca se puede.</p></div>
    <div class="temas">
      <div><h3>Tu criterio</h3><p>Lo que de verdad frena tus decisiones: el miedo, el cansancio y la historia que te cuentas sobre lo que puedes hacer.</p></div>
      <div><h3>Marca personal y redes</h3><p>Miro tu marca como alguien que acaba de descubrirte: qué transmites y qué no está llegando como crees.</p></div>
      <div><h3>Captación y ventas</h3><p>Con quién quieres trabajar, cómo llegar a esa persona y cómo vender sin sentir que interpretas un guion.</p></div>
      <div><h3>Eventos y presentaciones</h3><p>Mensaje, experiencia, tiempos y las decisiones que suelen aparecer a última hora.</p></div>
    </div>
  </div>
</section>

<section class="seccion papel">
  <div class="wrap">
    <div class="cabecera"><h2>Cómo empezamos</h2><p class="lead">Primero nos conocemos. Después decides si seguimos.</p></div>
    <div class="oferta">
      <div>
        <h3>Primera conversación</h3>
        <p class="precio">0 €</p>
        <p class="sub">Sin compromiso de continuar.</p>
        <ul class="checks">
          <li>Un cuestionario de 5 preguntas, con tus palabras</li>
          <li>Una reunión presencial o por videollamada</li>
          <li>Sales con más orden, sigamos o no</li>
        </ul>
        <div class="botones"><a class="btn btn-acento" href="/cristhiamsilva/confiaenti/">Hacer el cuestionario</a></div>
      </div>
      <div class="destacada">
        <h3>Acompañamiento</h3>
        <p class="precio">Desde 500 € <small>al mes</small></p>
        <p class="sub">Según el caso. Compromiso mínimo de 3 meses.</p>
        <ul class="checks">
          <li>Sesiones de trabajo sobre decisiones reales</li>
          <li>WhatsApp directo conmigo</li>
          <li>Revisión de decisiones, marca y contenido</li>
          <li>Ajuste continuo según lo que ocurre</li>
        </ul>
        <p class="sub" style="margin-top:18px">La web propia, la ejecución de ventas y la logística de eventos se presupuestan aparte.</p>
      </div>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="wrap dos-col">
    <div><h2 style="font-size:clamp(1.6rem,2.8vw,2.2rem);margin-bottom:24px">Encajamos si…</h2>
      <ul class="checks"><li>quieres tomar decisiones, no acumular más teoría</li><li>estás dispuesto a hablar con honestidad</li><li>valoras que alguien cuestione tus ideas</li><li>quieres implicarte en el proceso</li></ul></div>
    <div><h2 style="font-size:clamp(1.6rem,2.8vw,2.2rem);margin-bottom:24px">No es para ti si…</h2>
      <ul class="checks no"><li>buscas una fórmula rápida sin contexto</li><li>prefieres que alguien decida por ti</li><li>solo necesitas una ejecución puntual</li><li>esperas resultados garantizados</li></ul></div>
  </div>
</section>

<section class="seccion papel">
  <div class="wrap dos-col">
    <h2>Preguntas habituales</h2>
    <div class="faq">
      <details><summary>¿La primera conversación tiene coste?</summary><p>No. Primero quiero entender tu situación y comprobar contigo si mi forma de trabajar puede aportarte algo.</p></details>
      <details><summary>¿Tengo que saber qué necesito?</summary><p>No. El cuestionario hace ese trabajo. Solo respóndelo con honestidad.</p></details>
      <details><summary>¿Trabajas online?</summary><p>Sí, por videollamada. Y cuando tiene sentido, también en persona.</p></details>
      <details><summary>¿Por qué un mínimo de 3 meses?</summary><p>Aclarar una decisión puede ocurrir en una conversación. Sostener una forma distinta de decidir exige verla funcionar en la realidad y ajustarla.</p></details>
    </div>
  </div>
</section>

<section class="seccion oscuro cierre">
  <div class="wrap">
    <h2>Recupera tu criterio. Esta vez, acompañado.</h2>
    <p class="lead">Cinco preguntas, con calma. Después hablamos con contexto real.</p>
    <div class="botones"><a class="btn btn-acento" href="/cristhiamsilva/confiaenti/">Empezar el cuestionario</a></div>
  </div>
</section>
'''
page("/cristhiamsilva/", "Cristhiam Silva — Acompañamiento personal",
     "Acompañamiento personal y para emprendedores con Cristhiam Silva: claridad para decidir en tu vida y en tu negocio. Primera conversación sin coste.",
     "personal", PERSONAL, "personal")

# ───────────────────────── CUESTIONARIO ─────────────────────────
def pregunta(n, nombre, texto, ayuda=""):
    a = f'<span class="ayuda">{ayuda}</span>' if ayuda else ''
    return f'<div class="campo"><label for="{nombre}">{n}. {texto}{a}</label><textarea id="{nombre}" name="{nombre}" required></textarea></div>'

objetivos = ["Crecimiento personal", "Claridad y toma de decisiones", "Cambio importante en mi vida",
             "Empezar un proyecto o negocio", "Hacer crecer mi negocio", "Marca personal o visibilidad",
             "Conseguir más clientes", "Mejorar mis ventas"]
momentos = [("Ya tengo mi propio negocio", "Empresario"),
            ("Estoy empezando o preparando mi proyecto", "Emprendedor inicial"),
            ("Me gustaría emprender en el futuro", "Futuro emprendedor"),
            ("De momento no pienso emprender", "Crecimiento personal")]
obj_html = "".join(f'<label><input type="checkbox" name="objetivos" value="{o}">{o}</label>' for o in objetivos)
mom_html = "".join(f'<label><input type="radio" name="momento" value="{t}" data-clasificacion="{c}" required>{t}</label>' for t, c in momentos)

CUEST = f'''
<section class="pagina-hero personal-hero">
  <div class="wrap">
    <p style="margin-bottom:28px"><a href="/cristhiamsilva/">Volver</a></p>
    <h1>Antes de nada, confía en ti.</h1>
    <p class="lead">No busco respuestas perfectas. Busco entender cómo piensas y qué quieres construir. Cuanto más real sea lo que escribas, mejor aprovecharemos nuestra primera conversación.</p>
  </div>
</section>
<section class="seccion" style="padding-top:48px">
  <div class="wrap" style="max-width:820px">
    <div class="formulario">
      <form data-web3 data-asunto="Confía en ti">
        {hidden("")}
        <div class="campo"><label for="q-nombre">Nombre</label><input id="q-nombre" name="nombre" autocomplete="name" required></div>
        <div class="campo"><label for="q-tel">Teléfono o WhatsApp</label><input id="q-tel" name="telefono" type="tel" autocomplete="tel" required></div>
        <div class="campo"><label for="q-email">Email</label><input id="q-email" name="email" type="email" autocomplete="email" required></div>
        <fieldset class="campo"><legend>¿Qué te gustaría trabajar? <span class="ayuda">Marca todas las que encajen.</span></legend><div class="opciones">{obj_html}</div></fieldset>
        <fieldset class="campo"><legend>¿En qué punto estás?</legend><div class="opciones">{mom_html}</div></fieldset>
        <hr style="border:0;border-top:1px solid var(--linea);margin:28px 0">
        {pregunta(1, "pregunta_01", "Describe dónde estás ahora y dónde te gustaría estar dentro de 6 meses.")}
        {pregunta(2, "pregunta_02", "¿Qué es lo que más te está frenando para avanzar?")}
        {pregunta(3, "pregunta_03", "¿En qué inviertes tu tiempo cada día, desde hace unos meses?")}
        {pregunta(4, "pregunta_04", "Dime 3 cosas que cambiarías de ti y 3 de las que te sientas orgulloso.")}
        {pregunta(5, "pregunta_05", "Si pudiéramos sentarnos mañana, ¿qué sería lo primero que querrías resolver conmigo?")}
        <button class="btn btn-acento" type="submit" style="width:100%">Enviar mis respuestas</button>
        <p class="estado" role="status"></p>
        <p class="legal-form">Uso estos datos solo para preparar nuestra conversación y contactarte. Más información en la <a href="/privacidad/">política de privacidad</a>.</p>
      </form>
      <div class="gracias">
        <h3>Gracias por confiar en mí.</h3>
        <p>Ya tengo tus respuestas. Voy a leerlas con calma y te escribo para fijar nuestra conversación.</p>
        <div class="botones"><a class="btn btn-acento" href="{WA}" target="_blank" rel="noopener">Escribirme por WhatsApp</a></div>
      </div>
    </div>
  </div>
</section>
'''
page("/cristhiamsilva/confiaenti/", "Confía en ti — Cristhiam Silva",
     "Cuestionario previo a la primera conversación con Cristhiam Silva.", "personal", CUEST, "personal", noindex=True)

# ───────────────────────── CONTACTO ─────────────────────────
CONTACTO = f'''
<section class="pagina-hero oscuro">
  <div class="wrap">
    <h1>Hablemos de tu empresa.</h1>
    <p class="lead">Reserva una llamada de 30 minutos o cuéntanos tu situación. Respondemos en menos de 24 horas laborables.</p>
  </div>
</section>
<section class="seccion">
  <div class="wrap dos-col">
    <div>
      <h2 style="font-size:clamp(1.6rem,2.8vw,2.2rem)">La forma más rápida</h2>
      <div class="botones" style="flex-direction:column;align-items:flex-start">
        <a class="btn btn-oro" href="{CAL}" target="_blank" rel="noopener">Reservar una llamada</a>
        <a class="btn btn-linea" href="{WA}?text=Hola%2C%20me%20interesa%20hablar%20con%20CRS%20Growth." target="_blank" rel="noopener">Escribir por WhatsApp</a>
      </div>
      <ul class="checks" style="margin-top:40px">
        <li><a href="mailto:{MAIL}">{MAIL}</a></li>
        <li><a href="tel:+34697293677">+34 697 293 677</a></li>
        <li>Sevilla, España. Trabajamos también en remoto.</li>
      </ul>
    </div>
    <div class="formulario">
      <form data-web3 data-asunto="Contacto web">
        {hidden("")}
        <div class="campo"><label for="k-nombre">Nombre</label><input id="k-nombre" name="nombre" autocomplete="name" required></div>
        <div class="campo"><label for="k-empresa">Empresa <span class="ayuda">Opcional</span></label><input id="k-empresa" name="empresa" autocomplete="organization"></div>
        <div class="campo"><label for="k-email">Email</label><input id="k-email" name="email" type="email" autocomplete="email" required></div>
        <div class="campo"><label for="k-tel">Teléfono <span class="ayuda">Opcional</span></label><input id="k-tel" name="telefono" type="tel" autocomplete="tel"></div>
        <div class="campo"><label for="k-motivo">¿Sobre qué quieres hablar?</label>
          <select id="k-motivo" name="motivo" required>
            <option value="">Elige una opción</option>
            <option>Dirección y gestión de mi empresa</option>
            <option>Constituir una empresa</option>
            <option>Acompañamiento personal con Cristhiam</option>
            <option>Otro tema</option>
          </select></div>
        <div class="campo"><label for="k-msg">Cuéntanos tu situación</label><textarea id="k-msg" name="mensaje" required></textarea></div>
        <button class="btn btn-tinta" type="submit" style="width:100%">Enviar mensaje</button>
        <p class="estado" role="status"></p>
        <p class="legal-form">Usamos tus datos solo para responderte. Más información en la <a href="/privacidad/">política de privacidad</a>.</p>
      </form>
      <div class="gracias"><h3>Mensaje enviado.</h3><p>Te respondemos en menos de 24 horas laborables.</p></div>
    </div>
  </div>
</section>
'''
page("/contacto/", "Contacto — CRS Growth", "Reserva una llamada o escríbenos. Respondemos en menos de 24 horas laborables.", "contacto", CONTACTO)

# ───────────────────────── LEGALES ─────────────────────────
TITULAR = f'''<table>
<tr><td>Titular</td><td>Novaryn OÜ</td></tr>
<tr><td>Marca comercial</td><td>CRS Growth</td></tr>
<tr><td>Código de registro</td><td>17556049, Registro Mercantil de Estonia (Tartu Maakohus, departamento de registro)</td></tr>
<tr><td>Domicilio social</td><td>Ahtri tn 12, Kesklinna linnaosa, 15551 Tallinn, Harju maakond, Estonia</td></tr>
<tr><td>Email de contacto</td><td><a href="mailto:{MAIL}">{MAIL}</a></td></tr>
<tr><td>Teléfono</td><td>+34 697 293 677</td></tr>
</table>'''

def legal(path, titulo, cuerpo, desc):
    page(path, f"{titulo} — CRS Growth", desc, "",
         f'<section class="pagina-hero papel"><div class="wrap"><h1 style="font-size:clamp(2.2rem,5vw,3.6rem)">{titulo}</h1><p class="lead">Última actualización: noviembre de 2026.</p></div></section>'
         f'<section class="seccion" style="padding-top:56px"><div class="wrap texto-legal">{cuerpo}</div></section>')

legal("/aviso-legal/", "Aviso legal", f'''
<h2>Datos del titular</h2>
<p>En cumplimiento de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), se informa de los datos del titular de este sitio web:</p>
{TITULAR}
<h2>Objeto</h2>
<p>Este sitio web informa sobre los servicios de dirección y gestión de empresas, constitución de sociedades y acompañamiento personal que se prestan bajo la marca CRS Growth y bajo el nombre profesional de Cristhiam Silva.</p>
<h2>Condiciones de uso</h2>
<p>El acceso a este sitio es gratuito y supone la aceptación de este aviso legal. El usuario se compromete a hacer un uso adecuado de los contenidos y a no emplearlos para actividades ilícitas o contrarias a la buena fe.</p>
<h2>Propiedad intelectual e industrial</h2>
<p>Los textos, diseños, logotipos y demás contenidos de este sitio son titularidad de Novaryn OÜ o se utilizan con autorización. Queda prohibida su reproducción, distribución o transformación sin autorización expresa.</p>
<h2>Responsabilidad</h2>
<p>La información de este sitio tiene carácter general y no constituye asesoramiento profesional para un caso concreto. El titular no se hace responsable del uso que se haga de ella ni del contenido de los sitios de terceros enlazados.</p>
<h2>Legislación aplicable</h2>
<p>Este aviso legal se rige por la legislación española y de la Unión Europea que resulte aplicable a los usuarios que acceden desde España.</p>
''', "Aviso legal del sitio web de CRS Growth, marca comercial de Novaryn OÜ.")

legal("/privacidad/", "Política de privacidad", f'''
<h2>Responsable del tratamiento</h2>
{TITULAR}
<h2>Qué datos tratamos y para qué</h2>
<p>Tratamos los datos que nos facilitas en los formularios de contacto, de presupuesto y en el cuestionario previo (nombre, email, teléfono, empresa y la información que decidas escribir) con estas finalidades:</p>
<ul><li>Responder a tu solicitud y preparar la primera conversación.</li><li>Enviarte el presupuesto o la información que nos pidas.</li><li>Mantener la relación profesional si llegas a ser cliente.</li></ul>
<p>No usamos tus datos para enviarte publicidad sin tu consentimiento ni tomamos decisiones automatizadas sobre ti.</p>
<h2>Base legal</h2>
<p>Tu consentimiento al enviar el formulario y, en su caso, la aplicación de medidas precontractuales a petición tuya o la ejecución del contrato de servicios.</p>
<h2>Conservación</h2>
<p>Conservamos los datos mientras dure la relación o mientras sean necesarios para atender tu solicitud y, después, durante los plazos legales aplicables. Si no llegamos a trabajar juntos, los eliminamos en un plazo máximo de 12 meses.</p>
<h2>Proveedores que intervienen</h2>
<p>Para que la web funcione utilizamos estos proveedores, que pueden tratar datos por cuenta nuestra:</p>
<ul>
<li>Web3Forms: recibe los formularios y nos los envía por email.</li>
<li>Calendly: gestiona la reserva de llamadas si decides usarlo.</li>
<li>WhatsApp (Meta): si decides escribirnos por ese canal.</li>
<li>GitHub Pages: alojamiento del sitio web.</li>
</ul>
<p>Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo, con las garantías previstas en el Reglamento General de Protección de Datos.</p>
<h2>Tus derechos</h2>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a <a href="mailto:{MAIL}">{MAIL}</a>. Si consideras que no hemos atendido bien tu solicitud, puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>
''', "Política de privacidad de CRS Growth.")

legal("/cookies/", "Política de cookies", '''
<h2>Qué cookies usa este sitio</h2>
<p>Este sitio no instala cookies propias ni utiliza herramientas de analítica o publicidad.</p>
<h2>Servicios de terceros</h2>
<p>Las tipografías están alojadas en nuestro propio servidor, sin conexiones a terceros. Si decides abrir Calendly o WhatsApp desde los enlaces de la web, esos servicios pueden instalar sus propias cookies conforme a sus políticas, que se aplican en sus sitios y no en este.</p>
<h2>Cambios</h2>
<p>Si en el futuro incorporamos analítica u otras cookies no necesarias, actualizaremos esta política y te pediremos el consentimiento antes de instalarlas.</p>
''', "Política de cookies de CRS Growth.")

# ───────────────────────── 404 y redirecciones ─────────────────────────
NF = f'''<section class="pagina-hero oscuro" style="min-height:60vh"><div class="wrap">
<h1>Esta página ya no existe.</h1>
<p class="lead">Hemos simplificado la web. Lo que buscabas probablemente esté en el inicio.</p>
<div class="botones"><a class="btn btn-oro" href="/">Ir al inicio</a><a class="btn btn-linea" href="/contacto/">Contactar</a></div>
</div></section>'''
out = head("Página no encontrada — CRS Growth", "Página no encontrada.", "/404.html", "", True) + nav("") + NF + FOOT
open("404.html", "w", encoding="utf-8").write(out); print("ok 404.html")

for p in ["/servicios/", "/nosotros/", "/paquetes/", "/enterprise/", "/diagnostico/", "/realestate/"]:
    redirect(p, "/")
for p in ["/start/", "/start/diagnostico/"]:
    redirect(p, "/constitucion/")

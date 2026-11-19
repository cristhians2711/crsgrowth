# ───────────── LEGALES ─────────────
TIT = f'''<table>
<tr><td>Titular</td><td>Novaryn OÜ</td></tr>
<tr><td>Marca comercial</td><td>CRS Growth</td></tr>
<tr><td>Código de registro</td><td>17556049, Registro Mercantil de Estonia (Tartu Maakohus, departamento de registro)</td></tr>
<tr><td>Domicilio social</td><td>Ahtri tn 12, Kesklinna linnaosa, 15551 Tallinn, Harju maakond, Estonia</td></tr>
<tr><td>Email</td><td><a class="link" href="mailto:{MAIL}">{MAIL}</a></td></tr>
<tr><td>Teléfono</td><td>+34 697 293 677</td></tr>
</table>'''

def legal(path, t, body, desc):
    page(path, f"{t}, CRS Growth", desc, "",
         f'<section class="page-hero plain-2"><div class="container"><h1>{t}</h1><p class="lead">Actualizado en noviembre de 2026.</p></div></section>'
         f'<section class="section plain" style="padding-top: var(--space-2xl)"><div class="container legal">{body}</div></section>')

legal("/aviso-legal/", "Aviso legal", f'''
<h2>Datos del titular</h2><p>En cumplimiento de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico, estos son los datos del titular de este sitio:</p>{TIT}
<h2>Objeto</h2><p>Este sitio informa sobre los servicios de dirección y gestión de empresas, constitución de sociedades y acompañamiento personal que se prestan bajo la marca CRS Growth y bajo el nombre profesional de Cristhiam Silva.</p>
<h2>Condiciones de uso</h2><p>El acceso es gratuito y supone aceptar este aviso. El usuario se compromete a hacer un uso adecuado de los contenidos.</p>
<h2>Propiedad intelectual</h2><p>Los textos, diseños y logotipos de este sitio son de Novaryn OÜ o se usan con autorización. No se pueden reproducir sin permiso expreso.</p>
<h2>Responsabilidad</h2><p>La información de este sitio es general y no constituye asesoramiento para un caso concreto. El titular no responde del contenido de sitios de terceros enlazados.</p>
<h2>Legislación aplicable</h2><p>Este aviso se rige por la legislación española y de la Unión Europea aplicable a los usuarios que acceden desde España.</p>
''', "Aviso legal de CRS Growth, marca comercial de Novaryn OÜ.")

legal("/privacidad/", "Política de privacidad", f'''
<h2>Responsable</h2>{TIT}
<h2>Qué datos tratamos y para qué</h2><p>Los que nos das en los formularios y en el cuestionario: nombre, email, teléfono, empresa y lo que decidas escribir. Los usamos para responder a tu solicitud, preparar la primera conversación, enviarte un presupuesto y, si llegas a ser cliente, mantener la relación profesional. No enviamos publicidad sin tu consentimiento ni tomamos decisiones automatizadas sobre ti.</p>
<h2>Base legal</h2><p>Tu consentimiento al enviar el formulario y, en su caso, las medidas precontractuales que pides o la ejecución del contrato.</p>
<h2>Conservación</h2><p>Mientras dure la relación y después durante los plazos legales. Si no llegamos a trabajar juntos, los borramos en un plazo máximo de 12 meses.</p>
<h2>Proveedores</h2><ul><li>Web3Forms recibe los formularios y nos los envía por email.</li><li>Calendly gestiona la reserva de llamadas si decides usarlo.</li><li>WhatsApp, de Meta, si nos escribes por ese canal.</li><li>GitHub Pages aloja el sitio.</li></ul><p>Algunos pueden tratar datos fuera del Espacio Económico Europeo, con las garantías del Reglamento General de Protección de Datos.</p>
<h2>Tus derechos</h2><p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a <a class="link" href="mailto:{MAIL}">{MAIL}</a>. También puedes reclamar ante la Agencia Española de Protección de Datos.</p>
''', "Política de privacidad de CRS Growth.")

legal("/cookies/", "Política de cookies", '''
<h2>Qué cookies usa este sitio</h2><p>Ninguna propia, y ninguna de analítica o publicidad. Las tipografías se sirven desde nuestro propio dominio.</p>
<h2>Servicios de terceros</h2><p>Si abres Calendly o WhatsApp desde nuestros enlaces, esos servicios pueden usar sus propias cookies en sus sitios.</p>
<h2>Cambios</h2><p>Si algún día añadimos analítica, te pediremos el consentimiento antes.</p>
''', "Política de cookies de CRS Growth.")

# ───────────── 404 y redirecciones ─────────────
NF = '''<section class="hero desk"><div class="container"><div class="hero-text">
<h1>Esta página ya no existe.</h1><p class="lead">Hemos simplificado la web. Lo que buscabas estará en el inicio.</p>
<div class="actions"><a class="btn btn--ink" href="/">Ir al inicio</a><a class="link" href="/contacto/">Contactar</a></div></div></div></section>'''
open("404.html", "w", encoding="utf-8").write(head("Página no encontrada, CRS Growth", "Página no encontrada.", "/404.html", "", True) + nav("") + NF + FOOT)

for p in ["/servicios/", "/nosotros/", "/paquetes/", "/enterprise/", "/diagnostico/", "/realestate/", "/lab/", "/generador/"]:
    redirect(p, "/")
for p in ["/start/", "/start/diagnostico/"]:
    redirect(p, "/constitucion/")
print("listo")

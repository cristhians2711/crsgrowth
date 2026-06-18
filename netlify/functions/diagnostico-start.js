/**
 * CRS Growth — Netlify Function
 * Diagnóstico CRS Start
 * 
 * - Crea ficha en Notion CRM
 * - Envía email HTML al cliente
 * - Envía email con datos completos a CRS
 * 
 * ENV VARS requeridas en Netlify:
 *   NOTION_TOKEN      → (añadir en Netlify → Project configuration → Environment variables)
 *   NOTION_DB_ID      → faaa0b6d-9dbf-4fba-8e4c-506a7f1db027
 *   RESEND_API_KEY    → (pegar cuando tengas Resend)
 *   CRS_EMAIL         → cristhiam.silva@crsgrowth.com
 */

const NOTION_TOKEN  = process.env.NOTION_TOKEN;
const NOTION_DB_ID  = process.env.NOTION_DB_ID  || 'faaa0b6d-9dbf-4fba-8e4c-506a7f1db027';
const RESEND_KEY    = process.env.RESEND_API_KEY;
const CRS_EMAIL     = process.env.CRS_EMAIL || 'cristhiam.silva@crsgrowth.com';
const FROM_EMAIL    = 'CRS Growth <noreply@crsgrowth.com>';
const WHATSAPP_URL  = 'https://wa.me/34697293677';

// ── ICP SCORE CALCULATOR ─────────────────────────────────────────
function calcICP(data) {
  var score = 0;
  // Completo el diagnóstico web
  score += 2;
  // Es el decisor (autónomo o fundador implícito)
  score += 2;
  // Tiene negocio real o proyecto serio
  if (data.situacion !== 'idea_vaga') score += 2;
  // Problema concreto marcado
  if (data.preocupaciones && data.preocupaciones.length >= 2) score += 1;
  // Puede capitalizar el paro
  if (data.laboral === 'paro') score += 1;
  // Tiene clientes o ingresos previos
  if (data.clientes === 'si') score += 1;
  return Math.min(score, 10);
}

// ── PROFILE CALCULATOR ────────────────────────────────────────────
function getProfile(data) {
  if (data.laboral === 'paro') {
    var urgente = data.tiempo_paro === 'menos3' || data.tiempo_paro === '3a8';
    return {
      id: 'P1',
      titulo: urgente
        ? 'Tienes que actuar ya — tu prestación tiene fecha de caducidad'
        : 'Puedes usar el paro para financiar tu empresa',
      cuerpo: urgente
        ? 'Puedes capitalizar tu prestación por desempleo para financiar la constitución de tu empresa. Es la mejor decisión económica que puedes tomar ahora mismo — y tiene fecha de caducidad. Cada semana que pasa es dinero que pierdes. Te explicamos cómo funciona y qué necesitas exactamente.'
        : 'Tienes tiempo suficiente para hacerlo bien. La capitalización del paro puede financiar tu empresa y ahorrarte años de cuotas de autónomo. Antes de decidir nada, necesitas entender qué opciones tienes sobre la mesa.',
      tag: 'Capitalización del paro · Urgente',
    };
  }
  if (data.socios === 'si' && data.preocupaciones && data.preocupaciones.includes('socio')) {
    return {
      id: 'P3',
      titulo: 'Montar empresa con socios requiere hacerlo bien desde el principio',
      cuerpo: 'Montar empresa con socios sin tenerlo todo por escrito es el error más caro que cometen los emprendedores. Los estatutos mal redactados y los pactos de socios inexistentes generan conflictos que destruyen empresas y relaciones. Antes de constituir nada, necesitas tener claras las reglas del juego.',
      tag: 'Sociedad con socios · Pacto de socios',
    };
  }
  if (data.clientes === 'si' || data.situacion === 'autonomo') {
    return {
      id: 'P2',
      titulo: 'Estás listo para constituir — solo necesitas hacerlo bien',
      cuerpo: 'Tu proyecto tiene base real. El error más común ahora es elegir mal la estructura jurídica o firmar estatutos que no te protegen — y eso condiciona los próximos cinco años. Antes de ir a la notaría, necesitas 30 minutos de orientación que te ahorren años de problemas.',
      tag: 'Constitución · Estructura jurídica',
    };
  }
  return {
    id: 'P4',
    titulo: 'Primero claridad, luego acción',
    cuerpo: 'Todavía no tienes que constituir nada. Lo que necesitas ahora es claridad: qué forma jurídica te conviene, si el momento es el adecuado, cuánto te va a costar realmente y cuál es el primer paso concreto. Una sesión de 30 minutos te ahorra meses de errores y decisiones equivocadas.',
    tag: 'Orientación inicial · Hoja de ruta',
  };
}

// ── EMAIL HTML CLIENTE ─────────────────────────────────────────────
function emailCliente(nombre, profile) {
  return `<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Tu diagnóstico CRS Start</title>
</head>
<body style="margin:0;padding:0;background:#F2EFE9;font-family:Arial,Helvetica,sans-serif;">
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#F2EFE9;padding:32px 16px;">
<tr><td align="center">
<table cellpadding="0" cellspacing="0" border="0" width="560" style="max-width:560px;width:100%;">

  <!-- TOP GOLD BAR -->
  <tr><td style="height:3px;background:linear-gradient(90deg,#B8860B,#D4A017,#B8860B);font-size:0;">&nbsp;</td></tr>

  <!-- HEADER -->
  <tr><td style="background:#0D0D0D;padding:24px 32px;">
    <table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>
      <td><span style="font-family:Arial,sans-serif;font-size:20px;font-weight:bold;color:#EDE9E0;letter-spacing:-0.01em;">CRS <span style="color:#B8860B;">Growth</span></span></td>
      <td align="right"><span style="font-family:Arial,sans-serif;font-size:11px;color:#777;letter-spacing:0.08em;text-transform:uppercase;">Diagnóstico · CRS Start</span></td>
    </tr></table>
  </td></tr>

  <!-- BODY -->
  <tr><td style="background:#FFFFFF;padding:40px 32px;">
    <p style="margin:0 0 8px 0;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;color:#B8860B;text-transform:uppercase;letter-spacing:0.1em;">Tu resultado</p>
    <h1 style="margin:0 0 20px 0;font-family:Arial,sans-serif;font-size:24px;font-weight:bold;color:#0D0D0D;line-height:1.2;">${profile.titulo}</h1>

    <table cellpadding="0" cellspacing="0" border="0" width="100%" style="margin-bottom:24px;">
      <tr><td style="height:3px;background:linear-gradient(90deg,#B8860B,#D4A017);"></td></tr>
    </table>

    <p style="margin:0 0 20px 0;font-family:Arial,sans-serif;font-size:15px;color:#444;line-height:1.75;">${profile.cuerpo}</p>

    <table cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#FDF8EC;border:1px solid rgba(184,134,11,0.2);margin-bottom:28px;">
      <tr><td style="padding:16px 20px;">
        <p style="margin:0;font-family:Arial,sans-serif;font-size:12px;font-weight:bold;color:#B8860B;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:4px;">Área de enfoque</p>
        <p style="margin:0;font-family:Arial,sans-serif;font-size:14px;color:#1A1A1A;font-weight:bold;">${profile.tag}</p>
      </td></tr>
    </table>

    <p style="margin:0 0 16px 0;font-family:Arial,sans-serif;font-size:15px;color:#444;line-height:1.7;">El siguiente paso es una sesión gratuita de 30 minutos donde revisamos tu situación concreta y te decimos exactamente qué tienes que hacer y en qué orden.</p>

    <table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>
      <td style="padding:0 8px 0 0;" width="50%">
        <a href="${WHATSAPP_URL}?text=Hola%2C%20acabo%20de%20hacer%20el%20diagn%C3%B3stico%20de%20CRS%20Start%20y%20me%20gustar%C3%ADa%20hablar%20con%20vosotros." style="display:block;background:#25D366;color:#fff;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;text-align:center;padding:13px 16px;text-decoration:none;letter-spacing:0.04em;">WhatsApp →</a>
      </td>
      <td style="padding:0 0 0 8px;" width="50%">
        <a href="mailto:${CRS_EMAIL}?subject=Diagnóstico%20CRS%20Start%20—%20${encodeURIComponent(nombre)}" style="display:block;background:#0D0D0D;color:#B8860B;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;text-align:center;padding:13px 16px;text-decoration:none;letter-spacing:0.04em;">Enviar email →</a>
      </td>
    </tr></table>
  </td></tr>

  <!-- FOOTER -->
  <tr><td style="background:#0D0D0D;padding:20px 32px;">
    <table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>
      <td><span style="font-family:Arial,sans-serif;font-size:12px;color:#555;">Consultoría de Alto Rendimiento Empresarial</span></td>
      <td align="right"><a href="https://www.crsgrowth.com" style="font-family:Arial,sans-serif;font-size:12px;color:#B8860B;text-decoration:none;font-weight:bold;">crsgrowth.com</a></td>
    </tr></table>
  </td></tr>

  <!-- BOTTOM BAR -->
  <tr><td style="height:2px;background:#B8860B;font-size:0;">&nbsp;</td></tr>

</table>
</td></tr>
</table>
</body>
</html>`;
}

// ── EMAIL HTML CRS ─────────────────────────────────────────────────
function emailCRS(data, profile, icp) {
  var preocupaciones = data.preocupaciones
    ? data.preocupaciones.join(', ')
    : 'No especificadas';

  var rows = [
    ['Nombre', data.nombre || '—'],
    ['Email', data.email || '—'],
    ['WhatsApp', data.whatsapp || 'No facilitado'],
    ['Perfil asignado', profile.id + ' — ' + profile.titulo],
    ['ICP Score', icp + '/10'],
    ['Situación laboral', data.laboral || '—'],
    ['Tiempo de prestación', data.tiempo_paro || 'No aplica'],
    ['Situación', data.situacion || '—'],
    ['Clientes previos', data.clientes || '—'],
    ['Socios', data.socios || '—'],
    ['Sector / Actividad', data.sector || '—'],
    ['Preocupaciones', preocupaciones],
    ['Fecha y hora', new Date().toLocaleString('es-ES', { timeZone: 'Europe/Madrid' })],
  ];

  var rowsHTML = rows.map(function(r, i) {
    return '<tr>' +
      '<td style="padding:9px 14px;font-family:Arial,sans-serif;font-size:13px;font-weight:bold;color:#B8860B;text-transform:uppercase;letter-spacing:0.06em;background:' + (i%2===0?'#FDF8EC':'#FAF8F4') + ';width:35%;">' + r[0] + '</td>' +
      '<td style="padding:9px 14px;font-family:Arial,sans-serif;font-size:13px;color:#1A1A1A;background:' + (i%2===0?'#FFFFFF':'#FAF8F4') + ';">' + (r[1] || '—') + '</td>' +
    '</tr>';
  }).join('');

  return `<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"/><title>Nuevo lead CRS Start</title></head>
<body style="margin:0;padding:0;background:#F2EFE9;font-family:Arial,Helvetica,sans-serif;">
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="background:#F2EFE9;padding:32px 16px;">
<tr><td align="center">
<table cellpadding="0" cellspacing="0" border="0" width="580" style="max-width:580px;width:100%;">
  <tr><td style="height:3px;background:linear-gradient(90deg,#B8860B,#D4A017,#B8860B);font-size:0;">&nbsp;</td></tr>
  <tr><td style="background:#0D0D0D;padding:20px 28px;">
    <table cellpadding="0" cellspacing="0" border="0" width="100%"><tr>
      <td><span style="font-family:Arial,sans-serif;font-size:18px;font-weight:bold;color:#EDE9E0;">CRS <span style="color:#B8860B;">Growth</span></span></td>
      <td align="right"><span style="font-family:Arial,sans-serif;font-size:11px;color:#555;letter-spacing:0.08em;text-transform:uppercase;">Nuevo lead · CRS Start</span></td>
    </tr></table>
  </td></tr>
  <tr><td style="background:#FFFFFF;padding:28px;">
    <p style="margin:0 0 6px 0;font-family:Arial,sans-serif;font-size:11px;font-weight:bold;color:#B8860B;text-transform:uppercase;letter-spacing:0.1em;">Nuevo diagnóstico recibido</p>
    <h2 style="margin:0 0 20px 0;font-family:Arial,sans-serif;font-size:20px;font-weight:bold;color:#0D0D0D;">${data.nombre || 'Sin nombre'} &nbsp;<span style="font-size:14px;color:#777;font-weight:normal;">· ICP Score: <strong style="color:#B8860B;">${icp}/10</strong></span></h2>
    <table cellpadding="0" cellspacing="0" border="0" width="100%" style="border-collapse:collapse;border:1px solid #E0DDD6;">
      ${rowsHTML}
    </table>
    <div style="margin-top:20px;padding:16px;background:#0D0D0D;border-left:3px solid #B8860B;">
      <p style="margin:0 0 4px 0;font-family:Arial,sans-serif;font-size:11px;color:#B8860B;font-weight:bold;text-transform:uppercase;letter-spacing:0.08em;">Acción recomendada</p>
      <p style="margin:0;font-family:Arial,sans-serif;font-size:14px;color:#EDE9E0;">Contactar en menos de 24h. Abrir <a href="https://www.notion.so" style="color:#B8860B;">Notion CRM</a> para ver la ficha completa.</p>
    </div>
  </td></tr>
  <tr><td style="background:#0D0D0D;padding:16px 28px;text-align:center;">
    <span style="font-family:Arial,sans-serif;font-size:12px;color:#555;">crsgrowth.com &nbsp;·&nbsp; cristhiam.silva@crsgrowth.com</span>
  </td></tr>
  <tr><td style="height:2px;background:#B8860B;font-size:0;">&nbsp;</td></tr>
</table>
</td></tr>
</table>
</body>
</html>`;
}

// ── NOTION CREATE PAGE ─────────────────────────────────────────────
async function createNotionPage(data, profile, icp) {
  var body = {
    parent: { database_id: NOTION_DB_ID },
    properties: {
      'Nombre del lead': {
        title: [{ text: { content: data.nombre || 'Sin nombre' } }]
      },
      'Empresa': {
        rich_text: [{ text: { content: data.sector || '' } }]
      },
      'Etapa': {
        select: { name: '1 — Contacto nuevo' }
      },
      'Fuente': {
        select: { name: 'Web / Diagnóstico' }
      },
      'Servicio de interés': {
        select: { name: 'CRS START' }
      },
      'ICP Score': {
        number: icp
      },
      'Email': {
        email: data.email || null
      },
      'Próxima acción': {
        rich_text: [{ text: { content: 'Contactar en menos de 24h — Diagnóstico Start recibido' } }]
      },
      'Notas diagnóstico': {
        rich_text: [{ text: { content:
          'Perfil: ' + profile.id + ' — ' + profile.titulo + '\n' +
          'Situación laboral: ' + (data.laboral || '—') + '\n' +
          (data.tiempo_paro ? 'Tiempo prestación: ' + data.tiempo_paro + '\n' : '') +
          'Situación: ' + (data.situacion || '—') + '\n' +
          'Clientes previos: ' + (data.clientes || '—') + '\n' +
          'Socios: ' + (data.socios || '—') + '\n' +
          'Preocupaciones: ' + (data.preocupaciones ? data.preocupaciones.join(', ') : '—') + '\n' +
          'WhatsApp: ' + (data.whatsapp || 'No facilitado')
        } }]
      },
      'Responsable': {
        select: { name: 'Cristhiam' }
      },
    }
  };

  var resp = await fetch('https://api.notion.com/v1/pages', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + NOTION_TOKEN,
      'Content-Type': 'application/json',
      'Notion-Version': '2022-06-28',
    },
    body: JSON.stringify(body),
  });

  if (!resp.ok) {
    var err = await resp.text();
    console.error('Notion error:', err);
    throw new Error('Notion API error: ' + resp.status);
  }
  return resp.json();
}

// ── SEND EMAIL VIA RESEND ──────────────────────────────────────────
async function sendEmail(to, subject, html) {
  if (!RESEND_KEY) {
    console.log('RESEND_API_KEY not set — skipping email to:', to);
    return;
  }
  var resp = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + RESEND_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ from: FROM_EMAIL, to: [to], subject: subject, html: html }),
  });
  if (!resp.ok) {
    var err = await resp.text();
    console.error('Resend error:', err);
  }
}

// ── MAIN HANDLER ──────────────────────────────────────────────────
exports.handler = async function(event) {
  // CORS
  var headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Content-Type': 'application/json',
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers: headers, body: '' };
  }
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers: headers, body: JSON.stringify({ error: 'Method not allowed' }) };
  }

  try {
    var data = JSON.parse(event.body || '{}');

    // Validate required fields
    if (!data.email) {
      return { statusCode: 400, headers: headers, body: JSON.stringify({ error: 'Email requerido' }) };
    }

    // Calculate profile and score
    var profile = getProfile(data);
    var icp = calcICP(data);

    // 1. Create Notion page
    await createNotionPage(data, profile, icp);

    // 2. Send email to client
    await sendEmail(
      data.email,
      'Tu diagnóstico CRS Start — ' + (data.nombre || ''),
      emailCliente(data.nombre || '', profile)
    );

    // 3. Send email to CRS
    await sendEmail(
      CRS_EMAIL,
      'Nuevo lead CRS Start — ' + (data.nombre || 'Sin nombre') + ' · ICP ' + icp + '/10',
      emailCRS(data, profile, icp)
    );

    return {
      statusCode: 200,
      headers: headers,
      body: JSON.stringify({
        ok: true,
        profile: { id: profile.id, titulo: profile.titulo, cuerpo: profile.cuerpo, tag: profile.tag },
        icp: icp,
      }),
    };

  } catch (err) {
    console.error('Handler error:', err);
    return {
      statusCode: 500,
      headers: headers,
      body: JSON.stringify({ error: 'Error interno. Por favor inténtalo de nuevo.' }),
    };
  }
};

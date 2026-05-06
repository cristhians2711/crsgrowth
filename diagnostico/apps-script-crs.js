/**
 * CRS Growth — Apps Script para diagnóstico web
 *
 * Qué hace:
 *   1. Guarda cada diagnóstico en Google Sheets
 *   2. Envía email a Cristhiam con el resumen del lead
 *   3. Envía email al cliente con su resultado completo
 *
 * Instalación:
 *   1. Ve a script.google.com → Nuevo proyecto
 *   2. Pega este código completo
 *   3. Guarda (Ctrl+S)
 *   4. Implementar → Nueva implementación → Aplicación web
 *      · Ejecutar como: Yo
 *      · Acceso: Cualquier usuario (incluidos anónimos)
 *   5. Copia la URL de implementación
 *   6. Pégala en diagnostico/index.html donde dice APPS_URL
 */

const SPREADSHEET_ID = '1GgutPmCupC8Oox5Vu-gXCdnsJ-D5iHcB1W2Z4rVvGhE';
const SHEET_NAME     = 'Diagnosticos';
const CRS_EMAIL      = 'cristhiam.silva@crsgrowth.com';
const CALENDLY_URL   = 'https://calendly.com/cristhiam-silva-crsgrowth/30min';

function doPost(e) {
  try {
    const raw  = (e && e.postData && e.postData.contents) ? e.postData.contents : '{}';
    const data = JSON.parse(raw);

    // ── 1. Guardar en Sheets ──────────────────────────────────────────────
    const sheet = getOrCreateSheet_();
    sheet.appendRow([
      new Date(),
      data.nombre     || '',
      data.empresa    || '',
      data.email      || '',
      data.puntuacion || '',
      data.maximo     || '',
      data.porcentaje || '',
      data.nivel      || '',
      data.titulo     || '',
      data.accion     || '',
      data.servicios  || '',
      data.detalle    || '',
      data.timestamp  || ''
    ]);

    // ── 2. Email a Cristhiam ──────────────────────────────────────────────
    const subjectCRS = '🔔 Nuevo diagnóstico — ' + (data.empresa || data.nombre || 'Anónimo')
                     + ' [' + (data.nivel || '-') + ']';

    const bodyCRS = [
      'Nuevo diagnóstico completado en crsgrowth.com',
      '─────────────────────────────────────',
      '',
      'CONTACTO',
      'Nombre:   ' + (data.nombre   || '-'),
      'Empresa:  ' + (data.empresa  || '-'),
      'Email:    ' + (data.email    || '-'),
      '',
      'RESULTADO',
      'Puntuación: ' + (data.puntuacion || '-') + ' / ' + (data.maximo || '-')
                     + ' (' + (data.porcentaje || '-') + '%)',
      'Nivel:      ' + (data.nivel  || '-'),
      'Título:     ' + (data.titulo || '-'),
      '',
      'ACCIÓN RECOMENDADA',
      data.accion || '-',
      '',
      'SERVICIOS PRIORITARIOS',
      data.servicios || '-',
      '',
      'DESGLOSE POR ÁREA',
      formatDetalle_(data.detalle),
      '',
      '─────────────────────────────────────',
      'Reservar llamada: ' + CALENDLY_URL
    ].join('\n');

    MailApp.sendEmail({
      to:      CRS_EMAIL,
      subject: subjectCRS,
      body:    bodyCRS,
      replyTo: data.email || undefined,
      name:    'CRS Diagnóstico Web'
    });

    // ── 3. Email al cliente ───────────────────────────────────────────────
    if (data.email) {
      const nombre   = data.nombre || 'Hola';
      const nivel    = data.nivel  || '';
      const titulo   = data.titulo || '';
      const accion   = data.accion || '';
      const servicios = data.servicios || '';
      const pct      = data.porcentaje || '';
      const pts      = data.puntuacion || '';
      const max      = data.maximo     || '';

      const subjectCliente = 'Tu diagnóstico empresarial CRS — ' + nivel;

      const bodyCliente = [
        'Hola ' + nombre + ',',
        '',
        'Gracias por completar el diagnóstico empresarial de CRS Growth.',
        'Aquí tienes tu resultado completo.',
        '',
        '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━',
        'RESULTADO: ' + nivel.toUpperCase(),
        '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━',
        '',
        titulo,
        '',
        'Puntuación: ' + pts + ' / ' + max + ' (' + pct + '%)',
        '',
        '─────────────────────────────',
        'QUÉ SIGNIFICA ESTO PARA TI',
        '─────────────────────────────',
        accion,
        '',
        '─────────────────────────────',
        'SERVICIOS RECOMENDADOS',
        '─────────────────────────────',
        servicios,
        '',
        '─────────────────────────────',
        'DESGLOSE POR ÁREA',
        '─────────────────────────────',
        formatDetalle_(data.detalle),
        '',
        '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━',
        'PRÓXIMO PASO',
        '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━',
        '',
        'Reserva una sesión gratuita de 30 minutos para revisar',
        'tu diagnóstico juntos y definir el primer paso concreto:',
        '',
        CALENDLY_URL,
        '',
        'O escríbenos directamente:',
        'WhatsApp: +34 697 293 677',
        'Email:    info@crsgrowth.com',
        '',
        '─────────────────────────────',
        'CRS Growth',
        'Tu empresa funciona. Tú diriges.',
        'www.crsgrowth.com'
      ].join('\n');

      MailApp.sendEmail({
        to:      data.email,
        subject: subjectCliente,
        body:    bodyCliente,
        name:    'CRS Growth',
        replyTo: CRS_EMAIL
      });
    }

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    MailApp.sendEmail({
      to:      CRS_EMAIL,
      subject: 'Error Apps Script — diagnóstico web',
      body:    String(err && err.stack ? err.stack : err)
    });
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function getOrCreateSheet_() {
  const ss    = SpreadsheetApp.openById(SPREADSHEET_ID);
  let   sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow([
      'Fecha', 'Nombre', 'Empresa', 'Email',
      'Puntuación', 'Máximo', '%',
      'Nivel', 'Título', 'Acción', 'Servicios',
      'Detalle JSON', 'Timestamp front'
    ]);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function formatDetalle_(detalle) {
  if (!detalle) return '-';
  try {
    const parsed = typeof detalle === 'string' ? JSON.parse(detalle) : detalle;
    if (!Array.isArray(parsed)) return String(detalle);
    return parsed.map(function(a) {
      return (a.area || 'Área') + ': ' + (a.puntos || 0) + '/4';
    }).join('\n');
  } catch(e) {
    return String(detalle);
  }
}

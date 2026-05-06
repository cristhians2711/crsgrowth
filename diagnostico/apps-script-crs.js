/**
 * CRS Consulting - Registro de diagnóstico
 *
 * Qué hace:
 * 1) Guarda cada diagnóstico en Google Sheets
 * 2) Te envía un email con el resumen del lead y su resultado
 *
 * Pasos:
 * 1. Pega este código en Google Apps Script
 * 2. Guarda
 * 3. Implementar > Administrar implementaciones > Editar la implementación actual
 *    o crea una nueva implementación como Aplicación web
 * 4. Acceso: Cualquier usuario
 */

const SPREADSHEET_ID = '1GgutPmCupC8Oox5Vu-gXCdnsJ-D5iHcB1W2Z4rVvGhE';
const SHEET_NAME = 'Diagnosticos';
const NOTIFY_EMAIL = 'cristhiam.silva@crsgrowth.com';

function doPost(e) {
  try {
    const raw = e && e.postData && e.postData.contents ? e.postData.contents : '{}';
    const data = JSON.parse(raw);
    const sheet = getOrCreateSheet_();

    const detalleTexto = formatDetalle_(data.detalle);

    sheet.appendRow([
      new Date(),
      data.nombre || '',
      data.empresa || '',
      data.email || '',
      data.telefono || '',
      data.sector || '',
      data.empleados || '',
      data.puntuacion || '',
      data.maximo || '',
      data.porcentaje || '',
      data.nivel || '',
      data.titulo || '',
      data.accion || '',
      data.servicios || '',
      data.detalle || '',
      data.timestamp || ''
    ]);

    const subject = 'Nuevo diagnóstico recibido - ' + (data.empresa || data.nombre || 'Sin identificar');
    const body = [
      'Se ha recibido un nuevo diagnóstico en la web.',
      '',
      'DATOS DEL CONTACTO',
      'Nombre: ' + (data.nombre || '-'),
      'Empresa: ' + (data.empresa || '-'),
      'Email: ' + (data.email || '-'),
      'Teléfono: ' + (data.telefono || '-'),
      'Sector: ' + (data.sector || '-'),
      'Empleados: ' + (data.empleados || '-'),
      '',
      'RESULTADO',
      'Puntuación: ' + (data.puntuacion || '-') + '/' + (data.maximo || '-'),
      'Porcentaje: ' + (data.porcentaje || '-') + '%',
      'Nivel: ' + (data.nivel || '-'),
      'Título: ' + (data.titulo || '-'),
      '',
      'ACCIÓN RECOMENDADA',
      data.accion || '-',
      '',
      'SERVICIOS PRIORITARIOS',
      data.servicios || '-',
      '',
      'DETALLE DEL DIAGNÓSTICO',
      detalleTexto,
      '',
      'JSON ORIGINAL',
      data.detalle || '-'
    ].join('\n');

    MailApp.sendEmail({
      to: NOTIFY_EMAIL,
      subject: subject,
      body: body,
      replyTo: data.email || undefined,
      name: 'CRS Diagnóstico Web'
    });

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    MailApp.sendEmail({
      to: NOTIFY_EMAIL,
      subject: 'Error en Apps Script - diagnóstico web',
      body: String(err && err.stack ? err.stack : err)
    });

    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function getOrCreateSheet_() {
  const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  let sheet = ss.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    sheet.appendRow([
      'fecha_registro',
      'nombre',
      'empresa',
      'email',
      'telefono',
      'sector',
      'empleados',
      'puntuacion',
      'maximo',
      'porcentaje',
      'nivel',
      'titulo',
      'accion',
      'servicios',
      'detalle',
      'timestamp_front'
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

    const blocks = [];
    parsed.forEach(function(area) {
      blocks.push('[' + (area.area || 'Área') + '] ' + (area.puntos || 0) + '/' + (area.maximo || 0));
      if (Array.isArray(area.preguntas)) {
        area.preguntas.forEach(function(p) {
          blocks.push('- ' + (p.pregunta || 'Pregunta'));
          blocks.push('  Respuesta: ' + (p.respuesta || '-'));
          blocks.push('  Puntos: ' + (p.puntos || 0));
        });
      }
      blocks.push('');
    });
    return blocks.join('\n');
  } catch (e) {
    return String(detalle);
  }
}

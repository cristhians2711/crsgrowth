/**
 * CRS Growth — Apps Script v3
 * ─────────────────────────────────────────────────────────────
 * 1. Guarda diagnóstico en Google Sheets
 * 2. Envía email HTML a Cristhiam con informe completo del lead
 * 3. Envía email al cliente con su resultado y enlace a Calendly
 *
 * INSTALACIÓN:
 *   1. script.google.com → Nuevo proyecto → pega este código
 *   2. Implementar → Nueva implementación → Aplicación web
 *      · Ejecutar como: Yo
 *      · Acceso: Cualquier usuario (incluidos anónimos)
 *   3. Copia la URL → pégala en diagnostico/index.html
 *      donde dice: var APPS_URL = 'PASTE_YOUR_APPS_SCRIPT_URL_HERE';
 */

var CRS_EMAIL  = 'cristhiam.silva@crsgrowth.com';
var CALENDLY   = 'https://calendly.com/cristhiam-silva-crsgrowth/30min';
var SHEET_ID   = '1GgutPmCupC8Oox5Vu-gXCdnsJ-D5iHcB1W2Z4rVvGhE';
var SHEET_NAME = 'Diagnósticos';

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    saveToSheet(data);
    sendToCRS(data);
    if (data.email) sendToClient(data);
    return ok();
  } catch(err) {
    try {
      MailApp.sendEmail(CRS_EMAIL, '⚠ Error Apps Script diagnóstico', String(err));
    } catch(e2){}
    return error(String(err));
  }
}

function doGet() {
  return ContentService.createTextOutput('CRS Diagnóstico API — OK');
}

function ok()    { return ContentService.createTextOutput(JSON.stringify({ok:true})).setMimeType(ContentService.MimeType.JSON); }
function error(m){ return ContentService.createTextOutput(JSON.stringify({ok:false,error:m})).setMimeType(ContentService.MimeType.JSON); }

// ── SHEETS ──────────────────────────────────────────────────
function saveToSheet(d) {
  var ss    = SpreadsheetApp.openById(SHEET_ID);
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    var heads = ['Fecha','Nombre','Empresa','Email','Puntuación','Máximo','%','Nivel','Título','Acción','Servicios','Detalle'];
    sheet.appendRow(heads);
    var hr = sheet.getRange(1,1,1,heads.length);
    hr.setBackground('#13110E');
    hr.setFontColor('#B8860B');
    hr.setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  sheet.appendRow([
    new Date(d.timestamp || Date.now()),
    d.nombre     || '—',
    d.empresa    || '—',
    d.email      || '—',
    Number(d.puntuacion) || 0,
    Number(d.maximo)     || 24,
    Number(d.porcentaje) || 0,
    d.nivel      || '—',
    d.titulo     || '—',
    d.accion     || '—',
    d.servicios  || '—',
    d.detalle    || '—'
  ]);
}

// ── EMAIL A CRISTHIAM ────────────────────────────────────────
function sendToCRS(d) {
  var col = d.nivel === 'Listo para Escalar' ? '#27ae60'
          : d.nivel === 'Sistema en Progreso' ? '#B8860B'
          : d.nivel === 'Ordenar para Crecer'  ? '#f39c12'
          : '#e74c3c';

  var areasHTML = '';
  try {
    var det = JSON.parse(d.detalle || '[]');
    areasHTML = det.map(function(a){
      var pct = Math.round((a.puntos/4)*100);
      var c   = a.puntos<=1?'#e74c3c':a.puntos===2?'#f39c12':a.puntos===3?'#B8860B':'#27ae60';
      return '<tr>'
        +'<td style="padding:8px 12px;border-bottom:1px solid #1e1e22;color:#8a8070;font-size:13px;">'+a.area+'</td>'
        +'<td style="padding:8px 12px;border-bottom:1px solid #1e1e22;color:'+c+';font-size:13px;font-weight:bold;text-align:center;">'+a.puntos+'/4</td>'
        +'<td style="padding:8px 12px;border-bottom:1px solid #1e1e22;font-size:12px;"><div style="height:6px;background:#1e1e22;border-radius:3px;overflow:hidden;width:120px;"><div style="height:100%;width:'+pct+'%;background:'+c+';border-radius:3px;"></div></div></td>'
        +'</tr>';
    }).join('');
  } catch(e) { areasHTML = '<tr><td colspan="3" style="color:#8a8070;padding:8px 12px;">—</td></tr>'; }

  var html = '<!DOCTYPE html><html><head><meta charset="UTF-8"></head>'
    +'<body style="margin:0;padding:0;background:#0a0a0c;font-family:Georgia,serif;">'
    +'<div style="max-width:620px;margin:0 auto;padding:36px 24px;">'

    // Header
    +'<div style="text-align:center;margin-bottom:32px;">'
    +'<div style="font-size:9px;letter-spacing:.4em;text-transform:uppercase;color:#B8860B;margin-bottom:10px;">CRS GROWTH</div>'
    +'<div style="width:40px;height:1px;margin:0 auto 14px;background:linear-gradient(90deg,transparent,#B8860B,transparent);"></div>'
    +'<h1 style="font-size:20px;font-weight:normal;color:#EDE9E0;margin:0 0 5px;">Nuevo Diagnóstico</h1>'
    +'<p style="font-size:11px;color:#6a6258;margin:0;letter-spacing:.08em;">'+new Date().toLocaleDateString('es-ES',{weekday:'long',year:'numeric',month:'long',day:'numeric'})+'</p>'
    +'</div>'

    // Contact data
    +'<div style="background:rgba(255,255,255,.03);border:1px solid rgba(184,134,11,.2);border-radius:3px;padding:22px;margin-bottom:16px;">'
    +'<div style="font-size:9px;letter-spacing:.26em;text-transform:uppercase;color:#B8860B;margin-bottom:14px;">Datos del contacto</div>'
    +'<table style="width:100%;border-collapse:collapse;">'
    +[['Nombre',d.nombre],['Empresa',d.empresa||'—'],['Email',d.email]].map(function(r){
      return '<tr><td style="padding:6px 0;font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:#6a6258;width:30%;">'+r[0]+'</td>'
            +'<td style="padding:6px 0;font-size:14px;color:#EDE9E0;">'+r[1]+'</td></tr>';
    }).join('')
    +'</table></div>'

    // Score
    +'<div style="background:'+col+'0d;border:1px solid '+col+'40;border-radius:3px;padding:24px;text-align:center;margin-bottom:16px;">'
    +'<div style="font-size:9px;letter-spacing:.3em;text-transform:uppercase;color:'+col+';margin-bottom:10px;">Resultado</div>'
    +'<div style="font-size:56px;font-weight:bold;color:'+col+';line-height:1;margin-bottom:5px;">'+d.puntuacion+'<span style="font-size:18px;opacity:.4;">/'+d.maximo+'</span></div>'
    +'<div style="font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:'+col+';margin-bottom:12px;">'+d.nivel+'</div>'
    +'<div style="max-width:280px;margin:0 auto 16px;height:5px;background:rgba(255,255,255,.06);border-radius:3px;overflow:hidden;">'
    +'<div style="width:'+d.porcentaje+'%;height:100%;background:linear-gradient(90deg,'+col+','+col+'bb);border-radius:3px;"></div></div>'
    +'<h2 style="font-size:16px;color:#EDE9E0;font-weight:normal;margin:0 0 8px;">'+d.titulo+'</h2>'
    +'<p style="font-size:13px;color:#b8b0a0;line-height:1.7;margin:0;">'+d.accion+'</p>'
    +'</div>'

    // Services
    +'<div style="background:rgba(184,134,11,.05);border:1px solid rgba(184,134,11,.25);border-radius:3px;padding:18px;margin-bottom:16px;">'
    +'<div style="font-size:9px;letter-spacing:.26em;text-transform:uppercase;color:#B8860B;margin-bottom:10px;">Servicios prioritarios</div>'
    +'<div>'+(d.servicios||'').split(',').map(function(s){return '<span style="display:inline-block;font-size:10px;letter-spacing:.12em;color:#B8860B;border:1px solid rgba(184,134,11,.3);padding:4px 10px;border-radius:2px;margin:0 4px 4px 0;">'+s.trim()+'</span>';}).join('')+'</div>'
    +'</div>'

    // Areas table
    +'<div style="background:rgba(255,255,255,.02);border:1px solid rgba(255,255,255,.06);border-radius:3px;padding:22px;margin-bottom:24px;">'
    +'<div style="font-size:9px;letter-spacing:.26em;text-transform:uppercase;color:#B8860B;margin-bottom:14px;">Desglose por área</div>'
    +'<table style="width:100%;border-collapse:collapse;"><tbody>'+areasHTML+'</tbody></table>'
    +'</div>'

    // CTA
    +'<div style="text-align:center;">'
    +'<a href="'+CALENDLY+'" style="display:inline-block;background:linear-gradient(135deg,#B8860B,#D4A017,#B8860B);color:#13110E;text-decoration:none;padding:13px 30px;font-size:10px;letter-spacing:.2em;text-transform:uppercase;font-weight:bold;border-radius:2px;">Preparar llamada con '+d.nombre+' →</a>'
    +'<p style="font-size:10px;color:#6a6258;margin-top:10px;">crsgrowth.com · CRS Consulting</p>'
    +'</div>'

    +'</div></body></html>';

  MailApp.sendEmail({
    to:       CRS_EMAIL,
    subject:  '🎯 Diagnóstico CRS — '+(d.empresa||d.nombre||'Anónimo')+' ['+d.nivel+' · '+d.puntuacion+'/'+d.maximo+']',
    htmlBody: html,
    replyTo:  d.email || undefined
  });
}

// ── EMAIL AL CLIENTE ─────────────────────────────────────────
function sendToClient(d) {
  var nombre = d.nombre || 'Hola';

  var areasText = '';
  try {
    var det = JSON.parse(d.detalle || '[]');
    areasText = det.map(function(a){
      var stars = '';
      for(var i=0;i<4;i++){ stars += i < a.puntos ? '●' : '○'; }
      return '  ' + a.area + ': ' + stars + ' (' + a.puntos + '/4)';
    }).join('\n');
  } catch(e) { areasText = '  —'; }

  var bodyCliente = [
    'Hola ' + nombre + ',',
    '',
    'Aquí tienes el resultado de tu diagnóstico empresarial de CRS Growth.',
    '',
    '━━━━━━━━━━━━━━━━━━━━━━━━━━',
    'RESULTADO: ' + (d.nivel||'').toUpperCase(),
    '━━━━━━━━━━━━━━━━━━━━━━━━━━',
    '',
    d.titulo || '',
    '',
    'Puntuación: ' + d.puntuacion + ' / ' + d.maximo + ' (' + d.porcentaje + '%)',
    '',
    '─────────────────────────',
    'QUÉ SIGNIFICA PARA TI',
    '─────────────────────────',
    d.accion || '',
    '',
    '─────────────────────────',
    'DESGLOSE POR ÁREA',
    '─────────────────────────',
    areasText,
    '',
    '─────────────────────────',
    'SERVICIOS RECOMENDADOS',
    '─────────────────────────',
    d.servicios || '',
    '',
    '━━━━━━━━━━━━━━━━━━━━━━━━━━',
    'PRÓXIMO PASO',
    '━━━━━━━━━━━━━━━━━━━━━━━━━━',
    '',
    'Reserva una sesión gratuita de 30 minutos para revisar',
    'tu diagnóstico y definir el primer paso concreto:',
    '',
    CALENDLY,
    '',
    'O escríbenos:',
    'WhatsApp: +34 697 293 677',
    'Email: info@crsgrowth.com',
    '',
    '─────────────────────────',
    'CRS Growth',
    'Tu empresa funciona. Tú diriges.',
    'www.crsgrowth.com'
  ].join('\n');

  MailApp.sendEmail({
    to:      d.email,
    subject: 'Tu diagnóstico CRS Growth — ' + (d.nivel||''),
    body:    bodyCliente,
    name:    'CRS Growth',
    replyTo: CRS_EMAIL
  });
}

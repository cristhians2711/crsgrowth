/**
 * ══════════════════════════════════════════════════════════════
 *  CRS CONSULTING — BACKEND DIAGNÓSTICO ESTRATÉGICO
 *  Google Apps Script · v2
 *
 *  → Guarda cada diagnóstico en Google Sheets
 *  → Envía email de notificación a Cristhiam con informe completo
 * ══════════════════════════════════════════════════════════════
 */

// ─── CONFIGURACIÓN ────────────────────────────────────────────
const EMAIL_CRS    = "cristhiam.silva@crsgrowth.com";
const HOJA         = "Diagnósticos";
const ASUNTO_PRE   = "🎯 Diagnóstico CRS — ";

// ─── ENTRADA ─────────────────────────────────────────────────
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    guardarEnSheet(data);
    enviarEmail(data);
    return ok();
  } catch (err) {
    return error(err.message);
  }
}

function doGet(e) {
  // Permite testear desde el navegador
  return ContentService.createTextOutput("CRS Diagnóstico API — OK").setMimeType(ContentService.MimeType.TEXT);
}

function ok()    { return ContentService.createTextOutput(JSON.stringify({ok:true})).setMimeType(ContentService.MimeType.JSON); }
function error(m){ return ContentService.createTextOutput(JSON.stringify({ok:false,error:m})).setMimeType(ContentService.MimeType.JSON); }

// ─── GOOGLE SHEETS ────────────────────────────────────────────
function guardarEnSheet(d) {
  const ss    = SpreadsheetApp.getActiveSpreadsheet();
  let   sheet = ss.getSheetByName(HOJA);

  if (!sheet) {
    sheet = ss.insertSheet(HOJA);
    const heads = [
      "Fecha","Nombre","Empresa","Email","Teléfono","Sector","Empleados",
      "Puntuación","Máximo","Porcentaje (%)","Nivel","Diagnóstico",
      "Acción","Servicios prioritarios","Respuestas detalladas"
    ];
    sheet.appendRow(heads);
    const h = sheet.getRange(1,1,1,heads.length);
    h.setBackground("#0d0d10");
    h.setFontColor("#c9a84c");
    h.setFontWeight("bold");
    h.setFontSize(10);
    sheet.setFrozenRows(1);
    sheet.setColumnWidth(1,160); // Fecha
    sheet.setColumnWidth(2,140); // Nombre
    sheet.setColumnWidth(3,160); // Empresa
    sheet.setColumnWidth(4,200); // Email
    sheet.setColumnWidth(12,280);// Diagnóstico
    sheet.setColumnWidth(13,300);// Acción
  }

  sheet.appendRow([
    new Date(d.timestamp || Date.now()),
    d.nombre    || "—",
    d.empresa   || "—",
    d.email     || "—",
    d.telefono  || "—",
    d.sector    || "—",
    d.empleados || "—",
    Number(d.puntuacion) || 0,
    Number(d.maximo)     || 36,
    Number(d.porcentaje) || 0,
    d.nivel     || "—",
    d.titulo    || "—",
    d.accion    || "—",
    d.servicios || "—",
    d.detalle   || "—"
  ]);
}

// ─── EMAIL ────────────────────────────────────────────────────
function enviarEmail(d) {
  const colNivel = { "CRÍTICO":"#d95555","DÉBIL":"#d4883a","EN DESARROLLO":"#c9b84a","SÓLIDO":"#c9a84c" };
  const col = colNivel[d.nivel] || "#c9a84c";

  let areasHTML = "";
  try {
    const detalle = JSON.parse(d.detalle || "[]");
    areasHTML = detalle.map(area => {
      const pct = Math.round(area.puntos / area.maximo * 100);
      const c   = pct<34?"#d95555":pct<56?"#d4883a":pct<80?"#c9b84a":"#5cb87a";
      const qs  = area.preguntas.map(p=>`
        <tr>
          <td style="padding:9px 12px;border-bottom:1px solid #1e1e22;color:#8a8070;font-size:13px;width:58%;vertical-align:top">${p.pregunta}</td>
          <td style="padding:9px 12px;border-bottom:1px solid #1e1e22;color:#b8b0a0;font-size:13px;vertical-align:top">${p.respuesta}</td>
          <td style="padding:9px 12px;border-bottom:1px solid #1e1e22;color:${c};font-size:13px;text-align:center;vertical-align:top;white-space:nowrap">${p.puntos}/3</td>
        </tr>`).join("");
      return `
        <div style="margin-bottom:18px;border:1px solid #1e1e22;border-radius:3px;overflow:hidden">
          <div style="background:#12121a;padding:11px 16px;display:flex;justify-content:space-between;align-items:center">
            <span style="font-size:13px;color:#f0ede8;letter-spacing:0.04em">${area.area}</span>
            <span style="color:${c};font-size:13px;font-weight:bold">${area.puntos}/${area.maximo}</span>
          </div>
          <table style="width:100%;border-collapse:collapse"><tbody>${qs}</tbody></table>
        </div>`;
    }).join("");
  } catch(e) {
    areasHTML = `<p style="color:#8a8070;font-size:13px">No se pudieron procesar los detalles de las respuestas.</p>`;
  }

  const fecha = new Date().toLocaleDateString('es-ES',{weekday:'long',year:'numeric',month:'long',day:'numeric'});

  const html = `<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#0a0a0c;font-family:Georgia,serif">
<div style="max-width:680px;margin:0 auto;padding:40px 24px">

  <!-- Header -->
  <div style="text-align:center;margin-bottom:36px">
    <div style="font-size:9px;letter-spacing:0.4em;text-transform:uppercase;color:#c9a84c;margin-bottom:12px">CRS CONSULTING</div>
    <div style="width:48px;height:1px;margin:0 auto 16px;background:linear-gradient(90deg,transparent,#c9a84c,transparent)"></div>
    <h1 style="font-size:22px;font-weight:normal;color:#f0ede8;margin:0 0 6px">Nuevo Diagnóstico Completado</h1>
    <p style="font-size:12px;color:#6a6258;margin:0;letter-spacing:0.1em">${fecha}</p>
  </div>

  <!-- Datos del prospecto -->
  <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(201,168,76,0.2);border-radius:3px;padding:26px;margin-bottom:18px">
    <div style="font-size:9px;letter-spacing:0.28em;text-transform:uppercase;color:#c9a84c;margin-bottom:16px">Datos del prospecto</div>
    <table style="width:100%;border-collapse:collapse">
      ${[["Nombre",d.nombre],["Empresa",d.empresa],["Email",d.email],
         ["Teléfono",d.telefono||"—"],["Sector",d.sector||"—"],["Empleados",d.empleados||"—"]]
        .map(([k,v])=>`<tr>
          <td style="padding:7px 0;font-size:10px;letter-spacing:0.12em;text-transform:uppercase;color:#6a6258;width:32%">${k}</td>
          <td style="padding:7px 0;font-size:14px;color:#f0ede8">${v}</td>
        </tr>`).join("")}
    </table>
  </div>

  <!-- Puntuación -->
  <div style="background:${col}0d;border:1px solid ${col}40;border-radius:3px;padding:28px;text-align:center;margin-bottom:18px">
    <div style="font-size:9px;letter-spacing:0.32em;text-transform:uppercase;color:${col};margin-bottom:12px">Resultado del diagnóstico</div>
    <div style="font-size:62px;font-weight:bold;color:${col};line-height:1;margin-bottom:6px">
      ${d.puntuacion}<span style="font-size:20px;opacity:0.38">/${d.maximo}</span>
    </div>
    <div style="font-size:13px;letter-spacing:0.22em;text-transform:uppercase;color:${col};margin-bottom:14px">${d.nivel}</div>
    <!-- Bar -->
    <div style="max-width:320px;margin:0 auto 18px;height:5px;background:rgba(255,255,255,0.06);border-radius:3px;overflow:hidden">
      <div style="width:${d.porcentaje}%;height:100%;background:linear-gradient(90deg,${col},${col}bb);border-radius:3px"></div>
    </div>
    <h2 style="font-size:18px;color:#f0ede8;font-weight:normal;margin:0 0 10px">${d.titulo}</h2>
    <p style="font-size:14px;color:#b8b0a0;line-height:1.8;margin:0">${d.accion}</p>
  </div>

  <!-- Servicios -->
  <div style="background:rgba(201,168,76,0.05);border:1px solid rgba(201,168,76,0.28);border-radius:3px;padding:22px;margin-bottom:18px">
    <div style="font-size:9px;letter-spacing:0.28em;text-transform:uppercase;color:#c9a84c;margin-bottom:12px">Servicios prioritarios</div>
    <div>${(d.servicios||"").split(',').map(s=>`<span style="display:inline-block;font-size:10px;letter-spacing:0.14em;color:#c9a84c;border:1px solid rgba(201,168,76,0.3);padding:5px 11px;border-radius:2px;margin:0 5px 5px 0">${s.trim()}</span>`).join("")}</div>
  </div>

  <!-- Respuestas por área -->
  <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:3px;padding:26px;margin-bottom:28px">
    <div style="font-size:9px;letter-spacing:0.28em;text-transform:uppercase;color:#c9a84c;margin-bottom:18px">Respuestas completas por área</div>
    ${areasHTML}
  </div>

  <!-- CTA -->
  <div style="text-align:center">
    <a href="https://calendly.com/cristhiam-silva-crsgrowth/30min"
       style="display:inline-block;background:linear-gradient(135deg,#c9a84c,#e8c96a,#c9a84c);color:#0d0d10;text-decoration:none;padding:14px 34px;font-size:10px;letter-spacing:0.22em;text-transform:uppercase;font-weight:bold;border-radius:3px">
      Preparar Kick-off con ${d.nombre} →
    </a>
    <p style="font-size:10px;color:#6a6258;margin-top:12px;letter-spacing:0.08em">
      Email generado automáticamente · CRS Consulting · crsgrowth.com
    </p>
  </div>

</div>
</body></html>`;

  MailApp.sendEmail({
    to:       EMAIL_CRS,
    subject:  `${ASUNTO_PRE}${d.empresa||"—"} [${d.nivel} · ${d.puntuacion}/36]`,
    htmlBody: html
  });
}

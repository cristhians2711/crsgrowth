# CRS Growth — Guía de Despliegue v2

## Antes de empezar: backup obligatorio

```bash
# En tu máquina local, dentro del repositorio:
git checkout -b backup-pre-v2
git add -A
git commit -m "backup: estado anterior al rediseño v2"
git push origin backup-pre-v2
```

Esto crea una rama de seguridad. Si algo falla, puedes volver en 30 segundos.

---

## Estructura de archivos a subir

```
crsgrowth/
├── css/
│   └── styles.css          ← NUEVO (reemplaza el anterior)
├── js/
│   └── main.js             ← Sin cambios (preservado exacto)
├── components/
│   ├── nav.html            ← ACTUALIZADO (añade ★ Constitución)
│   └── footer.html         ← ACTUALIZADO (añade Constitución + WhatsApp)
├── constitucion/
│   └── index.html          ← NUEVO
├── index.html              ← NUEVO (homepage rediseñado)
├── servicios/index.html    ← NUEVO
├── nosotros/index.html     ← ACTUALIZADO
├── contacto/index.html     ← ACTUALIZADO
├── realestate/index.html   ← Nav/footer actualizados, contenido preservado
├── diagnostico/index.html  ← Nav/footer actualizados, SCRIPT PRESERVADO INTACTO
├── aviso-legal/index.html  ← Nav/footer actualizados
├── privacidad/index.html   ← Nav/footer actualizados
├── cookies/index.html      ← Nav/footer actualizados
├── 404.html                ← ACTUALIZADO al nuevo diseño
├── firma.html              ← Sin cambios
├── sitemap.xml             ← ACTUALIZADO (constitución con priority 1.0)
├── robots.txt              ← Sin cambios
├── logo.png                ← Sin cambios
├── CNAME                   ← Sin cambios (www.crsgrowth.com)
└── backend-google-apps-script/  ← Sin cambios
```

---

## Paso a paso: subir a GitHub

### Opción A — GitHub Desktop (recomendado si no usas terminal)

1. Abre GitHub Desktop
2. Selecciona el repositorio `crsgrowth`
3. Arrastra y suelta todos los archivos del ZIP sobre la carpeta del repositorio
   - Cuando te pregunte, selecciona **"Reemplazar"** para todos los archivos existentes
4. En GitHub Desktop verás todos los cambios en la columna izquierda
5. En el campo "Summary" escribe: `feat: rediseño completo v2 + landing constitución`
6. Haz clic en **"Commit to main"**
7. Haz clic en **"Push origin"**
8. Espera 2-3 minutos y visita https://www.crsgrowth.com para verificar

### Opción B — Terminal (git)

```bash
# 1. Ve a la carpeta del repositorio
cd ruta/a/tu/repositorio/crsgrowth

# 2. Crea rama de backup primero (OBLIGATORIO)
git checkout -b backup-pre-v2
git add -A && git commit -m "backup: estado anterior al rediseño v2"
git push origin backup-pre-v2

# 3. Vuelve a main
git checkout main

# 4. Copia todos los archivos del ZIP encima del repositorio
# (hazlo manualmente desde el Finder o con cp -r)

# 5. Añade todos los cambios
git add -A

# 6. Revisa qué va a subir (opcional pero recomendado)
git status

# 7. Commit
git commit -m "feat: rediseño completo v2 — hero centrado, servicio estrella constitución, nav unificada, sistema de componentes limpio"

# 8. Push
git push origin main
```

---

## Verificación post-despliegue (checklist)

Después de publicar, verifica estas URLs en orden:

| URL | Qué comprobar |
|-----|--------------|
| https://www.crsgrowth.com | Hero centrado, ticker, sección Constitución estrella |
| https://www.crsgrowth.com/constitucion/ | Landing completa, hero oscuro, 8 trámites |
| https://www.crsgrowth.com/servicios/ | Card estrella de constitución arriba |
| https://www.crsgrowth.com/diagnostico/ | Formulario funciona, resultado aparece |
| https://www.crsgrowth.com/nosotros/ | Hero unificado correcto |
| https://www.crsgrowth.com/contacto/ | Formulario envía correctamente |
| https://www.crsgrowth.com/realestate/ | Contenido preservado |
| https://www.crsgrowth.com/aviso-legal/ | Carga sin errores |
| https://www.crsgrowth.com/404-test-xyz | Página 404 personalizada |

**Nav:** Comprobar que "★ Constitución" aparece en dorado en todas las páginas.

**Diagnóstico:** Rellenar el formulario completo y verificar que:
- El resultado aparece correctamente
- Llega un email a cristhiam.silva@crsgrowth.com
- El dato se registra en Google Sheets

---

## Si algo falla: cómo revertir en 30 segundos

```bash
git checkout backup-pre-v2
git checkout -b main-temp
git branch -D main
git branch -m main
git push origin main --force
```

O desde GitHub.com: Settings → Branches → restaurar desde `backup-pre-v2`.

---

## Archivos que NO debes borrar del repositorio original

Estos archivos del repositorio anterior no están en el ZIP pero deben mantenerse si existen:
- `.github/` (configuración de GitHub Actions si existe)
- Cualquier imagen o asset en subcarpetas que no sea logo.png

---

## Notas técnicas

**¿Por qué no hay react/webpack?**
El sitio es HTML estático puro, desplegado en GitHub Pages. No requiere build process. Los cambios se publican directamente al hacer push.

**Sistema de componentes**
Nav y footer se cargan dinámicamente desde `/components/nav.html` y `/components/footer.html` vía fetch en `main.js`. Para actualizar el nav en toda la web, solo editas ese archivo.

**Diagnóstico / Apps Script**
El script de Google Apps Script NO se modifica. La URL `https://script.google.com/macros/s/AKfycbxi7m.../exec` está hardcodeada en `diagnostico/index.html` y funciona igual que antes.

**DNS**
El `CNAME` apunta a `www.crsgrowth.com`. No tocar.

---

*CRS Growth · rediseño v2 · junio 2026*

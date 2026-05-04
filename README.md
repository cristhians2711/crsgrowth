# CRS Consulting — estructura final

## Qué contiene
- Todas las secciones principales están como carpetas con `index.html`:
  - `/servicios/`
  - `/nosotros/`
  - `/realestate/`
  - `/contacto/`
  - `/aviso-legal/`
  - `/privacidad/`
  - `/cookies/`
- La home queda en `/index.html`.
- Los antiguos `.html` de raíz quedan como redirecciones para no romper enlaces.
- Todo usa el mismo `style.css`, `main.js`, navegación, footer y logo `logo.png`.
- Real Estate usa “Valoración”, no “Diagnóstico”.
- El logo se carga siempre como archivo `logo.png`, sin base64 ni fondo negro incrustado.

## Cómo subirlo
1. En GitHub, elimina o sustituye los archivos antiguos de raíz.
2. Sube el contenido de esta carpeta a la raíz del repositorio.
3. Asegúrate de que `index.html`, `style.css`, `main.js`, `logo.png`, `CNAME`, `robots.txt` y `sitemap.xml` quedan en raíz.
4. Las carpetas `/servicios`, `/nosotros`, `/realestate`, `/contacto`, `/aviso-legal`, `/privacidad` y `/cookies` deben quedar también en raíz.


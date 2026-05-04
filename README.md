# CRS Growth / CRS Consulting — GitHub Pages listo

## Estructura
- `/index.html` — página principal
- `/servicios.html`
- `/nosotros.html`
- `/contacto.html`
- `/realestate/index.html` — URL pública: `https://www.crsgrowth.com/realestate/`
- `/diagnostico/index.html` — URL pública: `https://www.crsgrowth.com/diagnostico/`
- `/aviso-legal.html`
- `/privacidad.html`
- `/cookies.html`
- `/firma.html`
- `/logo.png`
- `/CNAME`
- `/robots.txt`
- `/sitemap.xml`

## Subida a GitHub Pages
1. Entra en el repositorio de la web.
2. Borra o reemplaza los archivos antiguos.
3. Sube todo el contenido de esta carpeta a la raíz del repositorio.
4. Comprueba que `index.html`, `logo.png`, `CNAME`, `robots.txt` y `sitemap.xml` quedan en la raíz.
5. En GitHub: Settings > Pages.
6. Source: Deploy from branch.
7. Branch: `main` / folder `/root`.
8. En Custom domain usa: `www.crsgrowth.com`.

## DNS recomendado
En el proveedor del dominio:
- CNAME: `www` → `TU-USUARIO.github.io`
- Si quieres usar dominio raíz sin www, añade los A records oficiales de GitHub Pages.

## Cambios aplicados
- Calendly actualizado: `https://calendly.com/cristhiam-silva-crsgrowth/30min`
- Logo unificado: `logo.png`
- Real Estate pasa de "diagnóstico" a "valoración" solo en esa página.
- Real Estate queda como carpeta para funcionar en `/realestate/`.
- Diagnóstico queda como carpeta para funcionar en `/diagnostico/`.
- Enlaces internos normalizados.

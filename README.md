# crsgrowth.com — v4 (noviembre 2026)

Web estática para GitHub Pages. Sin dependencias ni proceso de compilación.

## Estructura
- `/` Inicio CRS Growth (dirección y gestión de empresas)
- `/constitucion/` Constitución de empresas + formulario de presupuesto
- `/cristhiamsilva/` Acompañamiento personal · `/cristhiamsilva/confiaenti/` cuestionario (5 preguntas)
- `/contacto/` Contacto · `/aviso-legal/` `/privacidad/` `/cookies/`
- `css/site.css` y `js/site.js`: una sola hoja de estilos y un solo script para todo el sitio
- `fonts/archivo.woff2`: tipografía alojada en el propio dominio (licencia OFL)
- Redirecciones de URLs antiguas: /servicios/, /nosotros/, /paquetes/, /enterprise/, /diagnostico/, /realestate/ → inicio; /start/ → /constitucion/

## Formularios
Todos envían a Web3Forms con la clave ya existente. Llegan al email con el que se creó esa clave.

## Editar textos
Los textos están en `_paginas.py`. Tras editar, ejecutar `python3 _build.py` y subir los cambios.
(También se puede editar el HTML directamente si es un cambio pequeño.)

## Publicar
Sustituir el contenido del repositorio por esta carpeta (conservando `.git`), commit y push a `main`.
Hacer antes una rama de copia: `git checkout -b backup-v3 && git push origin backup-v3 && git checkout main`.

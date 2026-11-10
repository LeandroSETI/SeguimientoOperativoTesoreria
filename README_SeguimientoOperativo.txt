INFORME SEMANAL CaaS TESORERÍA

Archivos requeridos en la misma carpeta:
- SeguimientoOperativo.html
- Contexto_HAs_JSON.json
- Generar_Seguimiento_PDF.py
- generar_pdf.bat
- Logo-SETI.png
- bancolombia-s-a-logo-png_seeklogo-402324.png

Generar el informe con los datos activos:
1. Actualiza Contexto_HAs_JSON.json.
2. Ejecuta generar_pdf.bat.

El PDF usa el número de Sprint y la fecha_corte del JSON. El nombre tiene
el formato:
Informe semanal CaaS Tesoreria_Sprint[NUMERO]_[DD-MM-YYYY]_001.pdf

Si el archivo ya existe, se crea el siguiente consecutivo sin sobrescribirlo.
El script usa primero el Python del entorno .venv del proyecto.

Para validar el diseño con los datos de ejemplo:
  .venv\Scripts\python.exe Generar_Seguimiento_PDF.py --json Contexto_HAs_JSON_Ejemplo.json

El JSON de ejemplo se carga directamente y no reemplaza ni modifica
Contexto_HAs_JSON.json.

Primera instalación:
- Instala Python 3.12.
- pip install playwright
- playwright install chromium

Vista HTML:
El HTML debe servirse desde un servidor local para permitir la carga dinámica
del JSON. No se recomienda abrirlo con doble clic.

  .venv\Scripts\python.exe servir_seguimiento.py --open

Luego, si no se abre automáticamente, visita:
  http://127.0.0.1:8000/SeguimientoOperativo.html

El reporte se actualiza al detectar cambios en el JSON. Los campos opcionales
ausentes se muestran como no informados o se omiten, según la sección. Las
células, épicas y valores se leen del JSON; no se infieren desde descripciones.

El Anexo Ejecutivo agrupa los elementos por épica y célula e incluye solamente
HU/HA operativas. No muestra tareas ni tareas sintéticas.

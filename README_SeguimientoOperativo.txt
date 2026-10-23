PAQUETE DE SEGUIMIENTO OPERATIVO

Archivos requeridos en la misma carpeta:
- SeguimientoOperativo.html
- Contexto_HAs_JSON.json
- Generar_Seguimiento_PDF.py
- generar_pdf.bat
- Logo-SETI.png
- bancolombia-s-a-logo-png_seeklogo-402324.png

Flujo:
1. Actualiza Contexto_HAs_JSON.json.
   El HTML también carga Contexto_HAs_JSON_Ejemplo.json cuando el archivo principal todavía no existe.
   Mientras el reporte está abierto, consulta cambios del JSON cada 5 segundos.
   `epica_proyecto` acepta tanto un texto como un objeto con la propiedad `nombre`.
2. Ejecuta generar_pdf.bat (o py -3.12 Generar_Seguimiento_PDF.py).
3. Se genera un PDF con el número de sprint del JSON y un consecutivo para no sobrescribir reportes anteriores, por ejemplo:
   Reporte Seguimiento Operativo 255_001.pdf, Reporte Seguimiento Operativo 255_002.pdf.

Primera instalación:
- pip install playwright
- playwright install chromium

Nota: abrir el HTML con doble clic puede bloquear la carga del JSON por seguridad del navegador. Para que el reporte se actualice automáticamente, debe abrirse desde un servidor local. Usa una de estas opciones:
- python servir_seguimiento.py
- python -m http.server 8000
Luego abre: http://127.0.0.1:8000/SeguimientoOperativo.html

El script Python de PDF también levanta un servidor local automáticamente y evita ese problema.
El título del reporte y el nombre predeterminado del PDF usan el formato `Reporte Seguimiento Operativo %Sprint%`, reemplazando `%Sprint%` por el número del sprint.

Novedades ejecutivas
- El campo opcional `novedades_ejecutivas` permite mostrar novedades ejecutivas en el reporte y PDF.
- Puede omitirse completamente o existir como `"novedades_ejecutivas": []`; en ambos casos no se dibuja la sección.
- Cada elemento puede incluir `ha_hu` y `descripcion`; los elementos sin ambos datos se ignoran.

Ejemplo:
  "novedades_ejecutivas": [
    {
      "ha_hu": 7860649,
      "descripcion": "HU trasladada al siguiente Sprint para su continuación y cierre."
    }
  ]

Novedades de seguimiento
- El campo opcional `novedades` está disponible en `Contexto_HAs_JSON.json`.
- Puede omitirse completamente.
- También puede existir como `"novedades": []`.
- Si no contiene elementos, el HTML y el PDF no muestran la sección.
- Si contiene elementos, el HTML genera las tarjetas automáticamente sin editar manualmente el HTML.
- El comando actual para generar el PDF no cambia.

Ejemplo mínimo:
  "novedades": []

Ejemplo con una novedad:
  "novedades": [
    {
      "id": "NOV-001",
      "fecha": "06/10/2026",
      "categoria": "DEPENDENCIA EXTERNA",
      "item_relacionado": "7868791",
      "titulo": "HA trasladada por dependencia externa",
      "descripcion": "La HA quedó pendiente por dependencia externa.",
      "impacto": "No pudo completarse dentro del Sprint.",
      "dependencias": ["Ultron"],
      "estado": "ABIERTA",
      "proximo_paso": "Completar la dependencia y continuar con la actividad.",
      "traslada_sprint": true,
      "sprint_destino": 255
    }
  ]

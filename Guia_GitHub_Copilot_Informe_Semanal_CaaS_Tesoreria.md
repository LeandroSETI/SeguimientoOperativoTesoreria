# Guía maestra para evolucionar el Informe Semanal

**Implementación asistida con GitHub Copilot - CaaS Tesorería**

> **Propósito:** documento editable listo para entregar a GitHub Copilot en modo **Agent**. Contiene referencias, reglas funcionales, estructura JSON, cálculos, validaciones, pruebas y criterios visuales para modificar el programa completo sin perder compatibilidad.

## Resultado esperado

El proceso local debe continuar funcionando mediante `generar_pdf.bat` y producir un PDF dinámico con el nombre:

```text
Informe semanal CaaS Tesoreria_Sprint[NUMERO]_[DD-MM-YYYY].pdf
```

El programa debe conservar los reportes históricos, no sobrescribir archivos existentes y ejecutar el flujo completo:

```text
metricas_celula.json
+
Contexto_Manual_Sprint_CaaS.txt
        ↓
Contexto_HAs_JSON.json
        ↓
SeguimientoOperativo.html
        ↓
Generar_Seguimiento_PDF.py
        ↓
generar_pdf.bat
        ↓
Informe semanal PDF
```

---

# 1. Archivos que deben estar en el workspace

| Archivo | Uso esperado |
|---|---|
| `SeguimientoOperativo.html` | Plantilla dinámica, estilos, secciones y renderizado del JSON. |
| `Generar_Seguimiento_PDF.py` | Servidor local, Playwright, validación, espera de render y producción del PDF. |
| `generar_pdf.bat` / `abrir_seguimiento.bat` | Ejecución sencilla en Windows y manejo de errores. |
| `servir_seguimiento.py` | Vista previa opcional desde servidor local. |
| `Contexto_HAs_JSON.json` | Datos reales del Sprint. |
| `Contexto_HAs_JSON_Ejemplo.json` | Prueba integral DEMO de todas las secciones y casos límite. |
| `Contexto_Manual_Sprint_CaaS.txt` | Contexto manual que Azure DevOps no contiene. |
| `Informe_semanal_CaaS_Tesoreria_03-11-26_PROPUESTA.pdf` | Referencia visual. No usar sus datos simulados como información real. |
| `Logo-SETI.png` y logo de Bancolombia | Identidad visual local sin dependencias de Internet. |
| `README_SeguimientoOperativo.txt` | Tutorial práctico actualizado. |

---

# 2. Checklist antes de activar GitHub Copilot

1. Crear un respaldo con Git:

   ```bash
   git init
   git add .
   git commit -m "Respaldo antes de evolucionar informe semanal"
   ```

2. Ejecutar el `generar_pdf.bat` actual y confirmar que el programa funciona antes de modificarlo.
3. Abrir en Visual Studio Code la carpeta completa del proyecto, no solamente el HTML.
4. Poner el PDF visual de referencia, el JSON DEMO y el contexto manual en la misma carpeta.
5. Abrir GitHub Copilot Chat en modo **Agent**.
6. Adjuntar el PDF de referencia e indicar: **“Reproduce el diseño, no sus datos.”**
7. Pegar únicamente el prompt consolidado de este documento.
8. Permitir que GitHub Copilot inspeccione el proyecto antes de aceptar cambios.
9. Exigir la ejecución real de `generar_pdf.bat`, la generación del PDF y su revisión visual.
10. Probar después un JSON histórico para validar compatibilidad.

> **Prueba crítica:** dos HU/HA comprometidas, una completada y una trasladada por mala estimación deben producir **50% de cumplimiento**, no 100%.

---

# 3. Prompt maestro consolidado para GitHub Copilot

Copia desde aquí hasta el final de esta sección y pégalo completo en GitHub Copilot Chat, modo **Agent**.

---

## ROL Y OBJETIVO

ACTÚA COMO DESARROLLADOR SENIOR PYTHON, HTML, CSS, JAVASCRIPT Y PLAYWRIGHT, ESPECIALIZADO EN GENERACIÓN AUTOMATIZADA DE REPORTES PDF.

Analiza el workspace completo y modifica directamente los archivos necesarios para evolucionar el programa del Informe Semanal CaaS Tesorería.

Conserva:

- la arquitectura útil existente;
- la compatibilidad con JSON históricos;
- la ejecución mediante `generar_pdf.bat`;
- los PDF históricos sin modificarlos.

No entregues solo sugerencias. Debes:

1. inspeccionar;
2. implementar;
3. ejecutar;
4. probar;
5. generar el PDF;
6. revisarlo visualmente;
7. corregir los errores encontrados;
8. documentar los cambios.

## REFERENCIA VISUAL

Usa `Informe_semanal_CaaS_Tesoreria_03-11-26_PROPUESTA.pdf` como **DISEÑO OBJETIVO**.

Prioridad:

1. `Contexto_HAs_JSON.json` define los **datos**.
2. Este prompt define el **comportamiento**.
3. El PDF de referencia define el **diseño visual**.

Reproduce:

- jerarquía;
- márgenes;
- paleta de colores;
- tablas;
- indicadores;
- semáforos;
- encabezados;
- pies de página;
- espaciados;
- paginación.

No copies los datos simulados del PDF.

## INSPECCIÓN PREVIA OBLIGATORIA

Antes de editar:

1. Identifica cómo el HTML carga el JSON.
2. Identifica cómo Python levanta el servidor local.
3. Identifica cómo Playwright espera el renderizado.
4. Identifica cómo se construye el nombre del PDF.
5. Revisa cómo funcionan los archivos BAT.
6. Revisa el CSS de impresión.
7. Revisa cómo se cargan los logos.
8. Revisa qué campos históricos consume el programa.
9. Identifica dependencias entre HTML, JavaScript, Python, BAT y servidor.
10. Conserva los comportamientos que siguen siendo útiles.

No asumas estructuras que puedas inspeccionar.

## MODELO CONCEPTUAL

Diferencia estrictamente:

1. **Items operativos:** qué HU/HA forman parte de la vista operativa actual.
2. **Avance de ejecución:** cuánto ha avanzado técnicamente el trabajo.
3. **Cumplimiento del Sprint:** cuánto del compromiso formal fue completado.
4. **Valor generado:** qué capacidad técnica o funcional quedó materializada.

Ninguno sustituye a otro.

El avance ponderado usa tareas y Story Points.

El cumplimiento usa la línea base del compromiso.

La clasificación de valor usa evidencia de capacidad materializada.

## FILTRO DE ITEMS

En `items` incluir y mostrar únicamente HU/HA cuyo estado administrativo sea:

- `Active`
- `Closed`

Excluir HU/HA `New` de:

- tarjetas;
- conteo operativo;
- Story Points operativos;
- avance individual;
- avance ponderado.

Una HU/HA `Active` sí puede contener tareas `New`, `Active` o `Closed`. No eliminar esas tareas del cálculo interno.

## REGLA CLOSED

Para el medidor operativo, toda HU/HA `Closed` se representa al **100%**.

Si no tiene tareas suficientes, se permite una tarea sintética:

```json
{
  "id": null,
  "nombre": "Tarea sintética para cálculo de avance de HU/HA cerrada",
  "estado": "Closed",
  "origen": "REGLA_CIERRE_100_PORCIENTO"
}
```

La tarea sintética:

- se utiliza únicamente para cálculo;
- no representa una actividad real;
- nunca debe aparecer en el PDF.

`Closed = 100%` no implica automáticamente:

- Valor Funcional;
- DoD cumplido;
- criterios de aceptación cumplidos;
- cumplimiento oficial del Sprint.

## REGLA ACTIVE

Para `Active` calcular:

```text
Avance = tareas Closed / total de tareas × 100
```

Cuando exista información suficiente.

Si hay tareas, pero ninguna está cerrada:

```text
Avance = 0%
```

Esto no significa que no exista actividad. El contexto puede indicar que el desarrollo está en ejecución.

Si no existe información suficiente, mostrar:

```text
Información insuficiente para calcular avance
```

Nunca producir `NaN`.

## AVANCE PONDERADO

Calcular:

```text
Σ(avance HU/HA × Story Points)
--------------------------------
Σ(Story Points incluidos)
```

Excluir solamente del cálculo de avance los elementos sin Story Points válidos o sin avance calculable.

Si existen exclusiones, mostrar:

```text
AVANCE PONDERADO PARCIAL
```

E indicar:

- Story Points totales;
- Story Points incluidos;
- elementos incluidos;
- elementos excluidos.

## CUMPLIMIENTO DEL SPRINT

Usar exclusivamente:

```text
Completados
------------------------------------------ × 100
Comprometidos - Impedimentos cliente
```

Umbrales:

- objetivo: `>= 90%`;
- mínimo: `85%`.

No calcular cumplimiento desde:

- `items` actuales;
- avance ponderado;
- Story Points;
- elementos que todavía permanecen visibles;
- traslados restados automáticamente.

Crear y usar:

```text
cumplimiento_sprint.items_comprometidos
```

como fotografía histórica del compromiso formal.

## LÍNEA BASE Y TRASLADOS

Una HU/HA comprometida permanece en `items_comprometidos` aunque:

- sea trasladada;
- cambie su Iteration Path;
- desaparezca de la extracción final;
- desaparezca de `items`;
- quede pendiente al cierre.

Puede salir de `items` y aparecer en `novedades_ejecutivas`, pero continúa dentro del denominador del Sprint original.

Un traslado no equivale a impedimento cliente.

No excluyen del KPI:

- mala estimación;
- retraso atribuible a SETI;
- trabajo no terminado;
- retrabajo;
- deuda técnica;
- Issues de Sonar atribuibles a ejecución;
- pruebas pendientes atribuibles al equipo;
- despliegue no ejecutado por causas internas.

## IMPEDIMENTOS CLIENTE

Solo descontar un elemento del denominador cuando:

```text
impedimento_cliente = true
excluido_kpi = true
evidencia_impedimento tiene contenido
```

Posibles casos, siempre con evidencia:

- ambiente cliente no disponible;
- retraso de acceso;
- cambio de alcance del negocio;
- integración con tercero atribuible al cliente;
- autorización pendiente del cliente;
- prerrequisito cliente incumplido.

Una dependencia, bloqueo o traslado no son automáticamente impedimento cliente.

Si falta evidencia:

- no excluir;
- establecer o conservar `excluido_kpi = false`;
- generar una advertencia clara.

## REPLANIFICACIÓN FORMAL

La línea base solamente puede cambiar con evidencia de una replanificación formal acordada.

Registrar:

- elemento que sale;
- elemento que entra;
- motivo;
- evidencia;
- fecha, si está disponible;
- participantes, si están informados.

No modificar silenciosamente el compromiso original.

## ESTADOS DEL KPI

Al cierre:

| Resultado | Estado |
|---:|---|
| `>= 90%` | CUMPLIDO |
| `85% a <90%` | RIESGO / MEJORA |
| `<85%` | INCUMPLIMIENTO |

Durante el Sprint mostrar:

```text
EN CURSO
```

O:

```text
PENDIENTE DE CIERRE
```

Si no existe línea base confiable:

```text
INFORMACIÓN INSUFICIENTE
```

No inventar porcentaje.

## CÉLULA ORIGEN Y ÉPICA

`CaaS Tesorería` es el servicio transversal ejecutor.

`item.celula` representa la célula origen del backlog:

- Rocket;
- Flintstones;
- Eagle.

Normalizar capitalización, pero no inferir la célula mediante términos como:

- MAC;
- MPT;
- frontend;
- microservicio;
- nombre de la HU/HA;
- patrones históricos.

Si falta la célula, mostrar:

```text
NO INFORMADA
```

Si aparece una célula futura o desconocida:

- conservar el valor;
- emitir advertencia;
- continuar generando el PDF.

`epica_proyecto` identifica la iniciativa.

Si falta, mostrar:

```text
ÉPICA / INICIATIVA NO INFORMADA
```

No inferir la épica.

## ESTRUCTURA DEL PDF

Orden recomendado:

1. Encabezado e información general.
2. Lo más importante.
3. Resumen ejecutivo.
4. Capacidad atendida por célula origen.
5. Iniciativas y épicas atendidas.
6. Avances con desviación.
7. Valor esperado.
8. Hitos.
9. Riesgos e impedimentos.
10. Compromisos.
11. Anexo ejecutivo agrupado por épica, célula y HU/HA.
12. Información insuficiente, cuando aplique.

Ocultar completamente las secciones vacías.

## RESUMEN EJECUTIVO

Mostrar:

- avance operativo;
- cumplimiento del Sprint;
- Story Points operativos;
- HU/HA operativas;
- comprometidos;
- completados;
- trasladados;
- impedimentos cliente validados;
- semáforo general.

Mostrar únicamente cuando exista información:

- logro principal;
- desviación crítica;
- decisión requerida;
- entregas principales;
- impacto sobre la fecha final.

## DISTRIBUCIÓN DE CAPACIDAD

Calcular desde `items`:

```text
Célula origen | Cantidad HU/HA | SP totales | SP Closed | SP Active
```

Agrupar también por:

```text
epica_proyecto + celula
```

para mostrar las iniciativas atendidas.

Estas cifras operativas no sustituyen la línea base de cumplimiento.

## SEMÁFORO

Usar `item.semaforo` cuando exista.

Valores permitidos:

- `VERDE`
- `AMARILLO`
- `ROJO`
- `SIN INFORMACIÓN`

Derivación permitida:

- **ROJO:** bloqueo o decisión/apoyo crítico comprobado.
- **AMARILLO:** desviación, traslado, dependencia o recuperación.
- **VERDE:** `Closed` o ausencia de desviaciones y riesgos.
- **SIN INFORMACIÓN:** evidencia insuficiente.

No marcar rojo solamente por bajo avance.

No confundir semáforo con clasificación de valor.

## RIESGOS, HITOS Y COMPROMISOS

Riesgos e impedimentos deben mostrar:

- tipo;
- HA/HU;
- célula;
- épica;
- descripción;
- impacto;
- mitigación;
- responsable;
- fecha;
- estado.

Diferenciar:

- dependencia;
- bloqueo;
- riesgo.

Los hitos solo se muestran cuando son explícitos:

- CUMPLIDO;
- RETRASADO;
- PLANIFICADO.

Los compromisos no son tareas de Azure DevOps. Deben incluir responsable y fecha solo cuando estén informados.

## ANEXO EJECUTIVO

Agrupar por:

```text
Épica / iniciativa
        ↓
Célula origen
        ↓
HU/HA
```

Mostrar por HU/HA:

- ID;
- tipo;
- nombre;
- célula;
- épica;
- Story Points;
- clasificación;
- estado;
- avance;
- valor generado;
- próximo paso;
- semáforo.

No mostrar:

- tareas;
- IDs de tareas;
- tareas sintéticas;
- detalle interno del cálculo.

## NOMBRE Y VERSIONADO

Generar:

```text
Informe semanal CaaS Tesoreria_Sprint[NUMERO]_[DD-MM-YYYY].pdf
```

Reglas:

- el número viene de `sprint.numero`;
- la fecha es la fecha real de generación;
- no utilizar `fecha_corte` en el nombre;
- si existe el archivo, crear `_001`, `_002`, etc.;
- no sobrescribir;
- no renombrar archivos históricos;
- detener con error claro si falta `sprint.numero`.

## PLAYWRIGHT Y SERVIDOR

`Generar_Seguimiento_PDF.py` debe:

1. iniciar el servidor local;
2. esperar su disponibilidad;
3. cargar HTML, JSON e imágenes;
4. esperar que el JavaScript termine;
5. esperar:

   ```javascript
   window.REPORTE_LISTO === true
   ```

6. imprimir en A4 con fondos habilitados;
7. cerrar navegador y servidor incluso ante errores;
8. devolver código de salida distinto de cero cuando falle.

La vista previa mediante `servir_seguimiento.py` es opcional y no debe ser requisito para generar el PDF.

## CSS DE IMPRESIÓN

Usar A4 y márgenes coherentes:

```css
@page {
  size: A4;
  margin: 12mm 12mm 15mm 12mm;
}
```

Agregar o validar:

```css
print-color-adjust: exact;
-webkit-print-color-adjust: exact;

thead {
  display: table-header-group;
}

tfoot {
  display: table-footer-group;
}
```

Controlar saltos de página sin provocar páginas vacías.

Evitar:

- texto cortado;
- títulos aislados;
- tablas fuera del margen;
- pies superpuestos;
- cajas demasiado grandes que no puedan dividirse.

Pie requerido:

```text
SETI | CaaS Tesorería | Informe semanal | Número de página
```

## COMPATIBILIDAD HACIA ATRÁS

Aceptar JSON históricos con valores predeterminados seguros.

Si faltan:

- `resumen_ejecutivo`;
- `cumplimiento_sprint`;
- `hitos`;
- `riesgos_identificados`;
- `compromisos`;
- `valor_esperado`;

el programa no debe fallar.

Debe ocultar las secciones vacías.

Si falta `cumplimiento_sprint`, mostrar:

```text
Pendiente de cálculo
```

No reconstruir el KPI desde `items` actuales.

Nunca mostrar:

- `undefined`;
- `null`;
- `NaN`.

## SEGURIDAD Y CALIDAD

- Escapar todo texto proveniente del JSON.
- Evitar `innerHTML` sin saneamiento.
- Usar UTF-8.
- No ejecutar HTML arbitrario del JSON.
- No depender de Internet.
- Utilizar solamente archivos locales.
- No modificar PDF históricos.
- No inventar célula, épica, fechas, responsables, compromisos o impactos.

## PRUEBAS OBLIGATORIAS

Probar como mínimo:

1. JSON extendido completo.
2. JSON histórico.
3. Listas opcionales vacías.
4. `Closed` sin tareas.
5. `Active` con tareas activas.
6. Avance insuficiente.
7. Nombre de PDF repetido.
8. Caracteres especiales.
9. Célula vacía.
10. Célula futura desconocida.
11. Épica vacía.
12. Varias épicas para una célula.
13. Misma épica para varias células.
14. Traslado fuera de `items` pero dentro del KPI.

Casos obligatorios del KPI:

| Caso | Datos | Resultado |
|---|---|---:|
| A | 2 comprometidas, 2 completadas, 0 impedimentos | 100% |
| B | 2 comprometidas, 1 completada, 1 trasladada por mala estimación | 50% |
| C | 2 comprometidas, 1 completada, 1 impedimento cliente documentado | 100% |
| D | Impedimento cliente sin evidencia | No excluir y emitir advertencia |
| E | Extracción final muestra una Closed, línea base conserva dos comprometidas | 50%, no 100% |
| F | No existe línea base confiable | INFORMACIÓN INSUFICIENTE |

## README Y ENTREGA

Actualizar el README con:

- requisitos;
- instalación de Python;
- instalación de Playwright;
- flujo del proceso;
- estructura JSON;
- célula origen;
- épica;
- avance;
- cumplimiento;
- línea base;
- traslados;
- impedimentos cliente;
- nombre del PDF;
- consecutivos;
- ejecución mediante BAT;
- vista previa;
- solución de problemas.

Al finalizar, reportar:

1. archivos modificados;
2. cambios realizados por archivo;
3. estructura JSON soportada;
4. pruebas realizadas;
5. resultado de los casos KPI;
6. ruta del PDF generado;
7. advertencias pendientes;
8. compatibilidad con JSON históricos;
9. instrucción exacta para ejecutar el reporte.

## CRITERIO FINAL

No terminar solamente porque el HTML abre o Python no falla.

El trabajo se considera terminado cuando:

```text
generar_pdf.bat
        ↓
genera correctamente
        ↓
Informe semanal CaaS Tesoreria_Sprint[NUMERO]_[DD-MM-YYYY].pdf
```

Y además:

- el resultado es visualmente equivalente a la referencia;
- utiliza datos dinámicos;
- no presenta recortes;
- no muestra secciones vacías;
- conserva compatibilidad histórica;
- la prueba crítica del traslado devuelve 50%, no 100%;
- una HU/HA trasladada no desaparece de la línea base;
- ningún impedimento cliente se descuenta sin evidencia;
- las células y épicas son visibles;
- las tareas sintéticas no aparecen;
- los elementos `New` no aparecen como items operativos.

---

# 4. Estructura JSON extendida de referencia

```json
{
  "sprint": {
    "numero": 257,
    "periodo": "",
    "fecha_corte": "",
    "proyecto": "CaaS Tesorería",
    "servicio": "EVC Tesorería Bancolombia",
    "project_manager": ""
  },
  "resumen_ejecutivo": {
    "avance_real": null,
    "cumplimiento_sprint": null,
    "semaforo_general": "",
    "logro_principal": "",
    "desviacion_critica": "",
    "decision_requerida": ""
  },
  "cumplimiento_sprint": {
    "estado": "EN CURSO",
    "items_comprometidos": [
      {
        "ha_hu": 1001,
        "story_points": 5,
        "estado_cierre": "COMPLETADO",
        "trasladado": false,
        "sprint_destino": null,
        "motivo_traslado": "",
        "impedimento_cliente": false,
        "evidencia_impedimento": "",
        "excluido_kpi": false
      }
    ],
    "comprometidos": null,
    "completados": null,
    "trasladados": null,
    "impedimentos_cliente": null,
    "denominador_kpi": null,
    "porcentaje": null,
    "estado_kpi": ""
  },
  "items": [],
  "novedades_ejecutivas": [],
  "valor_esperado": [],
  "hitos": [],
  "riesgos_identificados": [],
  "compromisos": [],
  "informacion_insuficiente": []
}
```

---

# 5. Revisión final antes de aceptar los cambios

- [ ] El PDF utiliza el nombre corporativo.
- [ ] Crea consecutivo sin sobrescribir.
- [ ] CaaS Tesorería aparece como servicio ejecutor.
- [ ] Rocket, Flintstones y Eagle aparecen como células origen.
- [ ] Cada HU/HA muestra claramente célula y épica.
- [ ] La distribución por célula e iniciativa se calcula desde `items`.
- [ ] Avance y cumplimiento aparecen separados.
- [ ] Una HU/HA trasladada puede salir de la vista operativa, pero permanece en la línea base del KPI.
- [ ] Los impedimentos cliente solamente se descuentan con evidencia.
- [ ] `Closed` aparece al 100%.
- [ ] Las tareas sintéticas no aparecen.
- [ ] Las HU/HA `New` no aparecen como items operativos.
- [ ] No existen `undefined`, `null` o `NaN` visibles.
- [ ] No hay texto cortado ni tablas fuera del margen.
- [ ] No se generan páginas vacías innecesarias.
- [ ] Un JSON histórico continúa generando el PDF.
- [ ] El README explica el nuevo proceso.
- [ ] El caso 1 completada + 1 trasladada por mala estimación devuelve 50%.

## Commit final recomendado

```bash
git status
git add .
git commit -m "Nuevo informe semanal ejecutivo CaaS Tesoreria"
```

---

# 6. Principio final de gobierno

El reporte no debe hacer que el Sprint parezca mejor de lo que realmente está. Debe presentar una visión objetiva, trazable y auditable.

En particular:

- el avance ponderado no sustituye el cumplimiento;
- mover una HU/HA al siguiente Sprint no mejora el KPI anterior;
- un traslado no es un impedimento cliente;
- una exclusión del KPI necesita evidencia;
- CaaS Tesorería es la célula transversal ejecutora;
- Rocket, Flintstones y Eagle representan el origen del backlog;
- la clasificación de valor debe basarse en capacidad materializada, no solamente en el estado administrativo.

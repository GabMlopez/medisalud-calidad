# Escenario 8 — Automatización de la Medición

**Caso de estudio:** Red Hospitalaria MediSalud Ecuador  
**Norma aplicada:** ISO/IEC 25022 — Measurement of Quality in Use  
**Objetivo del Escenario:** Diseñar, implementar y verificar un pipeline de automatización bajo prácticas de Integración Continua (CI/CD) para calcular periódicamente las 5 métricas de Calidad en Uso consolidadas en el Escenario 7, exportando un reporte JSON estructurado para alimentar el visualizador.

---

## Paso 1: Desacoplamiento de Parámetros (`config.json`)

Para evitar malas prácticas de arquitectura de software, como el "hardcodeo" de umbrales de aceptación y rutas de carpetas de entrada dentro de los scripts de cálculo, se implementó un archivo de configuración centralizado en la raíz del proyecto. 

Este archivo estructura de manera independiente:
* **Umbrales de calidad:** Parámetros de control ajustables para cada una de las 5 dimensiones.
* **Rutas de datos:** Ubicaciones relativas de los datasets limpios generados en el escenario anterior.
* **Parámetros globales:** Datos operativos de control como el volumen total de transacciones estimadas de la plataforma de Telemedicina.

Esto permite que el personal de aseguramiento de la calidad (QA) o de negocio ajuste los límites de aceptación de las métricas en el sistema sin necesidad de modificar o alterar el código lógico de procesamiento en Python.

---

## Paso 2: Motor de Cálculo Lógico (`scripts/metricas_iso25022.py`)

Se desarrolló el motor de cálculo en Python que importa dinámicamente los 5 datasets del Escenario 7 mediante la librería Pandas, aplicando las fórmulas de normalización matemática correspondientes a cada dimensión de la norma **ISO/IEC 25022**:

### Matriz de Operacionalización de Métricas de Calidad en Uso

| # | Métrica Calculada | Dimensión ISO 25022 | Variable Operacionalizada | Unidad | Umbral de Aceptación |
|---|-------------------|---------------------|---------------------------|--------|----------------------|
| **1** | Tasa de precisión de tarea | Efectividad | `citas_agendadas['datos_correctos']` (Promedio) | Proporción | $\ge$ 0.85 (85%) |
| **2** | Complejidad de tarea | Eficiencia | `intentos_agendamiento['pasos']` (Promedio) | Pasos | $\le$ 3.0 pasos |
| **3** | Potencial de riesgo financiero | Libertad de Riesgo | `pagos_seguros['duplicado']` (Promedio) | Proporción | $\le$ 0.01 (1.0%) |
| **4** | Puntaje de satisfacción | Satisfacción | `encuesta_satisfaccion_telemedicina['puntaje_satisfaccion']` (Promedio) | Puntos (100) | $\ge$ 80.0 puntos |
| **5** | Rendimiento entre dispositivos | Cobertura de Contexto | Conteo consolidado de filas en `incidencias_telemedicina` | Incidencias | $\le$ 50 errores |

---

## Paso 3: Orquestación y Consolidación (`scripts/exportar_reporte.py`)

Se implementó un script exportador encargado de coordinar la ejecución del motor matemático y estructurar la salida del reporte final en un formato estándar de intercambio de información.

### Flujo de Ejecución Local
1. Comprobación y creación automática del directorio de salida (`dashboards/`).
2. Invocación de la función de cálculo de métricas para obtener los promedios reales y estados de cumplimiento (Cumple / No Cumple).
3. Agrupación y desglose de datos secundarios, como el conteo de incidentes de Cobertura de Contexto segmentado por plataforma (Android, iOS, Web).
4. Exportación y persistencia de la estructura final consolidada en el archivo estructurado de intercambio de datos: `dashboards/indicadores.json`.

---

## Paso 4: Automatización en la Nube mediante GitHub Actions

Para consolidar la infraestructura de medición continua, se configuró una receta de integración y despliegue continuos (CI/CD) ubicada en la ruta `.github/workflows/medicion_calidad.yml`. 

### Especificaciones del Pipeline de Automatización
* **Disparador Programado (Cron):** Configurado para realizar la medición de forma autónoma todos los lunes a las 06:00 UTC, garantizando reportes actualizados al inicio de cada semana laboral.
* **Disparador Manual (Workflow Dispatch):** Habilitado en la interfaz web de GitHub para permitir ejecuciones bajo demanda en cualquier momento por parte del equipo técnico.
* **Entorno de Ejecución:** Servidor virtualizado con sistema operativo Ubuntu Linux de última generación, aprovisionamiento de Python 3.11, e instalación automatizada de las dependencias lógicas Pandas y Numpy.
* **Persistencia de Entregables:** Al completarse exitosamente las tareas, el archivo de salida es empaquetado y publicado como un artefacto descargable y persistente en la plataforma de control de versiones.

---

## Preguntas de Discusión

### 1. ¿Qué ventajas ofrece programar la medición en GitHub Actions frente a ejecutarla manualmente cada trimestre?
* **Análisis Preventivo y Continuo:** Automatizar la medición con una frecuencia alta (ej. semanal) permite al equipo técnico y médico de la red hospitalaria identificar inmediatamente fallas críticas en la usabilidad de la telemedicina o picos de incidentes técnicos de forma temprana, en lugar de esperar tres meses a consolidar datos históricos cuando el impacto en los usuarios ya es grave.
* **Consistencia e Integridad:** Elimina por completo los fallos humanos asociados al cálculo manual, tales como la pérdida accidental de archivos CSV, la alteración no intencionada de fórmulas matemáticas de la ISO/IEC 25022 o la manipulación subjetiva de resultados.
* **Disponibilidad para Toma de Decisiones:** Al ejecutarse de forma constante en la nube, el archivo final de salida permanece actualizado para alimentar visualizadores gráficos automatizados sin intervención de ingenieros.

### 2. ¿Qué riesgo existe si el umbral (como el promedio de pasos o la tasa de duplicados) queda "hardcodeado" en el script en lugar de estar en un archivo de configuración externo?
* **Riesgo de Regresión en Código:** Si la red de salud decide ajustar un umbral (por ejemplo, permitir un promedio de pasos máximo de 4 temporalmente tras una actualización de diseño), modificar un valor embebido en el código de cálculo de producción obliga a alterar el código fuente del programa. Esto incrementa innecesariamente el riesgo de introducir fallos accidentales de sintaxis o lógica (bugs) en partes críticas del sistema.
* **Acoplamiento de Arquitectura:** Viola el principio de responsabilidad única de diseño de software. El script lógico debe ser responsable de procesar la matemática de la métrica, pero no de determinar qué es comercial u operativamente aceptable para el negocio. Separar los umbrales a un archivo JSON externo independiza las reglas operativas de la lógica de software.

---

## Conclusiones Parciales

Al completar este escenario se ha establecido un **pipeline industrializado, autónomo y reproducible de medición de Calidad en Uso (ISO/IEC 25022)** para la Red Hospitalaria MediSalud. El sistema procesa de forma precisa los 5 conjuntos de datos reales de telemedicina validados en el escenario anterior. La persistencia continua del reporte consolidado (`dashboards/indicadores.json`) proporciona la fuente de datos estructurada y depurada requerida para dar inicio directo al **Escenario 9**, centrado en la interfaz de visualización interactiva para la gerencia.
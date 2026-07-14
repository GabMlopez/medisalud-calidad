# Escenario 7 — Obtención de Datos

**Caso de estudio:** Red Hospitalaria MediSalud Ecuador
**Norma aplicada:** ISO/IEC 25022 — Measurement of Quality in Use

## Objetivo del Escenario

Generar y validar los conjuntos de datos base necesarios para calcular, en el Escenario 8, las 5 métricas de Calidad en Uso diseñadas previamente en el Escenario 6.

---

## Paso 1: Generación de datasets sintéticos

Se desarrollaron 5 scripts en Python (`scripts/generar_*.py`), cada uno con semilla fija (`random.seed(42)`) para garantizar reproducibilidad, generando datos simulados para 5 sedes (Quito, Guayaquil, Cuenca, Ambato, Manta) a lo largo de 5 días hábiles.

| # | Script | Archivo generado | Métrica que alimenta |
|---|---|---|---|
| 1 | `generar_citas_agendadas.py` | `data/citas_agendadas.csv` | Tasa de precisión de tarea (Efectividad) |
| 2 | `generar_intentos_agendamiento.py` | `data/intentos_agendamiento.csv` | Complejidad de tarea (Eficiencia) |
| 3 | `generar_pagos_seguros.py` | `data/pagos_seguros.csv` | Potencial de riesgo financiero (Libertad de Riesgo) |
| 4 | `generar_encuesta_satisfaccion_telemedicina.py` | `data/encuesta_satisfaccion_telemedicina.csv` | Puntaje de satisfacción (Satisfacción) |
| 5 | `generar_incidencias_telemedicina.py` | `data/incidencias_telemedicina.csv` | Rendimiento entre dispositivos (Cobertura de Contexto) |

### Estructura de columnas por archivo

**citas_agendadas.csv**
`cita_id, fecha, sede, paciente_id, datos_correctos`

**intentos_agendamiento.csv**
`intento_id, fecha, sede, usuario_id, pasos`

**pagos_seguros.csv**
`pago_id, fecha, paciente_id, aseguradora, monto, duplicado`

**encuesta_satisfaccion_telemedicina.csv**
`respuesta_id, sede, rol, puntaje_satisfaccion`

**incidencias_telemedicina.csv**
`incidencia_id, fecha, sede, plataforma, tipo_incidencia`

### Ejecución

```bash
mkdir -p data
python3 scripts/generar_citas_agendadas.py
python3 scripts/generar_intentos_agendamiento.py
python3 scripts/generar_pagos_seguros.py
python3 scripts/generar_encuesta_satisfaccion_telemedicina.py
python3 scripts/generar_incidencias_telemedicina.py
```

---

## Paso 2: Validación de datos con Pandas

Se creó `scripts/01_validacion_datos.py`, que para cada archivo verifica:
1. Valores nulos por columna
2. Registros duplicados (por ID)
3. Rangos lógicos (valores negativos o fuera de escala)
4. Resumen estadístico (`describe()`) de las columnas numéricas relevantes

### Resultados de la validación

| Dataset | Registros | Nulos | Duplicados | Rangos fuera de lo esperado |
|---|---|---|---|---|
| citas_agendadas.csv | 2,100 | 0 | 0 | Ninguno |
| intentos_agendamiento.csv | 1,750 | 0 | 0 | Ninguno |
| pagos_seguros.csv | 2,000 | 0 | 0 | Ninguno |
| encuesta_satisfaccion_telemedicina.csv | 150 | 0 | 0 | Ninguno |
| incidencias_telemedicina.csv | 208 | 0 | 0 | Ninguno |

**Conclusión de la validación:** los 5 datasets están limpios — sin valores nulos, sin duplicados y sin registros fuera de rango — cumpliendo el resultado esperado del escenario.

### Estadísticas descriptivas destacadas

- **datos_correctos** (citas): media = 0.882 → 88.2% de citas con datos correctos
- **pasos** (intentos de agendamiento): media = 2.79, rango 1–6 pasos
- **monto** (pagos con seguro): media = $186.41, rango $20.22–$349.87
- **duplicado** (pagos): media = 0.0045 → 0.45% de pagos duplicados
- **puntaje_satisfaccion** (telemedicina): media = 84.39, rango 62–100

---

## Preguntas de Discusión

**1. ¿Qué consecuencias tendría calcular la métrica de tiempo/pasos sin antes eliminar los valores atípicos (outliers) causados por sesiones abandonadas?**

Si se incluyen intentos abandonados a mitad de proceso (con muy pocos pasos registrados) o sesiones anómalas con un número de pasos excesivamente alto por errores del sistema, el promedio de la métrica "Complejidad de tarea" se distorsiona. El indicador dejaría de reflejar la experiencia típica del usuario y podría llevar a conclusiones erróneas: por ejemplo, ocultar que el sistema realmente cumple el umbral de 3 pasos (RNF-02) o, al contrario, aparentar que no cumple cuando el problema real es un grupo pequeño de casos atípicos.

**2. ¿Por qué la fuente de datos de Satisfacción (encuestas) es cualitativamente distinta a la de Eficiencia (logs)? ¿Qué implica esto para su frecuencia de recolección?**

Los logs se generan automáticamente en cada interacción del sistema: son datos continuos, de alto volumen y no requieren ninguna acción adicional del usuario. Las encuestas, en cambio, dependen de que el paciente o médico decida voluntariamente responder, lo que genera un volumen mucho menor (150 respuestas frente a miles de eventos de log) y un posible sesgo de participación (solo responden quienes tienen una opinión fuerte, positiva o negativa).

Esta diferencia implica que la frecuencia de recolección también debe ser distinta: los logs pueden analizarse en tiempo real o de forma diaria, mientras que las encuestas de satisfacción normalmente se consolidan y revisan de forma semanal o mensual, dado el tiempo que toma acumular una muestra representativa.

---

## Conclusiones Parciales

Al finalizar este escenario se cuenta con **5 datasets sintéticos validados** (`citas_agendadas.csv`, `intentos_agendamiento.csv`, `pagos_seguros.csv`, `encuesta_satisfaccion_telemedicina.csv`, `incidencias_telemedicina.csv`), libres de valores nulos, duplicados y datos fuera de rango. Estos archivos quedan listos para ser procesados automáticamente en el Escenario 8, donde se implementará el pipeline en Python que calculará las 5 métricas de Calidad en Uso definidas en el Escenario 6.

# Escenario 2: Comprensión de ISO/IEC 25022
## Actividad Práctica - Apartado 2

---

### Paso 2: Clasificación de Incidentes según las Cinco Características

A continuación se presenta la clasificación de los incidentes reportados en el sistema **MediSalud HIS**, evaluados bajo el marco de la norma **ISO/IEC 25022 (Calidad en Uso)**:

| ID | Característica Asignada | Justificación Técnica |
| :--- | :--- | :--- |
| **1005** | **Eficiencia** | El paciente logra ingresar al portal, pero el tiempo invertido (más de 18s) excede ampliamente los recursos temporales aceptables para la tarea en horas pico. |
| **1002** | **Eficacia** (Efectividad) | El médico no logra completar la tarea de sincronizar la orden médica con el módulo de farmacia, fallando en el grado de completitud y precisión del objetivo. |
| **1001** | **Eficacia** (Efectividad) | El paciente falla totalmente en alcanzar su objetivo específico de agendar la cita médica tras 2 intentos, evidenciando una nula efectividad en su flujo. |
| **1003** | **Eficacia** (Efectividad) | El sistema falla en la precisión de la tarea al permitir una doble reserva de un mismo cupo por dos pacientes distintos, impidiendo el cumplimiento correcto del objetivo. |
| **1006** | **Ausencia de Riesgo** (Libertad de Riesgo) | Una firma electrónica que no se valida compromete la legalidad y seguridad de la consulta médica, generando un riesgo regulatorio y de auditoría grave para el hospital. |
| **1004** | **Eficacia** (Efectividad) | Al no aparecer los signos vitales registrados por enfermería en la HCE del médico, el sistema impide que este alcance su objetivo de revisar la información clínica completa. |

---

### Preguntas de Discusión

#### 1. ¿Puede un sistema ser efectivo pero no eficiente? Dé un ejemplo del caso MediSalud.
**Sí, es completamente posible.** Según la norma ISO/IEC 25022, un sistema es **efectivo** si el usuario logra alcanzar su objetivo específico con precisión y completitud. Sin embargo, la **eficiencia** evalúa cuántos recursos (como tiempo, esfuerzo o capacidad de procesamiento) se consumieron para lograr esa efectividad.

* **Ejemplo en MediSalud HIS:** Un médico logra registrar y guardar su nota de evolución clínica en el sistema de manera correcta y completa (es efectivo). Sin embargo, debido a la sobrecarga y lentitud del módulo en horas pico (10:00 - 12:00), el sistema tarda 22 segundos en procesar el guardado en lugar de los 8 segundos fijados en los requerimientos no funcionales (RNF-01). Por lo tanto, el sistema es efectivo, pero carece de eficiencia.

#### 2. ¿Por qué la Cobertura de Contexto es especialmente relevante para una red hospitalaria con sedes en cinco ciudades distintas?
La **Cobertura de Contexto** mide el grado en que el producto software puede ejecutarse con calidad en uso (efectividad, eficiencia, satisfacción y libertad de riesgo) en diferentes entornos, tanto en los contextos previstos como en aquellos no previstos inicialmente.

Para **MediSalud Ecuador**, esta característica es de criticidad alta debido a que:
* **Diversidad de infraestructura:** El sistema HIS no opera bajo condiciones uniformes; debe funcionar con la misma confiabilidad en un hospital general de tercer nivel en Quito (con redes de alta velocidad y servidores robustos) que en un centro de atención ambulatoria en Manta o Ambato (donde la conectividad o el hardware pueden ser más limitados).
* **Diversidad de perfiles y dispositivos:** El portal y la app móvil acceden a los mismos microservicios desde múltiples dispositivos, anchos de banda y ubicaciones geográficas. 

Si el software presenta degradación de rendimiento, caídas de conexión o fallos de sincronización dependiendo de la sede hospitalaria o el tipo de acceso, su cobertura de contexto es deficiente, lo que compromete directamente la continuidad operativa y la equidad en la atención médica a nivel nacional.
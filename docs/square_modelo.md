# Escenario 3 – Comprensión del Modelo SQuaRE (ISO/IEC 25000)

## Objetivo del Escenario
Comprender en profundidad el modelo **SQuaRE (Software product Quality Requirements and Evaluation)**, sus divisiones principales y la relación entre **ISO/IEC 25010** y **ISO/IEC 25022**, aplicándolo al caso MediSalud HIS.

---

## Parte 1 – Fundamento Teórico

### 3.1.1 ¿Qué es SQuaRE?

La familia de normas **ISO/IEC 25000 (SQuaRE)** establece un marco integral para la evaluación de la calidad del software.  
Se organiza en cinco divisiones:

| División              | Norma ejemplo       | Descripción breve |
|-----------------------|---------------------|-------------------|
| **Modelos de calidad** | ISO/IEC 25010       | Define las características de calidad del producto (internas y externas). |
| **Medición de calidad** | ISO/IEC 25022       | Establece métricas para evaluar la calidad en uso. |
| **Requisitos de calidad** | ISO/IEC 25030       | Guía la especificación de requisitos de calidad. |
| **Evaluación de calidad** | ISO/IEC 25040       | Define procesos y métodos de evaluación. |
| **Extensiones y guías** | ISO/IEC 25060       | Aplicaciones específicas y contextuales (ej. telemedicina). |

### 3.1.2 Relación entre ISO/IEC 25010 y 25022

- **ISO/IEC 25010**: Modelo conceptual de calidad del producto software.  
- **ISO/IEC 25022**: Instrumento de medición de la calidad en uso.  

**Ejemplo aplicado a MediSalud HIS:**
- ISO/IEC 25010 asegura atributos como **seguridad, fiabilidad y usabilidad**.  
- ISO/IEC 25022 mide si médicos y pacientes logran sus tareas de manera **efectiva, eficiente y satisfactoria** en contextos reales.

---

## Parte 2 – Actividad Práctica

### Tabla: Divisiones de la familia ISO/IEC 25000 aplicadas a MediSalud HIS

| División              | Norma ejemplo       | Aplicación en MediSalud HIS |
|-----------------------|---------------------|-----------------------------|
| Modelos de calidad    | ISO/IEC 25010       | Define atributos como seguridad y usabilidad. |
| Medición de calidad   | ISO/IEC 25022       | Mide efectividad y eficiencia en tareas clínicas. |
| Requisitos de calidad | ISO/IEC 25030       | Formaliza RNF-01 a RNF-05 del HIS. |
| Evaluación de calidad | ISO/IEC 25040       | Proceso de evaluación del sistema hospitalario. |
| Extensiones y guías   | ISO/IEC 25060       | Aplicaciones específicas como telemedicina. |

### Niveles de calidad aplicados a MediSalud HIS
1. **Calidad interna** → Arquitectura de microservicios, código fuente y base de datos.  
2. **Calidad externa** → Comportamiento observable: tiempos de respuesta, errores de facturación.  
3. **Calidad en uso** → Experiencia real de médicos, pacientes y administrativos en tareas críticas.

---

## Resultado esperado
Al finalizar este escenario, el estudiante:
- Comprende la estructura de la familia **ISO/IEC 25000 (SQuaRE)**.  
- Relaciona **ISO/IEC 25010** y **ISO/IEC 25022** en un caso hospitalario real.  
- Documenta divisiones y niveles de calidad aplicados al HIS de MediSalud en formato académico.  

---

## Conclusiones
Este escenario permitió conectar el **modelo conceptual de calidad (ISO/IEC 25010)** con la **medición práctica de calidad en uso (ISO/IEC 25022)** dentro del marco **SQuaRE**, aplicándolo directamente al sistema hospitalario MediSalud HIS.

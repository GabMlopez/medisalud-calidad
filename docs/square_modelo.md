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


### Actividad 1 - Investigación Dirigida

#### Comparación entre calidad interna, externa y en uso.

Tanto la calidad interna como la calidad externa son métricas que se enfocan en la calidad de producto, es decir, evalúan basados en estándares y métricas con carácter exacto y objetivo, y siempre desde la perspectiva de especialistas. La calidad interna se enfoca en una calidad "estática" del producto, revisando el código y estructura del software sin ejecutar con el fin de detectar carencias o vulnerabilidades producidas por malas prácticas de programación. Por su parte, la calidad externa mide la calidad "dinámica" del software en ejecución, considerando aspectos de desempeño del producto como el uso de recursos, seguridad, tolerancia a fallos, e interacción con otros elementos de su entorno.

La calidad en uso por su parte, también se rige por métricas y estándares pero tiene un carácter mucho más flexible y subjetivo, siendo probado por usuarios reales o de prueba, y recolectando sus datos de interacción. Este tipo de calidad se enfoca en la pertinencia del software, es decir en su nivel de utilidad y aporte para el propósito con el que fue desarrollado, así como en la comodidad y experiencia que da a sus usuarios.

### Actividad 2 - Aplicación al caso MediSalud

#### Tabla: Divisiones de la familia ISO/IEC 25000 aplicadas a MediSalud HIS

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

### Preguntas de Discusión

#### 1. ¿Puede un sistema tener excelente calidad interna (código limpio) y mala calidad en uso? Explique con un ejemplo.

Sí, un sistema puede estar estructurado siguiendo buenas prácticas y estándares de calidad interna, pero sin considerar las necesidades y objetivos del usuario. 
Un ejemplo puede ser un sistema diseñado para una escuela, el cual cuenta con excelenete modularidad, calidad de código, escalabilidad y fiabilidad. Sin embargo, los flujos de acciones son muy complejos para los profesores y estudiantes ya que necesitan alrededor de 6 pasos solo para ver las calificaciones, además de que solo permite asignar tareas en forma de comentarios de texto, sin adjuntar imágenes u otros documentos como material de apoyo.           

#### 2. ¿Por qué SonarQube (Calidad Interna) no es suficiente para que MediSalud resuelva su problemática de lentitud percibida por los médicos?

Porque SonarQube evalúa la complejidad del código y ciertos aspectos como tamaños de datos, pero no considera toda la información que se debe procesar o la concurrencia de usuarios promedio que tiene el sistema. Se necesitan de mecanismos adicionales como pruebas de carga, y verificación con usuarios para identificar los puntos de fallo y poder implementar una solución.    

---

## Resultado esperado
Al finalizar este escenario, el estudiante:
- Comprende la estructura de la familia **ISO/IEC 25000 (SQuaRE)**.  
- Relaciona **ISO/IEC 25010** y **ISO/IEC 25022** en un caso hospitalario real.  
- Documenta divisiones y niveles de calidad aplicados al HIS de MediSalud en formato académico.  

---

## Conclusiones
Este escenario permitió conectar el **modelo conceptual de calidad (ISO/IEC 25010)** con la **medición práctica de calidad en uso (ISO/IEC 25022)** dentro del marco **SQuaRE**, aplicándolo directamente al sistema hospitalario MediSalud HIS.

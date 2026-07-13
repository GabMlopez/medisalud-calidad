# Tareas del sistema 


### Ficha 1: Agendamiento y Admisión de Pacientes

| Campo | Ejemplo completado |
| :--- | :--- |
| **Proceso** | Agendamiento y admisión de pacientes |
| **Usuario primario** | Paciente (portal web y app móvil) y Personal de Admisión |
| **Tarea representativa** | Agendar una cita médica con un especialista a través del portal del paciente. |
| **Contexto de uso** | Dispositivos móviles y de escritorio, desde diversas ubicaciones (domicilio, trabajo) con conexiones a internet variables. Alta demanda en horas de la mañana (08:00-10:00) y durante campañas de salud. |
| **Atributos de Calidad en Uso relevantes** | - **Efectividad:** Tasa de éxito al agendar una cita sin errores de disponibilidad.<br>- **Eficiencia:** Tiempo que tarda el usuario en completar el proceso de agendamiento (número de pasos y tiempo de respuesta).<br>- **Satisfacción:** Claridad del formulario y percepción de facilidad de uso (evitar abandono). |
| **Justificación basada en incidentes** | Los incidentes muestran problemas como "Usuario no logra agendar tras 3 intentos" (ID 1002), "Formulario confuso, abandono de registro" (ID 2017), "Doble reserva de un mismo cupo" (ID 2235) y altos tiempos de espera en el portal (ID 2057). Esto demuestra que la tarea es frustrante, ineficiente y, a veces, inefectiva para el usuario. |

---

### Ficha 2: Facturación 

| Campo | Ejemplo completado |
| :--- | :--- |
| **Proceso** | Facturación y gestión de seguros/reaseguros |
| **Usuario primario** | Personal de Admisión y Paciente |
| **Tarea representativa** | Procesar el pago de una consulta médica, aplicando el copago correspondiente del seguro médico. |
| **Contexto de uso** | Puntos de atención (cajas) con alta presión y flujo de pacientes. Módulo de facturación utilizado en horario de atención continua. Transacciones con tarjetas de crédito/débito. |
| **Atributos de Calidad en Uso relevantes** | - **Efectividad:** Precisión en el cálculo del copago y aplicación del convenio con la aseguradora.<br>- **Libertad de Riesgo:** Tasa de errores de facturación (facturas duplicadas, montos incorrectos) y exposición de datos financieros sensibles.<br>- **Eficiencia:** Tiempo de procesamiento de la transacción. |
| **Justificación basada en incidentes** | Los incidentes "El sistema no reconoce el convenio con la aseguradora" (ID 2020), "Reintento de transaccion genera doble cobro" (ID 3543) y "Error de calculo en el copago" (ID 1610) indican un alto riesgo de error financiero y una amenaza a la seguridad económica del paciente y la reputación de MediSalud. |

---

### Ficha 3: Telemedicina 

| Campo | Ejemplo completado |
| :--- | :--- |
| **Proceso** | Telemedicina y seguimiento remoto |
| **Usuario primario** | Médico y Paciente |
| **Tarea representativa** | Completar una teleconsulta en video sin interrupciones. |
| **Contexto de uso** | Diferentes ubicaciones geográficas, horarios programados. Calidad de la conexión a internet variable, tanto para el médico como para el paciente. |
| **Atributos de Calidad en Uso relevantes** | - **Efectividad:** Tasa de finalización de la teleconsulta con éxito (generación de receta).<br>- **Libertad de Riesgo:** Seguridad y confiabilidad de la conexión para evitar la pérdida de información clínica.<br>- **Cobertura de Contexto:** Calidad de la experiencia en diferentes dispositivos y condiciones de red.<br>- **Satisfacción:** Calidad de la imagen y el audio; percepción de que la consulta fue útil y cercana a una presencial. |
| **Justificación basada en incidentes** | Incidentes como "Videollamada se corta a los 4 minutos" (ID 1004), "Calidad de video muy baja" (ID 3430) y "Receta electronica no se genera al finalizar la teleconsulta" (ID 2349) afectan directamente la viabilidad de la telemedicina como servicio, erosionando la confianza del paciente y el médico. |

---

### Ficha 4: Registro y Actualización de Historia Clínica Electrónica (HCE)

| Campo | Ejemplo completado |
| :--- | :--- |
| **Proceso** | Atención médica y registro de historia clínica |
| **Usuario primario** | Médico tratante y Personal de Enfermería |
| **Tarea representativa** | Registrar una nota de evolución clínica completa de un paciente durante una consulta. |
| **Contexto de uso** | Consulta externa, horario de alta demanda (10:00-12:00), red interna del hospital. El médico debe atender al paciente mientras interactúa con el sistema. |
| **Atributos de Calidad en Uso relevantes** | - **Eficiencia:** Tiempo que toma registrar la nota de evolución.<br>- **Efectividad:** Precisión y completitud de los datos registrados (diagnósticos, medicamentos).<br>- **Libertad de Riesgo:** Prevención de errores médicos (ej. dosis incorrecta) y exposición de datos de otros pacientes. |
| **Justificación basada en incidentes** | Los incidentes "Nota de evolucion tarda 22s en guardarse" (ID 1001), "Receta electronica se genera con la dosis incorrecta" (ID 3980) y "Datos de otro paciente visibles" (ID 1005) demuestran que la tarea es crítica, lenta y propensa a errores que ponen en riesgo la seguridad del paciente. |

---

### Ficha 5: Dispensación y Gestión de Inventario de Farmacia

| Campo | Ejemplo completado |
| :--- | :--- |
| **Proceso** | Prescripción y dispensación de medicamentos |
| **Usuario primario** | Personal de Farmacia |
| **Tarea representativa** | Dispensar un medicamento recetado, actualizando el inventario y registrando la entrega al paciente. |
| **Contexto de uso** | Horario de atención de farmacia, alta demanda en horas pico de la mañana y tarde. El personal debe verificar la disponibilidad y precisión de los medicamentos. |
| **Atributos de Calidad en Uso relevantes** | - **Efectividad:** Precisión en la dispensación del medicamento correcto.<br>- **Libertad de Riesgo:** Tasa de errores en la dispensación (ej. medicamento incorrecto) y alertas de vencimiento.<br>- **Eficiencia:** Tiempo de respuesta del módulo de farmacia. |
| **Justificación basada en incidentes** | Los incidentes "Duplicidad de codigos entre dos presentaciones de un mismo farmaco" (ID 1786), "Alerta de vencimiento de lote no se muestra" (ID 1072) y "Tiempo de respuesta del modulo de farmacia supera los 31s" (ID 1056) evidencian riesgos de seguridad del paciente y problemas de eficiencia operativa. |

---

### Ficha 6: Generación de Reportes Gerenciales

| Campo | Ejemplo completado |
| :--- | :--- |
| **Proceso** | Generación de reportes gerenciales para toma de decisiones |
| **Usuario primario** | Gerencia y Personal de Calidad |
| **Tarea representativa** | Generar un reporte de ocupación hospitalaria mensual para la toma de decisiones estratégicas. |
| **Contexto de uso** | Oficinas administrativas, fin de mes. Se requiere acceso a datos consolidados de múltiples módulos (facturación, admisión). |
| **Atributos de Calidad en Uso relevantes** | - **Efectividad:** Precisión de los datos reflejados en el reporte.<br>- **Eficiencia:** Tiempo de generación del reporte.<br>- **Satisfacción:** Utilidad y claridad de la información presentada. |
| **Justificación basada en incidentes** | Incidentes como "Discrepancia entre el reporte financiero y el modulo de facturacion" (ID 1196), "El reporte de ocupacion hospitalaria no se actualiza automaticamente" (ID 1986) y "Tiempo de generacion del reporte mensual supera los 25 minutos" (ID 2467) indican que la información para la gerencia no es confiable, oportuna ni exacta, lo que afecta la toma de decisiones. |

**Preguntas de Discusión**

1.  **¿Por qué es incorrecto definir una tarea como "usar el sistema HIS" en lugar de "registrar una nota de evolución clínica"?**

    - Es muy general por lo que se puede realizar un flujo incorrecto o innecesario, por ello es necesario hacerlo más explícito, tanto para los testers como los desarrolladores para revisar cual es el incoveniente correcto  

2.  **¿Qué ocurre si se mide la eficiencia sin haber definido el contexto de uso (por ejemplo, sin diferenciar hora pico de hora valle)?**

    - Los datos obtenidos pueden realizarse en contextos no reales que dan lugar a  falsos positivos, se obvian a su vez problemas en el sistema que deben ser revisados y se generan métricas ficticias que no aseguran la calidad del producto en la realidad.
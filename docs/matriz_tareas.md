# Mapeo de métricas de calidad

**Tabla 5.1: Matriz de mapeo tarea-característica-prioridad**

| Tarea | Impacto | Frecuencia | Característica(s) ISO 25022 | Prioridad |
| :--- | :--- | :--- | :--- | :--- |
| **1. Agendar una cita médica por el portal** | Alto | Alta | **Efectividad**, **Satisfacción**, **Eficiencia** | **1** |
| **2. Procesar el pago de una consulta con seguro** | Alto | Media | **Libertad de Riesgo**, **Efectividad** | **1** |
| **3. Registrar nota de evolución clínica (HCE)** | Alto | Alta | **Eficiencia**, **Efectividad**, **Libertad de Riesgo** | **1** |
| **4. Completar una teleconsulta** | Medio | Media | **Efectividad**, **Cobertura de Contexto**, **Satisfacción** | **2** |
| **5. Facturar y gestionar el reembolso de un seguro** | Alto | Baja | **Libertad de Riesgo**, **Efectividad** | **2** |
| **6. Consultar historial de resultados de laboratorio** | Bajo | Alta | **Satisfacción**, **Eficiencia** | **3** |

---

**Preguntas de Discusión**

1.  **¿Qué riesgo corre una organización que intenta medir absolutamente todo desde el primer día de un programa de calidad en uso?**

    -  Se consume tiempo y recursos incorrectamente, por el poco tiempo de análisis no se realizan examenes exhaustivos que muestren los problemas de software y espacios de mejora ademas de obtener métricas no planificadas correctamente a diferencia de análisis por fases.

2.  **¿Por qué "Consultar historial de resultados" tiene menor prioridad pese a tener alta frecuencia?**

    -   En este caso a pesar de ser frecuentemente utilizada, solo afecta al usuario médico por lo que su alta frecuencia se debe al uso constante de este tipo de usuarios que son apenas un 10-15% de los usuarios, a diferencia de módulos que interactuan directamente con el paciente que son los usuarios más abundantes del sistema y por tanto más críticos.
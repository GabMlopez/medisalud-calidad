## Diseño de Métricas de Calidad

### Métrica N°1
| Campo Documentado | Valor |
|---|---|
|Nombre|Tasa de precisión de tarea - Agendamiento de cita médica|
|Característica|Efectividad|
|Propósito|Determinar la pertinencia y capacidad del sistema para guiar al usuario en el ingreso de datos para agendar la cita.|
|Fórmula|$$X=100-\frac{C_{i}}{C_{T}}$$|
|Definición de variables|$$\begin{align*}&C_{c}\text{: Número de citas que contienen datos incorrectos}\\ &C_{c}\text{: Número total de citas ingresadas}\end{align*}$$|
|Unidad de Medida|% de citas agendadas con errores.|
|Rango Deseado/Umbral|Un valor adecuado sería entre el 80 y 90%, y un valor óptimo sería mayor al 90%.|
|Fuente de Datos|Base de datos con citas agendadas|
|Interpretación|Valores de menos del 80% indican que una parte importante de usuarios tiene problemas para ingresar datos o que el sistema no está validando correctamente.|
### Métrica N°2
| Campo Documentado | Valor |
|---|---|
|Nombre|Complejidad de Tarea - Agendamiento de cita médica|
|Característica|Eficiencia|
|Propósito|Medir la eficiencia con que el portal de citas permite a los usuarios agendar una reunión.|
|Fórmula|$$X=\frac{\sum{p_{i}}}{n}$$|
|Definición de variables|$$\begin{align*}&p_{i}\text{: Cantidad de pasos del "i"ésimo intento}\\ &n\text{: Total de intentos}\end{align*}$$|
|Unidad de Medida|Pasos por intento|
|Rango Deseado/Umbral|El valor óptimo es menor a 3 como indica el RNF-02|
|Fuente de Datos|Pruebas de usuarios - Encuestas|
|Interpretación|Si el promedio de pasos por intento es mayor a 3 significa que el proceso es complejo y toma demasiado en completar.|
### Métrica N°3
| Campo Documentado | Valor |
|---|---|
|Nombre|Potencial de riesgo financiero - Pagos de consulta con seguros|
|Característica|Libertad de riesgo|
|Propósito|Determinar la tasa de riesgo financiero existente por un posible pago duplicado con el seguro.|
|Fórmula|$$X=\frac{T_{d}}{T_{p}}$$|
|Definición de variables|$$\begin{align*}&T_{d}\text{: Total de pagos duplicados}\\ &T_{p}\text{: Total de pagos revisados}\end{align*}$$|
|Unidad de Medida|% de posibilidad de pago duplicado|
|Rango Deseado/Umbral|$<1\%$ - Tal como define el RNF-04 para las facturas|
|Fuente de Datos|Historial de pagos procesados|
|Interpretación|Si el porcentaje es mayor al 1% significa que existe un peligro real de generar pagos duplicados y que el cliente tenga pérdidas económicas, lo que puede llevar a problemas legales.|
## Métrica N°4
| Campo Documentado | Valor |
|---|---|
|Nombre|Puntaje de satisfacción - Consultas de telemedicina|
|Característica|Satisfacción|
|Propósito|Medir el nivel de satisfacción de pacientes y médicos al usar el módulo de telemedicina|
|Fórmula|$$X=\frac{\sum{s_{i}}}{n}$$|
|Definición de variables|$$\begin{align*}&s_{i}\text{: Puntaje (score) de satisfacción del "i"ésimo encuestado}\\ &n\text{: Total de encuestados}\end{align*}$$|
|Unidad de Medida|Puntos|
|Rango Deseado/Umbral|$>85$|
|Fuente de Datos|Encuesta de satisfacción aplicada al final de la teleconsulta.|
|Interpretación|Valores menores a 85 indican problemas severos con la consulta (estabilidad, calidad de imagen/audio, entre otros) que afectan la experiencia del usuario de manera significativa |
## Métrica N°5
| Campo Documentado | Valor |
|---|---|
|Nombre|Rendimiento entre dispositiviso - Consultas de telemedicina |
|Característica|Cobertura de contexto|
|Propósito|Determinar si existe una diferencia significativa entre el rendimiento en la plataforma web frente a la app móvil.|
|Fórmula|$$X=\frac{\|C_W-C_M\|}{C_T}$$|
|Definición de variables|$$\begin{align*}&C_W:\text{ Número de reuniones caídas en plataforma web}\\ &C_M:\text{ Número de reuniones caídas en app móvil}\\ &C_T:\text{ Total de reuniones caídas}\end{align*}$$|
|Unidad de Medida|% de diferencia de rendimiento|
|Rango Deseado/Umbral|$<10\%$|
|Fuente de Datos|Reportes de incidencias/Quejas|
|Interpretación|Si existe una diferencia mayor al 10% esto indica que el funcionamiento del sistema no es consistente entre entornos, lo que puede afectar la experiencia del cliente según su dispositivo.|
## Preguntas de Discusión

### ¿Por qué es importante fijar de antemano el *rango deseado* y no solo calcular el valor de la métrica? 
Porque sin un valor o valores que actúen como objetivo o referencia, el valor que se obtenga al calcular la métrica no tendrá mucho sentido, ya que no se puede interpretar ni determinar si es algo positivo o negativo.

### ¿Qué diferencia existe entre una métrica de *Eficiencia* y un simple cronómetro de tiempo de respuesta del servidor? 
En primer lugar, la métrica de eficiencia mide el uso de recursos, no solamente de tiempo, puede ser de esfuerzo y complejidad. 

Además, las métricas de eficiencia con tiempo se comparan con el resultado obtenido en el contexto de una tarea específica. Los tiempos de respuesta no tienen mucho valor por si solos si no se contextualizan, ya que cada tarea requiere diferentes plazos para completarse.
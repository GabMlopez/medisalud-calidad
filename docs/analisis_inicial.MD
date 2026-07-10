# Análisis del caso

|  Preguntas guía | Respuestas  |  
|---|--- |
| ¿Cuáles son los 3 procesos más críticos del negocio? |  El sistema tiene 6 procesos críticos, pero los mas importantes son los siguientes: <br /> Agendamiento y admisión de pacientes <br /> Facturación y gestión de seguros/reaseguros<br /> Telemedicina y seguimiento remoto| 
| ¿Qué usuarios se ven más afectados por la problemática actual? |  Los usuarios mas afectados son los pacientes que no podian ni agendar citas para recibir un tratamiento y luego tenian problemas al no poder obtener sus medicamentos durante el proceso |
|  ¿Qué evidencia tiene hoy MediSalud sobre la calidad de su software?   | MediSalud cuenta con un registro de los problemas y sus clasificaciones para tener metricas de control del software, ademas de uso de frameworks y herramientas que acompañan el desarrollo como docker para despliegues rápidos y Github para control de cambios y  |
|¿Qué evidencia le falta?| Es necesario tener métricas cuantitativas que muestren en que grado estan cumpliendo las expectativas del cliente en base a un estandar como el 25010,  |

## Preguntas de Discusión

1. ¿Por qué la disponibilidad de servidores (uptime) no es suficiente para afirmar que un sistema tiene buena calidad en uso?

Por los problemas que presenta sobre todo en las horas pico de 10-12 am con tiempos de respuesta muy lentos para los usuarios

2. ¿Qué diferencia existe entre la calidad interna, la calidad externa y la calidad en uso de un producto software?

En la calidad interna es como se manejo el proceso de desarrollo del producto de software, la gestión del proceso y  la cuantificación y mediciones realizadas antes del despliegue, la calidad externa es como el producto es percibido por los usuarios, sean sus componentes funcionales como no funcionales, la calidad de uso finalmente es la respuesta del producto de software ante ambientes reales y condiciones que miden realmente la resiliencia y efectividad del producto. 

3. En el caso de MediSalud, ¿qué stakeholder se beneficiaría más de un programa de medición de calidad en uso: el paciente, el médico o la gerencia? Justifique.

El paciente es al que más le afecta el producto, se beneficiaria de el control de calidad al poder mejorar los procesos de citas y medicamentos que el software deberia de facilitar al ser el sistema diseñado para estos usuarios y contar con la mayor concurrencia aproximadamente de +38.000 usuarios del mismo a diferencia de gerencia y medicos que en conjunto solo son entre 1890 usuarios, aunque tendria un efecto al poder facilitar problemas del sistema en gestión y para los medicos ayudar indirectamente en la velocidad de los procesos para los pacientes.
"""
Genera una encuesta sintetica de satisfaccion aplicada al final de
teleconsultas, en escala 0-100, para calcular el Puntaje de
satisfaccion (Satisfaccion). Umbral deseado: >85.
"""
import csv
import random

random.seed(42)

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
ROLES = ["Paciente", "Medico"]

filas = []
N_RESPUESTAS = 150

for respuesta_id in range(1, N_RESPUESTAS + 1):
    sede = random.choice(SEDES)
    rol = random.choices(ROLES, weights=[0.8, 0.2])[0]

    # Puntaje centrado en 82, con dispersion normal, acotado 0-100
    puntaje = min(100, max(0, round(random.gauss(82, 10))))

    filas.append({
        "respuesta_id": respuesta_id,
        "sede": sede,
        "rol": rol,
        "puntaje_satisfaccion": puntaje,
    })

with open("data/encuesta_satisfaccion_telemedicina.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=filas[0].keys())
    writer.writeheader()
    writer.writerows(filas)

print(f"Se generaron {len(filas)} respuestas en data/encuesta_satisfaccion_telemedicina.csv")
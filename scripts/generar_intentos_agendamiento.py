"""
Genera un dataset sintetico de intentos de agendamiento de citas,
registrando el numero de pasos que tomo cada intento, para calcular
la Complejidad de tarea (Eficiencia). RNF-02 exige <=3 pasos.
"""
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
FECHA_INICIO = datetime(2025, 11, 3)
DIAS = 5

filas = []
intento_id = 1

for dia in range(DIAS):
    fecha_dia = FECHA_INICIO + timedelta(days=dia)
    for sede in SEDES:
        n_intentos = 100 if sede in ("Quito", "Guayaquil") else 50
        for _ in range(n_intentos):
            usuario_id = f"USR-{random.randint(1000, 9999)}"

            # La mayoria completa en 2-3 pasos, algunos requieren mas
            pasos = max(1, round(random.gauss(2.8, 0.9)))

            filas.append({
                "intento_id": intento_id,
                "fecha": fecha_dia.strftime("%Y-%m-%d"),
                "sede": sede,
                "usuario_id": usuario_id,
                "pasos": pasos,
            })
            intento_id += 1

with open("data/intentos_agendamiento.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=filas[0].keys())
    writer.writeheader()
    writer.writerows(filas)

print(f"Se generaron {len(filas)} intentos en data/intentos_agendamiento.csv")
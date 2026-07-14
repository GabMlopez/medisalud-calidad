"""
Genera un dataset sintetico de citas agendadas en el portal de MediSalud,
marcando si los datos ingresados fueron correctos o no, para calcular
la Tasa de precision de tarea (Efectividad).
"""
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
FECHA_INICIO = datetime(2025, 11, 3)
DIAS = 5

filas = []
cita_id = 1

for dia in range(DIAS):
    fecha_dia = FECHA_INICIO + timedelta(days=dia)
    for sede in SEDES:
        n_citas = 120 if sede in ("Quito", "Guayaquil") else 60
        for _ in range(n_citas):
            paciente_id = f"PAC-{random.randint(10000, 99999)}"

            # 88% de las citas se agendan con datos correctos
            datos_correctos = int(random.random() < 0.88)

            filas.append({
                "cita_id": cita_id,
                "fecha": fecha_dia.strftime("%Y-%m-%d"),
                "sede": sede,
                "paciente_id": paciente_id,
                "datos_correctos": datos_correctos,
            })
            cita_id += 1

with open("data/citas_agendadas.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=filas[0].keys())
    writer.writeheader()
    writer.writerows(filas)

print(f"Se generaron {len(filas)} citas en data/citas_agendadas.csv")
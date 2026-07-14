"""
Genera un dataset sintetico de reuniones caidas en teleconsultas,
separadas por plataforma (web / movil), para calcular el
Rendimiento entre dispositivos (Cobertura de Contexto).
Umbral deseado: diferencia <10% entre plataformas.
"""
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
PLATAFORMAS = ["web", "movil"]
FECHA_INICIO = datetime(2025, 11, 3)
DIAS = 5

filas = []
incidencia_id = 1

for dia in range(DIAS):
    fecha_dia = FECHA_INICIO + timedelta(days=dia)
    for sede in SEDES:
        # La app movil tiende a tener mas caidas que la web
        n_caidas_web = random.randint(1, 4)
        n_caidas_movil = random.randint(3, 9)

        for _ in range(n_caidas_web):
            filas.append({
                "incidencia_id": incidencia_id,
                "fecha": fecha_dia.strftime("%Y-%m-%d"),
                "sede": sede,
                "plataforma": "web",
                "tipo_incidencia": "caida de conexion",
            })
            incidencia_id += 1

        for _ in range(n_caidas_movil):
            filas.append({
                "incidencia_id": incidencia_id,
                "fecha": fecha_dia.strftime("%Y-%m-%d"),
                "sede": sede,
                "plataforma": "movil",
                "tipo_incidencia": "caida de conexion",
            })
            incidencia_id += 1

with open("data/incidencias_telemedicina.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=filas[0].keys())
    writer.writeheader()
    writer.writerows(filas)

print(f"Se generaron {len(filas)} incidencias en data/incidencias_telemedicina.csv")
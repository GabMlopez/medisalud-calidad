"""
Genera un dataset sintetico de pagos de consultas procesados con seguros,
marcando pagos duplicados, para calcular el Potencial de riesgo
financiero (Libertad de Riesgo). RNF-04 exige <1% de duplicados.
"""
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

ASEGURADORAS = ["Salud S.A.", "SegurosVida", "EcuaSalud", "ProteVida"]
FECHA_INICIO = datetime(2025, 11, 3)
DIAS = 5

filas = []
pago_id = 1

for dia in range(DIAS):
    fecha_dia = FECHA_INICIO + timedelta(days=dia)
    n_pagos = 400  # pagos revisados por dia
    for _ in range(n_pagos):
        paciente_id = f"PAC-{random.randint(10000, 99999)}"
        aseguradora = random.choice(ASEGURADORAS)
        monto = round(random.uniform(20, 350), 2)

        # 0.6% de los pagos resultan duplicados
        duplicado = int(random.random() < 0.006)

        filas.append({
            "pago_id": pago_id,
            "fecha": fecha_dia.strftime("%Y-%m-%d"),
            "paciente_id": paciente_id,
            "aseguradora": aseguradora,
            "monto": monto,
            "duplicado": duplicado,
        })
        pago_id += 1

with open("data/pagos_seguros.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=filas[0].keys())
    writer.writeheader()
    writer.writerows(filas)

print(f"Se generaron {len(filas)} pagos en data/pagos_seguros.csv")
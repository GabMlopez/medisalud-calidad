import json
import pandas as pd

def cargar_configuracion():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Error: No se encontró el archivo 'config.json'.")
        raise

def cargar_datos(config):
    try:
        citas = pd.read_csv(config["rutas"]["citas"])
        intentos = pd.read_csv(config["rutas"]["intentos"])
        pagos = pd.read_csv(config["rutas"]["pagos"])
        encuestas = pd.read_csv(config["rutas"]["encuestas"])
        incidencias = pd.read_csv(config["rutas"]["incidencias"])
        return citas, intentos, pagos, encuestas, incidencias
    except FileNotFoundError as e:
        print(f"❌ Error al cargar archivos del Escenario 7: {e}")
        raise

def metrica_efectividad(citas, umbral):
    """Métrica 1: Tasa de precisión de tarea."""
    valor = round(citas["datos_correctos"].mean(), 4)
    return {
        "nombre": "Tasa de precisión de tarea (Citas correctas)",
        "caracteristica": "Efectividad (ISO 25022)",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": umbral,
        "cumple": bool(valor >= umbral)
    }

def metrica_eficiencia(intentos, umbral):
    """Métrica 2: Complejidad de tarea (Promedio de pasos)."""
    valor = round(intentos["pasos"].mean(), 2)
    return {
        "nombre": "Complejidad de tarea (Promedio de pasos)",
        "caracteristica": "Eficiencia (ISO 25022)",
        "valor": valor,
        "unidad": "pasos",
        "umbral": umbral,
        "cumple": bool(valor <= umbral)
    }

def metrica_libertad_riesgo(pagos, umbral):
    """Métrica 3: Potencial de riesgo financiero (Pagos duplicados)."""
    valor = round(pagos["duplicado"].mean(), 4)
    return {
        "nombre": "Tasa de transacciones duplicadas",
        "caracteristica": "Libertad de Riesgo Financiero (ISO 25022)",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": umbral,
        "cumple": bool(valor <= umbral)
    }

def metrica_satisfaccion(encuestas, umbral):
    """Métrica 4: Puntaje de satisfacción."""
    valor = round(encuestas["puntaje_satisfaccion"].mean(), 2)
    return {
        "nombre": "Puntaje promedio de satisfacción",
        "caracteristica": "Satisfacción (ISO 25022)",
        "valor": valor,
        "unidad": "puntos (escala 100)",
        "umbral": umbral,
        "cumple": bool(valor >= umbral)
    }

def metrica_cobertura_contexto(incidencias, umbral):
    """Métrica 5: Rendimiento de cobertura (Tasa total de incidencias)."""
    valor = len(incidencias)
    return {
        "nombre": "Total de incidencias en dispositivos",
        "caracteristica": "Cobertura de Contexto (ISO 25022)",
        "valor": valor,
        "unidad": "incidencias",
        "umbral": umbral,
        "cumple": bool(valor <= umbral)
    }

def desglose_cobertura_dispositivos(incidencias):
    """Agrupación de incidencias por plataforma."""
    if "plataforma" in incidencias.columns:
        return (
            incidencias.groupby("plataforma")["incidencia_id"]
            .count()
            .reset_index()
            .rename(columns={"incidencia_id": "total_incidencias"})
            .to_dict(orient="records")
        )
    return []

def generar_reporte():
    config = cargar_configuracion()
    citas, intentos, pagos, encuestas, incidencias = cargar_datos(config)
    
    umbrales = config["umbrales"]
    
    reporte = {
        "efectividad": metrica_efectividad(citas, umbrales["efectividad_precision_citas"]),
        "eficiencia": metrica_eficiencia(intentos, umbrales["eficiencia_pasos_agendamiento"]),
        "libertad_riesgo": metrica_libertad_riesgo(pagos, umbrales["riesgo_pagos_duplicados"]),
        "satisfaccion": metrica_satisfaccion(encuestas, umbrales["satisfaccion_telemedicina"]),
        "cobertura_contexto": metrica_cobertura_contexto(incidencias, umbrales["cobertura_limite_incidencias"])
    }
    
    desglose_plataformas = desglose_cobertura_dispositivos(incidencias)
    return reporte, desglose_plataformas

if __name__ == "__main__":
    reporte, desglose = generar_reporte()
    print("==================================================")
    print("   REPORTE DE CALIDAD EN USO (ISO/IEC 25022)")
    print("==================================================")
    for k, m in reporte.items():
        estado = "✅ CUMPLE" if m["cumple"] else "❌ NO CUMPLE"
        print(f"\nMétrica: {m['nombre']}")
        print(f"  - Característica: {m['caracteristica']}")
        print(f"  - Valor Actual  : {m['valor']} {m['unidad']}")
        print(f"  - Umbral Límite : {m['umbral']} | Estado: {estado}")
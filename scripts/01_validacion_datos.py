import pandas as pd

def validar(nombre_archivo, columnas_numericas=None, columna_id=None):
    print(f"\n{'='*60}")
    print(f"VALIDANDO: {nombre_archivo}")
    print('='*60)

    df = pd.read_csv(f"data/{nombre_archivo}")

    # 1. Valores nulos
    print("\nValores nulos por columna:")
    print(df.isnull().sum())

    # 2. Duplicados (si hay columna id)
    if columna_id:
        print(f"\nRegistros duplicados ({columna_id}):", df.duplicated(subset=[columna_id]).sum())

    # 3. Rangos logicos en columnas numericas
    if columnas_numericas:
        for col in columnas_numericas:
            print(f"\nResumen estadistico de '{col}':")
            print(df[col].describe())

    print(f"\nTotal de registros: {len(df)}")
    return df


# --- Metrica 1: Citas agendadas ---
validar("citas_agendadas.csv",
        columnas_numericas=["datos_correctos"],
        columna_id="cita_id")

# --- Metrica 2: Intentos de agendamiento ---
df2 = validar("intentos_agendamiento.csv",
              columnas_numericas=["pasos"],
              columna_id="intento_id")
print("\nIntentos con pasos fuera de rango (<1 o >10):")
print(df2[(df2["pasos"] < 1) | (df2["pasos"] > 10)])

# --- Metrica 3: Pagos con seguros ---
df3 = validar("pagos_seguros.csv",
              columnas_numericas=["monto", "duplicado"],
              columna_id="pago_id")
print("\nPagos con monto invalido (<=0):")
print(df3[df3["monto"] <= 0])

# --- Metrica 4: Encuesta de satisfaccion telemedicina ---
df4 = validar("encuesta_satisfaccion_telemedicina.csv",
              columnas_numericas=["puntaje_satisfaccion"],
              columna_id="respuesta_id")
print("\nPuntajes fuera de rango (<0 o >100):")
print(df4[(df4["puntaje_satisfaccion"] < 0) | (df4["puntaje_satisfaccion"] > 100)])

# --- Metrica 5: Incidencias telemedicina ---
validar("incidencias_telemedicina.csv",
        columnas_numericas=None,
        columna_id="incidencia_id")
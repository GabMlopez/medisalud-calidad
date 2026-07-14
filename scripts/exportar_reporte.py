import json
import os
from metricas_iso25022 import generar_reporte

def exportar():
    os.makedirs("dashboards", exist_ok=True)
    reporte, desglose_plataformas = generar_reporte()
    
    datos_salida = {
        "proyecto": "MediSalud Telemedicina - Calidad en Uso",
        "norma": "ISO/IEC 25022",
        "metricas_globales": reporte,
        "cobertura_contexto_dispositivos": desglose_plataformas
    }
    
    ruta_salida = "dashboards/indicadores.json"
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(datos_salida, f, indent=2, ensure_ascii=False)
        
    print(f"\n🎉 ¡Éxito! Archivo de indicadores exportado a: {ruta_salida}")

if __name__ == "__main__":
    exportar()
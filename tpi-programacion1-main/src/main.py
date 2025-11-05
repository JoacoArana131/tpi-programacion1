from api import cargar_datos_csv, exportar_csv, obtener_paises_desde_api
from menu import mostrar_menu
import os

csv_path = "src/paises.csv"

# Si no existe el CSV, lo genera desde la API
if not os.path.exists(csv_path):
    print("📄 No se encontró 'paises.csv'. Generando desde la API...")
    paises = obtener_paises_desde_api()
    if paises:
        exportar_csv(paises, csv_path)
        print("✅ Archivo 'paises.csv' generado correctamente.")
    else:
        print("❌ No se pudo generar el archivo CSV. Abortando.")
        exit()

# Carga los datos desde el CSV (ya sea generado o existente)
paises = cargar_datos_csv(csv_path)

# Llama al menú con los datos cargados
mostrar_menu(paises)
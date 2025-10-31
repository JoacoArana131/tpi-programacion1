# Importa funciones para cargar/exportar datos y mostrar el menú.
from api import cargar_datos_csv, exportar_csv, obtener_paises_desde_api
from menu import mostrar_menu
import os

# Verifica si el archivo 'paises.csv' existe.
# Si no existe, lo genera automáticamente obteniendo los datos desde la API.
if not os.path.exists("paises.csv"):
    print("📄 No se encontró 'paises.csv'. Generando desde la API...")
    paises = obtener_paises_desde_api()
    if paises:

        # Si se obtuvieron datos válidos desde la API, los exporta al archivo CSV.
        exportar_csv(paises, "paises.csv")
        print("✅ Archivo 'paises.csv' generado correctamente.")
    else:

        # Si no se pudieron obtener datos desde la API, muestra un error y termina el programa.
        print("❌ No se pudo generar el archivo CSV. Abortando.")
        exit()

# Inicia el menú principal para que el usuario interactúe con el sistema.
mostrar_menu()




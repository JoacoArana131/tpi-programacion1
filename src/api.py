
def cargar_datos_csv(nombre_archivo):
   
    """
    Carga datos desde un archivo CSV y los convierte en una lista de diccionarios.
    Maneja errores de archivo y conversión de tipos.
    """
    import csv
    paises = []
    try:
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        'nombre': fila['nombre'].strip(),
                        'poblacion': int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente'].strip()
                    }
                    paises.append(pais)
                except ValueError:
                    print(f"⚠️ Error en conversión de tipos en fila: {fila}")
    except FileNotFoundError:
        print(f"❌ Archivo '{nombre_archivo}' no encontrado.")
    return paises

def exportar_csv(paises, nombre_archivo):
    """
    Exporta una lista de países a un archivo CSV.
    """
    import csv
    try:
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
        print(f"✅ Archivo exportado como '{nombre_archivo}'")
    except Exception as e:
        print(f"❌ Error al exportar: {e}")





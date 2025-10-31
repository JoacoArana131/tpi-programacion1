
# Carga datos desde un archivo CSV y los convierte en una lista de diccionarios.
# Valida y convierte los campos 'poblacion' y 'superficie' a enteros.
# Si hay errores en la conversión, los muestra por consola.
# Si el archivo no existe, informa el error y devuelve una lista vacía.

def cargar_datos_csv(nombre_archivo):

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

# Exporta una lista de países a un archivo CSV.
# Escribe los campos 'nombre', 'poblacion', 'superficie' y 'continente'.
# Si ocurre un error durante la escritura, lo informa por consola.

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

# Obtiene datos de países desde una API externa.
# Valida que los campos estén presentes y sean correctos.
# Normaliza los datos (nombre y continente en minúsculas, sin espacios).
# Descarta países con datos inválidos y muestra cuántos fueron omitidos.
# Si falla la conexión, informa el error por consola.        

def obtener_paises_desde_api():
    import requests
    url = "https://api-paises-zilz.onrender.com/paises"
    paises = []
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()

        errores = 0
        for p in datos:
            try:
                nombre = p['pais'].strip().lower()
                poblacion = int(p['poblacion'])
                superficie = int(p['superficie'])
                continente = p['continente'].strip().lower()

                if nombre and poblacion > 0 and superficie > 0:
                    paises.append({
                        'nombre': nombre,
                        'poblacion': poblacion,
                        'superficie': superficie,
                        'continente': continente
                    })
            except (KeyError, ValueError):
                errores += 1

        if errores:
            print(f"⚠️ Se descartaron {errores} países por datos inválidos.")

    except requests.RequestException as e:
        print(f"❌ Error al conectar con la API: {e}")

    return paises




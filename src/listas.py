# Funciones de búsqueda, filtrado, ordenamiento y estadísticas

def buscar_pais(paises, nombre):
    """Busca países por coincidencia parcial en el nombre."""
    return [p for p in paises if nombre.lower() in p['nombre'].lower()]

def filtrar_por_continente(paises, continente):
    """Filtra países por continente exacto."""
    return [p for p in paises if p['continente'].lower() == continente.lower()]

def filtrar_por_poblacion(paises, min_pob, max_pob):
    """Filtra países por rango de población."""
    return [p for p in paises if min_pob <= p['poblacion'] <= max_pob]

def filtrar_por_superficie(paises, min_sup, max_sup):
    """Filtra países por rango de superficie."""
    return [p for p in paises if min_sup <= p['superficie'] <= max_sup]

def ordenar_paises(paises, clave, descendente=False):
    """Ordena países por clave (nombre, población, superficie)."""
    return sorted(paises, key=lambda p: p[clave], reverse=descendente)

def mostrar_paises(lista):
    """Muestra países en formato legible."""
    if not lista:
        print("⚠️ No se encontraron resultados.")
        return
    print("\n📋 Resultados:")
    for p in lista:
        print(f"• {p['nombre']} - {p['poblacion']} hab - {p['superficie']} km² - {p['continente']}")

def mostrar_estadisticas(paises):
    """Calcula y muestra estadísticas básicas."""
    if not paises:
        print("⚠️ No hay datos para mostrar estadísticas.")
        return

    pais_mayor = max(paises, key=lambda p: p['poblacion'])
    pais_menor = min(paises, key=lambda p: p['poblacion'])
    promedio_pob = sum(p['poblacion'] for p in paises) / len(paises)
    promedio_sup = sum(p['superficie'] for p in paises) / len(paises)

    continentes = {}
    for p in paises:
        cont = p['continente']
        continentes[cont] = continentes.get(cont, 0) + 1

    print(f"🔹 País con mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']})")
    print(f"🔹 País con menor población: {pais_menor['nombre']} ({pais_menor['poblacion']})")
    print(f"🔹 Promedio de población: {promedio_pob:.2f}")
    print(f"🔹 Promedio de superficie: {promedio_sup:.2f}")
    print("🔹 Cantidad de países por continente:")
    for cont, cantidad in continentes.items():
        print(f"   - {cont}: {cantidad}")

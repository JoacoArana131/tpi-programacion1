# Menú principal e interacción con el usuario
from api import cargar_datos_csv, exportar_csv
from listas import *
import os

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado():
    """Muestra el encabezado visual del menú."""
    print("=" * 50)
    print("🌍 GESTIÓN DE DATOS DE PAÍSES EN PYTHON 🌍".center(50))
    print("=" * 50)

def mostrar_menu():
    """Muestra el menú principal y gestiona la interacción con el usuario."""
    paises = cargar_datos_csv("paises.csv")

    if not paises:
        print("⚠️ No se cargaron países. Verifique el archivo CSV.")
        return

    while True:
        limpiar_pantalla()
        mostrar_encabezado()
        print("1️⃣ Buscar país por nombre")
        print("2️⃣ Filtrar países")
        print("3️⃣ Ordenar países")
        print("4️⃣ Mostrar estadísticas")
        print("5️⃣ Exportar resultados filtrados")
        print("6️⃣ Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            nombre = input("🔍 Ingrese el nombre o parte del nombre: ")
            resultado = buscar_pais(paises, nombre)
            mostrar_paises(resultado)

        elif opcion == "2":
            print("\n📂 FILTROS DISPONIBLES")
            print("a) Por continente")
            print("b) Por rango de población")
            print("c) Por rango de superficie")
            sub = input("Seleccione filtro (a/b/c): ").lower()

            if sub == "a":
                cont = input("🌎 Ingrese continente: ")
                resultado = filtrar_por_continente(paises, cont)
                mostrar_paises(resultado)

            elif sub == "b":
                try:
                    min_p = int(input("🔢 Población mínima: "))
                    max_p = int(input("🔢 Población máxima: "))
                    resultado = filtrar_por_poblacion(paises, min_p, max_p)
                    mostrar_paises(resultado)
                except ValueError:
                    print("❌ Error: ingrese números válidos.")

            elif sub == "c":
                try:
                    min_s = int(input("📏 Superficie mínima: "))
                    max_s = int(input("📏 Superficie máxima: "))
                    resultado = filtrar_por_superficie(paises, min_s, max_s)
                    mostrar_paises(resultado)
                except ValueError:
                    print("❌ Error: ingrese números válidos.")

            else:
                print("❌ Filtro inválido.")

        elif opcion == "3":
            print("\n🔃 ORDENAR POR")
            print("a) Nombre")
            print("b) Población")
            print("c) Superficie")
            sub = input("Seleccione criterio (a/b/c): ").lower()
            descendente = input("¿Orden descendente? (s/n): ").lower() == 's'

            clave = {'a': 'nombre', 'b': 'poblacion', 'c': 'superficie'}.get(sub)
            if clave:
                resultado = ordenar_paises(paises, clave, descendente)
                mostrar_paises(resultado)
            else:
                print("❌ Criterio inválido.")

        elif opcion == "4":
            mostrar_estadisticas(paises)

        elif opcion == "5":
            nombre_archivo = input("📝 Nombre del archivo CSV a crear: ")
            exportar_csv(paises, nombre_archivo)

        elif opcion == "6":
            print("👋 Gracias por usar el sistema. ¡Hasta pronto!")
            break

        else:
            print("❌ Opción inválida.")

        input("\nPresione ENTER para continuar...")


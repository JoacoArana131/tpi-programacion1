# Importa funciones para cargar datos, procesarlos y mostrar el menú.

from api import cargar_datos_csv
from listas import *
import os

# Limpia la consola según el sistema operativo (Windows o Unix).

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Muestra el encabezado decorativo del sistema en la consola.

def mostrar_encabezado():
    """Muestra el encabezado visual del menú."""
    print("=" * 50)
    print("🌍 GESTIÓN DE DATOS DE PAÍSES EN PYTHON 🌍".center(50))
    print("=" * 50)

# Función principal que muestra el menú y gestiona la interacción con el usuario.
# Carga los datos desde el CSV y permite buscar, filtrar, ordenar y ver estadísticas.

def mostrar_menu(paises):
    
    # Carga los datos desde el archivo CSV.
    # Si no se pudo cargar, muestra un mensaje de error y termina el menú.


    if not paises:
        print("⚠️ No se cargaron países. Verifique el archivo CSV.")
        return

    # Bucle principal del menú.
    # Se repite hasta que el usuario elija salir.
    # Muestra las opciones disponibles y gestiona la interacción.

    while True:
        limpiar_pantalla()
        mostrar_encabezado()
        print("1️⃣ Buscar país por nombre")
        print("2️⃣ Filtrar países")
        print("3️⃣ Ordenar países")
        print("4️⃣ Mostrar estadísticas")
        print("5️⃣ Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción (1-5): ").strip()

        # Opción 1: Buscar países por nombre parcial.
        # Muestra el resultado encontrado en formato legible.

        if opcion == "1":
            nombre = input("🔍 Ingrese el nombre o parte del nombre: ").strip()
            resultado = buscar_pais(paises, nombre)
            mostrar_paises(resultado)

         # Opción 2: Aplicar filtros.
         # Permite filtrar por continente, población o superficie.

        elif opcion == "2":
            print("\n📂 FILTROS DISPONIBLES")
            print("a) Por continente")
             
            print("b) Por rango de población")
            
            print("c) Por rango de superficie")
            sub = input("Seleccione filtro (a/b/c): ").lower().strip()

             # Filtra por continente exacto. 
            if sub == "a":
                cont = input("🌎 Ingrese continente: ").strip()
                resultado = filtrar_por_continente(paises, cont)
                mostrar_paises(resultado)

             # Filtra por rango de población, con validación de números.
            elif sub == "b":
                try:
                    min_p = int(input("🔢 Población mínima: ").strip())
                    max_p = int(input("🔢 Población máxima: ").strip())
                    resultado = filtrar_por_poblacion(paises, min_p, max_p)
                    mostrar_paises(resultado)
                except ValueError:
                    print("❌ Error: ingrese números válidos.")
             
             # Filtra por rango de superficie, con validación de números.
            elif sub == "c":
                try:
                    min_s = int(input("📏 Superficie mínima: ").strip())
                    max_s = int(input("📏 Superficie máxima: ").strip())
                    resultado = filtrar_por_superficie(paises, min_s, max_s)
                    mostrar_paises(resultado)
                except ValueError:
                    print("❌ Error: ingrese números válidos.")

            else:
                print("❌ Filtro inválido.")

         # Opción 3: Ordenar países.
         # Permite ordenar por nombre, población o superficie.
         # El usuario puede elegir orden ascendente o descendente.

        elif opcion == "3":
            print("\n🔃 ORDENAR POR")
            print("a) Nombre")
            print("b) Población")
            print("c) Superficie")
            sub = input("Seleccione criterio (a/b/c): ").lower().strip()
            descendente = input("¿Orden descendente? (s/n): ").lower().strip() == 's'

            clave = {'a': 'nombre', 'b': 'poblacion', 'c': 'superficie'}.get(sub)
            if clave:
                resultado = ordenar_paises(paises, clave, descendente)
                mostrar_paises(resultado)
            else:
                print("❌ Criterio inválido.")

         # Opción 4: Mostrar estadísticas básicas.
         # Calcula país con mayor y menor población, promedios y cantidad por continente.

        elif opcion == "4":
            mostrar_estadisticas(paises)

         # Opción 5: Salir del sistema.
         # Finaliza el programa con un mensaje de despedida.

        elif opcion == "5":
            print("👋 Gracias por usar el sistema. ¡Hasta pronto!")
            break

           # Opción inválida: informa al usuario y espera ENTER para continuar.
           
        else:
            print("❌ Opción inválida.")

        input("\nPresione ENTER para continuar...")


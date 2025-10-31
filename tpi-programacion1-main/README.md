INTEGRADOR DE PROGRAMACION 1 

Participantes: ARANA JOAQUIN - CORDOBA EZEQUIEL 

# 🌍 Gestión de Datos de Países en Python

Este proyecto consiste en una aplicación de consola desarrollada en Python que permite gestionar información sobre países. Utiliza estructuras de datos como listas y diccionarios, lectura desde archivos CSV, y funciones para aplicar filtros, ordenamientos y estadísticas.

El sistema está modularizado en archivos separados y permite al usuario interactuar mediante un menú para realizar búsquedas, aplicar criterios de filtrado, ordenar los datos y visualizar indicadores clave.

## 🛠️ Estructura del proyecto

- `main.py`: punto de entrada, genera el CSV desde una API externa si no existe.
- `menu.py`: gestiona la interacción con el usuario y muestra el menú principal.
- `listas.py`: contiene funciones de búsqueda, filtrado, ordenamiento y estadísticas.
- `api.py`: obtiene datos de países desde una API pública y los exporta a CSV.
- `paises.csv`: archivo con los datos base (nombre, población, superficie, continente).

## 📂 Funcionalidades principales

- 🔍 Buscar país por nombre (coincidencia parcial).
- 📂 Filtrar países por:
  - Continente
  - Rango de población
  - Rango de superficie
- 🔃 Ordenar países por:
  - Nombre
  - Población
  - Superficie (ascendente o descendente)
- 📊 Mostrar estadísticas:
  - País con mayor y menor población
  - Promedio de población
  - Promedio de superficie
  - Cantidad de países por continente

---

## ▶️ Ejecución

1. Asegurarse de tener Python 3.x instalado, haber escrito "pip install requests
" en Consola, Terminal o PowerShell  y/o Visual Studio Code (opcional)
2. Si no tiene Visual Studio Code, escriba en su PowerShell, Terminal o Consola:

   cd *ruta de la carpeta src*

o en Linux/macOS:

   cd ~*ruta de la carpeta src*

3. Ejecutar el programa desde `main.py`

Si lo esta haciendo en Consola, Terminal o PowerShell, escriba:

   python main.py

4. Al ejectuar el programa, si el archivo paises.csv no existe, se generará automáticamente desde la API.

5. Use el menú interactivo para:

- Buscar países

  Ejemplo: 
  🔍 Ingrese el nombre o parte del nombre: vene

  📋 Resultados:
   • Venezuela - 28720000 hab - 916445 km² - america

- Aplicar filtros

  Ejemplo:
  📂 FILTROS DISPONIBLES
   a) Por continente
   b) Por rango de población
   c) Por rango de superficie
   Seleccione filtro (a/b/c): a

  🌎 Ingrese continente: america

  📋 Resultados:
  • Argentina - 45851378 hab - 2736690 km² - america
  • Bolivia - 12637909 hab - 1083300 km² - america
  ...

- Ordenar por distintos criterios

  Ejemplo:
 🔃 ORDENAR POR
  a) Nombre
  b) Población
  c) Superficie
  Seleccione criterio (a/b/c): a

  ¿Orden descendente? (s/n): si

  📋 Resultados:
  • Afganistan - 42594582 hab - 652230 km² - asia
  • Albania - 2800000 hab - 28748 km² - europa
  ...

  - Ver estadísticas

  Ejemplo:
  🔹 País con mayor población: China (1444216107)
  ...

6. Presione ENTER para volver al menú después de cada operación.


api.py, main.py, Informe, Marco Teorico y Test/Arreglos hechos por Cordoba Ezequiel
lista.py, menu.py, capturas y readme hecho por Arana Joaquín





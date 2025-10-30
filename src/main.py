import os
print("📁 Carpeta actual:", os.getcwd())
print("📄 Existe paises.csv:", os.path.exists("paises.csv"))

# Punto de entrada del programa
from menu import mostrar_menu

if __name__ == "__main__":
    mostrar_menu()



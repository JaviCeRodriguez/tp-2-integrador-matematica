from modulos import login, resumen, mapa, datos

def mostrar_menu():
    print("""
==================================================
  🧮 TRABAJO INTEGRADOR - MATEMÁTICA Y PROGRAMACIÓN
==================================================

Seleccione la unidad que desea explorar:

1️⃣  Unidad 1 - Álgebra de Boole (Inicio de sesión)
2️⃣  Unidad 3 - Lógica aplicada a rutas
3️⃣  Unidad 6 - Grafos y análisis de rutas
0️⃣  Salir
""")

def main():
    # Cargar datos comunes
    rutas = datos.obtener_rutas()
    grafo = datos.obtener_mapa(rutas)
    sesion_iniciada = False

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            if not sesion_iniciada:
                print("\n🔹 UNIDAD 1: Álgebra de Boole aplicada a decisiones lógicas 🔹")
                print("Simulación de login con verificación de email y contraseña.\n")
                sesion_iniciada = login.iniciar_sesion()
            else:
                print("Sesión iniciada previamente! Seleccione otra opción.")

        elif opcion == "2":
            if sesion_iniciada:
                print("\n🔹 UNIDAD 3: Lógica y validación de rutas 🔹")
                print("Aplicación de operadores lógicos (AND, OR, NOT) para analizar las rutas.\n")
                resumen.validar_rutas(rutas=rutas)
            else:
                print("Inicie sesión para acceder a esta opción.")

        elif opcion == "3":
            if sesion_iniciada:
                print("\n🔹 UNIDAD 6: Grafos y Árboles 🔹")
                print("Análisis de rutas mediante grafos ponderados (distancia y tráfico).\n")
                mapa.analizar_rutas(rutas, grafo)
            else:
                print("Inicie sesión para acceder a esta opción.")

        elif opcion == "0":
            print("\n👋 ¡Gracias por explorar el trabajo integrador! Hasta luego.")
            break

        else:
            print("\n⚠️  Opción no válida. Intente nuevamente.\n")

        input("\nPresione Enter para volver al menú principal...")

if __name__ == "__main__":
    main()

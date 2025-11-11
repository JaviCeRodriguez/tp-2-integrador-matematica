def validar_rutas(datos):
    if not datos:
        print("🚨\nError: No hay datos cargados.")
        return

    print("=== Validación de rutas Tigre → La Plata ===\n")

    for nombre, datos in rutas.items():
        print(f"➡️  {nombre.upper()} | Trayecto: {' → '.join(datos['trayecto'])}")

        # Validación 1: Es turística y no pasa por CABA
        if datos["turistica"] and not datos["pasa_por_caba"]:
            print("✅ Es una ruta turística que NO pasa por CABA.")
        
        # Validación 2: Es turística y fue recorrida
        if datos["turistica"] and datos["recorrida"]:
            print("🏞️  Es una ruta turística que ya fue recorrida.")
        
        # Validación 3: No es turística
        if not datos["turistica"]:
            print("🚗 Esta ruta NO es turística.")
        
        print("-" * 50)


if __name__ == "__main__":
    from datos import obtener_rutas

    rutas = obtener_rutas()
    validar_rutas(datos=rutas)
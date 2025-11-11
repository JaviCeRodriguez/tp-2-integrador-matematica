import random

def analizar_rutas(rutas, grafo):
    # Función auxiliar: calcular el tiempo total de una ruta
    def calcular_tiempo(trayecto):
        tiempo_total = 0
        for i in range(len(trayecto) - 1):
            origen, destino = trayecto[i], trayecto[i + 1]
            conexiones = grafo.get(origen, [])
            # Buscar el enlace correspondiente
            for ciudad, tiempo in conexiones:
                if ciudad == destino:
                    tiempo_total += tiempo
                    break
        return tiempo_total

    print("=== ANÁLISIS DE RUTAS ===\n")

    ruta_mas_larga = None
    ruta_mas_lugares = None
    max_tiempo = 0
    max_lugares = 0

    for nombre, info in rutas.items():
        trayecto = info['trayecto']
        tiempo_total = calcular_tiempo(trayecto)
        cantidad_lugares = len(trayecto)

        print(f"{nombre.upper()}: {' => '.join(trayecto)}")
        print(f" - Tiempo estimado total: {tiempo_total} minutos")
        print(f" - Cantidad de lugares: {cantidad_lugares}")
        print(f" - Recorrida: {'Sí' if info['recorrida'] else 'No'}")
        print(f" - Turística: {'Sí' if info['turistica'] else 'No'}")
        print(f" - Pasa por CABA: {'Sí' if info['pasa_por_caba'] else 'No'}\n")

        # Determinar ruta más larga
        if tiempo_total > max_tiempo:
            max_tiempo = tiempo_total
            ruta_mas_larga = nombre

        # Determinar ruta con más lugares
        if cantidad_lugares > max_lugares:
            max_lugares = cantidad_lugares
            ruta_mas_lugares = nombre

    print("=== RESULTADOS ===\n")
    print(f"Ruta que toma más tiempo: {ruta_mas_larga} ({max_tiempo} minutos)")
    print(f"Ruta que visita más lugares: {ruta_mas_lugares} ({max_lugares} lugares)\n")

    # Generar una nueva ruta sugerida
    nueva_ruta = recomendar_nueva_ruta(rutas, grafo)
    print("=== NUEVA RUTA RECOMENDADA ===")
    print(" => ".join(nueva_ruta))


def recomendar_nueva_ruta(rutas, grafo):
    rutas_existentes = [set(info['trayecto']) for info in rutas.values()]

    # Intentar formar una ruta no repetida con base en conexiones intermedias
    for origen, conexiones in grafo.items():
        for destino, _ in conexiones:
            # Crear una ruta tentativa de 3 pasos (si hay conexiones desde destino)
            if destino in grafo:
                for siguiente, _ in grafo[destino]:
                    # Evitar repetir el origen
                    if siguiente != origen:
                        candidata = [origen, destino, siguiente]

                        # Comprobar si esta combinación ya aparece completa en alguna ruta
                        if not any(set(candidata).issubset(r) for r in rutas_existentes):
                            return candidata

    # Si no se encontró combinación nueva, crear una ruta extendida alternativa
    nodos = list(grafo.keys())
    if len(nodos) >= 3:
        return [nodos[0], nodos[-2], nodos[-1]]

    return ["No se pudo generar una nueva ruta"]


if __name__ == "__main__":
    from datos import obtener_rutas, obtener_mapa

    rutas = obtener_rutas()
    print("Rutas:", rutas)
    mapa = obtener_mapa(rutas)
    print("Mapa (Grafo):", mapa)

    analizar_rutas(rutas, mapa)

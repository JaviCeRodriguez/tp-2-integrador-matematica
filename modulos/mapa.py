def calcular_tiempo(trayecto, grafo):
    """
    Calcula el tiempo total de un trayecto sumando los tiempos de cada segmento.
    """
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


def analizar_rutas(rutas, grafo):

    print("=== ANÁLISIS DE RUTAS ===\n")

    ruta_mas_larga = None
    ruta_mas_lugares = None
    max_tiempo = 0
    max_lugares = 0

    for nombre, info in rutas.items():
        trayecto = info['trayecto']
        tiempo_total = calcular_tiempo(trayecto, grafo)
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
    
    # Encontrar la mejor ruta existente (más rápida)
    mejor_ruta, mejor_tiempo = encontrar_mejor_ruta_existente(rutas, grafo)
    if mejor_ruta:
        print("=== MEJOR RUTA EXISTENTE ===")
        print(f"Ruta más rápida: {' => '.join(mejor_ruta)}")
        print(f"Tiempo: {mejor_tiempo} minutos\n")

    # Generar una nueva ruta sugerida usando Dijkstra
    nueva_ruta = recomendar_nueva_ruta(rutas, grafo)
    print("=== NUEVA RUTA RECOMENDADA (usando Dijkstra) ===")
    if nueva_ruta and nueva_ruta[0] != "No se pudo generar una nueva ruta":
        tiempo_nueva = calcular_tiempo(nueva_ruta, grafo)
        print(f" => ".join(nueva_ruta))
        print(f"Tiempo estimado: {tiempo_nueva} minutos")
    else:
        print(" => ".join(nueva_ruta))
    print()


def encontrar_ruta_mas_rapida_dijkstra(origen, destino, grafo):
    """
    Algoritmo de Dijkstra para encontrar la ruta MÁS RÁPIDA (menor tiempo total)
    entre dos ciudades en un grafo ponderado.
    
    Características del algoritmo:
    - Considera los tiempos de viaje (pesos de las aristas)
    - Garantiza encontrar la ruta con menor tiempo total
    - Usa una cola de prioridad (heap) para explorar siempre el camino más corto primero
    - Es el algoritmo estándar para caminos más cortos en grafos ponderados
    
    Complejidad: O(V²) donde V = vértices (ciudades)
    """
    import heapq
    
    # Diccionario para almacenar el tiempo mínimo hasta cada ciudad
    tiempos = {ciudad: float('inf') for ciudad in grafo.keys()}
    tiempos[origen] = 0
    
    # Diccionario para reconstruir la ruta
    predecesores = {}
    
    # Cola de prioridad: (tiempo_acumulado, ciudad_actual)
    cola = [(0, origen)]
    visitados = set()
    
    while cola:
        tiempo_actual, ciudad_actual = heapq.heappop(cola)
        
        # Si ya visitamos esta ciudad con un tiempo menor, la saltamos
        if ciudad_actual in visitados:
            continue
        
        visitados.add(ciudad_actual)
        
        # Si llegamos al destino, reconstruimos la ruta
        if ciudad_actual == destino:
            ruta = []
            ciudad = destino
            while ciudad is not None:
                ruta.append(ciudad)
                ciudad = predecesores.get(ciudad)
            return ruta[::-1]  # Invertir para tener origen -> destino
        
        # Explorar vecinos
        if ciudad_actual in grafo:
            for ciudad_vecina, tiempo_viaje in grafo[ciudad_actual]:
                if ciudad_vecina not in visitados:
                    nuevo_tiempo = tiempo_actual + tiempo_viaje
                    
                    # Si encontramos un camino más corto, lo actualizamos
                    if nuevo_tiempo < tiempos[ciudad_vecina]:
                        tiempos[ciudad_vecina] = nuevo_tiempo
                        predecesores[ciudad_vecina] = ciudad_actual
                        heapq.heappush(cola, (nuevo_tiempo, ciudad_vecina))
    
    return None  # No se encontró ruta


def encontrar_mejor_ruta_existente(rutas, grafo, destino="La Plata"):
    """
    Encuentra la mejor ruta entre las rutas existentes que terminan en el destino.
    Compara directamente los tiempos de cada ruta.
    """
    mejor_ruta = None
    menor_tiempo = float('inf')
    
    for nombre, info in rutas.items():
        trayecto = info['trayecto']
        # Solo considerar rutas que terminan en el destino
        if trayecto and trayecto[-1] == destino:
            tiempo = calcular_tiempo(trayecto, grafo)
            if tiempo < menor_tiempo:
                menor_tiempo = tiempo
                mejor_ruta = trayecto
    
    return mejor_ruta, menor_tiempo


def recomendar_nueva_ruta(rutas, grafo):
    """
    Encuentra una nueva ruta usando el algoritmo de Dijkstra.
    Si todas las rutas van al mismo destino, usa Dijkstra para encontrar la ruta más rápida.
    """
    # Detectar el destino común
    destinos = [info['trayecto'][-1] for info in rutas.values() if info['trayecto']]
    destino_comun = destinos[0] if len(set(destinos)) == 1 else None
    
    # Detectar el origen común
    origenes = [info['trayecto'][0] for info in rutas.values() if info['trayecto']]
    origen_comun = origenes[0] if len(set(origenes)) == 1 else None
    
    # Si hay origen y destino comunes, usar Dijkstra para encontrar la ruta más rápida
    if origen_comun and destino_comun:
        ruta_optima = encontrar_ruta_mas_rapida_dijkstra(origen_comun, destino_comun, grafo)
        if ruta_optima:
            # Verificar si esta ruta ya existe
            rutas_existentes = [info['trayecto'] for info in rutas.values()]
            if ruta_optima not in rutas_existentes:
                return ruta_optima
    
    # Si la ruta óptima ya existe, intentar encontrar rutas alternativas
    # explorando diferentes orígenes y destinos
    ciudades = list(grafo.keys())
    rutas_existentes = [info['trayecto'] for info in rutas.values()]
    
    # Buscar rutas entre diferentes pares de ciudades
    for origen in ciudades:
        for destino in ciudades:
            if origen != destino:
                ruta_candidata = encontrar_ruta_mas_rapida_dijkstra(origen, destino, grafo)
                if ruta_candidata and len(ruta_candidata) >= 3:
                    # Verificar si esta ruta es diferente a las existentes
                    if ruta_candidata not in rutas_existentes:
                        return ruta_candidata
    
    # Fallback: devolver una ruta simple si no se encontró ninguna nueva
    if len(ciudades) >= 3:
        return [ciudades[0], ciudades[-2], ciudades[-1]]
    
    return ["No se pudo generar una nueva ruta"]


if __name__ == "__main__":
    from datos import obtener_rutas, obtener_mapa

    rutas = obtener_rutas()
    print("Rutas:", rutas)
    mapa = obtener_mapa(rutas)
    print("Mapa (Grafo):", mapa)

    analizar_rutas(rutas, mapa)

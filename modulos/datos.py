import random


def obtener_rutas():
    rutas = {
        "ruta_1": {
            "trayecto": ["Tigre", "San Fernando", "Vicente Lopez", "Belgrano", "Quilmes", "La Plata"],
            "recorrida": True,
            "turistica": False,
            "pasa_por_caba": True
        },
        "ruta_2": {
            "trayecto": ["Tigre", "Palermo", "Belgrano", "Quilmes", "La Plata"],
            "recorrida": False,
            "turistica": False,
            "pasa_por_caba": True
        },
        "ruta_3": {
            "trayecto": ["Tigre", "San Fernando", "Tandil", "Quilmes", "La Plata"],
            "recorrida": True,
            "turistica": True,
            "pasa_por_caba": False
        }
    }

    return rutas


def obtener_mapa(datos):
    grafo = {}

    def agregar_conexion(origen, destino, tiempo):
        # Evita duplicados comprobando si el enlace ya existe
        if origen not in grafo:
            grafo[origen] = []
        if destino not in grafo:
            grafo[destino] = []

        # Verificar si la conexión ya fue agregada (en cualquier sentido)
        if not any(vecino == destino for vecino, _ in grafo[origen]):
            grafo[origen].append((destino, tiempo))
        if not any(vecino == origen for vecino, _ in grafo[destino]):
            grafo[destino].append((origen, tiempo))
    
    for _, datos in rutas.items():
        trayecto = datos["trayecto"]
        for i in range(len(trayecto) - 1):
            origen = trayecto[i]
            destino = trayecto[i + 1]

            # Generar pesos aleatorios
            distancia = random.randint(10, 60)   # km
            trafico = random.randint(1, 5)       # nivel de tráfico
            tiempo = distancia * trafico

            agregar_conexion(origen, destino, tiempo)

    return grafo


if __name__ == "__main__":
    rutas = obtener_rutas()
    mapa = obtener_mapa(rutas)
    print("datos", mapa)
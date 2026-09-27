# busqueda.py
# Algoritmo de búsqueda heurística A*

from rutas import obtener_vecinos

def heuristica(estacion, destino):
    """
    Función heurística.

    Para este proyecto utilizamos una estimación
    sencilla basada en una tabla de valores.
    """

    estimaciones = {
        ("Atocha", "Ciudad Universitaria"): 15,
        ("Sol", "Ciudad Universitaria"): 12,
        ("Nuevos Ministerios", "Ciudad Universitaria"): 10,
        ("Chamartín", "Ciudad Universitaria"): 12,
        ("Gran Vía", "Ciudad Universitaria"): 7,
        ("Moncloa", "Ciudad Universitaria"): 5,

        ("Atocha", "Chamartín"): 15,
        ("Sol", "Chamartín"): 10,
        ("Nuevos Ministerios", "Chamartín"): 7,

        ("Atocha", "Moncloa"): 12,
        ("Sol", "Moncloa"): 9,
        ("Gran Vía", "Moncloa"): 9
    }

    return estimaciones.get((estacion, destino), 0)


def reconstruir_ruta(padres, actual):
    """Reconstruye la ruta desde el destino hasta el origen."""

    ruta = [actual]

    while actual in padres:
        actual = padres[actual]
        ruta.append(actual)

    ruta.reverse()

    return ruta


def a_estrella(origen, destino):
    """
    Algoritmo A* para encontrar una ruta de coste reducido
    entre un origen y un destino.
    """

    abiertos = [origen]

    padres = {}

    coste_g = {
        origen: 0
    }

    coste_f = {
        origen: heuristica(origen, destino)
    }

    cerrados = set()

    while abiertos:

        # Seleccionamos el nodo con menor f(n)
        actual = min(
            abiertos,
            key=lambda estacion: coste_f.get(estacion, float("inf"))
        )

        # Hemos llegado al destino
        if actual == destino:
            ruta = reconstruir_ruta(padres, actual)
            return ruta, coste_g[actual]

        abiertos.remove(actual)
        cerrados.add(actual)

        # Analizamos los vecinos
        for vecino, coste in obtener_vecinos(actual):

            if vecino in cerrados:
                continue

            nuevo_coste = coste_g[actual] + coste

            if vecino not in abiertos:
                abiertos.append(vecino)

            elif nuevo_coste >= coste_g.get(
                vecino,
                float("inf")
            ):
                continue

            # Guardamos la mejor ruta conocida
            padres[vecino] = actual
            coste_g[vecino] = nuevo_coste

            coste_f[vecino] = (
                nuevo_coste +
                heuristica(vecino, destino)
            )

    # No existe una ruta
    return None, None
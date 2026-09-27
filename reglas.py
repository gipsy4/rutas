# reglas.py
# Reglas lógicas utilizadas por el sistema

from rutas import conexiones


def estacion_existe(estacion):
    """Comprueba si una estación existe en la base de conocimiento."""
    return estacion in conexiones


def existe_conexion(origen, destino):
    """Comprueba si existe una conexión directa entre dos estaciones."""

    if origen not in conexiones:
        return False

    for estacion, coste in conexiones[origen]:
        if estacion == destino:
            return True

    return False


def obtener_coste_conexion(origen, destino):
    """Devuelve el coste de una conexión directa."""

    if origen in conexiones:
        for estacion, coste in conexiones[origen]:
            if estacion == destino:
                return coste

    return None
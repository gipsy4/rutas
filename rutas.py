# conocimiento.py
# Base de conocimiento del sistema de transporte

conexiones = {
    "Atocha": [
        ("Sol", 4)
    ],

    "Sol": [
        ("Atocha", 4),
        ("Nuevos Ministerios", 8),
        ("Gran Vía", 3)
    ],

    "Nuevos Ministerios": [
        ("Sol", 8),
        ("Chamartín", 7)
    ],

    "Chamartín": [
        ("Nuevos Ministerios", 7)
    ],

    "Gran Vía": [
        ("Sol", 3),
        ("Moncloa", 9)
    ],

    "Moncloa": [
        ("Gran Vía", 9),
        ("Ciudad Universitaria", 5)
    ],

    "Ciudad Universitaria": [
        ("Moncloa", 5)
    ]
}


def obtener_estaciones():
    """Devuelve todas las estaciones disponibles."""
    return list(conexiones.keys())


def obtener_vecinos(estacion):
    """Devuelve las estaciones conectadas y sus costes."""
    return conexiones.get(estacion, [])
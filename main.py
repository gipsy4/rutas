# main.py
# Programa principal del sistema inteligente de rutas

from rutas import obtener_estaciones
from reglas import estacion_existe
from inteligenciaArtificial import a_estrella


def mostrar_estaciones():
    """Muestra las estaciones disponibles."""

    print("\nEstaciones disponibles:")

    for estacion in obtener_estaciones():
        print(f"- {estacion}")


def ejecutar_sistema():

    print("=" * 50)
    print(" SISTEMA INTELIGENTE DE BÚSQUEDA DE RUTAS")
    print("=" * 50)

    mostrar_estaciones()

    origen = input("\nIntroduce la estación de origen: ").strip()
    destino = input("Introduce la estación de destino: ").strip()

    # Comprobación de las estaciones
    if not estacion_existe(origen):
        print(f"\nError: la estación '{origen}' no existe.")

        return

    if not estacion_existe(destino):
        print(f"\nError: la estación '{destino}' no existe.")

        return

    # Caso en el que origen y destino son iguales
    if origen == destino:
        print("\nEl origen y el destino son la misma estación.")
        print("Coste total: 0 minutos.")

        return

    # Ejecutamos A*
    ruta, coste = a_estrella(origen, destino)

    if ruta is None:
        print("\nNo se ha encontrado una ruta disponible.")

        return

    print("\n" + "=" * 50)
    print(" RUTA ENCONTRADA")
    print("=" * 50)

    print("\n" + " -> ".join(ruta))

    print(f"\nNúmero de estaciones: {len(ruta)}")
    print(f"Tiempo estimado: {coste} minutos")

    print("=" * 50)


if __name__ == "__main__":
    ejecutar_sistema()
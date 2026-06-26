from models import Estado, Proyecto


# ===== UTILIDADES =====

def imprimir_titulo(texto: str) -> None:
    linea = "=" * (len(texto) + 4)
    print(f"\n{linea}")
    print(f"  {texto}")
    print(f"{linea}")


def imprimir_separador() -> None:
    print("\n")


def mostrar_proyecto(proyecto: Proyecto) -> None:
    for campo, valor in proyecto.items():
        # Si el valor es un Enum mostramos su texto legible (.value)
        v = valor.value if isinstance(valor, Estado) else valor
        print(f"     {campo}: {v}")


def listar_proyectos(proyectos: list[Proyecto]) -> None:
    for i, p in enumerate(proyectos, 1):
        print(f"  {i}. {p['nombre']}")


# ===== SELECCIÓN =====

def seleccionar_estado() -> Estado:
    estados = list(Estado)
    imprimir_titulo("SELECCIONA UN ESTADO")
    for i, e in enumerate(estados, 1):
        print(f"  {i}. {e.value}")
    imprimir_separador()

    while True:
        try:
            eleccion = int(input("Elige estado: ")) - 1
        except ValueError:
            print("Ingresa un número.")
            continue

        if 0 <= eleccion < len(estados):
            return estados[eleccion]

        print("Opción inválida.")


def seleccionar_campo(proyecto: Proyecto) -> str | None:
    campos = [k for k in proyecto.keys() if k != "nombre"]

    while True:
        imprimir_titulo("¿QUÉ CAMPO ACTUALIZAR?")
        for i, campo in enumerate(campos, 1):
            print(f"  {i}. {campo}")
        print(f"  {len(campos) + 1}. Cancelar")
        imprimir_separador()

        try:
            eleccion = int(input("Elige: "))
        except ValueError:
            print("Ingresa un número.")
            continue

        if eleccion == len(campos) + 1:
            return None

        if 1 <= eleccion <= len(campos):
            return campos[eleccion - 1]

        print("Opción inválida.")

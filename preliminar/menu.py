from models import Estado, Proyecto
from repository import actualizar, agregar, buscar_indice, eliminar
from ui import (
    imprimir_separador,
    imprimir_titulo,
    listar_proyectos,
    mostrar_proyecto,
    seleccionar_campo,
    seleccionar_estado,
)

# ===== FLUJOS =====


def agregar_proyecto(proyectos: list[Proyecto]) -> None:
    imprimir_titulo("AGREGAR PROYECTO")
    nombre = input("Nombre: ")
    cliente = input("Cliente: ")
    fecha = input("Fecha inicio (DD-MM-YYYY): ")
    estado = Estado.POR_HACER

    proyecto: Proyecto = {
        "nombre": nombre,
        "cliente": cliente,
        "estado": estado,
        "fecha_inicio": fecha,
    }

    agregar(proyectos, proyecto)
    imprimir_separador()
    print(f"Proyecto '{nombre}' agregado.")


def mostrar_proyectos(proyectos: list[Proyecto]) -> None:
    imprimir_titulo("PROYECTOS DISPONIBLES")
    if not proyectos:
        print("  No hay proyectos.")
        return

    # enumerate muestra el indice + el elemento,
    # otra opcion es usar range(len(lista))
    for i, proyecto in enumerate(proyectos, 1):
        print(f"\n  {i}.")
        mostrar_proyecto(proyecto)
    imprimir_separador()


def actualizar_proyecto(proyectos: list[Proyecto]) -> None:
    imprimir_titulo("ACTUALIZAR PROYECTO")
    if not proyectos:
        print("  No hay proyectos.")
        return

    listar_proyectos(proyectos)
    imprimir_separador()

    try:
        idx = int(input("Número de proyecto: ")) - 1
    except ValueError:
        print("Ingresa un número válido.")
        return

    if not (0 <= idx < len(proyectos)):
        print("Índice fuera de rango.")
        return

    campo = seleccionar_campo(proyectos[idx])
    if campo is None:
        return

    valor = (
        seleccionar_estado()
        if campo == "estado"
        else input(f"Nuevo valor para '{campo}': ")
    )
    actualizar(proyectos, idx, campo, valor)
    imprimir_separador()
    print("Actualizado.")


def eliminar_proyecto(proyectos: list[Proyecto]) -> None:
    imprimir_titulo("ELIMINAR PROYECTO")
    nombre = input("Nombre del proyecto a eliminar: ")
    idx = buscar_indice(proyectos, nombre)

    if idx is None:
        print("Proyecto no encontrado.")
        return

    eliminar(proyectos, idx)
    imprimir_separador()
    print(f"'{nombre}' eliminado.")


def buscar_proyecto(proyectos: list[Proyecto]) -> None:
    imprimir_titulo("BUSCAR PROYECTO")
    nombre = input("Nombre a buscar: ")
    idx = buscar_indice(proyectos, nombre)

    if idx is None:
        print("Proyecto no encontrado.")
        return

    imprimir_separador()
    mostrar_proyecto(proyectos[idx])


# ===== MENÚ =====

OPCIONES = [
    ("Agregar proyecto", agregar_proyecto),
    ("Mostrar proyectos", mostrar_proyectos),
    ("Actualizar proyecto", actualizar_proyecto),
    ("Eliminar proyecto", eliminar_proyecto),
    ("Buscar proyecto", buscar_proyecto),
]


def _mostrar_menu() -> None:
    imprimir_titulo("ADMINISTRA TU INVENTARIO")
    # enumerate muestra el indice + el elemento,
    # otra opcion es usar range(len(lista))
    for i, (label, _) in enumerate(OPCIONES, 1):
        print(f"  {i}. {label}")
    print(f"  {len(OPCIONES) + 1}. Salir")
    imprimir_separador()


def menu_proyectos(proyectos: list[Proyecto]) -> None:
    while True:
        _mostrar_menu()

        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Ingresa un número.")
            continue

        if opcion == len(OPCIONES) + 1:
            break

        if 1 <= opcion <= len(OPCIONES):
            _, accion = OPCIONES[opcion - 1]
            accion(proyectos)
        else:
            print("Opción inválida.")

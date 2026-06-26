from models import Estado, Proyecto


def agregar(lista: list[Proyecto], proyecto: Proyecto) -> None:
    lista.append(proyecto)


def buscar_indice(lista: list[Proyecto], nombre: str) -> int | None:
    # Recorre la lista buscando coincidencia por nombre (sin importar mayúsculas)
    # Retorna el índice si lo encuentra, None si no existe
    for i, p in enumerate(lista):
        if p["nombre"].lower() == nombre.lower():
            return i
    return None


def actualizar(
    lista: list[Proyecto], indice: int, campo: str, valor: Estado | str
) -> None:
    lista[indice][campo] = valor


def eliminar(lista: list[Proyecto], indice: int) -> None:
    lista.pop(indice)

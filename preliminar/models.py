from enum import Enum
from typing import TypedDict


class Estado(Enum):
    POR_HACER   = "Por hacer"
    EN_PROGRESO = "En progreso"
    TERMINADO   = "Terminado"


class Proyecto(TypedDict):
    nombre: str
    cliente: str
    estado: Estado
    fecha_inicio: str

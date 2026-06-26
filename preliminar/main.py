from menu import menu_proyectos
from models import Proyecto

# ===== ENTRADA =====

if __name__ == "__main__":
    proyectos: list[Proyecto] = []
    menu_proyectos(proyectos)

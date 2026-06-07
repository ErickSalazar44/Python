# Identación
# Nomenclatura
# Comentarios y Docstring

"""
Lo recomendado son 4 espacios para python, los archivos
los archivos se escriben con snake_case
"""

# Ide

def my_function():
    if True:
        print("Esto tiene 2 niveles de identación (8 espacios)")

# Nomenclatura

    """
    Variables Funciones // snake_case
    Constantes          // UPPER_SNAKE_CASE
    Clases              // PascalCase
    Módulos(.py)        // snake_case
    """

# Comentarios => existen 2 con "#" p con 3 """ """

def calculate_tax(amount: float) -> float:
    """
    Calcula el impuesto basado en el estándar regional 2026.
    
    Args:
        amount (float): El monto base para el cálculo.

    Returns:
        float: Monto Total con impuestos incluidos
    """
    return amount * 1.18


print(calculate_tax.__doc__)
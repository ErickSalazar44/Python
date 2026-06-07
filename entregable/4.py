"""
4. Cálculo de bonificación por desempeño El programa debe pedir un puntaje de
   evaluación entre 0 y 100. Dependiendo del valor, debe indicar el porcentaje
   de bonificación: 20%, 10%, 5% o ninguna.
"""

PUNTAJE = {
    "20%": (90, 100),
    "10%": (80, 89),
    "5%": (70, 79)
}

def calcular_bonificacion(puntaje):
    for bonificacion, (minimo, maximo) in PUNTAJE.items():
        if minimo <= puntaje <= maximo:
            return f"Bonificación del {bonificacion}."
    return "No hay bonificación."
  
# Ejemplo de uso
puntaje = int(input("Ingrese el puntaje de evaluación (0-100): "))
resultado = calcular_bonificacion(puntaje)
print(resultado)
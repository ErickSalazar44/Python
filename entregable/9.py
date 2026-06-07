"""
9. Asignación de tipo de contrato Con base en la edad del postulante y su
   experiencia, el estudiante debe indicar si el contrato es de prácticas,
   temporal o fijo.

"""
VALIDACION = {
    "practicas": "Contrato de prácticas",
    "temporal": "Contrato temporal",
    "fijo": "Contrato fijo"
}


def asignar_tipo_contrato(edad, experiencia):
    if edad < 25 and experiencia < 2:
        return VALIDACION["practicas"]
    elif edad < 30 and experiencia < 5:
        return VALIDACION["temporal"]
    else:
        return VALIDACION["fijo"]
      
# Ejemplo de uso
print(asignar_tipo_contrato(22, 1))  # Output: Contrato de prácticas
print(asignar_tipo_contrato(28, 3))  # Output: Contrato temporal
print(asignar_tipo_contrato(35, 10)) # Output: Contrato fijo
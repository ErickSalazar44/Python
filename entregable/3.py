"""
3. Evaluación de entrega de documentos El estudiante debe evaluar si el empleado
   ha entregado los 3 documentos requeridos. Si se entregaron todos, se indica
   que está completo. De lo contrario, que falta documentación. NIVEL INTERMEDIO
"""

def evaluar_entrega_documentos(documentos_entregados):
    documentos_requeridos = 3
    if documentos_entregados >= documentos_requeridos:
        return "Entrega completa. Todos los documentos han sido entregados."
    else:
        return "Falta documentación. No se han entregado todos los documentos requeridos." 
      
# Ejemplo de uso
documentos_entregados = int(input("Ingrese la cantidad de documentos entregados: "))
resultado = evaluar_entrega_documentos(documentos_entregados)

print(resultado)

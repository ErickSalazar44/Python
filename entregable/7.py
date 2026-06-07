"""
7. Evaluador de riesgos financieros El estudiante debe evaluar el nivel de
   riesgo de un cliente con base en sus ingresos y si tiene deudas. El resultado
   será riesgo bajo, medio o alto.
"""


def evaluar_riesgo_financiero(ingresos, tiene_deudas):
    
    if ingresos >= 50000 and not tiene_deudas:
        return "Riesgo bajo"
    elif ingresos >= 30000 and not tiene_deudas:
        return "Riesgo medio"
    else:
        return "Riesgo alto"
      
# Ejemplo de uso
ingresos_cliente = float(input("Ingrese los ingresos del cliente: "))
tiene_deudas_cliente = input("¿El cliente tiene deudas? (sí/no): ").strip().lower() 

nivel_riesgo = evaluar_riesgo_financiero(ingresos_cliente, tiene_deudas_cliente)
print(f"El nivel de riesgo del cliente es: {nivel_riesgo}")
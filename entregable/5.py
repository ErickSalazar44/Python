"""
5. Gestión de pedidos urgentes El estudiante debe solicitar el tipo de pedido
   (normal, urgente, muy urgente) y devolver el tiempo de entrega asociado. Si
   se ingresa otro valor, debe notificar que no es válido. FUNDAMENTOS DE
   PROGRAMACIÓN
"""

tipos_de_pedido = {
    "normal": "5 días",
    "urgente": "2 días",
    "muy urgente": "1 día"
}

def determinar_tiempo_entrega(tipo_pedido):
    return tipos_de_pedido.get(tipo_pedido, "Tipo de pedido no válido.")

# Ejemplo de uso
tipo_pedido = input("Ingrese el tipo de pedido (normal, urgente, muy urgente): ")
tiempo_entrega = determinar_tiempo_entrega(tipo_pedido)
print(f"El tiempo de entrega es: {tiempo_entrega}")
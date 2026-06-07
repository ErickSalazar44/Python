"""
  8. Validación de envío de productos El sistema debe determinar si un pedido
   puede ser enviado. Depende de si el pago está confirmado y si hay suficiente
   stock. Deben manejarse tres posibles situaciones: pago pendiente, sin stock,
   o listo para envío.
"""

def validar_envio(pago_confirmado, stock_disponible):
    if not pago_confirmado:
        return "Pago pendiente"
    elif stock_disponible <= 0:
        return "Sin stock"
    else:
        return "Listo para envío"
# Ejemplo de uso
print(validar_envio(False, 10))  # Output: Pago pendiente
print(validar_envio(True, 0))    # Output: Sin stock
print(validar_envio(True, 5))    # Output: Listo para envío


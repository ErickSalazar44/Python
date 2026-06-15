# Estructura
# Creación de excepciones
# Context Managers


# Anatomía del bloque completo en Python


def procesar_transaccion(monto: float, saldo: float) -> None:
    # Intentar
    try:
        print("1. Conectando al servidor del banco...")
        if monto > saldo:
            # En JS usarías: throw new Error()
            raise ValueError("Fondos insuficientes para realizar la operación.")

        nuevo_saldo = saldo - monto

    # Catch - Manejo de errores específicos
    except ValueError as error:
        # Aquí cae SOLO si el error fue un ValueError
        print(f"Error de validación: {error}")

    # Catch - Manejo de errores generales (no recomendado, pero útil para imprevistos)
    except Exception as general_error:
        # Aquí cae si fue cualquier otro error imprevisto (ej: se cayó el internet)
        print(f"Error crítico del sistema: {general_error}")

    # Else - Solo corre si NO hubo ningún error en el bloque 'try'
    else:
        # ESTO ES NUEVO: Solo corre si el 'try' fue un éxito rotundo
        print(f"Transacción exitosa. Tu nuevo saldo es: S/. {nuevo_saldo}")

    finally:
        # Corre SIEMPRE (limpieza de recursos)
        print("Cerrando conexión segura con el banco...")


# Ejercicio:


def dividir_cuenta_cabbios(ticket_total: float, num_person: int) -> None:

    result = 0
    try:
        # Calcular cúanto debe pagar cada person
        result = ticket_total / num_person

    except ZeroDivisionError:
        # Por si intentan dividir entre 0
        print("No se puede dividir la cuenta entre cero personas.")

    else:
        print(f"Total peaple have pay: S/.{result}")

    finally:
        print("Operate box final.")


# Test 1
intento = dividir_cuenta_cabbios(120, 3)


class LimitePedidoExcedidoError(Exception):
    """Excepción lanzada cuando el limite del pedido exedio"""

    def __init__(self, cantidad_platos: int):
        self.cantidad_platos = cantidad_platos

        super().__init__(
            f"Limite de pedido excedido: cantidad de intentos: {cantidad_platos}"
        )


def registrar_pedido_mesa(cantidad_platos: int) -> None:
    try:
        if cantidad_platos > 20:
            raise LimitePedidoExcedidoError(cantidad_platos)

    except LimitePedidoExcedidoError as error:
        print(f"Operación incorrecta {error}")
        print(f"Auditoria log -> Solicito: {error.cantidad_platos}")

    else:
        print("Pedido enviado con éxito a la cocina.")


intento_2 = registrar_pedido_mesa(30)

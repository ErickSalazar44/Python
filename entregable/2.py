"""
2. Verificación de inventario Debe preguntarse al usuario cuántas unidades hay
   en el inventario. Si hay más de 0, se indica que el producto está disponible.
   Si no hay stock, se debe mostrar que está agotado.
"""

STOCK_AVAILABLE = 0

def main():
    unidades = int(input("Ingrese la cantidad de unidades en el inventario: "))
    
    ## Esto truena si envio una letra, quizas tengamos que validar la entrada, pero por ahora lo dejamos asi
    
    if unidades > STOCK_AVAILABLE:
        print("El producto está disponible.")
    else:
        print("El producto está agotado.")

if __name__ == "__main__":    main()
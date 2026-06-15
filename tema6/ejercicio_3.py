"""
Control de stock en un supermercado
"""

stock = {}


def decorador(n=40):
    print("=" * n)


def mostrar_menu():
    decorador()
    print("SUPERMERCADO")
    decorador()
    for num, (name, _) in COMANDOS.items():
        print(f"{num}. {name}")


def agregar():
    nombre = input("Nombre del producto: ").strip()
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    stock[nombre] = {"cantidad": cantidad, "precio": precio}
    print(f"Producto '{nombre}' agregado.")


def listar():
    if not stock:
        print("Stock vacío.")
        return
    decorador()
    print(f"{'Producto':<20} {'Cantidad':>8} {'Precio':>8}")
    decorador()
    for nombre, datos in stock.items():
        print(f"{nombre:<20} {datos['cantidad']:>8} {datos['precio']:>8.2f}")


def eliminar():
    nombre = input("Nombre del producto a eliminar: ").strip()
    if nombre in stock:
        del stock[nombre]
        print(f"Producto '{nombre}' eliminado.")
    else:
        print(f"Producto '{nombre}' no encontrado.")


def buscar():
    nombre = input("Nombre del producto a buscar: ").strip()
    if nombre in stock:
        datos = stock[nombre]
        print(f"{nombre}: cantidad={datos['cantidad']}, precio={datos['precio']:.2f}")
    else:
        print(f"Producto '{nombre}' no encontrado.")


def actualizar():
    nombre = input("Nombre del producto a actualizar: ").strip()
    if nombre not in stock:
        print(f"Producto '{nombre}' no encontrado.")
        return
    cantidad = int(input("Nueva cantidad: "))
    precio = float(input("Nuevo precio: "))
    stock[nombre] = {"cantidad": cantidad, "precio": precio}
    print(f"Producto '{nombre}' actualizado.")


def salir():
    print("Saliendo del sistema.")
    exit()


COMANDOS = {
    1: ("Agregar", agregar),
    2: ("Listar", listar),
    3: ("Eliminar", eliminar),
    4: ("Buscar", buscar),
    5: ("Actualizar", actualizar),
    6: ("Salir", salir),
}

while True:
    mostrar_menu()

    opcion = int(input("Ingresa una opción: "))
    if opcion in COMANDOS:
        COMANDOS[opcion][1]()
    else:
        print("Opción inválida.")

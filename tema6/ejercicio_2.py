# EJERCICIO 1
student = []

while True:
    name = input("Ingrese el nombre del estudiante (para salir ingrese 'exit'): ")

    if name.lower() == 'exit':
        break

    student.append(name)

print(f"\nTienes {len(student)} estudiantes")
for e in student:
    print("-", e)
print() 


# EJERCICIO 2
products = []

while True:
    product = input("Ingrese el nombre del producto (para salir ingrese 'exit'): ")

    if product.lower() == 'exit':
        break

    products.extend([product]) 

print(f"\nTienes {len(products)} productos:")
for p in products:
    print("-", p)

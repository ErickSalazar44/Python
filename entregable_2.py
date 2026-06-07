
# =================== Actividad: Nivel básico ====================

# 1. while básico: Imprimir los números del 1 al 10.
count = 1
while count <= 10:
    print(count)
    count += 1
# 2. for con range(): Mostrar los múltiplos de 2 del 2 al 20. (n - 1)
for num in range(2, 21, 2):
    print(num)
    
# 3. continue: Imprimir los números del 1 al 10, pero saltar el número 5.
for num in range(1, 11):
    if num == 5:
        continue
    print(num)

# 4. break: Pedir números al usuario hasta que ingrese el 0.
while True:
    num = int(input("Ingrese un número (0 para salir): "))
    if num == 0:
        break
    print(num)

# 5. String con for: Recorrer una palabra y mostrar cada letra en una línea.
word = "Bendito sea Guido van Rossum"
for letter in word:
    print(letter)
    
# =================== Actividad: Nivel intermedio ====================

# 1. while True: Menú interactivo con 3 opciones (ej. calcular suma, multiplicación, salir).
while True:
    print("Menú:")
    print("1. Calcular suma")
    print("2. Calcular multiplicación")
    print("3. Salir")
    
    choice = input("Seleccione una opción: ")
    
    if choice == '1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La suma es: {num1 + num2}")
    elif choice == '2':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"La multiplicación es: {num1 * num2}")
    elif choice == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")


# 2. for con lista: Mostrar todos los nombres de una lista de estudiantes.

students = ["Erick", "Betzy<3", "Ana", "Carlos", "Lucía"]
for student in students:
    print(student) # Output: Erick, Betzy<3, Ana, Carlos, Lucía


# 3. else en while: Pedir contraseñas hasta que sea correcta; si se logra, mostrar “Acceso concedido”, si no, usar else para decir “Acceso denegado”.

password = "nttdata123"
incorrect_attempts = 0
while True: # Limitar a 3 intentos para evitar un bucle infinito
    user_input = input("Ingrese la contraseña: ")
    if user_input == password:
        print("Acceso concedido")
        break
    else:
        print("Acceso denegado")
        incorrect_attempts += 1
    if incorrect_attempts >= 3:
        print("Demasiados intentos fallidos. Acceso denegado.")
        break


# 4. for con string: Contar cuántas vocales tiene una palabra.

word = "Profe - disculpe el atrevimiento pero me gustaría que me hablara sobre su rol en ntt data y cómo es trabajar allí."
vowels = "aeiouAEIOU" # Vocales en mayúscula y minúscula
count = 0
for letter in word:
    if letter in vowels: # Si la letra es una vocal, incrementamos el contador
        count += 1
print(f"La palabra '{word}' tiene {count} vocales.")


# 5. break: Buscar un número en una lista y detener el bucle al encontrarlo.

numbers = range(1, 21) # Lista de números del 1 al 20
search_num = int(input("Ingrese el número a buscar: "))

for num in numbers:
    if num == search_num:
        print(f"Número {search_num} encontrado en la lista.")
        break
else:    print(f"Número {search_num} no encontrado en la lista.")


# =================== Actividad: Nivel Avanzado ====================

# 1. Bucles anidados: Crear la tabla de multiplicar del 1 al 10.

for i in range(1, 11): # Bucle externo para los números del 1 al 10
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11): # Bucle interno para multiplicar el número i por los números del 1 al 10
        print(f"{i} x {j} = {i * j}")
    print() # Línea en blanco para separar las tablas


# 2. for con diccionarios: Mostrar claves y valores de un diccionario de productos con sus precios.

products = {
    "Manzana": 1.5,
    "Banana": 2,
    "Naranja": 3.5,
    "Pera": 2.5
}
for product, price in products.items(): # Iteramos sobre las claves y valores del diccionario
    print(f"Producto: {product}, Precio: s/ {price:.2f} el kilo")


# 3. while con condiciones múltiples: Simular un cajero automático (saldo, retiros, depósitos, salir).

balance = 1000.0  # Saldo inicial

while True:
    print("\nBienvenido al Cajero Automático")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir")

    choice = input("Seleccione una opción (1-4): ")

    if choice == '1':
        print("========================================")
        print(f"|{'Saldo Actual':^38}|")
        print(f"|{f's/ {balance:.2f}':^38}|")
        print("========================================")

    elif choice == '2':
        amount = float(input("Ingrese el monto a retirar: "))

        if amount > balance: # Importante para no dejar el saldo en negativo
            print("========================================")
            print(f"|{'Fondos insuficientes':^38}|")
            print(f"|{'No puede retirar más de su saldo.':^38}|")
            print(f"|{f'Saldo: s/ {balance:.2f}':^38}|")
            print("========================================")

        else:
            balance -= amount
            print("========================================")
            print(f"|{'Retiro Exitoso':^38}|")
            print(f"|{f'Monto: s/ {amount:.2f}':^38}|")
            print(f"|{f'Nuevo saldo: s/ {balance:.2f}':^38}|")
            print("========================================")

    elif choice == '3':
        amount = float(input("Ingrese el monto a depositar: "))
        balance += amount
        print("========================================")
        print(f"|{'Depósito Exitoso':^38}|")
        print(f"|{f'Monto: s/ {amount:.2f}':^38}|")
        print(f"|{f'Nuevo saldo: s/ {balance:.2f}':^38}|")
        print("========================================")

    elif choice == '4':
        print("========================================")
        print(f"|{'Gracias por usar el Cajero':^38}|")
        print(f"|{'Automático. ¡Vuelva pronto!':^38}|")
        print("========================================")
        break

    else:
        print("========================================")
        print(f"|{'Opción no válida':^38}|")
        print(f"|{'Por favor, seleccione una opción':^38}|")
        print(f"|{'del 1 al 4':^38}|")
        print("========================================")
        
        
# 4. continue + validación: Recorrer una lista de números y saltar los negativos, procesando solo los positivos.

numbers = [10, -5, 20, -3, 15, -1, 0]
for num in numbers:
    if num < 0: # Si el número es negativo, saltamos al siguiente
        continue
    print(f"Número positivo: {num}") # Solo se imprimirán los números positivos y el cero
    
# 5. while True con break: Juego de adivinanza de un número (se repite hasta adivinar o hasta 5 intentos).

import random # Profe quizas esta linea no deje ejecutar el código, pero es necesaria para generar el número aleatorio a adivinar

number_to_guess = random.randint(1, 50) # Número aleatorio entre 1 y 50
max_attempts = 5

while True:
    guess = int(input("Adivina el número (entre 1 y 50): "))
    if guess == number_to_guess:
        print("¡Felicidades! Has adivinado el número.")
        break
    elif guess < number_to_guess:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")
    
    max_attempts -= 1
    if max_attempts == 0:
        print(f"Lo siento, has agotado tus intentos. El número era: {number_to_guess}")
        break
      

# 6. Anidado + strings: Mostrar un patrón de pirámide con asteriscos usando bucles.

HEIGHT = 5 # Altura de la pirámide
# Piramide normal
for i in range(1, HEIGHT): # Rango de 1 a HEIGHT-1 para crear la pirámide
    spaces = HEIGHT - i # Cantidad de espacios antes de los asteriscos
    stars = 2 * i - 1 # Cantidad de asteriscos en la fila actual
    print(" " * spaces + "*" * stars) # Imprime los espacios seguidos de los asteriscos

# Piramide invertida
for i in range(HEIGHT, 0, -1): # del valor del alto hasta 0, (-1) para que vaya disminuyendo
    spaces = HEIGHT - i # Cantidad de espacios antes de los asteriscos
    stars = 2 * i - 1 # Cantidad de asteriscos en la fila actual
    print(" " * spaces + "*" * stars) # Imprime los espacios seguidos de los asteriscos

# Muchos cerros
for i in range(1, HEIGHT): # Rango de 1 a HEIGHT-1 para crear la pirámide
    for i in range(1, HEIGHT): # Rango de 1 a HEIGHT-1 para crear la pirámide
        print("*" * i) # Imprime los espacios seguidos de los asteriscos
    for i in range(HEIGHT, 0, -1): # del valor del alto hasta 0, (-1) para que vaya disminuyendo
        print("*" * i) # Imprime los espacios seguidos de los asteriscos
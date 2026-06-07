# Condicionales
# Bucles

"""
A diferencia de js donde usamos los condicionales || & o !
en Python usamos "ingles" not = ! or = || and = &

todo lo que puede devolver falso en python es
False None [] "" {} 0 0.0
Todo lo diferente a eso es True

"""

# not or in and

status_code = 404

# Nuevo metodo match desde 3.10+
match status_code:
    case 200:
        print("Éxito")
    case 404:
        print("No encontrado")
    case 500 | 501 | 502:  # Pipe para múltiples casos
        print("Error del servidor")
    case _:  # El default (underscore)
        print("Código desconocido")

# Iteración sobre obj for ... in ... recorre los elementos directamente
# continue = salta el paso actual
# break = Rompe el bucle y detiene la ejecucion
# else = si esta a nivel del for se ejecuta al final si este no fue detenido


# Ejercicio 1

usuario = {"nombre": "Erick", "rol": "invitado", "premium": True}

match usuario:
    case { "rol": "admin" }:
        print("Acceso Total" )
    case { "rol": "editor" }:
        print("Acceso de edición")
    case { "rol": "invitado", "premium": True }:
        print("Acceso de lectura VIP")
    case { "rol": "invitado"}: 
        print("Acceso limitado")
    case _:
        print("Acceso denegado", usuario)

# Ejercicio 2

servidores = ["online", "online", "maintenance", "online", "error", "online"]

for servidor in servidores: 
    if (servidor == 'maintenance'):
        print("Servidor en mantenimiento saltando...")
        continue

    if (servidor == "error"):
        print("¡CRÍTICO! Fallo detectado. Abortando auditoría...")
        break

else:
    print("✅ Auditoría completada: Todos los servidores operativo")
    
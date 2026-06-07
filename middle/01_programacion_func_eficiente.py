# List Comprenhensions
# Generadores

# 1. Limpieza de Datos (Data Sanitization)

emails_sucios = [" ERICK@mail.com", "betzy@MAIL.com ", "  alan@mail.com"]

# Limpiamos y estandarizamos en un segundo
emails_validados = [email.strip().lower() for email in emails_sucios]

# 2. Extracción de Atributos (Mapping)
usuarios_db = [{"id": 1, "nombre": "Erick"}, {"id": 2, "nombre": "Betzy"}]

# Extraemos solo los IDs para usarlos en otro query
ids_para_batch = [u["id"] for u in usuarios_db]

# 3. Diccionarios de Búsqueda Rápida (Indexing)

# Convertimos lista de dicts en un mapa de {id: objeto_completo}
mapa_usuarios = {u["id"]: u for u in usuarios_db}
# Ahora buscar al usuario 2 es instantáneo: mapa_usuarios[2]

# Ejercicio List de comprehensions

salarios_usd = [1000, 1500, 2000, 2500, 3000]

salarios_mxn = [s * 17.5 for s in salarios_usd if (s * 17.5) > 30000]


# Refuerzo
# TODO: Crea 'transacciones_validadas' en una sola línea
# Pista: usa .replace("$", "").strip() para limpiar el string antes del float()

transacciones_sucias = [" $100.50 ", " $600.00", "$ 1200.75", " $50.0 "]
transacciones = [
    float(r) for ts in transacciones_sucias if (r := ts.replace("$", "").strip())
]


# Refuerzo 2

empleados = ["  erick salazar ", "betzy psicologa", " nelson  ", "KARLA"]

result = [r for e in empleados if (r := e.strip().capitalize()) if len(r) > 5]
# Output : ['Erick salazar', 'Betzy psicologa', 'Nelson']

# Refuerzo 3


"""
Objetivo (En una sola línea):
Filtra los valores que sean None.
Filtra los valores que sean menores o iguales a 0.
Para los que pasen, multiplícalos por el precio del Bitcoin (imaginemos $60,000).
Extra: Usa el Walrus para que la multiplicación se guarde en una variable 
y solo devuelvas el monto si este es mayor a $50,000.
"""

saldos = [0.5, -1.2, None, 2.0, 0.0, -0.1, 1.5]
result_2 = [s * 60000 for s in saldos if (r := isinstance(s, (int, float)) and (s > 0))]

"""
Reto 2: El Desglose de Facturas 
Recibes un reporte de ventas del fin de semana.
Es una lista de diccionarios, donde cada diccionario representa 
una mesa y tiene una lista de los montos de cada plato pedido.
"""
ventas = [
    {"mesa": 1, "pedidos": [10.5, 20.0, 5.0]},
    {"mesa": 2, "pedidos": [50.0, 15.0]},
    {"mesa": 3, "pedidos": [100.0]},
]
new_list = [
    r * 1.18 for v in ventas for p in v.values() if (isinstance(p, list)) for r in p
]


# El Filtro de Seguridad de Finpulsa

raw_data = [100.5, None, "error", 500, 0, -20, 1200]
clean_data = [
    data for data in raw_data if (isinstance(data, (int, float)) and data > 0)
]

# El Consolidador de Cashback (Estructura Anidada)

usuarios = [
    {"user": "Erick", "compras": [1500, 2000, 800]},
    {"user": "Betzy", "compras": [3000, 5000]},
    {"user": "Invitado", "compras": [50, 80]},
]


result_cashback = [
    r
    for u in usuarios
    for c in u["compras"]
    if (u["user"] != "Invitado")
    if (r := c * 0.05)
    if (r > 100)
]

# Tengo una duda, estoy regresando el cashback de los que pasraon, pero si quieres
# Puedo devolver el cashback + la compra, solo seria sumarle a "r" la c


# Buscador de Tags en Descripciones

descripciones = [
    "Pago de #nomina",
    "Compra de #servidor AWS",
    "Transferencia interna",
    "#bono de mayo",
]

result_description = [
    p.replace("#", "").upper() 
    for frase in descripciones 
    for p in frase.split() 
    if p.startswith("#")
]



# Generadores

def mi_primer_yield():
    print("Iniciando motor...")
    yield "Taza 1"
    print("Retomando después de la primera taza...")
    yield "Taza 2"
    print("Fin del café.")

# 1. Crea el generador
maquina = mi_primer_yield()

# 2. Ejecuta esto uno por uno y mira los prints
print(next(maquina)) 


def procesador_pedidos(pedidos):
    # Tu código aquí usando for y yield
    for p in pedidos:
        if (p > 0):
            yield p + (p * 0.18)
        else:
            pass


# Para probarlo:
mis_pedidos = [100, 0, 50, -10, 200]
generador = procesador_pedidos(mis_pedidos)

print(next(generador)) # Debería dar 118.0
print(next(generador)) # Debería saltar el 0 y dar 59.0


# Ejercicio de Refuerzo:

""" 
    1. Formateo de Precios
    Tienes una lista de precios flotantes: precios_base = [5.5, 10.25, 50.0]. Crea una lista en una sola línea llamada precios_string que convierta cada número a string y le agregue el símbolo de soles al principio (Ej: "S/. 5.5").
"""

precios_base = [5.5, 10.25, 50.0]

precios_string = [f"S/. {p}" for p in precios_base]

"""
    2.Tienes strings de logs: logs = ["  error: base de datos  ", "info: inicio exitoso", " error: token expirado  "]. Crea una lista en una sola línea que: Limpie los espacios en blanco de cada string con .strip().
    Filtre y deje solo los que comiencen con "error".
    (Usa el Walrus para no hacer .strip() dos veces).
"""

logs = ["  error: base de datos  ", "info: inicio exitoso", " error: token expirado  "]

logs_filtrados = [l for log in logs if(l := log.strip()).startswith("error")]

"""
El Generador de Tokens (Generadores con Yield)
Escribe una función generadora llamada generador_cupones(). Cada vez que sea llamada (mediante un for o next), debe entregar un string con un código secuencial: primero "CUPON_1", luego "CUPON_2", y finalmente "CUPON_3".
"""
def generador_cupones():
    cupones = ["CUPON_1", "CUPON_2", "CUPON_3"]
    for c in cupones:
        yield c
    else:
        print("No hay más cupones disponibles.")

result_cupones = generador_cupones()
print(next(result_cupones)) # CUPON_1
print(next(result_cupones)) # CUPON_2
print(next(result_cupones)) # CUPON_3
print(next(result_cupones)) # No hay más cupones disponibles.
print(next(result_cupones)) # StopIteration Error, porque ya no hay más cupones para entregar.
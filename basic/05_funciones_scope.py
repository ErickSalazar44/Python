# Parametros
# Funciones Lambda
# Ámbito de variables

def create_api_response(status: int, data: dict | None = None) -> dict:
    """
    Genera una estructura de respuesta estandarizada.
    
    Args:
        status: Código HTTP de la respuesta.
        data: Diccionario con la carga útil (opcional).
    """
    return {
        "status": status,
        "data": data or {},
        "timestamp": 1713984000  # Ejemplo de timestamp fijo
    }

# El orden no importa, lo que importa es el nombre, 
response = create_api_response(data={"id": 1}, status=200)

# Flexibilidad Total: *args y kwargs

# *args = tuplas o strings o cualquier valor
# **kwargns = dict u objets 


# Functiones Lambda: Las "Anonimas"
# Ordenar una lista de dicts por edad
users = [{"name": "Erick", "age": 26}, {"name": "Alan", "age": 30}]
users_sorted = sorted(users, key=lambda u: u["age"])

# entiendo que este bloque es la funcion inline key=lambda u: u["age"] 


# Examen final basic 

raw_logs = [
    (" erick_01 ", "192.168.1.1", "SUCCESS"),
    ("admin_root", "10.0.0.5", "CRITICAL"),
    (" guest_user ", "172.16.0.1", "SUCCESS")
]

# NOTA : B
def process_access_logs(*logs: tuple[str, str, str], **metadata) -> list[str]:
    # Usamos la lambda internamente (no contamina el scope global)
    cleaner = lambda s: s.strip()
    allowed_users = []

    for log in logs:
        user, ip, status = log
        # 1. Asignamos el valor limpio a una variable
        user_clean = cleaner(user)    

        if status == "CRITICAL":
            # Usamos f-strings para un log claro
            print(f"🚨 ALERTA: Intento crítico del usuario '{user_clean}' en IP {ip}")

        if status == "SUCCESS":
            # 2. Guardamos SOLO el nombre limpio
            allowed_users.append(user_clean)
    
    if metadata:
        print("\n--- Metadatos del Proceso ---")
        for key, val in metadata.items():
            print(f"{key.upper()}: {val}")
            
    return allowed_users

# --- EJECUCIÓN ---
print("Procesando logs...\n")
result = process_access_logs(*raw_logs, env="production", version="2.0")

print(f"\nUsuarios finalmente permitidos: {result}")



# Exam 2
# Ráfaga de transacciones entrantes (ID, Monto, Moneda)
rafaga_txs = [
    (" tx_1001 ", 5000, "MXN"),
    ("  tx_1002", 15000, "MXN"),
    ("tx_1003  ", 2500, "USD"),  # Debería ser rechazada por moneda
    (" tx_1004 ", 9999, "MXN")
]

def validar_pagos_finpulsa(*transacciones: tuple[str, int, str], **config) -> dict:
    """
    Procesa, limpia y clasifica transacciones financieras.
    Retorna un diccionario con el estado de cada transacción.
    """
    # 1. Tu lambda para limpiar espacios
    limpiador_id = lambda tx_id: tx_id.strip()
    
    # Estructura de retorno esperada
    resultados = {
        "Aprobadas": [],
        "Revision": [],
        "Rechazadas": []
    }
    
    # --- TU LÓGICA DE ARQUITECTO AQUÍ ---
    for tx in transacciones:
        raw_id, monto, moneda = tx
        id_limpio = limpiador_id(raw_id)

# Lógica plana y eficiente (Early exit)
        if moneda != "MXN":
            resultados["Rechazadas"].append(id_limpio)
        elif monto > 10000:
            resultados["Revision"].append(id_limpio)
        else:
            resultados["Aprobadas"].append(id_limpio)

    
    
    # ------------------------------------
    
    # Imprimir config si existe (Bonus de legibilidad)
    if config:
        print("\n⚙️ Configuración del Motor:")
        for k, v in config.items():
            print(f"  - {k}: {v}")
            
    return resultados

# --- EJECUCIÓN DEL EXAMEN ---
# RECUERDA: ¿Cómo debes pasar 'rafaga_txs' para que Python la desempaquete correctamente?
# Llama a la función, guarda el resultado e imprímelo de forma bonita.

print(validar_pagos_finpulsa(*rafaga_txs))
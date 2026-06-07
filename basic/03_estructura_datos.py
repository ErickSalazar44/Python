# Listas
# Tuplas
# Diccionarios
# Sets

# String
name = 'Erick Earl'
name_2: str = 'Erick Earl 2'


# Number
age = 30
age_2: int = 26
peso: float = 70.5

# Array - List
hobbies = ['Programming', 'Music', 'Traveling']
hobbies_2: list[str] = ['Programming', 'Music', 'Traveling']
boolean_list: list[bool] = [True, False, True]
horarios: list[dict[str, str]] = [{'dia': 'Lunes', 'hora': '10:00'}, {'dia': 'Martes', 'hora': '14:00'}]

# Dictionary - Object
person = {
    'name': 'Erick Earl',
    'age': 30,
    'peso': 70.5
}

person_2: dict[str | tuple[str, str], str | int | float] = {
    ('name', 'nombre'): 'Erick Earl', 
    'age': 30,
    'peso': 70.5
}

# Tuple: Inmutable, más rápida que la lista
coordinates: tuple[float, float] = (-12.04, -77.04)

# Set
empty_set = set() # No uses {} porque eso es un dict
unique_numbers = {1, 2, 3, 4, 5}

print(name, age, peso)

# Bytes
data: bytes = b'Hello, World!'
token: bytes = b"secret_token_123"


# Ejercicio 1 
raw_users = ["Erick", "Betzy", "Erick", "Mateo", "Betzy", "Alan"]
raw_users_set = set(raw_users) # elimina duplicados
raw_users_set_list = list(raw_users_set)




# Ejercicio 2 
user_status = {
    "Erick": "active",
    "Betzy": "active",
}
user_status = dict.fromkeys(raw_users_set, "active")
user_status = {user: "active" for user in raw_users_set}
user_status = {}
for user in raw_users_set:
    user_status[user] = "active"

# Ejercicio 3
print(list(set(raw_users)))
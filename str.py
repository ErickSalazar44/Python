# Method for string type in Python


# Limpieza de espacios
text = "   Hello, World!   "
cleaned_text = text.strip()  # Elimina espacios al inicio y al final
cleaned_text_left = text.lstrip()  # Elimina espacios al inicio
cleaned_text_right = text.rstrip()  # Elimina espacios al final

print(cleaned_text)  # Output: "Hello, World!"
print(cleaned_text_left)  # Output: "Hello, World!   "
print(cleaned_text_right)  # Output: "   Hello, World!"

# Transformación Case (Normalizar db)
name = "erick earl"
name_upper = name.upper()  # Convierte a mayúsculas
name_lower = name.lower()  # Convierte a minúsculas
name_title = name.title()  # Convierte a formato título
name_capitalize = name.capitalize()  # Convierte la primera letra a mayúscula

print(name_upper)  # Output: "ERICK EARL"
print(name_lower)  # Output: "erick earl" 
print(name_title)  # Output: "Erick Earl"
print(name_capitalize)  # Output: "Erick earl"

# Búsqueda y validación (return boolean)
email = "erick@example.com"
is_valid_email = "@" in email  # Verifica si el email contiene "@"
email_starts_with_erick = email.startswith("erick")  # Verifica si el email empieza con "erick"
email_ends_with_com = email.endswith(".com")  # Verifica si el email termina con ".com"
print(is_valid_email)  # Output: True
print(email_starts_with_erick)  # Output: True
print(email_ends_with_com)  # Output: True

# Reemplazo y división
sentence = "The quick brown fox jumps over the lazy dog"
replaced_sentence = sentence.replace("fox", "cat")  # Reemplaza "fox" por "cat"
split_sentence = sentence.split(' ')  # Divide la oración en palabras
print(replaced_sentence)  # Output: "The quick brown cat jumps over the lazy dog"
print(split_sentence)  # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
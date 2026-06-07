"""
6. Control de acceso al sistema El estudiante debe validar el acceso a un
   sistema según el rol del usuario y su contraseña. Solo roles 'admin' o 'jefe'
   con clave '1234' acceden. NIVEL AVANZADO
"""

CREDENCIALES_VALIDAS = {
    'admin': '1234',
    'jefe': '1234'
}

def validar_acceso(rol, clave):
    if rol in CREDENCIALES_VALIDAS and CREDENCIALES_VALIDAS[rol] == clave:
        return "Acceso concedido."
    else:
        return "Acceso denegado."
      
# Ejemplo de uso
rol_usuario = input("Ingrese su rol (admin/jefe): ")
clave_usuario = input("Ingrese su clave: ")
resultado_acceso = validar_acceso(rol_usuario, clave_usuario)
print(resultado_acceso)
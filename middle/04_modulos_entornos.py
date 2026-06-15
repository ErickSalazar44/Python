# Importacion
# Uso pop y entornos virtuales (venv o conda)
# Estructura de paquetes (__init__.py)

"""
Las importaciones funcionan de una manera muy sencilla
1. Todo dato es exportable de manera automatica
2. la estructura de impotacion es
    - import <nombre del archivo>
    - import <nombre del archivo> from <lo que deseas traer>
    - import <nombre> from <data> as <para modificar el nombre>
"""

"""
Entornos virtuales
1. python -m venv .venv
2. acceder al entorno virtual 
    - win : .venv\Scripts\Activate.ps1
    - linux: source .venv/bin/activate
3. instalar paquetes nuevos
    - pip install requests
4. generar nuestro packgake en python se llama requirements.txt
    - pip freeze > requirements.txt
5. instalar paquetes existentes
    - pip install -r requirements.txt
"""

"""
__init__.py = index.js 
Sirve para inicializar correctamente tu sistema, esto evita
que se cargue codigo antes de las importaciones importantes,
tambien sirve para barril de importaciones
"""

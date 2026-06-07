# Clases y objetos
# Métodos especiales 
# Herencias, Polimorfismos y Encapsulamiento
# Propiedades


"""
  Clase es un molde o plantilla 
  Objeto es una instancia de una clase 
  
  !Importante: 
  si o si agregar el self como priemr argumento de los métodos, es la referencia al objeto mismo.
  No se usa la palabra 'new' para crear objetos, se llama a la clase como si fuera una función.
"""

class Usuario:
    # El Constructor (Doble guion bajo 'init' doble guion bajo)
    def __init__(self, nombre, rol):
        self.nombre = nombre  # Atributo de instancia (Como el this.nombre de JS)
        self.rol = rol        # Atributo de instancia

    # Un Método (Función dentro de una clase)
    def saludar(self):
        # Usamos self.nombre para acceder a la propiedad de este objeto
        return f"Hola, soy {self.nombre} y mi rol es {self.rol}"

# --- INSTANCIACIÓN (Crear el objeto) ---
# Nota: En Python NO se usa la palabra 'new'

erick = Usuario("Erick", "Architect") 
betzy = Usuario("Betzy", "Psicóloga")

# --- ACCESO A DATOS ---
print(erick.nombre)   # Output: Erick
print(betzy.saludar()) # Output: Hola, soy Betzy y mi rol es Psicóloga


class TarjetaDebito:
    def __init__(self, titular: str, saldo_inicial: float):
        self.titular: str = titular
        self.saldo: float = saldo_inicial

    # Método Dunder: Controla cómo se ve la tarjeta en consola/logs
    def __str__(self) -> str:
        return f"Tarjeta de {self.titular} (Saldo: S/. {self.saldo})"

    def realizar_pago(self, monto: float) -> bool:
        if monto > self.saldo:
            return False
        self.saldo -= monto
        return True


class Producto:
    iva: float = 1.18  # Atributo de clase (Estático)

    def __init__(self, nombre: str, precio_base: float):
        self.nombre: str = nombre
        self.precio_base: float = precio_base

    # La clase Producto ahora es responsable de saber su propio precio total
    @property
    def precio_total(self) -> float:
        return self.precio_base * self.iva

    def __str__(self) -> str:
        return f"{self.nombre} - S/. {self.precio_total:.2f}"


class Orden:
    def __init__(self, cliente_tarjeta: TarjetaDebito):
        self.tarjeta: TarjetaDebito = cliente_tarjeta
        # Guardamos diccionarios limpios en lugar de tuplas raras
        self.items: list[dict] = [] 

    def agregar_producto(self, nuevo_producto: Producto, cantidad: int) -> None:
        self.items.append({"producto": nuevo_producto, "cantidad": cantidad})

    def procesar_checkout(self) -> str:
        # Sumamos: (precio_total del producto) * (cantidad)
        total_orden: float = sum(item["producto"].precio_total * item["cantidad"] for item in self.items)
        
        # Delegamos el pago. La orden solo recibe un True o False del banco
        if self.tarjeta.realizar_pago(total_orden):
            return f"Pago exitoso. {self.tarjeta}"
        return "Error: Fondos insuficientes."
      
      
      
# 1. Instanciamos la billetera y el menú
tarjeta_erick = TarjetaDebito("Erick", 500.0)
pizza = Producto("Pizza Hawaiana", 40.0)

# 2. Creamos la orden
orden_mesa_1 = Orden(tarjeta_erick)
orden_mesa_1.agregar_producto(pizza, 2)

# 3. Procesamos
print(orden_mesa_1.procesar_checkout())
# Output: Pago exitoso. Tarjeta de Erick (Saldo: S/. 405.6)



# Ejercicio

class ItemCarrito:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    @property
    def subtotal(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"Producto: {self.nombre} - Cantidad: {self.cantidad}, Subtotal: S/. {self.subtotal:.2f}"
    

prueba = ItemCarrito("Camiseta", 50.0, 3)
print(prueba)  # Output: Producto: Camiseta - Cantidad: 3, Subtotal: S/. 150.00


"""
__eq__ (Equality): Hook que redefine cómo funciona el operador == para comparar lógicamente dos instancias.

__len__ (Length): Hook que permite a un objeto personalizado responder a la función nativa len(), devolviendo un entero.
"""
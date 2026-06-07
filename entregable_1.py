"""
1. Calculadora de Propina
• Pide al usuario ingresar el monto total de la cuenta en un restaurante.
• Pide ingresar el porcentaje de propina que desea dejar.
• Calcula y muestra:
o El monto de la propina.
o El total a pagar (incluyendo la propina).
"""

total_amount    = float(input("Ingresa el monto total de la cuenta: s/ "))
tip_percentage  = float(input("Ingresa el porcentaje de propina:   % "))

tip_amount  = total_amount * (tip_percentage / 100)
total_with_tip = total_amount + tip_amount

print(f"""
Precio base : s/ {total_amount:.2f}
Propina     : s/ {tip_amount:.2f}  ({tip_percentage:.0f}%)
Total a pagar: s/ {total_with_tip:.2f}
""")



"""
2. Calcular el salario semanal
• Pide al usuario ingresar las horas trabajadas en una semana y la tarifa por hora.
• Calcula cuanto le pagaran esa semana.
• Muestra su pago semanal
"""

hours_worked  = float(input("Ingresa las horas trabajadas en la semana: "))
hourly_rate   = float(input("Ingresa la tarifa por hora:               s/ "))

weekly_pay = hours_worked * hourly_rate

print(f"""
Horas trabajadas : {hours_worked:.2f} h
Tarifa por hora  : s/ {hourly_rate:.2f}
Pago semanal     : s/ {weekly_pay:.2f}
""")


"""
3. Precio con IGV
• Pide al usuario ingresar el precio de un producto.
• Calcula y muestra:
o El precio final a pagar incluido el IGV (Recordar que el IGV equivale al 18% del
precio)
"""

IGV_RATE = 0.18

product_price = float(input("Ingresa el precio del producto: s/"))
igv_amount = product_price * IGV_RATE
total_price = igv_amount + product_price
print(f"""
Precio del producto : s/ {product_price:.2f}
IGV ({IGV_RATE * 100:.0f})% : s/ {igv_amount:.2f}  
Precio total     : s/ {total_price:.2f}
""")


"""
4. Ahorro mensual
• Pide al usuario ingresar una meta de ahorro
• Calcular cuanto debe ahorrar al mes para alcanzar esa cantidad en 1 año
• Muestra el resultado en formato claro.
"""

savings_goal = float(input("Ingresa tu meta de ahorro: s/"))
monthly_savings = savings_goal / 12

print(f"""
Para lograr tu meta de : s/ {savings_goal:.2f}
Debes ahorrar mensualmente: s/ {monthly_savings:.2f}  
""")


"""
5) Costo de envío
• Pide al usuario ingresar el peso de un paquete (en kg) y la tarifa por (kg)
• Calcular el costo total de envío a pagar
• Muestra el resultado en soles.
"""

package_weight = float(input("Ingresa el peso del paquete: kg"))
rate_kg = float(input("Ingresa la tarifa por kg: s/"))

print(f"""
Peso del paquete : kg {package_weight:.2f}
Tarifa : s/ {rate_kg:.2f}  
Precio total     : s/ {package_weight * rate_kg:.2f}
""")
"""
1. Registro de asistencia El estudiante debe solicitar la hora de llegada de un
   trabajador y determinar si fue puntual o llegó tarde. La condición es si
   llega antes de las 9:00 a.m. se considera puntual, en caso contrario, se
   considera tardanza.
"""

def main():
    hora_llegada = input("Ingrese la hora de llegada (formato HH:MM): ")
    # Validar entrada y convertir a horas y minutos
    
    valores = hora_llegada.split(':')
    if len(valores) != 2:
        print("Formato de hora no válido. Use HH:MM.")
        return

    # Convertir a enteros
    hora, minuto = map(int, valores)

    # Validar rango de horas y minutos
    if not (0 <= hora <= 23 and 0 <= minuto <= 59):
        print("Hora o minuto no válido. Use HH:MM.")
        return
    # Convertir a enteros
    hora, minuto = map(int, valores)

    if hora < 9 or (hora == 9 and minuto == 0):
        print("El trabajador fue puntual.")
    else:
        print("El trabajador llegó tarde.")
        
        
if __name__ == "__main__":    main()
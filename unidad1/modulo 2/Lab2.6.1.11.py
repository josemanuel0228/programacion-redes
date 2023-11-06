'''
nombre: José Manuel Gutiérrez Pérez
fecha: 25 de septiembre del 2023
descripcion: La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. Las horas van de 0 a 23 y los minutos de 0 a 59. El resultado debe ser mostrado en la consola.
Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
No te preocupes si tu código no es perfecto, está bien si acepta una hora invalida, lo más importante es que el código produzca una salida correcta acorde a la entrada dada.
Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.
'''

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))


# Calcular las horas y minutos finales
minutos_totales = (hour * 60 + mins + dura)
hora_final = minutos_totales // 60
minutos_final = minutos_totales % 60

# Asegurarse de que la hora final esté en el rango de 0 a 23
hora_final = hora_final % 24

# Mostrar el tiempo final
print(f"El tiempo final es {hora_final:02d}:{minutos_final:02d}")


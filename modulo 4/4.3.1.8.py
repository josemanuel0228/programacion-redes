'''
nombre: José Manuel Gutiérrez Pérez
fecha: 9 de octubre del 2023
Escenario
Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes)
y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.
Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código.
Esta prueba es solo el comienzo.
'''

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days_per_month[1] = 29
    if 1 <= month <= 12:
        return days_per_month[month - 1]
    else:
        return None

def day_of_year(year, month, day):
    if is_year_leap(year):
        days_per_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= month <= 12 and 1 <= day <= days_per_month[month - 1]:
        total_days = sum(days_per_month[:month - 1]) + day
        return total_days
    else:
        return None

print(day_of_year(2000, 12, 31))

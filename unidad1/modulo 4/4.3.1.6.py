'''
nombre: José manuel gutiérrez Pérez 
fecha: 10 de octubre 2023
Escenario
Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.
Parte del esqueleto de la función ya está en el editor.
Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.
El código utiliza dos listas: una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.

'''


def is_year_leap(year):
  if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
  else:
        return False


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    result = is_year_leap(test_data[i])
    if result == test_results[i]:
        print(f"{test_data[i]} es bisiesto: {result}")
    else:
        print(f"{test_data[i]} no es bisiesto, se esperaba: {expected_results[i]}")
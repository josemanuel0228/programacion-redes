'''
nombre: José Manuel Gutiérrez Pérez
fecha: 9 de octubre del 2023
Escenario
El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros.
En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.
Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.
Las funciones:
Se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente.
Toman un argumento (el valor correspondiente a sus nombres).
Complementa el código en el editor.
Ejecuta tu código y verifica si tu salida es la misma que la nuestra.
Aquí hay información para ayudarte:
1 milla = 1609.344 metros.
1 galón = 3.785411784 litros.
'''

def liters_100km_to_miles_gallon(liters):
    # 1 litro = 0.264172 galones
    # 1 kilómetro = 0.621371 millas
    miles_gallon = 100 / (liters * 0.264172 / 0.621371)
    return miles_gallon

def miles_gallon_to_liters_100km(miles):
    # 1 galón = 3.785411784 litros
    # 1 milla = 1609.344 metros
    liters_100km = 100 / (miles / 3.785411784 * 1609.344)
    return liters_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

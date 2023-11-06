'''
Autor: Jose Manuel Gutiérrez Pérez 
Descripcion: laboratorio 3.2.1.10
fecha: 2 de octubre del 2023

'''
# Indicar al usuario que ingrese una palabra
user_word=input("ingresa una palabra: ")

# y asignarlo a la variable user_word.
user_word = user_word.upper()

letras_sobrantes= ""

for letra in user_word:
    # Completa el cuerpo del bucle for.
 
    if letra in "AEIOU":
        continue  # Saltar la vocal y continuar con la siguiente iteración
    letras_sobrantes += letra  # Agregar la letra a las letras no consumidas
 


for letra in letras_sobrantes:
    print(letra)


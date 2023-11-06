'''
Autor: Jose Manuel Gutiérrez Pérez 
Descripcion: laboratorio 3.2.1.14
fecha: 2 de octubre del 2023

'''
# Solicitar al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra ingresada a mayúsculas
user_word = user_word.upper()

# Inicializar una cadena vacía para almacenar las letras no vocales
word_without_vowels = ""

# Recorrer cada letra en la palabra
for letter in user_word:
    # Verificar si la letra es una vocal (A, E, I, O, U)
    if letter in "AEIOU":
        continue  # Saltar las vocales y continuar con la siguiente iteración
    word_without_vowels += letter  # Concatenar las letras no vocales

# Imprimir las letras no vocales
print("Palabra sin vocales:", word_without_vowels)


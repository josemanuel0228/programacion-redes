'''
Autor: Jose Manuel Gutiérrez Pérez 
Descripcion: laboratorio 3.6.1.9
fecha: 2 de octubre del 2023

'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]


# Lista temporal para almacenar elementos únicos
lista_sin_repeticiones = []

# Iterar a través de la lista original
for elemento in my_list:
    # Verificar si el elemento no está en la lista temporal
    if elemento not in lista_sin_repeticiones:
        # Si no está en la lista temporal, agrégalo
        lista_sin_repeticiones.append(elemento)


print("La lista con elementos únicos:")
print(lista_sin_repeticiones)

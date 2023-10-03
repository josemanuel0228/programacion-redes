'''
Autor: Jose Manuel Gutiérrez Pérez 
Descripcion: laboratorio 3.2.1.11
fecha: 2 de octubre del 2023

'''
blocks = int(input("Ingresa el número de bloques: "))
height  = 0
bloques_utilizados = 0

# Calcular la altura de la pirámide
while bloques_utilizados + height + 1 <= blocks:
    height += 1
    bloques_utilizados += height

    
    
print("La altura de la pirámide:", height)

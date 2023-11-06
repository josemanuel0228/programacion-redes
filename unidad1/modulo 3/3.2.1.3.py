'''
Autor: Jose Manuel Gutiérrez Pérez 
Descripcion: laboratorio 3.2.1.3
fecha: 2 de octubre del 2023

'''
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")


while secret_number:
    numero = int(input("Adivina el número secreto: "))

    if numero == secret_number:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break  # Salir del bucle cuando el usuario adivina correctamente
    else:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")


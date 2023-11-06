'''
Autor: Jose Manuel Gutiérrez Pérez 
Descripcion: laboratorio 3.2.1.15
fecha: 2 de octubre del 2023

'''
# Solicitar al usuario que ingrese un número natural
c0 = int(input("Ingrese un número : "))

# Inicializar una variable para contar los pasos
pasos = 0

# Mientras c0 no sea igual a 1, seguir realizando los cálculos
while c0 != 1:
    # Mostrar el valor actual de c0
    print(c0)
    
    # Verificar si c0 es par o impar y calcular el nuevo valor de c0
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    
    # Incrementar el contador de pasos
    pasos += 1

# Imprimir el valor final de c0 y el número de pasos
print(c0)
print("Pasos =", pasos)

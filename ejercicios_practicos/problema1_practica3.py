'''
nombre: josé Manuel Gutiérrez Pérez 
asignatura: Programación de redes
descripcion: problema1_practica 3

'''
#5
datos = []

#6
for i in range(4):
    dato = int(input("Ingresa un número entero: "))
    datos.append(dato)

print("Los datos ingresados son:", datos)
#7
tuplaDatos = tuple(datos)


# 8
def desplegar_tupla(tupla):
    for dato in tupla:
        print(dato, end=' ')
    print()

# 9
print("Contenido de la tupla:")
desplegar_tupla(tuplaDatos)

# 10
print("Longitud de la tupla:", len(tuplaDatos))

# 11
def suma_tupla(tupla):
    return sum(tupla)

# 12
resultado_suma = suma_tupla(tuplaDatos)
print("Resultado de la suma de la tupla:", resultado_suma)



# 15
def multiplica_tupla(tupla):
    resultado = 1
    for dato in tupla:
        resultado *= dato
    return resultado
#16
resultado_multiplicacion = multiplica_tupla(tuplaDatos)
print("Resultado de la multiplicación de la tupla:", resultado_multiplicacion)
# 13
tuplaDatos = tuple(x * 2 if i == len(tuplaDatos) - 1 else x for i, x in enumerate(tuplaDatos))

# 14
print("Contenido de la tupla después de reemplazar el último elemento:", tuplaDatos)
# 17
tuplaResultado = tuple(x + y for x, y in zip(tuplaDatos, tuplaDatos))
print("Resultado de la suma de las dos tuplas:", tuplaResultado)





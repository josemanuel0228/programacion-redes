'''
nombre: josé Manuel Gutiérrez Pérez 
asignatura: Programación de redes
descripcion: problema1_practica 3

Clonar repositorio de la asignatura en tu máquina local o extraer los datos de la nube.
Crear una carpeta llamada ejercicios_practicos en repositorio local, dentro de la carpeta recién creada crear una carpeta llamada practica3
Crear un script llamado problema1_practica3 dentro de la carpeta practica3.
Dentro del script ingresar tus datos como comentarios: nombre, asignatura y descripción del problema.
Dentro del script crear una lista vacía llamada datos.
Solicitar al usuario cinco datos de tipo entero e irlos almacenando en la lista llamada datos.
Convertir la lista en una tupla llamada tuplaDatos.
Crear una función que tome como argumento la tupla y despliegue el contenido de la tupla e invocarlo en el script
Invocar a la función recién creada.
Desplegar la longitud o tamaño de la tupla.
Crear una función que tome como argumento la tupla y sumar los datos de la tupla, regresar el total de la suma y desplegar su resultado, por ejemplo
tuplaDatos(1,2,3,4) debería devolver 10
Invocar a la función del paso anterior
Reemplazar el contenido del último elemento de la tupla por el doble de su valor.
Desplegar el contenido de la función
Crear una función que tome como argumento la tupla y multiplique los datos de la tupla, regresar el total de la multiplicación  y desplegar su resultado, por ejemplo
multiplica([1,2,3,4]) debería devolver 24.
Invocar a la función del paso anterior.
Sumar a las dos tuplas y desplegar el contenido resultante.
Guarda los cambios y subir a GitHub


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





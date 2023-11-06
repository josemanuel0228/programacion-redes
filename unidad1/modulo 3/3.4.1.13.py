'''
Autor: Jose Manuel Gutiérrez Pérez 
Descripcion: laboratorio 3.4.1.13
fecha: 2 de octubre del 2023

'''
 # paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)


# paso 3
nuevos_miembros = ["Stu Sutcliffe", "Pete Best"]
for miembro in nuevos_miembros:
    Beatles.append(miembro)
print("Paso 3:", Beatles)

# paso 4
del Beatles[3:5]  # Elimina los elementos en los índices 3 y 
print("Paso 4:", Beatles)
4
# paso 5
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)



# probando la longitud de la lista
print("Los Fav", len(Beatles))

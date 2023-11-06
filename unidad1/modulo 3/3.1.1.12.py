'''
Autor: Jose Manuel Gutiérrez Pérez 
Descripcion: laboratorio 3.1.1.12
fecha: 2 de octubre del 2023

'''
year = int(input("Introduce un año:"))
if year < 1582:
    print(" No esta dentro del período del calendario Gregoriano")
else:
  if year%4 !=0:
     print("Año común")
  elif year%100 !=0:
         print ("Año bisiesto")
  elif year%400 !=0:
         print ("Año común")
  else:
        print ("Año bisiesto")
     
    
    
         
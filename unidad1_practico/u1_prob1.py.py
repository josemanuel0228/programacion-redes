'''
nombre: José Manuel Gutiérrez Pérez
fecha: 10 de septiembre del 2023
'''

cantidad= int(input("ingresa la cantidad"))
primer_año=0
primer_año_ahorrado=0
segundo_año_ahorrado=0
tercer_año_ahorrado=0
segundo_año=0
tercer_año=0
print("cantidad depositada en la cuenta de ahorros",cantidad)
primer_año= cantidad/100*0.04
primer_año_ahorrado= cantidad-primer_año
round(primer_año_ahorrado,2)
print (" cantidad de ahorro por una año",primer_año_ahorrado)
segundo_año= cantidad/100*0.08
segundo_año_ahorrado= cantidad+primer_año_ahorrado-segundo_año
round(segundo_año_ahorrado,2)
print (" cantidad de ahorro por una año",segundo_año_ahorrado)
tercer_año= cantidad/100*0.12
tercer_año_ahorrado= cantidad+segundo_año_ahorrado-tercer_año
round(tercer_año_ahorrado,2)
print (" cantidad de ahorro por una año",tercer_año_ahorrado)
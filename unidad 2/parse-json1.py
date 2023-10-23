'''
Descripcion: Consumiendo API con Python
Autor: José Manuel Gutiérrez Pérez
Fecha: 20 de octubre del 2023


'''
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo "
dest = "San Miguel de Allende"
key = "gNVacrUOnJeJ5cTuv1KFxJ8cx15DNYhT"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
print(url)
json_data = requests.get(url).json()
print(json_data ['route']['sessionId'])

# Estrae la distancia y el tiempo
print (json_data['route']['time'])
print (json_data['route']['distance'])
#Estraer del primer elemento legs el campo formatitedTime 
print (json_data['route']['legs'][0]['formattedTime'])






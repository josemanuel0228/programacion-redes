'''
Descripcion: Consumiendo API con Python
Autor: José Manuel Gutiérrez Pérez
Fecha: 20 de octubre del 2023


'''
import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    dest = input("Destination: ")

    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "gNVacrUOnJeJ5cTuv1KFxJ8cx15DNYhT"

    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest}) 
    print(url)
    json_data = requests.get(url).json()

    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
    # codificar para manejar el error distinto  a cero
    else:
        print("API Status: " + str(json_status) + " = A failed route call.\n")







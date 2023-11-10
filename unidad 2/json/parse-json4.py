'''
Descripcion: Consumiendo API con Python
Autor: José Manuel Gutiérrez Pérez
Fecha: 20 de octubre del 2023


'''
import urllib.parse
import requests

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break


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
   







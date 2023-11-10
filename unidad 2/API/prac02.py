'CityBikes'
import requests

url = 'https://community-citybikes.p.rapidapi.com/valenbisi.json'
headers = {
    'X-RapidAPI-Key': 'c0b8acd66fmshc7410b3a4886920p1adb72jsn7a2765ad01b0',
    'X-RapidAPI-Host': 'community-citybikes.p.rapidapi.com'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica si hay errores HTTP

    print(response.json())  # Si la respuesta es JSON
except requests.exceptions.RequestException as error:
    print(error)

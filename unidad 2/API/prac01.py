import requests

url = 'https://free-football-soccer-videos.p.rapidapi.com/'
headers = {
    'X-RapidAPI-Key': 'c0b8acd66fmshc7410b3a4886920p1adb72jsn7a2765ad01b0',
    'X-RapidAPI-Host': 'free-football-soccer-videos.p.rapidapi.com'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica si hay errores HTTP

    print(response.json())  # Si la respuesta es JSON
except requests.exceptions.RequestException as error:
    print(error)

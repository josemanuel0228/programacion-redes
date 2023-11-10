''
import requests

url = 'https://baseball-data.p.rapidapi.com/tournament/teams'
params = {'tournamentId': '10'}
headers = {
    'X-RapidAPI-Key': 'c0b8acd66fmshc7410b3a4886920p1adb72jsn7a2765ad01b0',
    'X-RapidAPI-Host': 'baseball-data.p.rapidapi.com'
}

try:
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()  # Verifica si hay errores HTTP

    print(response.json())  # Si la respuesta es JSON
except requests.exceptions.RequestException as error:
    print(error)

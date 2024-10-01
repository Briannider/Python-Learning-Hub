"""
Esta aplicacion trata de utilizar una Api
"""

import requests
import json

URL = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(URL, timeout=10)

if response.status_code == 200:
    print("Solicitud exitosa")
    data = response.json()

else:
    print("Error en la solicitud, detalles:", response.text)

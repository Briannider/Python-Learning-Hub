"""
Esta aplicacion trata de utilizar una Api la misma requiere de la libreria requests como se puede ver en el archivo requirements.txt
la misma realiza una peticion GET a la url https://pokeapi.co/api/v2/pokemon/ditto y la imprime en consola
"""

import requests

# import json

URL = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(URL, timeout=10)

if response.status_code == 200:
    print("Solicitud exitosa")
    data = response.json()
    print(data.get("abilities"))
else:
    print("Error en la solicitud, detalles:", response.text)
    print("Status:", response.status_code)

"""
Esta aplicacion trata de utilizar una Api la misma requiere de la libreria requests como se puede ver en el archivo requirements.txt
la misma realiza una peticion GET a la url https://pokeapi.co/api/v2/pokemon/ditto y la imprime en consola
"""

import requests

# import json
find = False
URL = "https://pokeapi.co/api/v2/pokemon"
poke_name = input("Ingresa el nombre del pokemon: ")

response = requests.get(URL, timeout=10)
if response.status_code == 200:
    print("Solicitud exitosa")
    data = response.json()

    pokemon_list = data["results"]
    for pokemon in pokemon_list:
        if pokemon["name"] == poke_name:
            find = True

    if find:
        print(f"{poke_name} encontrado")
    else:
        print(f"{poke_name} no encontrado")

else:
    print("Error en la solicitud, detalles:", response.text)
    print("Status:", response.status_code)

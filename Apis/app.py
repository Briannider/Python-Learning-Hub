"""
Esta aplicacion trata de utilizar una Api
"""
import requests
import json
URL = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(URL, timeout=10)

if response.status_code == 200:
    print('Solicitud exitosa')
    data = response.json()
    id = data['id']
    name = data['name']
    height = data['height']
    weight = data['weight']
    # mensaje = f"""
    # id: {id}
    # name: {name}
    # height: {height}
    # weight: {weight}
    # """
    # print(mensaje)

    print(json.dumps(data, indent=2))
    for ability in data["abilities"]:
        for clave, valor in ability.items():
            print(f"{clave}: {valor}")

else:
    print('Error en la solicitud, detalles:', response.text)

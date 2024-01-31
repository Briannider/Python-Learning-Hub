"""
Esta aplicacion trata de utilizar una Api
"""
import requests

URL = "https://jsonplaceholder.typicode.com/users/3"
response = requests.get(URL, timeout=10)

if response.status_code == 200:
    print('Solicitud exitosa')
    data = response.json()
    for llave, valor in data.items():
        print(llave, valor)
else:
    print('Error en la solicitud, detalles:', response.text)

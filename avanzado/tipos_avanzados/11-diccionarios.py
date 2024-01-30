# Son sumamente utilizados ya que las bases de datos retornan valores asi
# Lo de la izquierda si o si es un string y lo de la derecha cualquier cosa
punto = {"x": 25, "y": 50}

print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
# print(punto, punto["lala"])
if "lala" in punto:
    print("Encontre lala ", punto["lala"])


print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del (punto["y"])


print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])


for valor in punto.items():
    print(valor)


for llave, valor in punto.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nico"},
    {"id": 4, "nombre": "Brian"},
    {"id": 5, "nombre": "Rodrigo"},
    {"id": 6, "nombre": "Gonza"},
]


for usuario in usuarios:
    print(usuario["nombre"])

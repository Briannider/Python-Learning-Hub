mascotas = ["Pelusa", "Pulga", "Wolfgang",
            "Felipe", "Chanchito Feliz", "Wolfgang"]

# => Busca el indice en la lista del elemento
# print(mascotas.index("Chanchito Feliz"))


print(mascotas.count("Wolfgang"))
if "Wolfgang" in mascotas:
    print(mascotas.index("Wolfgang"))  # => Si no la encuentra muestra un error

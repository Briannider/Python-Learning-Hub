mascotas = ["Wolfgang", "Pelusa", "Pulga", "Felipe", "Pulga", "Rinoceronte"]

mascotas.insert(1, "Melvin")  # => Inserta el elemento sin eliminar en la lista
# => Agrega un elemento al final de la lista
mascotas.append("Chanchito triste")


mascotas.remove("Pulga")  # => Elimina el elemento buscado
# =>  Elimina el ultimo elemento o si le damos un indice seria el que este en dicha posicion
mascotas.pop(1)
# Elimina el ultimo elemento o si le damos un indice seria el que este en dicha posicion
del mascotas[0]
mascotas.clear()  # Limpia la lista
print(mascotas)

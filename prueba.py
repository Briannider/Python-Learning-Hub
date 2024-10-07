# print("Hola! Ingrese el total de la cuenta:")
# cuenta = float(input())
# print("Ingrese el porcentaje de propina:")
# porcentaje = float(input())
# propina = cuenta * (porcentaje / 100)
# total = cuenta + propina
# print("La propina es de: $" + str(propina))
# print("El total a pagar es de: $" + str(total))


# * Consigna Contar la frecuencia de palabras en una lista dada
my_list = [
    "Casa",
    "Perro",
    "Casa",
    "Árbol",
    "Coche",
    "Perro",
    "Casa",
    "Flor",
    "Árbol",
    "Coche",
    "Casa",
    "Pájaro",
    "Perro",
    "Casa",
    "Flor",
    "Árbol",
    "Coche",
    "Casa",
    "Pájaro",
    "Perro",
]


#! Luego de definir la lista procedemos a contar la frecuencia de palabras
my_dict = {}
for word in my_list:
    my_dict[word] = my_dict.get(word, 0) + 1

print(my_dict)

numeros = [2, 46, 51, 65, 74, 82, 17]

# numeros.sort()  # Ordena la lista
# numeros.sort(reverse=True)  # Ordena la lista
numeros2 = sorted(numeros, reverse=True)  # => Nueva lista
print(numeros)
print(numeros2)

usuarios = [
    ["Chanchito", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]


# => Las funciones lambda son funciones como ternarias
usuarios.sort(key=lambda el: el[1])
print(usuarios)

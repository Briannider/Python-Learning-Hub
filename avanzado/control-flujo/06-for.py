buscar = 2
for numero in range(5):  # range es un iterable
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("No encontrado :(")


for char in "Ultimate Python":
    print(char)

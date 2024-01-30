numeros = [1, 2, 3]

# Esto es horrible:
# primero = numeros [0]
# segundo = numeros [1]
# tercero = numeros [2]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, segundo, *otros, penultimo, ultimo = numeros
print(primero, segundo, penultimo, ultimo, otros)

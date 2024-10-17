# Tuplas son inmutables, no se pueden cambiar luego de ser creadas
# Se pueden concatenar
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# Se puede crear una tupla a partir de una lista
punto = tuple([1, 2])
print(punto)

# Se puede desempaquetar una tupla en variables
menosNumeros = numeros[:2]
print(menosNumeros)

# Se puede desempaquetar una tupla en variables con el *

primero, segundo, *otros = numeros
print(primero, segundo, otros)

# Se puede iterar sobre una tupla
for n in numeros:
    print(n)

# Se puede convertir una tupla en una lista
listaNumeros = list(numeros)
# Y se puede cambiar
listaNumeros[0] = "Chanchito Feliz"
print(listaNumeros)

# ? Unpacking Tupla (Desempaquetar Tupla) esto lo que hace es desempaquetar una tupla en variables individuales
tupla = (1, 2, 3)
a, b, c = tupla
print(a, b, c)

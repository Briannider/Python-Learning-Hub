# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

print(primer | segundo)  # Union de sets
print(primer & segundo)  # Interseccion de sets
print(primer - segundo)  # Diferencia de sets
print(primer ^ segundo)  # Diferencia simetrica de sets

# Los sets estan desordenados y no es posible acceder por indice a los mismos

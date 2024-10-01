def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("Hola mundo")
tamaño = largo("Hola mundo")
print(tamaño)

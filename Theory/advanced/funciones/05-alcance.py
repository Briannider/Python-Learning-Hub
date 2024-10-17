saludo = "Hola global"


def saludar():
    # global saludo  # Muy mala practica -> mo se recomienda
    saludo = "Hola Mundo"
    print(saludo)


# def saludaChanchito():
#     saludo = "Hola Chanchito"
#     print(saludo)


print(saludo)
saludar()
print(saludo)

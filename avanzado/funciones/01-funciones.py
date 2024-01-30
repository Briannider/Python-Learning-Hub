# def saludar(nombre, apellido):  # (nombre, apellido) => parametros "Ya que son definidos en la funcion"
#     print("Hola Mundo!")
#     print(f"Bienvenido {nombre} {apellido}")


# # ("Brian", "Niderhaus") => argumentos "Ya que son las variables pasadas como argumentos a la funcion"
# saludar("Brian", "Niderhaus")


# Hacer que la funcion tome valores por defecto como argumento
def saludar(nombre, apellido="Feliz"):  # Lo definimos previamente => haciendo apellido="Feliz"
    print("Hola Mundo!")
    print(f"Bienvenido {nombre} {apellido}")


saludar("Brian", )

# Pasar argumentos desordenados (Si o si hay que seguir la sintaxis)
saludar(apellido="Niderhaus", nombre="Brian")

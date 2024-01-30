# lista1 = [1, 2, 3, 4]
# # tupla = (1, 2, 3, 4)
# # print(*lista)
# # print(*tupla)

# lista2 = [5, 6]

# combinada = ["Hola", *lista1, *lista2, "chanchito"]
# print(combinada)


punto1 = {"x": 19, "y": "Hola"}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "Hola mundo", **punto2, "z": "mundo"}
print(nuevoPunto)

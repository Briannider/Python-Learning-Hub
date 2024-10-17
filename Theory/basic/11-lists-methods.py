lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
lenguajes.insert(3,"C++")
lenguajes.insert(0,"C")
lenguajes.remove("Ruby")
print(lenguajes.pop(1))

# Busqueda de elementos en una lista
if "Ruby" in lenguajes :
    print("Si existe amigote 😁")
else :
    print("Tu busqueda no existe 🥺")

print(len(lenguajes))
# El metodo clear limpia toda la lista
# lenguajes.clear()


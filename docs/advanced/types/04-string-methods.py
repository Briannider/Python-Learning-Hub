animal = " Happy little pig"
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.lstrip())
print(animal.rstrip())
print(animal.casefold())
print(animal.__sizeof__())
# .find() Search on the string and then return the position in int
# Retorna -1 si no se encuentra dentro de la cadena
print(animal.find("ch"))
print(animal.find("rh"))
# .replace() remplaza el valor buscado como primer parametro por el segundo parametro
print(animal.replace("Chan", "Pe"))
print("Chan" in animal)  # Busca la cadena en el string
print("Chan" not in animal)  # Busca que la cadena no se encuentre en el string

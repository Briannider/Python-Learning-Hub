temperatura = float(input("Ingrese la temperatura a transformar: "))
escala = input("En que escala esta la temperatura? (C = Celsius o F = Fahrenheit): ").upper()


if escala == "C":
    fahrenheit = (temperatura * 1.8) + 32
    print("La temperatura en Fahrenheit es: ", fahrenheit )
elif escala == "F":
    celcius = (temperatura - 32) * 5/9
    print("La temperatura en Celcius es: ", celcius )
else:
    print("Flaco decidite por una de las Dos, no cualquier cosa")

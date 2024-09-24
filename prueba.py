print("Hola! Ingrese el total de la cuenta:")
cuenta = float(input())
print("Ingrese el porcentaje de propina:")
porcentaje = float(input())
propina = cuenta * (porcentaje / 100)
total = cuenta + propina
print("La propina es de: $" + str(propina))
print("El total a pagar es de: $" + str(total))


# Mi manera de hacerlo:

# print("Bienvenido a la calculadora")
# print("Las operaciones son las siguientes: (suma, resta, div, multi)")
# print("Para salir escribe (salir)")

# operacion = input("ingrese la operacion a ejecutar: ").lower()

# while operacion != "salir":
#     n1 = int(input("Ingrese el primer numero: "))
#     n2 = int(input("Ingrese el segundo numero: "))

#     if operacion == "suma":
#         mensaje = f"El resultado es: {n1+n2} "
#         print(mensaje)
#     elif operacion == "resta":
#         mensaje = f"El resultado es:  {
#             n1-n2}" if n1 >= n2 else f"El resultado de {n2} - {n1} = {n2-n1}"
#         print(mensaje)
#     elif operacion == "div":
#         mensaje = f"El resultado es: {n1/n2}"
#         print(mensaje)
#     elif operacion == "multi":
#         mensaje = f"El resultado es: {n1*n2}"
#         print(mensaje)
#     else:
#         mensaje = f"La operacion {operacion} no existe"
#         print(mensaje)
#         print("Las operaciones son las siguientes: (suma, resta, div, multi)")

#     operacion = input("ingrese la operacion a ejecutar: ")


# La manera de HolaMundo de hacerlo:

print("Bienvenidos a la calculadora")
print("Para salir escribe (salir)")
print("Las operaciones son las siguientes: (suma, resta, div, multi)")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese numero")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operacion invalida")
        break

    print(f"El resultado es {resultado}")

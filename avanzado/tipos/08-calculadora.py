n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2 if n2 != 0 else "No se puede dividir por 0"
pot = n1**n2

mensaje = f"""
Para los numeros {n1} y {n2}:
la suma es = {suma}
la resta es = {resta}
la multiplicacion es = {multi}
la division es = {div}
la potencia es = {pot}
"""

print(mensaje)

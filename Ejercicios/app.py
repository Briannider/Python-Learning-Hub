"""
This application resolve this task: 
A computer starts by printing the numbers 2023, 2024 and 2025.
Then, without stopping, it continues printing the sum of the three most recent numbers it has printed, such as 6072, 10121, 18218, and so on.
Can you tell me what the last four digits of the number printed in position 2023202320232023 are?
To illustrate, in position 50, the printed number is 8188013234823360, which ends in 3360.
"""


def encontrar_ultimos_4_digitos(posicion_objetivo):

    tupla_original = (2023, 2024, 2025)
    a1, a2, a3 = tupla_original
    posicion = 4

    while True:
        num_sig = (a1 + a2 + a3) % 10000
        a1, a2, a3 = a2, a3, num_sig
        tupla_actual = (a1, a2, a3)

        if tupla_actual == (2023, 2024, 2025):
            longitud_ciclo = posicion - 3
            print(f"Longitud del ciclo: {longitud_ciclo}")
            pos_ciclo = posicion_objetivo % longitud_ciclo

            if pos_ciclo < 4:
                return tupla_actual[pos_ciclo - 1]
            else:
                for _ in range(pos_ciclo - 3):
                    num_sig = (a1 + a2 + a3) % 10000
                    a1, a2, a3 = a2, a3, num_sig
                return a3

        posicion += 1


posicion_objetivo = 2023202320232023
print(
    f"Últimas cuatro cifras en la posición {posicion_objetivo}: {encontrar_ultimos_4_digitos(posicion_objetivo)}"
)

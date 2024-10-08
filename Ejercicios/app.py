"""
This application resolve this task: 
A computer starts by printing the numbers 2023, 2024 and 2025.
Then, without stopping, it continues printing the sum of the three most recent numbers it has printed, such as 6072, 10121, 18218, and so on.
Can you tell me what the last four digits of the number printed in position 2023202320232023 are?
To illustrate, in position 50, the printed number is 8188013234823360, which ends in 3360.
"""


def encontrar_ultimos_4_digitos(posicion_objetivo: int) -> int:
    """
    Returns the last four digits of the number printed in the given position.

    Args:
        posicion_objetivo (int): The position of the number to find the last four digits of.

    Returns:
        int: The last four digits of the number printed in the given position.
    """
    tupla_original = (2023, 2024, 2025)
    a1, a2, a3 = tupla_original
    posicion = 4

    while True:
        # Calculate the next number in the sequence
        num_sig = (a1 + a2 + a3) % 10000
        # Update the current tuple
        a1, a2, a3 = a2, a3, num_sig
        # Create a tuple with the current values
        tupla_actual = (a1, a2, a3)

        # If the current tuple is the same as the original one, calculate the length of the cycle
        if tupla_actual == (2023, 2024, 2025):
            longitud_ciclo = posicion - 3
            print(f"Longitud del ciclo: {longitud_ciclo}")
            # Calculate the position in the cycle
            pos_ciclo = posicion_objetivo % longitud_ciclo

            # If the position in the cycle is less than 4, return the last four digits of the number in that position
            if pos_ciclo < 4:
                return tupla_actual[pos_ciclo - 1]
            else:
                # Iterate over the cycle until the position is reached
                for _ in range(pos_ciclo - 3):
                    num_sig = (a1 + a2 + a3) % 10000
                    a1, a2, a3 = a2, a3, num_sig
                # Return the last four digits of the number in the given position
                return a3

        # Increment the position
        posicion += 1


posicion_objetivo = 2023202320232023
print(
    f"Últimas cuatro cifras en la posición {posicion_objetivo}: {encontrar_ultimos_4_digitos(posicion_objetivo)}"
)

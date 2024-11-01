"""
This application solves the following task: 
A computer starts by printing the numbers 2023, 2024, and 2025.
Then, without stopping, it continues printing the sum of the three most recent numbers it has printed, such as 6072, 10121, 18218, and so on.
Can you tell me what the last four digits of the number printed in position 2023202320232023 are?
To illustrate, in position 50, the printed number is 8188013234823360, which ends in 3360.
"""


def find_last_4_digits(target_position: int) -> int:
    """
    Returns the last four digits of the number printed in the given position.

    Args:
        target_position (int): The position of the number to find the last four digits of.

    Returns:
        int: The last four digits of the number printed in the given position.
    """
    original_tuple = (2023, 2024, 2025)
    a1, a2, a3 = original_tuple
    position = 4

    while True:
        # Calculate the next number in the sequence
        next_num = (a1 + a2 + a3) % 10000
        # Update the current tuple
        a1, a2, a3 = a2, a3, next_num
        # Create a tuple with the current values
        current_tuple = (a1, a2, a3)

        # If the current tuple is the same as the original one, calculate the length of the cycle
        if current_tuple == (2023, 2024, 2025):
            cycle_length = position - 3
            print(f"Cycle length: {cycle_length}")
            # Calculate the position in the cycle
            cycle_pos = target_position % cycle_length

            # If the position in the cycle is less than 4, return the last four digits of the number in that position
            if cycle_pos < 4:
                return current_tuple[cycle_pos - 1]
            else:
                # Iterate over the cycle until the position is reached
                for _ in range(cycle_pos - 3):
                    next_num = (a1 + a2 + a3) % 10000
                    a1, a2, a3 = a2, a3, next_num
                # Return the last four digits of the number in the given position
                return a3

        # Increment the position
        position += 1


target_position = 2023202320232023
print(
    f"Last four digits in position {target_position}: {find_last_4_digits(target_position)}"
)

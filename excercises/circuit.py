"""
HalfAdder

Keyword arguments:
a -- integer (binary digit 0 or 1)
b -- integer (binary digit 0 or 1)

Return: The sum of both numbers in binary. It's called half-adder because this function don't look over the previous carry of the before sum.
"""


def ask_bit(message):
    while True:
        try:
            value = int(input(message))
            if value in (0, 1):
                return value
            else:
                print("⚠ You can only enter 0 or 1.")
        except ValueError:
            print("⚠ You must enter a number (0 or 1).")


def half_adder(a, b):
    # XOR for the sum
    summation = int((a or b) and not (a and b))
    # AND for the carry
    carry = int(a and b)
    return summation, carry


# Full adder for two bits
# def full_adder(a, b, c):
#     summation, carry = half_adder(a, b)
#     print(f"A={a}, B = {b} -> Sum={summation}, Carry={carry}")
#     full_adder(summation, carry)

#     return


#! Example
# ask the bit with validation
a = ask_bit("Enter first bit (0 or 1): ")
b = ask_bit("Enter second bit (0 or 1): ")

# calculate and display
s, c = half_adder(a, b)
print(f"A={a}, B = {b} -> Sum={s}, Carry={c}")

# Full_adder


# s, c = full_adder(a, b, c)

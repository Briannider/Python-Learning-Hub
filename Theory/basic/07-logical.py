"""
This code demonstrates how to use logical operators in Python.

Logical operators are used to combine conditional statements.

The `and` operator returns True if both the conditions are True.
The `or` operator returns True if at least one of the conditions is True.
The `not` operator returns True if the condition is False.

"""

age = 22

# Check if the age is greater than 18 and less than 30
print(age > 18 and age < 30)  # True

# Check if the age is greater than 18 or less than 30
print(age > 18 or age < 30)  # True

# Check if the condition is False
print(not True)  # False

# Check if the condition is True
print(not False)  # True

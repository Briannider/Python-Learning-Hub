"""
This code demonstrates how to get user input and store it in a variable.
It also checks the type of the variable and does some calculations with it.
"""

# Get user age and store it in a variable
age = input("Enter your age: ")
print(type(age))  # Check the type of the variable
age = int(
    age
)  # Convert the 'age' from a string to an integer to perform numerical operations
print(age + 22)  # Add 22 to the user age and print the result

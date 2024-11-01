# Welcome the user to the calculator program
print("Welcome to the calculator")
print("The operations are as follows: (add, subtract, divide, multiply)")
print("To exit, type (exit)")

# Prompt the user to enter an operation and convert it to lowercase
operation = input("Enter the operation to execute: ").lower()

# Start a loop that continues until the user types "exit"
while operation != "exit":
    # Get the first and second numbers from the user
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    # Perform the operation based on user input
    if operation == "add":
        message = f"The result is: {n1 + n2}"
    elif operation == "subtract":
        message = f"The result is: {n1 - n2}"
    elif operation == "divide":
        # Check for division by zero
        if n2 == 0:
            message = "Division by zero is undefined"
        else:
            message = f"The result is: {n1 / n2}"
    elif operation == "multiply":
        message = f"The result is: {n1 * n2}"
    else:
        message = f"The operation {operation} does not exist"
        print("The operations are as follows: (add, subtract, divide, multiply)")

    # Print the result message
    print(message)
    # Prompt the user to enter another operation or exit
    operation = input("Enter the operation to execute: ").lower()

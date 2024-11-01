def greet(name, surname="Happy"):
    """
    Greets a user with a welcome message.

    Parameters:
    name (str): The first name of the user.
    surname (str): The surname of the user. Defaults to 'Happy'.
    """
    print("Hello World!")
    print(f"Welcome {name} {surname}")


# Call the greet function with only the name argument
greet("Brian")

# Call the greet function with unordered arguments
greet(surname="Niderhaus", name="Brian")

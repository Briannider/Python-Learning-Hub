def convert_temperature():
    """
    Convert temperature between Celsius and Fahrenheit.

    Prompts the user to enter a temperature and its scale,
    then converts it to the other scale and prints the result.
    """
    # Get the temperature value from the user
    temperature = float(input("Enter the temperature to convert: "))

    # Get the temperature scale from the user and convert it to uppercase
    scale = input(
        "What scale is the temperature in? (C = Celsius or F = Fahrenheit): "
    ).upper()

    # Check if the scale is Celsius
    if scale == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * 1.8) + 32
        print("The temperature in Fahrenheit is: ", fahrenheit)
    # Check if the scale is Fahrenheit
    elif scale == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * 5 / 9
        print("The temperature in Celsius is: ", celsius)
    else:
        # Handle invalid scale input
        print("Dude, choose one of the two, not anything")


convert_temperature()

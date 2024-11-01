age = 18


def check_age_requirement(age):
    """
    Check if the user meets the age requirement.

    Parameters:
    age (int): The age of the user.

    Returns:
    None
    """
    # Check if the age is 18 or older
    if age >= 18:
        print("The user meets the age requirement")
    # Check if the age is less than 18
    elif age < 18:
        print("The user does not meet the age requirement")
    # This else block will never be executed with the current conditions
    else:
        print("Go away, little friend")


# Call the function to check the age requirement
check_age_requirement(age)

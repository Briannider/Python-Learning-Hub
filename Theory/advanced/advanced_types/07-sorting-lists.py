"""
This script demonstrates sorting lists in Python using both the sort method and the sorted function.
"""

# List of numbers
numbers = [2, 46, 51, 65, 74, 82, 17]

# Sort the list in reverse order and create a new list
numbers2 = sorted(numbers, reverse=True)
print(numbers)  # Original list remains unchanged
print(numbers2)  # New sorted list

# List of users with a name and a numerical value
users = [["Little pig", 4], ["Felipe", 1], ["Flea", 5]]

# Sort the list of users based on the second element of each sublist (the numerical value)
users.sort(key=lambda el: el[1])
print(users)  # Users list sorted by their numerical value

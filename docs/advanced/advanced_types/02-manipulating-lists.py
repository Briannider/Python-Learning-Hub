# Accessing elements in a list
pets = ["Wolfgang", "Fluff", "Flea", "Copito"]
print(pets[0])  # Access the first element
pets[0] = "The bug"  # Modify the first element

# Slicing a list
print(pets)
print(pets[1:3])  # Access elements from index 1 to 3
print(pets[-1])  # Access the last element
print(pets[1:2:2])  # Access every two elements, starting from index 1

# Manipulating a list of numbers
numbers = list(range(21))
print(numbers[::2])  # Every two elements
print(numbers[1::2])  # Odd elements

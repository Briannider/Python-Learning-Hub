# Tuples are immutable, meaning they cannot be changed after creation
numbers_tuple = (1, 2, 3) + (4, 5, 6)  # Concatenating tuples

# Tuples can also be created from other iterable types like lists
point = tuple([1, 2])

# Tuples support slicing, which can create a new tuple
fewer_numbers = numbers_tuple[:2]

# Tuple unpacking allows us to assign multiple variables at once
first, second, *others = numbers_tuple

# Tuples can be iterated over using a simple loop
for n in numbers_tuple:
    print(n)

# Convert tuple to a list to make it mutable (changeable)
list_numbers = list(numbers_tuple)

# Once converted to a list, we can modify elements
# list_numbers[0] = "Happy"  # Example of modification

# Tuple unpacking: assigning values from the tuple to variables in one line
tuple = (1, 2, 3)
a, b, c = tuple

# Extra: demonstrating tuple immutability
# Trying to modify an element in a tuple will result in an error
try:
    numbers_tuple[0] = 10  # This will raise a TypeError
except TypeError:
    print("Tuples are immutable and cannot be modified.")

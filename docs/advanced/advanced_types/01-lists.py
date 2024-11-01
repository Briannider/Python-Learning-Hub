# Lists are ordered collections of items that can be of any data type, including strings, integers, floats, and other lists.
# Lists are defined using square brackets and elements are separated by commas.
# Lists are mutable, meaning they can be changed after they are created.

numbers = [1, 2, 3]  # => List of integers
letters = ["a", "b", "c"]  # => List of strings
words = ["Happy", "little pig"]  # => List of strings
happyWords = [words, "Felipe", "Student"]  # => List of lists and strings
booleans = [True, False, True, False]  # => List of booleans
matrix = [[0, 1], [1, 0]]  # => List of lists (matrix)

# Automatic creation of a list with 10 cells filled with zeros
zeros = [0] * 10
# Automatic creation of a list alternating zeros and ones 10 times
zeros_ones = [0, 1] * 10

# Concatenation of lists
alphanumeric = numbers + letters

# List comprehension
range_list = list(range(1, 11))
characters = list("Hello world")

print(characters)

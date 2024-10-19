# set means group or set
"""
This code demonstrates the use of sets in Python.
It includes examples of the union, intersection, difference, and symmetric difference of sets.
"""

first = {1, 1, 2, 2, 3, 4}
second = [3, 4, 5]
second = set(second)

# Union of sets
print(first | second)  # {1, 2, 3, 4, 5}

# Intersection of sets
print(first & second)  # {3, 4}

# Set difference
print(first - second)  # {1, 2}

# Symmetric difference of sets
print(first ^ second)  # {1, 2, 5}

# Sets are unordered and cannot be accessed by index

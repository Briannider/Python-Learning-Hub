# Iterating over lists
# ======================

# => iterables, just like strings
pets = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

# Iterate over the list using a for loop
for pet in pets:
    print(pet)


# Iterate over the list using a for loop with an index
for index, pet in enumerate(pets):  # => Tuples
    """
    The enumerate() function adds a counter to an iterable and returns it in a form
    of enumerate object. The syntax is enumerate(iterable, start).
    """
    print(index, pet)

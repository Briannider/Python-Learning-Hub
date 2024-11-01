"""Examples of adding and removing elements from a list."""

pets = ["Wolfgang", "Fluff", "Flea", "Felipe", "Flea", "Rhinoceros"]

# Inserts the element without removing it from the list
pets.insert(1, "Melvin")

# Adds an element to the end of the list
pets.append("Sad Puppy")


# Removes the searched element
pets.remove("Flea")

# Removes the last element or if we give it an index, it would be the one in that position
pets.pop(1)

# Removes the last element or if we give it an index, it would be the one in that position
del pets[0]

# Clears the list
pets.clear()

print(pets)

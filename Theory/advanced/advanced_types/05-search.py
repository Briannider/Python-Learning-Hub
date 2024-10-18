pets = ["Pelusa", "Pulga", "Wolfgang", "Felipe", "Chanchito Feliz", "Wolfgang"]

"""
Checks if the element is in the list and returns its index
"""
# print(pets.index("Chanchito Feliz"))


"""
Counts the number of occurrences of the element in the list
"""
print(pets.count("Wolfgang"))


"""
Checks if the element is in the list and returns its index
If the element is not in the list, it raises a ValueError
"""
if "Wolfgang" in pets:
    print(pets.index("Wolfgang"))

# Unpacking Lists and Tuples
# ===========================

# Unpacking a list
list1 = [1, 2, 3, 4]
# Unpacking a tuple
tuple1 = (1, 2, 3, 4)

# Print the unpacked lists and tuples
print(*list1)
print(*tuple1)


# Unpacking Multiple Lists
list2 = [5, 6]

# Combine the lists
combined = ["Hello", *list1, *list2, "piglet"]
print(combined)


# Unpacking Dictionaries
point1 = {"x": 19, "y": "Hello"}
point2 = {"y": 15}

# Combine the dictionaries
newPoint = {**point1, "lala": "Hello world", **point2, "z": "world"}
print(newPoint)

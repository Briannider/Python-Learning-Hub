# Dictionaries are highly used because databases return values like this
# The left side must be a string and the right side can be anything
point = {"x": 25, "y": 50}

# Print the dictionary
print(point)

# Print the value of the key "x"
print(point["x"])

# Print the value of the key "y"
print(point["y"])

# Add a new key-value pair to the dictionary
point["z"] = 45

# Check if the key "lala" is in the dictionary
if "lala" in point:
    # Print the value of the key "lala" if it exists
    print("I found lala ", point["lala"])

# Get the value of the key "x" using the get() method
print(point.get("x"))

# Get the value of the key "lala" using the get() method
# If the key doesn't exist, return 97 as the default value
print(point.get("lala", 97))

# Delete the key "x" from the dictionary
del point["x"]

# Delete the key "y" from the dictionary
del point["y"]

# Print the dictionary after deleting the keys
print(point)

# Add a new key-value pair to the dictionary
point["x"] = 25

# Iterate over the keys in the dictionary
for value in point:
    # Print the key and value
    print(value, point[value])

# Iterate over the key-value pairs in the dictionary
for value in point.items():
    # Print the key and value
    print(value)

# Iterate over the key-value pairs in the dictionary
for key, value in point.items():
    # Print the key and value
    print(key, value)

# Create a list of dictionaries
users = [
    {"id": 1, "name": "Little pig"},
    {"id": 2, "name": "Happy"},
    {"id": 3, "name": "Nico"},
    {"id": 4, "name": "Brian"},
    {"id": 5, "name": "Rodrigo"},
    {"id": 6, "name": "Gonza"},
]

# Iterate over the list of dictionaries
for user in users:
    # Print the value of the key "name"
    print(user["name"])

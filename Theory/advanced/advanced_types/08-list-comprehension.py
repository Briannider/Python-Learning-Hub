# List comprehension is a powerful tool for creating lists in a concise manner.
# It can be used for mapping, filtering and transforming lists.
users = [["Little pig", 4], ["Felipe", 1], ["Flea", 5]]

# Mapping - Transform
# This code creates a new list with the names of the users.
names = [user[0] for user in users]

# Filtering - Filter
# This code creates a new list with the names of the users that have a value greater than 2.
names = [user for user in users if user[1] > 2]

# Transforming and Filtering - Map and Filter
# This code creates a new list with the names of the users that have a value greater than 2.
names = [user[0] for user in users if user[1] > 2]

# Using the map function
# This code creates a new list with the names of the users.
names = list(map(lambda user: user[0], users))

# Using the filter function
# This code creates a new list with the names of the users that have a value greater than 2.
fewerUsers = list(filter(lambda user: user[1] > 2, users))
print(fewerUsers)

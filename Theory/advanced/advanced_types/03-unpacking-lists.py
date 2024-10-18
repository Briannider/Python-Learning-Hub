# Unpacking lists
# =================

# A terrible way to unpack a list:
numbers = [1, 2, 3]

# This is terrible:
first = numbers[0]
second = numbers[1]
third = numbers[2]

# A better way to unpack a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Unpack the list into variables
first, second, *others, second_to_last, last = numbers

# Print the unpacked variables
print(first, second, second_to_last, last, others)

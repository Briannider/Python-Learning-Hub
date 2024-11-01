"""
Example of using a ternary operator to assign a value to a variable
based on a condition.

The ternary operator is a shorthand way of writing a simple if-else
statement.

In this example, the variable 'message' is assigned the string "Is
older" if the variable 'age' is greater than 17, or "Is younger" if
it is not.

"""

age = 18

# Use the ternary operator to assign a value to the variable 'message'
message = "Is older" if age > 17 else "Is younger"

# The same code written with an if-else statement
# if age < 17 :
#     message = "Is older"
# else:
#     message = "Is younger"

print(message)

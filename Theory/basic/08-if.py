# This program checks the score of a test and prints out if it is a pass or a fail

# The score of the test
score = 49

# Check if the score is lower than 50
if score < 50:
    # Print out that the test was failed
    print("Failed")
# Check if the score is lower than 95
elif score < 95:
    # Print out that the test was passed
    print("Passed")
# If the score is higher than 95
else:
    # Print out that the test was passed with honors
    print("Passed with honors")

# Print out that we are outside of the if
print("Outside the if")

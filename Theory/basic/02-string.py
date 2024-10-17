"""
Introduction to Strings
========================================================

This code demonstrates the basics of strings in Python.
It includes upper and lower case, finding the index of a
word, checking if a word is in the text, and replacing a
word in the text.

"""

# Print a simple string
print("Hello world")

# Perform string methods
text = "Hello world"

# Uppercase the text
print(text.upper())

# Lowercase the text
print(text.lower())

# Find the index of the word "world"
print(text.find("world"))

# Check if "world" is in the text
print("world" in text)

# Replace a word in the text
newText = text.replace("world", "childs")

# Print the original and modified text
print(text, newText)

# Check if "world" is still in the text
print("world" in text)

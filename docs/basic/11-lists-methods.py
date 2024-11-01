languages = ["Python", "Ruby", "PHP", "Javascript", "Java"]
languages.insert(3, "C++")
languages.insert(0, "C")
languages.remove("Ruby")
print(languages.pop(1))

# Search for elements in a list
if "Ruby" in languages:
    print("Yes, it exists! 😁")
else:
    print("Your search does not exist 🥺")

print(len(languages))
# The clear method clears the entire list
# languages.clear()

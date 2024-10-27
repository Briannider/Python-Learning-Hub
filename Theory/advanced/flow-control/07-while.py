# number = 1
# while number < 100:
#     print(number)
#     number *= 2

# command = ""

# while command.lower() != "exit":
#     command = input("$ ")
#     print(command)


while True:
    command = input("$ ")
    print(command)
    if command.lower() == "exit":
        break

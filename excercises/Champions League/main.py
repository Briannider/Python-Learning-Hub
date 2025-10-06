from functions import manual_loading
from functions import automatic_loading

author = "Briannider"
__author__ = author

teams = []


def main():
    choice = int
    choice = int(
        input(
            "How would you like to initialize the football teams? (automatic = 0, manual = 1): "
        )
    )
    if choice == 0:
        print("Teams will be created automatically.")
        teams_count = int(input("How many teams? "))
        teams = automatic_loading(teams_count)
        for i in range(len(teams)):
            print(teams[i])
    elif choice == 1:
        print("You will enter the teams manually.")
        teams_count = int(input("How many teams? "))
        teams = manual_loading(teams_count)
        for i in range(len(teams)):
            print(teams[i])
    else:
        print("Invalid option.")


main()

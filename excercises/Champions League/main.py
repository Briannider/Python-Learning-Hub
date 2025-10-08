from functions import (
    clasification_order,
    generate_table,
    manual_loading,
    automatic_loading,
    show_table,
)

author = "Briannider"
__author__ = author

teams = []


def main():
    print("CHAMPIONS LEAGUE")
    print("=" * 80)
    option = int(
        input(
            "How would you like to initialize the football teams? (automatic = 0, manual = 1): "
        )
    )
    if option == 0:
        print("Teams will be created automatically.")
        teams_count = int(input("How many teams? "))
        teams = automatic_loading(teams_count)
        teams = clasification_order(teams, 1)
        for i in range(len(teams)):
            print(teams[i])
    elif option == 1:
        print("You will enter the teams manually.")
        teams_count = int(input("How many teams? "))
        teams = manual_loading(teams_count)
        for i in range(len(teams)):
            print(teams[i])
    else:
        print("Invalid option.")


main()

from functions import manual_loading
from functions import automatic_loading

author = "Briannider"
__author__ = author

teams = []


def main():
    choice = int
    print(
        "¿how would you like to initialice the futball teams? (automatic = 0 or manual = 1)"
    )
    while (choice != 0) or (choice != 1):
        teams = automatic_loading(10)
        for i in range(len(teams)):
            print(teams[i])

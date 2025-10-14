__author__ = "Briannider"

import random
from team import Team

#!Constants
MAX_POINTS = 20

# * Example list of 50 football team names (real + invented)
champions_league_teams = [
    #!REAL
    "Manchester United",
    "Manchester City",
    "Liverpool",
    "Chelsea",
    "Arsenal",
    "Tottenham Hotspur",
    "Newcastle United",
    "Aston Villa",
    "West Ham United",
    "Brighton & Hove Albion",
    "Everton",
    "Wolverhampton Wanderers",
    "Crystal Palace",
    "Fulham",
    "Nottingham Forest",
    "Brentford",
    "Bournemouth",
    "Leicester City",
    "Leeds United",
    "Southampton",
    #!INVENTED
    "Iron Valley Rovers",
    "Silverlake United",
    "Highland Warriors",
    "Eastport Mariners",
    "Blackstone FC",
    "Redwood Rangers",
    "Stormbridge City",
    "Northgate Lions",
    "Ashford Falcons",
    "Riverdale Titans",
    "Kingsport Thunder",
    "Oakwood Spartans",
    "Seabreeze Wanderers",
    "Stonehaven Wolves",
    "Greenfield Eagles",
    "Brookside Panthers",
    "Hillcrest Hawks",
    "Lakeshore Giants",
    "Midtown Chargers",
    "Westbridge Stallions",
    "Harborview Sharks",
    "Pinehill Bears",
    "Silverpeak Dragons",
    "Cedarfield Knights",
    "Grandport Raiders",
    "Maplewood Bulls",
    "Ravenhill Ravens",
    "Sunset Strikers",
    "Ironforge Titans",
    "Clearwater Comets",
]


def manual_loading(n):
    v = [None] * n
    for i in range(n):
        team_name = input("Enter the team : ")
        points = input("Points: ")
        goals = input("Goals: ")
        v[i] = Team(team_name, points, goals)
        return v


def automatic_loading(n):
    v = [None] * n
    random.shuffle(champions_league_teams)
    for i in range(n):
        team_name = champions_league_teams[i]
        points = random.randint(0, MAX_POINTS)
        goals = random.randint(0, 100)
        v[i] = Team(team_name, points, goals)
    return v


def clasification_order(v, option):  # Asc = 0 || Dsc = 1
    """
    Sorts a list of Team objects by points using bubble sort.

    Args:
        v (list): List of Team objects.
        option (int): Sorting option.
            - 0: Ascending order.
            - 1: Descending order.

    Returns:
        list: The sorted list of Team objects.
    """
    n = len(v)

    # Define the comparison function once
    if option == 0:

        def compare(a, b):
            return a.points > b.points
    elif option == 1:

        def compare(a, b):
            return a.points < b.points
    else:
        raise ValueError("Invalid option. Use 0 for Asc or 1 for Desc.")

    for i in range(n):
        for j in range(0, n - i - 1):
            if compare(v[j], v[j + 1]):
                v[j], v[j + 1] = v[j + 1], v[j]

    return v


def generate_table(teams):
    return [[team.team_name, team.points, team.goals] for team in teams]


def show_table(teams):
    headers = ["Equipo", "Puntos", "Goles"]
    rows = generate_table(teams)

    # Calcula el ancho de cada columna (incluye encabezados)
    col_widths = [
        max(len(str(cell)) for cell in column) for column in zip(*([headers] + rows))
    ]

    # Función para imprimir una fila con alineación
    def print_row(row):
        print(
            " | ".join(str(cell).ljust(width) for cell, width in zip(row, col_widths))
        )

    # Imprime encabezado y separador
    print_row(headers)
    print("-+-".join("-" * width for width in col_widths))

    # Imprime cada fila de datos
    for row in rows:
        print_row(row)

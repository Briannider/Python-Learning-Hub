__author__ = "Briannider"

import random
from team import Team

# Example list of 50 football team names (real + invented)
teams_name = [
    # Premier League / real clubs
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
    # Invented but realistic
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
    # Extra invented to reach 50
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
    random.shuffle(teams_name)
    for i in range(n):
        team_name = teams_name[i]
        points = random.randint(0, 20)
        goals = random.randint(0, 100)
        v[i] = Team(team_name, points, goals)
    return v

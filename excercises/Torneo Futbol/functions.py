__author__ = 'Briannider'

import random
from clase import Team

teams_name = [
    "Manchester United",
    "Liverpool",
    "Chelsea",
    "Arsenal",
    "Mancheste City",
    "Juventus",
    "AC Milan",
    "Inter Milan",
    "Ajax",
    "Porto",
    "Benfica",
    "Sporting CP",
    "Galatasaray",
    "Fenerbahce",
    "LA Galaxy",
    "New York City FC",
    "Inter Miami",
    "Toronto FC",
    "River Plate",
    "Boca Juniors",
    "Flamengo",
    "Palmeiras",
    "Santos"]


def manual_loading(n):
    v = [None] * n
    for i in range(n):
        team_name = input('Enter the team : ')
        points = input('Points: ')
        goals = input('Goals: ')
        v[i] = Team(team_name, points, goals)
        return v


def automatic_loading(n):
    v = [None] * n
    for i in range(n):
        team_name = random.choice(teams_name)
        points = random.randint(0, 20)
        goals = random.randint(0, 100)
        v[i] = Team(team_name, points, goals)
    return v

class Team:
    
    def __init__(self, team_name, points, goals ):
        self.team_name = team_name
        self.points = points
        self.goals = goals
        
    def __str__(self):
        return 'Team: {} - Points: {} - Goals: {}'.format(self.team_name, self.points, self.goals)
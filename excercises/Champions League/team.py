class Team:
    
    def __init__(self, team_name, points, goals ):
        self.team_name = team_name
        if points >= 0 and points <= 20:
            self.points = points
        else: 
            raise ValueError("Be real!")
        if goals <= 100:
            self.goals = goals
        else: 
            raise ValueError("Be real!")
            
        
    def __str__(self):
        return 'Team: {} - Points: {} - Goals: {}'.format(self.team_name, self.points, self.goals)
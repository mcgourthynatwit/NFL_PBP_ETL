from Pipeline.nfl_verse.helpers.get_teams import get_teams
import os 

def get_offense_totals():
    return 

def get_team_totals(directory):
    teams = get_teams()

    for team in teams:
        team_dir = os.path.join(directory, team)
        offense_plays = os.path.join(team_dir, "Offense", "plays.csv")
        get_offense_totals(offense_plays)
    return 
from Pipeline.nfl_verse.helpers.get_teams import get_teams
from Pipeline.nfl_verse.helpers.pass_plays import get_pass_play_stats
import os 
import pandas as pd

def get_offense_totals(offense_plays):
    return 

def get_team_totals(directory):
    teams = get_teams()
    team_stats = []
    for team in teams:
        team_dir = os.path.join(directory, team)
        offense_play_dir = os.path.join(team_dir, "Offense", "plays.csv")

        offense_plays = pd.read_csv(offense_play_dir)
        team_totals = {
            "team" : team,
            "pass_yards_sack" : 0,
            "pass_yards" : 0,
            "air_yards" : 0,
            "yards_after_catch" : 0,
            "interceptions" : 0,
            "completions" : 0,
            "attempts" : 0
        }

        for _, play in offense_plays.iterrows():
            if play['play_type'] == 'pass':
                sack_yards, pass_yards, air_yards, yards_after_catch, interception, completion, attempt = get_pass_play_stats(play)
                team_totals['pass_yards_sack'] += sack_yards
                team_totals['pass_yards'] += pass_yards
                team_totals['air_yards'] += air_yards
                team_totals['yards_after_catch'] += yards_after_catch
                team_totals['interceptions'] += interception
                team_totals['completions'] += completion
                team_totals['attempts'] += attempt
        team_stats.append(team_totals)
    
    sorted_team_stats = sorted(team_stats, key=lambda x: x['pass_yards_sack'], reverse=True)

    for team_stat in sorted_team_stats:
        print(f"{team_stat['team']} : {team_stat['attempts']} attempts for {team_stat['pass_yards_sack']} yards. {team_stat['interceptions']} interceptions")

    return 
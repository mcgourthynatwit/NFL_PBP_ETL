from Pipeline.nfl_verse.helpers.get_teams import get_teams
from Pipeline.nfl_verse.helpers.pass_plays import get_pass_play_stats
from Pipeline.nfl_verse.helpers.run_plays import get_rush_play_stats
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
        team_pass_totals = {
            "team" : team,
            "pass_yards_sack" : 0,
            "pass_yards" : 0,
            "air_yards" : 0,
            "yards_after_catch" : 0,
            "interceptions" : 0,
            "completions" : 0,
            "attempts" : 0
        }

        team_run_totals = {
            "team" : team,
            "attempts" : 0,
            "rush_yards" : 0,
            "touchdowns" : 0,
            "fumbles" : 0,
        }

        for _, play in offense_plays.iterrows():
            if play['play_type'] == 'pass':
                sack_yards, pass_yards, air_yards, yards_after_catch, interception, completion, attempt = get_pass_play_stats(play)
                team_pass_totals['pass_yards_sack'] += sack_yards
                team_pass_totals['pass_yards'] += pass_yards
                team_pass_totals['air_yards'] += air_yards
                team_pass_totals['yards_after_catch'] += yards_after_catch
                team_pass_totals['interceptions'] += interception
                team_pass_totals['completions'] += completion
                team_pass_totals['attempts'] += attempt
            if play['play_type'] == 'run' or play['qb_kneel'] == 1:
                attempt, rush_yards, touchdown, fumble = get_rush_play_stats(play)
                team_run_totals['attempts'] += attempt
                team_run_totals['rush_yards'] += rush_yards
                team_run_totals['touchdowns'] += touchdown
                team_run_totals['fumbles'] += fumble
            
        team_stats.append(team_run_totals)
    
    sorted_team_stats = sorted(team_stats, key=lambda x: x['touchdowns'], reverse=True)

    for team_stat in sorted_team_stats:
        print(f"{team_stat['team']} : {team_stat['attempts']} attempts for {team_stat['rush_yards']} yards. {team_stat['touchdowns']} touchdowns")

    return 
# Organizes plays into team folders( pass plays to passing, rush plays to rushing, etc )
import pandas as pd 
import os
from Pipeline.helpers.play_operations import organize_team_plays_defense
from Pipeline.helpers.play_operations import organize_team_plays_offense

def organize_plays(pbp_directory, teams_directory):
    df = pd.read_csv(pbp_directory)

    for team in os.listdir(teams_directory):
        defense_directory = os.path.join(teams_directory, team, "Defense", "plays.csv")
        offense_directory = os.path.join(teams_directory, team,  "Offense", "plays.csv")

        defense_df = organize_team_plays_defense(df, team)
        offense_df = organize_team_plays_offense(df, team)


        defense_df.to_csv(defense_directory, index=False)
        offense_df.to_csv(offense_directory, index=False)
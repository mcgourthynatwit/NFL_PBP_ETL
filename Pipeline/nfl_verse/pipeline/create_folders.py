import os 
from Pipeline.nfl_verse.helpers.get_teams import get_teams
import pandas as pd

def make_subfolders(dir, subfolder_name, subfolders):
    subfolder_dir = os.path.join(dir, subfolder_name)
    os.makedirs(subfolder_dir)

    for subfolder in subfolders:
        sub_dir = os.path.join(subfolder_dir, subfolder)
        os.makedirs(sub_dir)

def get_max_week(df):
    week = df[df['season_type'] == 'REG']['week'].max()
    return week

def create_week_folders(week, directory):
    week_directory = os.path.join(directory, 'Weeks')
    os.makedirs(week_directory)

    for i in range(1, (week+1)):
        current_week_directory = os.path.join(week_directory, str(i))
        os.makedirs(current_week_directory)
    print("Week folders created")

def create_team_folders(directory):
    team_directory = os.path.join(directory, "Teams")
    if os.path.exists(team_directory):
        return
    os.makedirs(team_directory)

    offense_subfolders = ['Passing', 'Rushing', 'Conversions']
    defense_subfolders = ['Passing', 'Rushing', 'Conversions']
    player_subfolders = ['Qb', 'Rb', 'Rec']

    teams = get_teams()

    for team in teams:
        team_dir = os.path.join(team_directory, team)
        os.makedirs(team_dir)
        make_subfolders(team_dir, 'Offense', offense_subfolders)
        make_subfolders(team_dir, 'Defense', defense_subfolders)
        make_subfolders(team_dir, 'Players', player_subfolders)

    print("Team folders created")

def create_folders(year, df):
    directory = os.path.join("Clean_Data/", str(year))
    
    print("Creating team folders")
    create_team_folders(directory)

    #max_week = get_max_week(df)

    #print("Creating week folders")
    #create_week_folders(max_week, directory)

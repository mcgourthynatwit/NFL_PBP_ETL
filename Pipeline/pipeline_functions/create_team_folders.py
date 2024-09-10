import os 
import pandas as pd 
from helpers.get_teams.py import *

offense_subfolders = ['Passing', 'Rushing', 'Conversions']
defense_subfolders = ['Passing', 'Rushing', 'Conversions']
player_subfolders = ['Qb', 'Rb', 'Rec']

def make_subfolders(dir, subfolder_name, subfolders):
    subfolder_dir = os.path.join(dir, subfolder_name)
    os.makedirs(subfolder_dir)

    for subfolder in subfolders:
        sub_dir = os.path.join(subfolder_dir, subfolder)
        os.makedirs(sub_dir)

def create_team_folders(source_directory, end_directory):
    df = pd.read_csv(source_directory)

    teams = get_teams(df)

    for team in teams:
        team_dir = os.path.join(end_directory, team)
        os.makedirs(team_dir)
        make_subfolders(team_dir, 'Offense', offense_subfolders)
        make_subfolders(team_dir, 'Defense', defense_subfolders)
        make_subfolders(team_dir, 'Players', player_subfolders)
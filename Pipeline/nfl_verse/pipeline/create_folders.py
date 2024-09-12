import os 
from Pipeline.nfl_verse.helpers.get_teams import get_teams

def make_subfolders(dir, subfolder_name, subfolders):
    subfolder_dir = os.path.join(dir, subfolder_name)
    os.makedirs(subfolder_dir)

    for subfolder in subfolders:
        sub_dir = os.path.join(subfolder_dir, subfolder)
        os.makedirs(sub_dir)

def create_folder(year):
    directory = os.path.join("Clean_Data/", str(year))
    os.makedirs(directory)

    offense_subfolders = ['Passing', 'Rushing', 'Conversions']
    defense_subfolders = ['Passing', 'Rushing', 'Conversions']
    player_subfolders = ['Qb', 'Rb', 'Rec']

    teams = get_teams()

    for team in teams:
        team_dir = os.path.join(directory, team)
        os.makedirs(team_dir)
        make_subfolders(team_dir, 'Offense', offense_subfolders)
        make_subfolders(team_dir, 'Defense', defense_subfolders)
        make_subfolders(team_dir, 'Players', player_subfolders)
from Pipeline.helpers.utils_operations import calc_duration
from Pipeline.helpers.utils_operations import get_teams
import os 
import pandas as pd 

# Creates blank CSV files for each game_id passed and places them into the correct week number folder
# Used by: create_week_files
def create_files(directory, week, game_id_arr):
    week_dir = os.path.join(directory, week)

    if not os.path.exists(week_dir):
        os.makedirs(week_dir)

    for game_id in game_id_arr:
        file_path = os.path.join(week_dir, f"{game_id}.csv")
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass 

# Iterates through all games and calls create_files to create blank CSV files for each week's game
# Used by: split_games.py 
def create_week_files(df, dates_with_weeks, week_directory):
    current_week = 1

    game_ids = []

    for date in dates_with_weeks.keys():
        if dates_with_weeks[date] is not current_week:
            create_files(week_directory, str(current_week), game_ids)
            game_ids = []
            current_week += 1
        
        games_on_date = df[df['GameDate'] == date]

        for _, row in games_on_date.iterrows():
            if row['GameId'] not in game_ids:
                game_ids.append(row['GameId'])

    # create the last week files
    create_files(week_directory, str(current_week), game_ids)

# Place plays from each game into correct file where plays are ordered from beginning to end
# Used by: split_games.py 
def sort_plays_to_file(df, directory, dates_with_weeks):
    for week in os.listdir(directory):
        week_path = os.path.join(directory, week)

        for game in os.listdir(os.path.join(directory, week)):
            game_path = os.path.join(week_path, game)

            game_id = game[:-4] # remove file ext

            game_df = df[df['GameId'] == int(game_id)]
            
            game_df['GameDate'] = game_df['GameDate'].astype(str)

            game_df['Duration'] = game_df.apply(calc_duration, axis=1)

            game_df['Week'] = game_df['GameDate'].map(dates_with_weeks)

            offense_team = game_df.iloc[0]['OffenseTeam']
            defense_team = game_df.iloc[0]['DefenseTeam']

            game_df[f'{offense_team}'] = 0
            game_df[f'{defense_team}'] = 0

            game_df.sort_values(by='Duration', inplace=True)
            game_df.to_csv(game_path, index=False)

# Helper function for create_team_folders
def make_subfolders(dir, subfolder_name, subfolders):
    subfolder_dir = os.path.join(dir, subfolder_name)
    os.makedirs(subfolder_dir)

    for subfolder in subfolders:
        sub_dir = os.path.join(subfolder_dir, subfolder)
        os.makedirs(sub_dir)

# Function to create team folders inside of a directory, used when creating a years blank folder for data
def create_team_folders(source_directory, end_directory):
    offense_subfolders = ['Passing', 'Rushing', 'Conversions']
    defense_subfolders = ['Passing', 'Rushing', 'Conversions']
    player_subfolders = ['Qb', 'Rb', 'Rec']

    df = pd.read_csv(source_directory)

    teams = get_teams(df)

    for team in teams:
        team_dir = os.path.join(end_directory, team)
        os.makedirs(team_dir)
        make_subfolders(team_dir, 'Offense', offense_subfolders)
        make_subfolders(team_dir, 'Defense', defense_subfolders)
        make_subfolders(team_dir, 'Players', player_subfolders)
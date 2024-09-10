import pandas as pd 
from Pipeline.helpers.utils_operations import get_teams
from Pipeline.helpers.date_operations import get_week
from Pipeline.helpers.file_operations import create_week_files
from Pipeline.helpers.file_operations import sort_plays_to_file
import os, re 

# Splits plays from pbp CSV file into their according games, sorted into according weeks folder
# Game plays are sorted in ascending order where first play is in the first row
# Used by: organize_pbp.py 

def split_games(source_directory, end_directory):
    df = pd.read_csv(source_directory)

    dropped_columns = ['Unnamed: 10', 'Unnamed: 12', 'Unnamed: 16', 'Unnamed: 17', 'IsMeasurement']
    df = df.drop(columns = dropped_columns)
    
    teams = get_teams(df)

    dates = (df['GameDate'].unique())
    dates = pd.to_datetime(dates)
    dates = sorted(dates)

    dates_with_weeks = get_week(dates)

    # Create week folder 1-18
    for i in range(1, 19):
        week_path = os.path.join(end_directory, str(i))

        if not os.path.exists(week_path):
            file_dir = os.path.join(week_path)
            os.makedirs(file_dir)

    create_week_files(df, dates_with_weeks, end_directory)

    sort_plays_to_file(df, end_directory)
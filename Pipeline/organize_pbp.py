# python3 -m Pipeline.organize_pbp

import os 
YEAR = 2023
SRC_DIRECTORY = "Data/pbp-2023.csv"
WEEK_DIRECTORY = "Clean_Data/Weeks"
TEAMS_DIRECTORY = "Clean_Data/Teams"

from Pipeline.pipeline_functions.split_games import split_games
from Pipeline.pipeline_functions.fix_direct_snap import fix_direct_snap
from Pipeline.helpers.file_operations import create_team_folders
from Pipeline.pipeline_functions.organize_plays import organize_plays
from Pipeline.pipeline_functions.team_totals import get_team_totals

#create_team_folders(SRC_DIRECTORY, TEAMS_DIRECTORY)
#fix_direct_snap(SRC_DIRECTORY)
#split_games(SRC_DIRECTORY, WEEK_DIRECTORY)

#organize_plays(SRC_DIRECTORY, TEAMS_DIRECTORY)

get_team_totals(TEAMS_DIRECTORY, "DAL")
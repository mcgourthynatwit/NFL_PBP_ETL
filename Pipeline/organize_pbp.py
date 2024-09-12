# python3 -m Pipeline.organize_pbp

import os 
import nfl_data_py as nfl
import pandas as pd
from Pipeline.nfl_verse.pipeline.create_folders import create_folders
from Pipeline.nfl_verse.pipeline.create_folders import get_max_week

play_cols = [
    "play_id",
    "game_id",
    "home_team",
    "away_team",
    "season_type",
    "week",
    "posteam",
    "drive",
    "qtr",
    "time",
    "down",
    "goal_to_go",
    "ydstogo",
    "yrdln",
    "desc",
    "play_type",
    "yards_gained",
    "shotgun",
    "qb_dropback",
    "qb_kneel",
    "qb_spike",
    "qb_scramble",
    "air_yards",
    "yards_after_catch",
    "run_location",
    "run_gap",
    "total_home_score",
    "total_away_score",
    "fg_prob",
    "td_prob",
    "ep",
    "epa",
    "incomplete_pass",
    "interception",
    "solo_tackle",
    "pass_attempt",
    "rush_attempt",
    "penalty",
    "qb_hit",
    "sack",
    "touchdown",
    "roof",
    "temp",
    "wind",
    "penalty_team",
    "penalty_yards",
    "two_point_conv_result",
    "fixed_drive",
    "drive_quarter_start",
    "drive_quarter_end",
    "drive_first_downs",
    "drive_inside20",
    "drive_ended_with_score",
    "drive_end_transition",
    "drive_start_yard_line",
    "first_down",
    "score_differential"
]

year = 2023

print("Importing pbp data...")
#df = nfl.import_pbp_data(years=[year], downcast=False, columns=play_cols)
df = pd.read_csv("Raw_data/pbp.csv")
#df.to_csv("pbp.csv", index=False)

print("Calling create_folders")
create_folders(year, df)

import pandas as pd
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_API_KEY = os.getenv('SUPABASE_KEY')

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

table_name = 'pbp_2024'
csv_path = "Raw_Data/play_by_play_2024.csv"

df = pd.read_csv(csv_path, low_memory=False)

# Function to map pandas dtypes to PostgreSQL types
def get_pg_type(dtype):
    if 'int' in str(dtype):
        return 'integer'
    elif 'float' in str(dtype):
        return 'float'
    elif 'datetime' in str(dtype):
        return 'timestamp'
    else:
        return 'text'

general_offense_pbp_cols = [
        "play_id",
        "game_id",
        "season_type",
        "week",
        "home_team",
        "away_team",
        "posteam",
        "posteam_type",
        "defteam",
        "yardline_100",
        "game_date",
        "half_seconds_remaining",
        "game_half",
        "qtr",
        "drive",
        "down",
        "goal_to_go",
        "time",
        "ydstogo",
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
        "score_differential",
        "first_down_rush",
        "first_down_pass",
        "first_down_penalty",
        "third_down_converted",
        "fourth_down_converted",
        "interception",
        "fumble_forced",
        "fumble_not_forced",
        "solo_tackle",
        "penalty",
        "tackled_for_loss",
        "fumble_lost",
        "qb_hit",
        "rush_attempt",
        "pass_attempt",
        "sack",
        "touchdown",
        "two_point_attempt",
        "complete_pass",
        "passer_player_id",
        "passing_yards",
        "receiver_player_id",
        "receiver_player_name",
        "receiving_yards",
        "rusher_player_name",
        "rusher_player_id",
        "rushing_yards",
        "lateral_rusher_player_id",
        "lateral_rushing_yards",
        "lateral_receiving_yards",
        "lateral_receiver_player_id",
        "penalty_yards",
        "penalty_team",
        "cp",
        "cpoe",
        "series",
        "fixed_drive",
        "drive_play_count",
        "drive_time_of_possession",
        "drive_first_downs",
        "drive_inside20",
        "drive_ended_with_score",
        "drive_end_transition",
        "drive_start_yard_line",
        "roof",
        "temp",
        "wind"
    ]

df = df[general_offense_pbp_cols]

columns = ',\n    '.join([f"\"{col}\" {get_pg_type(df[col].dtype)}" for col in df.columns])
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id SERIAL PRIMARY KEY,
    {columns}
);
"""

with open('Pipeline/supabase/query.txt', 'w') as file:
    file.write(create_table_query)

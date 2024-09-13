# Organizes plays in the play-by-play CSV into each team's respective folder with set columns
import os 
import pandas as pd
from Pipeline.nfl_verse.helpers.get_teams import get_teams
from Pipeline.nfl_verse.helpers.save_offense_plays import save_offense_plays
def offense_play(play):
    offense_cols = [
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
        "no_score_prob",
        "fg_prob",
        "td_prob",
        "ep",
        "epa",
        "total_home_epa",
        "total_away_epa",
        "total_home_rush_epa",
        "total_away_rush_epa",
        "total_home_pass_epa",
        "total_away_pass_epa",
        "wp",
        "wpa",
        "vegas_wp",
        "vegas_wpa",
        "total_home_rush_wpa",
        "total_away_rush_wpa",
        "total_home_pass_wpa",
        "total_away_pass_wpa",
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
        "receiving_yards",
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

    return play[offense_cols]

def organize_plays(directory, df):
    teams = get_teams()
    teams_complete = 0 
    total_teams = len(teams)

    for team in teams:
        offense_plays = []
        #defense_plays = []
        team_dir = os.path.join(directory, team)

        offense_dir= os.path.join(team_dir, "Offense")
        offense_file = os.path.join(offense_dir, "plays.csv")

        # defense_file= os.path.join(team_dir, "Defense", "plays.csv")

        # os.makedirs(defense_file)

        for _, play in df[df['posteam'] == team].iterrows():
            play = offense_play(play)
            offense_plays.append(play)
        
        offense_df = pd.DataFrame(offense_plays)
        offense_df.to_csv(offense_file, index=False)
        print(team, " offense pbp CSV saved")

        save_offense_plays(offense_dir)
        print(team, " run and pass pbp CSV saved")
        teams_complete += 1
        print(teams_complete, "/", total_teams, " offensive team plays saved.")


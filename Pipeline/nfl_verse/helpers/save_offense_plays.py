import os 
import pandas as pd 
from Pipeline.nfl_verse.helpers.check_play import check_play
# Saves team offensive run and pass plays to respective CSV files, given a team directory 
# Only saves plays that are ran in regular season (no two point conversions)

def save_offense_plays(directory):
    play_df = pd.read_csv(os.path.join(directory, "plays.csv"))

    rush_output_file = os.path.join(directory, 'Rushing', 'plays.csv')
    pass_output_file = os.path.join(directory, 'Passing', 'plays.csv')

    run_plays = []
    pass_plays = []

    for _, play in play_df.iterrows():
        curr_play = check_play(play)
        # Check if reg szn game and not a two point conv
        if curr_play is None or curr_play.empty:
            continue
        else:
            if curr_play['play_type'] == 'pass':
                pass_plays.append(play)
            elif curr_play['play_type'] == 'run' or curr_play['play_type'] == 'qb_kneel':
                run_plays.append(play)
    
    run_df = pd.DataFrame(run_plays)
    pass_df = pd.DataFrame(pass_plays)

    run_df.to_csv(rush_output_file, index=False)
    pass_df.to_csv(pass_output_file, index=False)
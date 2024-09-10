import pandas as pd 
import os, re 
from Pipeline.helpers.play_operations import fix_play_row

# Direct snaps in the original pbp CSV are not saved as run plays and do not track yards gained, this function corrects that error
def fix_direct_snap(pbp_dir):
    direct_snaps = []
   
    df = pd.read_csv(pbp_dir)

    for index, play in df.iterrows():
        if pd.isna(play['PlayType']) and not (
        play['Description'].startswith("TIMEOUT") or
        play['Description'] == 'TWO-MINUTE WARNING' or
        play['Description'].startswith('END')
        ):
            play_fixed = fix_play_row(play)
            direct_snaps.append(play_fixed)
            df.loc[index] = play_fixed

        
    fixed_pbp_df = pd.DataFrame(df)

    # Overwrite old pbp file
    fixed_pbp_df.to_csv(pbp_dir, index=False)

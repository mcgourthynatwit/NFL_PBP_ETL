import pandas as pd 

def check_play(play):
    if (
        play['season_type'] == 'REG' and # reg szn plays
        play['two_point_attempt'] == 0 # not a two point try
    ):
        return play 
    return None

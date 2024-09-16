from Pipeline.nfl_verse.helpers.check_play import check_play
# Takes in a play row and returns play if it is a valid run play

def get_rush_play_stats(play):
    rush_yards = 0
    touchdowns = 0
    fumbles = 0
    rush_play = check_play(play)
    
    if rush_play is None or rush_play.empty:
        return 0, 0, 0, 0
    if play['fumble_lost']:
        return 1, 0, 0, 1
    if play['fumble_forced'] == 1 or play['fumble_not_forced'] == 1:
        # plays where there is a fumble but not lost, if team recovers in endzone it is not technically a rushing td so need this check
        return 1, play['yards_gained'], 0, 0 
    return 1, play['yards_gained'], play['touchdown'], 0
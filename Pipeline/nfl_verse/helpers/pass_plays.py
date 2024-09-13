from Pipeline.nfl_verse.helpers.check_play import check_play

# Takes in a play, verifies valid play, returns the following
# Completion(1 or 0), passing yards(w/sack), passing yards(w/o sack), air yards, yards after catch, interception(1 or 0)

def get_pass_play_stats(play):
    pass_yards_sack = 0
    pass_yards = 0
    air_yards = 0
    yards_after_catch = 0
    interception = 0
    completion = 0

    pass_play = check_play(play)
    
    if pass_play is None or pass_play.empty:
        return 0, 0, 0, 0, 0, 0, 0
    if play['sack'] == 1 and play['penalty'] == 0 :    
        return play['yards_gained'], 0, 0, 0, 0, 0, 0
    if play['interception'] == 1:
        return 0, 0, 0, 0, 1, 0, 1
    return play['yards_gained'], play['yards_gained'], play['air_yards'], play['yards_after_catch'], 0, play['complete_pass'], 1    
     
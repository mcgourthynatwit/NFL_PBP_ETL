# Outputs an array of all 32 team names
def get_teams(df):
    teams = ['LA', 'GB', 'HOU', 'IND', 'WAS', 'NO', 'LV', 'NYG', 'PHI', 'DAL', 'NYJ', 'CHI', 'CLE', 'ARI', 'CIN', 'SF', 'TB', 'TEN', 'BUF', 'LAC', 'JAX', 'MIA', 'SEA', 'MIN', 'DEN', 'KC', 'DET', 'ATL', 'PIT', 'CAR', 'NE', 'BAL']

    return teams

# Helper function for duration to order plays from start to finish of each game
# Used by: sort_plays_to_file inside file_operations.py 
def calc_duration(play):
    # elapsed
    quarter_second = {
        1 : 0,
        2 : 900,
        3 : 1800,
        4 : 2700,
        5 : 3600, # OT
    }

    quarter_elapsed_seconds = 900 - ((play['Minute'] * 60) + play['Second'])
    
    elapsed_seconds = quarter_second.get(play['Quarter'], 0) + quarter_elapsed_seconds

    return elapsed_seconds

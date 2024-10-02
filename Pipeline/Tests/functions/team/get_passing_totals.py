import pandas as pd 

def get_pfr_passing_totals(pfr_df):
    team_offense = []

    for _, row in pfr_df.iterrows():
        team_passing = {
                "team": row['Tm'], 
                "attempts": row['Att'],
                "completions": row['Cmp'],
                "yards": row['Yds.1'],
                "td": row['TD'],
                "int": row['Int'],
                "first_down": row['1stD.1']
            }

        team_offense.append(team_passing)

    return team_offense

# Checks if a raw play is a 2-point & regular szn
def check_play(play):
    if (
        play['season_type'] == 'REG' and # reg szn plays
        play['two_point_attempt'] == 0 # not a two point try
        ):
        return True
    return False

# Gets the passing totals from the raw pdf sourced from nfl-verse
def get_raw_passing_totals(raw_df):
    team_passing_stats = []

    teams = raw_df['posteam'].unique()

    for team in teams:
        if pd.isna(team):
            continue 

        team_passing = {
            "team": team, 
            "attempts": 0,
            "completions": 0,
            "yards": 0,
            "td": 0,
            "int": 0,
            "first_down": 0
        }

        for _, play in raw_df[raw_df['posteam'] == team].iterrows():
            # is a regular szn non 2-pt pass play
            if check_play(play) and play['play_type'] == 'pass' or play['play_type'] == 'qb_spike':
                team_passing['attempts'] += play['pass_attempt']
                team_passing['int'] += play['interception']
                team_passing['completions'] += play['complete_pass']
                team_passing['first_down'] += play['first_down_pass']

                if pd.isna(play['passing_yards']):
                    passing_yards = 0
                else:
                    passing_yards = play['passing_yards']

                team_passing['yards'] += passing_yards

                # Not counting fumble or pick sixes for other team
                if not(play['interception'] or play['fumble']):
                    team_passing['td'] += play['touchdown']

            # Subtract one, if the play is a sack then the qb did not throw the ball
            if play['sack'] == 1:
                team_passing['attempts'] -= 1
                team_passing['yards'] += play['yards_gained']
                
        team_passing_stats.append(team_passing)
    return team_passing_stats

def get_passing_totals(pfr_df, raw_df):
    raw_passing_stats = get_raw_passing_totals(raw_df)
    pfr_passing_stats = get_pfr_passing_totals(pfr_df)
    return raw_passing_stats, pfr_passing_stats

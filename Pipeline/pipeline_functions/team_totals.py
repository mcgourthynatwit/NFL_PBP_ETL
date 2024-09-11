import pandas as pd 
import os, re
from Pipeline.helpers.utils_operations import calc_duration

def extract_spot(play_description):
    # Regex to capture the team acronym and the spot
    match = re.search(r'ENFORCED AT (\w+ \d+)', play_description)
    if match:
        # Extract the spot part
        spot = match.group(1).split()
        return spot
    else:
        return 0

def rush_ended_at(play):
    match = re.search(r'FOR (-?\d+) YARDS', play['Description'])
    print(match.group(1))
    if match:
        spot = match.group(1)
       
        return int(spot)
        
# Rushing yards can have holding calls enforced past the LOS and that difference counts for a rush & yards
def rush_enforced_at_fix(play):
    spot = extract_spot(play['Description'])

    team_yard_line = spot[0]
    yard_line = spot[1]

    # CHANGE THIS TO NORMAL YARD LINE AND CALCUALTE YARD_LINE
    # THIS WILL PROVIDE INCORRECT RESULTS FOR PLAYS THAT CROSS MIDFIELD PERHAPS
    if play['OffenseTeam'] == team_yard_line:
        print(int(yard_line) - int(play['YardLineFixed']), 'here')
        return int(yard_line) - int(play['YardLineFixed'])

    return int(play['YardLineFixed'] - int(yard_line))

def kneel_yards(play):
    match = re.search(r'FOR (-?\d+) YARDS', play['Description'])

    if match:
        return int(match.group(1))
    else:
        return 0

def aborted_snap(play):
    match = re.search(r'HANDOFF', play['Description'])
    if match:
        pattern = r"TO\s([A-Z]{2,3})\s(\d+)\sFOR"

        # Find all matches in the text
        matches = re.findall(pattern, play['Description'])
        
        if matches:
            # print(play['Description'], play['YardLineFixed'])
            team_code, yard_marker = matches[-1]
            gained = abs(int(yard_marker) - int(play['YardLineFixed']))
            return gained
        else:
            print("No match found.")
            return play['Yards']

def check_pass(pass_stats, play):
    if play['IsNoPlay'] == 0 and play['IsInterception'] == 0 and play['IsSack'] == 0 and play['IsTwoPointConversion'] == 0:
        pass_stats['plays'] += 1
        pass_stats['attempts'] += 1
        if play['IsIncomplete'] == 0:
            pass_stats['completions'] += 1
            pass_stats['yards'] += play['Yards']
        
        if play['IsTouchdown'] == 1:
            pass_stats['td'] += 1
        
    if play['IsSack'] == 1:
        pass_stats['yards'] += play['Yards']

    if play['IsNoPlay'] == 0 and play['IsInterception'] == 1:
        pass_stats['attempts'] += 1
        pass_stats['int'] += 1
    
    return pass_stats

def check_rush(plays, rush_stats, play):
    if play['PlayType'] == 'QB KNEEL':
        rush_stats['plays'] += 1
        rush_stats['attempts'] += 1

        yards = kneel_yards(play)
        rush_stats['yards'] += yards
        play['Yards'] = yards
        #plays.append(play)
        return rush_stats

    if play['IsNoPlay'] == 0 and (play['PenaltyTeam'] != play['OffenseTeam'] or play['IsPenaltyAccepted'] == 0) :
        rush_stats['plays'] += 1
        rush_stats['attempts'] += 1

        if play['IsFumble'] == 1:
            rush_stats['fumbles'] += 1
            # Aborted snap
            if play['PlayType'] == 'FUMBLES':
                yards = aborted_snap(play)
                rush_stats['yards'] += yards
                plays.append(play)
                return rush_stats

            rush_yards = rush_ended_at(play)
            rush_stats['yards'] += rush_yards
            print(play['Description'])
            plays.append(play)
            return rush_stats

        rush_stats['yards'] += play['Yards']
        
        if play['IsTouchdown'] == 1:
            rush_stats['td'] += 1
        if play['IsFumble'] == 1:
            rush_stats['fumbles'] += 1


    elif (play['PenaltyTeam'] == play['OffenseTeam'] and play['IsPenaltyAccepted'] == 1 and play['IsNoPlay'] == 0):
        try:
            gain = rush_enforced_at_fix(play)
            print('The gain is ', play['Yards'], gain)
            rush_stats['plays'] += 1
            rush_stats['attempts'] += 1
            rush_stats['yards'] += gain
            play['Yards'] = gain
        

        except Exception as e:  
            print(play['Description'])
            print(e)

    plays.append(play)
    return rush_stats

def get_team_totals(team_directory, team):     
    pass_stats = {
        "plays" : 0,
        "attempts" : 0, 
        "completions" : 0,
        "yards" : 0,
        "td" : 0,
        "int" : 0,
    }

    rush_stats = {
        "plays" : 0,
        "attempts" : 0,
        "yards" : 0,
        "td" : 0,
        "fumbles" : 0 
    }

    offense_directory = os.path.join(team_directory, team, "Offense", "plays.csv")

    df = pd.read_csv(offense_directory)

    offense_directory = os.path.join(team_directory, team, "Offense", "plays.csv")

    df = pd.read_csv(offense_directory)

    weeks = df['Week'].unique()
    weeks = sorted(map(int, weeks))
    #for i in range(18) :
    week_num = 9
    week_data = df[df['Week'] == week_num]
    
    # Initialize weekly stats
    weekly_pass_stats = {
        "plays" : 0,
        "attempts" : 0,
        "completions" : 0,
        "yards" : 0,
        "td" : 0,
        "int" : 0,
    }

    weekly_rush_stats = {
        "plays" : 0,
        "attempts" : 0,
        "yards" : 0,
        "td" : 0,
        "fumbles" : 0 
    }
    run_plays = []    
    count = 0
    for _, play in week_data.iterrows():
        if play['IsPass'] == 1 or play['PlayType'] == 'SACK':
            weekly_pass_stats = check_pass(weekly_pass_stats, play)

        elif play['IsRush'] == 1 or play['PlayType'] == 'QB KNEEL' or play['PlayType'] == 'FUMBLES':
            weekly_rush_stats = check_rush(run_plays, weekly_rush_stats, play)

    run_df = pd.DataFrame(run_plays)
    run_df['Duration'] = run_df.apply(calc_duration, axis=1)
    run_df.sort_values(by="Duration", inplace=True)
    run_df.to_csv("rushes.csv", index=False)

    print('Weekly rush stats:')
    
    print(f"Week {week_num}: {weekly_rush_stats['attempts']} : {weekly_rush_stats['yards']}")
    
    print('Weekly pass stats:')
    
    print(f"Week {week_num}: {weekly_pass_stats['attempts']} : {weekly_pass_stats['completions']} : {weekly_pass_stats['yards']}")

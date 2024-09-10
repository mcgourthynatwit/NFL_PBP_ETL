import pandas as pd 
import re
# DIRECT_SNAP Helpers 

# used by fix_play_row 
def extract_yardage(play_description):
    match = re.search(r'FOR (-?\d+) YARDS?', play_description)
    if match:
        return int(match.group(1))
    else:
        return 0
     
# Sets play_type & IsRush accordingly, using yards function to extract and set yards gained
# used by: fix_direct_snap.py
def fix_play_row(play):
    play['PlayType'] = 'RUSH'
    play['IsRush'] = 1
    yards = extract_yardage(play['Description'])
    play['Yards'] = yards
    
    return play


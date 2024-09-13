# python3 -m Pipeline.organize_pbp

import os 
import nfl_data_py as nfl
import pandas as pd
from Pipeline.nfl_verse.pipeline.create_folders import create_folders
from Pipeline.nfl_verse.pipeline.create_folders import get_max_week
from Pipeline.nfl_verse.pipeline.organize_plays import organize_plays
from Pipeline.nfl_verse.pipeline.get_team_totals import get_team_totals

year = 2023
teams_dir = f"Clean_Data/{year}/Teams"

#print("Importing pbp data...")
#df = nfl.import_pbp_data(years=[year], downcast=False, columns=list(cols))
#df = pd.read_csv(f'Raw_Data/play_by_play_{year}.csv', low_memory=False)
#df.to_csv("pbp.csv", index=False)

#print("Calling create_folders")
#create_folders(year, df)

#print("Sorting plays")
#organize_plays(teams_dir, df)

get_team_totals(teams_dir)


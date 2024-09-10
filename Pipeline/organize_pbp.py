# python3 -m Pipeline.organize_pbp

import os 
YEAR = 2023
SRC_DIRECTORY = "Data/pbp-2023.csv"
END_DIRECTORY = "Clean_Data/Weeks"

from Pipeline.pipeline_functions.split_games import split_games
from Pipeline.pipeline_functions.fix_direct_snap import fix_direct_snap

fix_direct_snap(SRC_DIRECTORY)
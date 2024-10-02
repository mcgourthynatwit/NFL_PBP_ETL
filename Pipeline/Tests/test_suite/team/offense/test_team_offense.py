from Pipeline.Tests.pfr_scrapers.get_team_offense import get_offense_csv
from Pipeline.Tests.test_suite.team.offense.test_team_passing import test_team_passing

import pandas as pd 
import os 

# Map PFR team name to team abbriviation used in the raw CSV
team_mapping = {
    'Arizona Cardinals': 'ARI',
    'Buffalo Bills': 'BUF',
    'Baltimore Ravens': 'BAL',
    'Kansas City Chiefs': 'KC',
    'New Orleans Saints': 'NO',
    'Carolina Panthers': 'CAR',
    'Dallas Cowboys': 'DAL',
    'Cleveland Browns': 'CLE',
    'Seattle Seahawks': 'SEA',
    'Denver Broncos': 'DEN',
    'Green Bay Packers': 'GB',
    'Philadelphia Eagles': 'PHI',
    'Indianapolis Colts': 'IND',
    'Houston Texans': 'HOU',
    'Miami Dolphins': 'MIA',
    'Jacksonville Jaguars': 'JAX',
    'Los Angeles Rams': 'LA',
    'Detroit Lions': 'DET',
    'Los Angeles Chargers': 'LAC',
    'Las Vegas Raiders': 'LV',
    'New York Giants': 'NYG',
    'Minnesota Vikings': 'MIN',
    'Cincinnati Bengals': 'CIN',
    'New England Patriots': 'NE',
    'New York Jets': 'NYJ',
    'San Francisco 49ers': 'SF',
    'Atlanta Falcons': 'ATL',
    'Pittsburgh Steelers': 'PIT',
    'Tennessee Titans': 'TEN',
    'Chicago Bears': 'CHI',
    'Tampa Bay Buccaneers': 'TB',
    'Washington Commanders': 'WAS'
}

def test_team_offense():
    # Get CSVs
    # get_offense_csv()

    pfr_offense_csv_path = "Pipeline/Tests/test_data/offense_team_stats.csv"
    raw_offense_csv_path = "Raw_Data/play_by_play_2024.csv"

    if not os.path.exists(pfr_offense_csv_path):
        raise FileNotFoundError("PFR CSV was not created")

    pfr_df = pd.read_csv(pfr_offense_csv_path)
    raw_df = pd.read_csv(raw_offense_csv_path, low_memory=False)

    test_team_passing(pfr_df, raw_df, team_mapping)

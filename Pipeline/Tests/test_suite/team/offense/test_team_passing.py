from Pipeline.Tests.functions.team.get_passing_totals import get_passing_totals

import pandas as pd 

def test_passing_attempts(raw_row, pfr_row):
    assert int(raw_row['attempts']) == pfr_row['attempts'], f"Mismatch in passing attempts for {pfr_row['team']}, expected {pfr_row['attempts']}, got {int(raw_row['attempts'])}"

def test_passing_completions(raw_row, pfr_row):
    assert int(raw_row['completions']) == pfr_row['completions'], f"Mismatch in completions for {pfr_row['team']}, expected {pfr_row['completions']}, got {int(raw_row['completions'])}"

def test_passing_yards(raw_row, pfr_row):
    assert int(raw_row['yards']) == pfr_row['yards'], f"Mismatch in passing yards for {pfr_row['team']}, expected {pfr_row['yards']}, got {int(raw_row['yards'])}"

def test_passing_touchdowns(raw_row, pfr_row):
    assert int(raw_row['td']) == pfr_row['td'], f"Mismatch in passing touchdowns for {pfr_row['team']}, expected {pfr_row['td']}, got {int(raw_row['td'])}"

def test_passing_interceptions(raw_row, pfr_row):
    assert int(raw_row['int']) == pfr_row['int'], f"Mismatch in interceptions for {pfr_row['team']}, expected {pfr_row['int']}, got {int(raw_row['int'])}"

def test_passing_first_downs(raw_row, pfr_row):
    assert int(raw_row['first_down']) == pfr_row['first_down'], f"Mismatch in first downs for {pfr_row['team']}, expected {pfr_row['first_down']}, got {int(raw_row['first_down'])}"

def test_team_passing(pfr_df, raw_df, team_mapping):
    raw_passing_stats, pfr_passing_stats = get_passing_totals(pfr_df, raw_df)
    for pfr_row in pfr_passing_stats:
        mapped_team = team_mapping[pfr_row['team']]
        matching_raw_rows = [r for r in raw_passing_stats if r['team'] == mapped_team]
        if matching_raw_rows:
            raw_row = matching_raw_rows[0]
            try:
                test_passing_attempts(raw_row, pfr_row)
                test_passing_completions(raw_row, pfr_row)
                test_passing_yards(raw_row, pfr_row)
                test_passing_touchdowns(raw_row, pfr_row)
                test_passing_interceptions(raw_row, pfr_row)
                test_passing_first_downs(raw_row, pfr_row)
            except AssertionError as e:
                print(f"Error: {str(e)}")
        else:
            print(f"No matching raw data found for {pfr_row['team']}")

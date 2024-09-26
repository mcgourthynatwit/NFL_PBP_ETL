# python3 -m Pipeline.nfl_verse.github.pull_latest
from dotenv import load_dotenv
import pandas as pd
import os 
import requests
import json

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def get_latest_release(owner, repo, file_name):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers)
    
    releases = response.json()
    for release in releases:
        for asset in release['assets']:
            if asset['name'] == file_name:
                return asset['updated_at'], asset['browser_download_url']
                
def update_txt(update_date):
    file = "Pipeline/nfl_verse/github/last_pull.txt"
    current_date = ""
    if os.path.exists(file):
        with open(file, 'r') as f:
            current_date = f.readline().strip()
    # Check if last update is a different timestamp then current pulled timestamp
    if current_date != update_date:
        print(f'Updating time from "{current_date}" to "{update_date}"')
        # Update file to new date
        with open(file, 'w') as f:
            f.write(update_date)
            print('Update needed...')
        return True
    print('No recent update.')
    return False

def download_release(download_url, file_name):
    print('Downloading new release')
    response = requests.get(download_url)

    with open(file_name, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {file_name} successfully.")

def add_id(df):
    print('adding ids')

    df['play_id_fixed'] = df['old_game_id'].astype(str) + df['play_id'].astype(str)
    
    return df

'''
This will likely be a running and constantly updated function as I find errors
'''
def fix_stats(df):
    print('fixing stats for laterals')
    for idx, play in df.iterrows():
        correct_yardage = play['rushing_yards'] + play['lateral_rushing_yards']

        if play['lateral_rush'] == 1 and correct_yardage != play['yards_gained']:
            print(f'{play['desc']} had incorrect yardages')
            print(f'Play yardage was {play['yards_gained']}, changed to {correct_yardage}')
            df.at[idx, 'yards_gained'] = correct_yardage
    return df

def pull_latest_csv():
    owner = "nflverse"
    repo = "nflverse-data"
    file_name = "play_by_play_2024.csv"
    output_file_name = f"Raw_Data/{file_name}"
    update_date, download_url = get_latest_release(owner, repo, file_name)

    print(update_date)
    update_needed = update_txt(update_date)

    if update_needed:
        download_release(download_url, output_file_name)
        
        df = pd.read_csv(output_file_name, low_memory=False)

        df = add_id(df)
        df = fix_stats(df)

        df.to_csv(output_file_name)
        
        return output_file_name
    return False
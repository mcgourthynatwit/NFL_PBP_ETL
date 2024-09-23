# python3 -m Pipeline.nfl_verse.github.pull_latest
from dotenv import load_dotenv
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
        print('Update complete')
        return True
    print('No recent update.')
    return False

def download_release(download_url, file_name):
    response = requests.get(download_url)

    with open(file_name, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {file_name} successfully.")

owner = "nflverse"
repo = "nflverse-data"
file_name = "play_by_play_2024.csv"
output_file_name = f"Raw_Data/{file_name}"
update_date, download_url = get_latest_release(owner, repo, file_name)

print(update_date)
update_needed = update_txt(update_date)

if update_needed:
    download_release(download_url, output_file_name)
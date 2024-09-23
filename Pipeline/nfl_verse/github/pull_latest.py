# python3 -m Pipeline.nfl_verse.github.pull_latest
from dotenv import load_dotenv
import os 
import requests

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

def get_latest_release(owner, repo, file_name):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    releases = response.json()
    for release in releases:
        for asset in release['assets']:
            if asset['name'] == file_name:
                return {
                    asset['name'],
                    asset['updated_at'],
                    asset['browser_download_url']
                }
    
    

owner = "nflverse"
repo = "nflverse-data"
file_name = "play_by_play_2024.csv"
asset = get_latest_release(owner, repo, file_name)
print(asset)
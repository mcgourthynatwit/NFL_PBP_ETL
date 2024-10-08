import pandas as pd 
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_API_KEY = os.getenv('SUPABASE_KEY')

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

csv_path = "Raw_Data/play_by_play_2024.csv"
df = pd.read_csv(csv_path, low_memory=False)


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

# Function to map pandas dtypes to PostgreSQL types
def get_pg_type(dtype):
    if 'int' in str(dtype):
        return 'integer'
    elif 'float' in str(dtype):
        return 'float'
    elif 'datetime' in str(dtype):
        return 'timestamp'
    else:
        return 'text'

table_name = 'pbp_2024'

columns = ',\n    '.join([f"\"{col}\" {get_pg_type(df[col].dtype)}" for col in df.columns])
create_table_query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
    id SERIAL PRIMARY KEY,
    {columns}
);
"""

# Print the SQL statement
print(create_table_query)
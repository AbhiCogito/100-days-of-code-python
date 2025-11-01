import os, json, gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
load_dotenv()
os.system("clear")

base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, os.pardir, os.pardir))
source_file = os.path.abspath(os.path.join(project_root, "data", "hevy_data_clean.json"))
cred_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
GOOGLE_CREDENTIALS_PATH = os.path.join(project_root, cred_path)

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_PATH, scopes=scopes)
client = gspread.authorize(creds)
sheet_id = "1tG_iFU4gSw2ajdjIMeubWnt-wMIiNvkavABO_wLvN_U"
sh = client.open_by_key(sheet_id)

with open(source_file, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df = df.fillna("") #Fix NaN values as gspread doesn't accept NaN
headers = df.columns.tolist()
data_rows = df.values.tolist()
data_dump = [headers] + data_rows

worksheet = sh.worksheet('2025')
worksheet.update('A1', data_dump)






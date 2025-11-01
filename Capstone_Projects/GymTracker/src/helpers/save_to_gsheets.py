import os
import gspread 
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
load_dotenv()
os.system("clear")

base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, os.pardir, os.pardir))
cred_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
GOOGLE_CREDENTIALS_PATH = os.path.join(project_root, cred_path)

print(GOOGLE_CREDENTIALS_PATH)

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_PATH, scopes=scopes)
client = gspread.authorize(creds)
sheet_id = "1tG_iFU4gSw2ajdjIMeubWnt-wMIiNvkavABO_wLvN_U"
sheet = client.open_by_key(sheet_id)

values_list = sheet.sheet1.row_values(1)
worksheet = sheet.worksheet('2025')

# Example data
data = [
    ["Date", "Workout", "Duration", "Effort"],
    ["2025-10-30", "Chest + Shoulders", "75 mins", "All Out"]
]

# worksheet.update('A1', data)
print("✅ Data written successfully!")


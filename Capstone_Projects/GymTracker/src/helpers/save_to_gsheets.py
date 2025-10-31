import os
import gspread 
from dotenv import load_dotenv
load_dotenv()

GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
print(GOOGLE_CREDENTIALS_PATH)
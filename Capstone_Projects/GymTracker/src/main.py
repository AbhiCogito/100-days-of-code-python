import requests as rq
from datetime import datetime, timedelta
import os, json, smtplib
from dotenv import load_dotenv
os.system("clear")
load_dotenv()

HEVY_API = os.getenv("HEVY_API")
print(HEVY_API)


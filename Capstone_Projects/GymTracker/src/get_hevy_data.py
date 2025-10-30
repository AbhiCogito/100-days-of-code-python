import requests as rq
from datetime import datetime, timedelta
import os, json
from dotenv import load_dotenv
os.system("clear")
load_dotenv()

# 1. Get the path to the current script's directory (capstone/src)
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go up one level (to capstone/) and then down into 'data'
filepath = os.path.join(script_dir, os.pardir, 'data', 'hevy_data.json')
# Note: os.pardir is a platform-independent way to say 'cd ..' (parent directory)

filepath = os.path.abspath(filepath)

HEVY_API = os.getenv("HEVY_API")
HEVY_ENDPOINT = "https://api.hevyapp.com/v1/workouts"

HEADERS = {
    "api-key": HEVY_API
}

PAGE = 1
PAGE_SIZE = 10
all_workouts = []

while True:

    PARAMETERS = {
        "page": PAGE,
        "pageSize": PAGE_SIZE
    }

    response = rq.get(url=HEVY_ENDPOINT, headers=HEADERS, params=PARAMETERS)
    data = response.json()

    more_data = data.get("workouts", [])

    if not more_data:
        print(f"Total {len(all_workouts)} workouts fetched. No more data.")
        break

    print(f"Data fetched from page {PAGE}")
    all_workouts.extend(more_data)
    PAGE+=1

try:
    with open(filepath, 'w') as json_file:
        json.dump(all_workouts, json_file, indent=2)
    print(f"Data successfully saved to {filepath}")
except IOError:
    print("Could not save data due to IO error!")

print(all_workouts)

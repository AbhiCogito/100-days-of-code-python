import json, os, requests
import pandas as pd
from dotenv import load_dotenv

os.system("clear")

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
env_path = os.path.join(project_root, '.env')

# Load .env from Capstone_Projects
load_dotenv(dotenv_path=env_path)

print("POST_SHEETY =", os.getenv("POST_SHEETY"))

GET_SHEETY = os.getenv("GET_SHEETY")
POST_SHEETY = os.getenv("POST_SHEETY")

script_dir = os.path.dirname(os.path.abspath(__file__))
hevy_data = os.path.join(script_dir, os.pardir, os.pardir, 'data', 'hevy_data.json')
hevy_file = os.path.abspath(hevy_data)

hevy_clean_data = os.path.join(script_dir, os.pardir, os.pardir,'data', 'hevy_data_clean.json')
clean_file = os.path.abspath(hevy_clean_data)

# Always use JSON to read nested data as using Pandas will often result in a DataFrame where 
# the exercises column contains an entire Python list of dictionaries (the nested exercise data).
with open(hevy_file, 'r') as file:
    all_workouts = json.load(file)

df = pd.json_normalize(
    data=all_workouts,
    record_path=['exercises', 'sets'],
    meta=['id', 'title', 'start_time', 'end_time', ['exercises', 'title']],
    errors='ignore'
)

#------Convert string to datetime format---------------#
df['start_time'] = pd.to_datetime(df['start_time'])
df['end_time'] = pd.to_datetime(df['end_time'])

df['Date'] = df['start_time'].dt.strftime('%d-%b-%Y') 
df['Duration'] = ((df['end_time'] - df['start_time']).dt.total_seconds() / 60).round().astype(int)

df = df.rename(columns={
    'exercises.start_time' : 'Date',
    'exercises.title': 'Exercise',
    'title': 'Title',
    'weight_kg': 'Weights (kg)',
    'reps': 'Reps',
    'distance_meters': 'Distance (meters)'
    })

#----------Rearrange df columns--------------------#
df = df[['Date','Title','Exercise', 'Duration', 'Weights (kg)','Reps','Distance (meters)','id']]

df.to_json(clean_file, orient='records', indent=2)










def refresh_sheet(df):
    # Step 1: Delete existing rows
    response = requests.get(GET_SHEETY)
    if response.status_code != 200:
        print("❌ Failed to fetch existing rows:", response.text)
        return

    rows = response.json().get("sheet1", [])
    for row in rows:
        row_id = row.get("id")
        if row_id:
            delete_url = f"{GET_SHEETY}/{row_id}"
            delete_response = requests.delete(delete_url)
            if delete_response.status_code == 200:
                print(f"🗑 Deleted row ID {row_id}")
            else:
                print(f"❌ Failed to delete row ID {row_id}: {delete_response.text}")

    # Step 2: Post new rows
    for _, row in df.iterrows():
        payload = {
            "2025": {
                "Date": row["Date"],
                "title": row["title"],
                "Exercise": row["Exercise"],
                "weight_kg": row["weight_kg"],
                "reps": row["reps"],
                "distance_meters": row["distance_meters"],
                "id": row["id"]
            }
        }

        post_response = requests.post(POST_SHEETY, json=payload)
        if post_response.status_code in [200, 201]:
            print(f"✅ Posted: {row['Exercise']} on {row['Date']}")
        else:
            print(f"❌ Failed to post: {post_response.text}")

# refresh_sheet(df)
# print("GET_SHEETY =", GET_SHEETY)

import json, os
import pandas as pd
os.system("clear")

script_dir = os.path.dirname(os.path.abspath(__file__))
hevy_data = os.path.join(script_dir, os.pardir, os.pardir, 'data', 'hevy_data.json')
hevy_file = os.path.abspath(hevy_data)

hevy_clean_data = os.path.join(script_dir, os.pardir, os.pardir,'data', 'hevy_data_clean.json')
clean_file = os.path.abspath(hevy_clean_data)

# Using JSON to read nested data as using Pandas will often result in a DataFrame where 
# the exercises column contains an entire Python list of dictionaries (the nested exercise data).
with open(hevy_file, 'r') as file:
    all_workouts = json.load(file)

df = pd.json_normalize(
    data=all_workouts,
    record_path=['exercises', 'sets'],
    meta=['id', 'title', 'start_time', ['exercises', 'title']],
    errors='ignore'
)

#------Convert string to datetime format---------------#
df['start_time'] = pd.to_datetime(df['start_time'])
df['Date'] = df['start_time'].dt.strftime('%d-%b-%Y') 

df = df.rename(columns={'exercises.start_time' : 'Date'})
df = df.rename(columns={'exercises.title': 'Exercise'})
#----------Rearrange df columns--------------------#
df = df[['Date','title','Exercise','weight_kg','reps','distance_meters','id']]

df.to_json(clean_file, orient='records', indent=2)


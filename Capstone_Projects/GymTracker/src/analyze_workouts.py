import os, json
import pandas as pd

os.system("clear")

base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, os.pardir))
source_file = os.path.abspath(os.path.join(project_root, "data", "hevy_data_clean.json"))

with open(source_file, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

print(df.head())
import os
import pandas as pd 

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Squirrels.csv")
os.system("clear")

data = pd.read_csv(file_path)
# print(data["condition"])
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])    

# monday = data[data["day"] == "Monday"]
# mon = monday.temp[1]
print(data.iloc[1]["Primary Fur Color"])

print(data["Primary Fur Color"].values)
print(data["Primary Fur Color"].value_counts(dropna = False))

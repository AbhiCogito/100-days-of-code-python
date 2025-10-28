import requests as rq
import os
from dotenv import load_dotenv

load_dotenv()
openweather_api = os.getenv("OPEN_WEATHER_API")
print(f"Loaded key: {openweather_api}")
os.system("clear")

parameters = {
    "lat": 28.5355,
    "lon": 77.3910,
    "appid": openweather_api,
    "units": "metric",
    "cnt": 3
}

response = rq.get(url="https://api.openweathermap.org/data/2.5/forecast" ,params=parameters)
response.raise_for_status()
data = response.json()

# weather = []
# for i in range(3):
#     weather.append(data["list"][i]["weather"][0]["main"])

weather = [data["list"][i]["weather"][0]["id"] for i in range(3)]
print(weather)
for w in weather:
    if w < 700:
        print("Umbrella")



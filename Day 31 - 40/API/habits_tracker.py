from datetime import datetime as dt
import requests as rq

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "sophiesingh"
TOKEN = "vb3irhugi3erb3984hfwkrf)"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "s25"

today_date = dt.today().strftime("%Y%m%d")
print(today_date)

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

NEW_GRAPH = {
    "id": "s25",
    "name": "Reading a Book",
    "unit": "Pages",
    "type": "int",
    "color": "sora"
}

UPDATE_GRAPH = {
    "date": today_date,
    "quantity": "18"
}

# response = rq.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}", headers=HEADERS, json=UPDATE_GRAPH)
# print(response.text)
print(f"{GRAPH_ENDPOINT}/{GRAPH_ID}")


import requests as rq
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
os.system("clear")

load_dotenv()
today = datetime.today()
from_date = (today - timedelta(10)).strftime('%Y-%m-%d')
to_date = today.strftime('%Y-%m-%d')


STOCK = ['AAPL', 'MSFT', 'NVDA', 'TSLA', 'AMZN']
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = os.getenv("ALPHAVANTAGE_API")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = os.getenv("NEWS_API")

def get_stock_news(stock):
    NEWS_PARAMS = {
        "apiKey": NEWS_API,
        "q": stock,
        "from": from_date,
        "to": to_date,
        "sortBy": "popularity",
        "pageSize": 3
    }
    
    response = rq.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    response.raise_for_status()
    data = response.json()
    print(data)

def get_stock_prices(stock):
    STOCK_PARAMS = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": STOCK_API
    }



    response = rq.get(url=STOCK_ENDPOINT ,params=STOCK_PARAMS)
    response.raise_for_status()
    data = response.json()
    print(data)
    time_series = data.get("Time Series (Daily)", {})  # safe way
    dates = sorted(time_series.keys(), reverse=True)

    latest, prev = dates[0], dates[1]
    latest_close = float(time_series[latest]["4. close"])
    prev_close = float(time_series[prev]["4. close"])
    change = ((latest_close - prev_close) / prev_close) * 100

    print(f"{stock} - {change}%")
    get_stock_news(stock)

# for s in STOCK:
    # get_stock_prices(s)
    # get_stock_news(s)

get_stock_news("TSLA")

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
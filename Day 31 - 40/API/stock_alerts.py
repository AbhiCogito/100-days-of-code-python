import requests as rq
from datetime import datetime, timedelta
import os, json, smtplib
from dotenv import load_dotenv
os.system("clear")
load_dotenv()

#-----Getting from and to dates to fetch stock prices-------#
today = datetime.today()
from_date = (today - timedelta(10)).strftime('%Y-%m-%d')
to_date = today.strftime('%Y-%m-%d')


STOCK = ['AAPL', 'MSFT', 'NVDA', 'TSLA', 'AMZN']
COMPANY_NAME = "Tesla Inc"
DIGEST = ""
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = os.getenv("ALPHAVANTAGE_API")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = os.getenv("NEWS_API")

def send_email():
    my_email = os.getenv("EMAIL_USER", "")
    my_password = os.getenv("EMAIL_PASS", "")

    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="gk4ias@gmail.com", 
                        msg=f"Subject: Stock price movement \n\n{DIGEST}".encode('utf-8'))
    connection.close()

def get_stock_news(stock):

    NEWS_PARAMS = {
        "apiKey": NEWS_API,
        "q": stock,
        "from": from_date,
        "to": to_date,
        "sortBy": "relevance",
        "pageSize": 3
    }
    
    response = rq.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    response.raise_for_status()
    data = response.json()

    #--------------Get only the first 3 articles(source+title)------------#
    news = ""
    for article in data.get("articles", [])[:3]:
        source = article.get("source", {}).get("name", "Unknown Source") 
        title = article.get("title", "No Title") 
        news += f"{source} - {title} \n"
    print(json.dumps(data, indent=4))

    return news

def get_stock_prices(stock):
    global DIGEST

    STOCK_PARAMS = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": STOCK_API
    }

    response = rq.get(url=STOCK_ENDPOINT ,params=STOCK_PARAMS)
    response.raise_for_status()
    data = response.json()

    #-------Get data from the last trading day---------#
    time_series = data.get("Time Series (Daily)", {})  
    dates = sorted(time_series.keys(), reverse=True)
    latest, prev = dates[0], dates[1]
    latest_close = float(time_series[latest]["4. close"])
    prev_close = float(time_series[prev]["4. close"])
    change = ((latest_close - prev_close) / prev_close) * 100

    if change:
        print(f"{stock} - {change:+.2f}%")
        news = get_stock_news(stock)
        DIGEST += f"{stock} ({change:+.2f}% change)\n{news}\n{'-'*180}\n"

for s in STOCK:
    get_stock_prices(s)

#------Send email only when there is some content---------#
if DIGEST.strip():
    send_email()
    print("Email sent.")
else:
    print("No significant stock movement found.")

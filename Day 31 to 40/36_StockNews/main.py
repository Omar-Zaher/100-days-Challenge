# ========================================================= Stock News ===================================================

# ------ Imports ---------
import requests as rq
import os
from twilio.rest import Client

# ----- Const and Variables --------
STOCK = "TSLA" # Write any stock you want 
COMPANY_NAME = "Tesla Inc" 

# Make sure you export these to the environment
STOCK_API = os.environ["STOCK_API"]
NEWS_API = os.environ["NEWS_API"]
twilio_sid = os.environ["twilio_sid"]
twilio_token = os.environ["twilio_token"]
twilio_phone = os.environ["twilio_phone"]
my_phone = os.environ["my_phone"]


# ------ Parameters --------
Stocks_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API,
    
}

News_params ={
    "apiKey": NEWS_API,
    "q": COMPANY_NAME,
    "pageSize": 3
}


# -------- Getting info of the stock --------------
stock = rq.get("https://www.alphavantage.co/query", params= Stocks_params)
stock.raise_for_status()
data = stock.json()["Time Series (Daily)"]
data_lis = [value for key,value in data.items()]
yesterday = float(data_lis[0]["4. close"])
day_before_yesterday = float(data_lis[1]["4. close"])

# ------- Sending message if difference is larger than 5% -------------------
difference = yesterday - day_before_yesterday
percentage = difference * 100 / yesterday
if percentage >= 5:
    news = rq.get("https://newsapi.org/v2/everything", params= News_params)
    news.raise_for_status()
    news_data = news.json()["articles"]

    # ------- Styling the message -----------
    message = ""
    for i in news_data:
        message =  f"{message}\nTitle: {i['title']}\n{i['description']}\nURL: {i['url']}\n"

    account_sid = twilio_sid
    auth_token = twilio_token
    client = Client(account_sid, auth_token)

    # Sending it using twilio 
    sms = client.messages.create(
        body=message,
        from_= twilio_phone,
        to=my_phone,
    )

# ========================================================================================================



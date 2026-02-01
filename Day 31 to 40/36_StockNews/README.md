# 📈 Stock News Alert (SMS Notification)

A Python automation script that monitors daily stock price changes and sends SMS news alerts when a significant movement occurs.

If a stock price changes by 5% or more, the program fetches the latest related news and sends it directly to your phone using Twilio SMS.

# 🚀 Features

Tracks any stock symbol

Calculates daily price percentage change

Detects major price movement (≥ 5%)

Fetches top related news articles

Sends formatted SMS alerts

Uses environment variables for security

# 🧠 How It Works

Retrieves daily stock data from Alpha Vantage

Compares yesterday’s closing price with the day before

Calculates percentage change

If change ≥ 5%:

Fetches top 3 related news articles

Formats the message

Sends SMS using Twilio

# 🧰 Technologies Used

Python

Alpha Vantage API (stock data)

NewsAPI (news articles)

Twilio API (SMS messaging)

Environment variables

# 📦 Requirements
Python version

Python 3.9+

Install dependencies
```bash
pip install requests twilio
```
# 🔑 API Setup (IMPORTANT)

This project requires three external services.

1️⃣ Alpha Vantage (Stock API)

Create a free account at Alpha Vantage

Generate an API key

2️⃣ NewsAPI

Create an account at NewsAPI

Get your API key

3️⃣ Twilio (SMS)

Create a Twilio account

Get:

Account SID

Auth Token

Twilio phone number

Verify your personal phone number

# 🌱 Environment Variables Setup
Windows (PowerShell)
```bash
$env:STOCK_API="your_alpha_vantage_api_key"
$env:NEWS_API="your_newsapi_key"
$env:twilio_sid="your_twilio_sid"
$env:twilio_token="your_twilio_auth_token"
$env:twilio_phone="+1234567890"
$env:my_phone="+9627XXXXXXXX"
```

⚠️ Phone numbers must include the country code.

These variables must be set in the same terminal session before running the script.

# ▶️ How to Run
```bash
python main.py
```

If the stock price change is 5% or greater, you will receive an SMS containing:

News title

Description

Article link

# ⚙️ Configuration
Change the stock symbol
```bash
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
```

Examples:

Company	Symbol
Apple	AAPL
Amazon	AMZN
Google	GOOGL
Nvidia	NVDA
# 📊 Percentage Logic
```bash
percentage = (yesterday - day_before_yesterday) * 100 / yesterday
```

Alert triggers when:
```bash
percentage ≥ 5%
```

You can change this threshold easily.

# ⚠️ Limitations

Free Alpha Vantage API has request limits

SMS costs apply after Twilio free trial

Script checks data only once per run

Not running automatically unless scheduled

# 💡 Possible Improvements

Add automatic daily scheduling

Support multiple stocks

Add up/down arrow indicators (🔺🔻)

Send separate SMS per article

Add email or Telegram notifications

Store historical alerts

# 👨‍💻 Learning Goals

This project demonstrates understanding of:

REST APIs

JSON data parsing

Environment variables

External services integration

Conditional logic

Real-world automation

# ⭐ Portfolio Note

This project is ideal for:

Python portfolios

Automation demos

API practice examples

Internship or junior developer showcases
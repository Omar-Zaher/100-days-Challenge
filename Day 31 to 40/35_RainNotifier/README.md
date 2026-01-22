# 🌧️ Rain Notifier (WhatsApp Alert)

A simple Python script that checks the weather forecast using the OpenWeather API and sends a WhatsApp message notification if rain is expected.

# 📌 Features

Uses real weather data from OpenWeather

Checks upcoming forecast for rain

Automatically sends a WhatsApp message

Uses environment variables for security

Beginner-friendly and easy to customize

# 🧠 How It Works

The script fetches weather forecast data for a specific location.

It checks the weather condition codes.

If rain is detected (weather ID < 700),
a WhatsApp message is sent using pywhatkit.

# ⚙️ Requirements

Make sure you have the following installed:

Python 3.9+

Google Chrome (recommended)

WhatsApp account

Internet connection

Python Libraries

Install required packages:
```bash
pip install requests pywhatkit
```
# 🔑 API Key Setup (IMPORTANT)

This project uses the OpenWeather API.

Step 1: Get an API key

Go to OpenWeather

Create a free account

Generate an API key

Step 2: Set environment variables
On Windows (PowerShell)
```bash
$env:API_KEY="your_openweather_api_key"
$env:Phone_Num="+9627XXXXXXXX"
```

# ⚠️ Phone number must include the country code.

Example:

+96279XXXXXXX


You must run these commands in the same terminal session before running the script.

# ▶️ How to Run

Make sure you are logged into WhatsApp Web
(https://web.whatsapp.com
)

Run the script:

python rain_notifier.py


If rain is expected, you will receive a WhatsApp message.

# 📍 Location Configuration

You can change the location by modifying:
```bash
parameters = {
    "lat": 40.7127281,
    "lon": -74.0060152,
}
```

Use latitude and longitude of your city.

# ☔ Weather Logic

The script checks:

if weather_id < 700:


According to OpenWeather:

IDs below 700 represent rain, drizzle, or snow.

⚠️ Important Notes

This script uses WhatsApp Web automation

Your browser will open automatically

Do not touch the mouse or keyboard while sending

Emojis may not always send correctly due to pywhatkit limitations

If the emoji fails, use:

"It might rain. Bring an umbrella!"

# 🚫 Limitations

Not a background service

Requires WhatsApp Web to be logged in

Not suitable for large-scale automation

Intended for personal use only

# 🧩 Possible Improvements

Add multiple phone numbers

Automatically calculate forecast time

Add email or Telegram notifications

Convert into a daily scheduled task

Add location detection

# 👨‍💻 Author

Created as a learning project to practice:

APIs

Environment variables

Automation

Python scripting
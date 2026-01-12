# ==================================================== ISS Overhead Notifier ====================================================

# ---- Imports ----
import requests as rq
import datetime as dt
import smtplib
from email.message import EmailMessage
import time

datetime = dt.datetime

# My cords
my_long = 0 # put your longitude
my_lat = 0 # put your latitude 

# ---- Functions ----
def send_email():
    email = "" # Your email here
    password = "" # Your email password here
    recipient = ""  # Recipient email here

    msg = EmailMessage()
    msg["Subject"] = "ISS IS Above YOU!"
    msg["From"] = email
    msg["To"] = recipient
    msg.set_content("ISS IS Above YOU! Go out and see the sky!")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # secure the connection
            connection.login(user=email, password=password)
            connection.send_message(msg)
        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError as e:
        print("Login failed:", e.smtp_code, e.smtp_error)
    except Exception as e:
        print("Something went wrong:", e)


# --- ISS position ---
def iss_position():
    
    try:
        response = rq.get("http://api.open-notify.org/iss-now.json", timeout=10)
        response.raise_for_status()
        data = response.json()
        iss_long = float(data["iss_position"]["longitude"])
        iss_lat = float(data["iss_position"]["latitude"])
        return my_long - 5 <= iss_long <= my_long + 5 and my_lat - 5 <= iss_lat <= my_lat + 5
    
    except Exception as e:
        print("ISS API error:", e)
        return False

def is_night():
    # ---- My time ----
    current_hour = datetime.now().hour

    # ---- Sunrise and Sunset ----
    parameters ={
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0  
    }

    res = rq.get("https://api.sunrise-sunset.org/json", params= parameters)
    res.raise_for_status()
    data2 = res.json()
    sunrise_utc = int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_utc = int(data2["results"]["sunset"].split("T")[1].split(":")[0])
    
    # Convert UTC to local hour (replace +4 with your timezone offset)
    utc_offset = 4  # example: Dubai is UTC+4
    sunrise = (sunrise_utc + utc_offset) % 24
    sunset = (sunset_utc + utc_offset) % 24

    return current_hour >= sunset or current_hour <= sunrise

# ---- logic ----
while True:
    if iss_position() and is_night():
        send_email()
        time.sleep(600) # wait 10 minutes to avoid spamming
    time.sleep(60)

# ====================================================================================================================

# =================================================== Birthday Wisher ===================================================

# ------ IMPORTS ------
import smtplib
import datetime as dt
import random
import pandas as pd
from email.message import EmailMessage

# ------ CONFIGURATION ------ 
email = "" # Your email here
password = "" # Your email password here
your_name = "" # Your name here

msg = EmailMessage()

# ----- MAIN CODE ------
# **** Read birthday data ****
with open("./32_Birthday Wisher/birthdays.csv") as data_file:
    data = pd.read_csv(data_file)
    data_dict = {
        (data_row["month"], data_row["day"]): data_row
        for (index, data_row) in data.iterrows()
    }

    today = dt.datetime.now()
    today_tuple = (today.month, today.day)
    
    # **** Check if today matches a birthday and send email ****
    if today_tuple in data_dict:
        person = data_dict[today_tuple]
        resever_email = person["email"]
        letter_path = f"./32_Birthday Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
        with open (letter_path, encoding="utf-8") as letter_file:
            letter = letter_file.read()
            personalized_letter = letter.replace("[NAME]", person["name"]).replace("[YOURNAME]", your_name)

        # initialize email message
        msg["Subject"] = "Happy Birthday!"
        msg["From"] = email
        msg["To"] = resever_email
        msg.set_content(personalized_letter)

        # send email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.send_message(msg)

# =============================================================================================================
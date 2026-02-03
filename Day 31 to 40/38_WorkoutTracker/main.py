# ======================================================================= Workout Tracker Application =======================================================================

# ------ Imports -------
import requests
from datetime import datetime
import os

# ------ Environment Variables -------
x_app_id= os.environ.get("x_app_id")

x_app_key= os.environ.get("x_app_key")

# ------ Extracting Exercise Data -------
headers = {
    "x-app-id": x_app_id,
    "x-app-key": x_app_key,
    "Content-Type": "application/json"
}

user_input = input("Enter your workout details: ")
exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
parameters = {
    "query": user_input,
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# ------ Storing Data in Google Sheets -------
sheety_endpoint = os.environ.get("sheety_endpoint")

exercise_data = {
    "workout": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercise": result["exercises"][0]["name"].title(),
        "duration": result["exercises"][0]["duration_min"],
        "calories": result["exercises"][0]["nf_calories"]
    }
}
sheety = requests.post(sheety_endpoint, json=exercise_data)
print(sheety.text)

# ============================================================================================================================
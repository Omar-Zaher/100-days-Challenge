# ============================================================== Rain Notifier ======================================================

# ----- Imports -------
import requests as rq
import pywhatkit 
import os


# ------ Getting Data ---------
# setting params
parameters ={
    "lat": 40.7127281, # As an example I have put the lat and lon of New York
    "lon": -74.0060152,
    "appid" : os.environ.get("API_KEY"),
    "cnt": 4 # getting data only for one day
}

# saving the data as json
result = rq.get("https://api.openweathermap.org/data/2.5/forecast", params = parameters)
result.raise_for_status()
data = result.json()

# -------- Will it Rain ? ---------
rain = False
for i in data["list"]:
    if i["weather"][0]["id"] < 700:
        rain = True
        break

# -------- Send Message ----------    
if rain:
    pywhatkit.sendwhatmsg_instantly(os.environ.get("Phone_Num"),"It might rain: Bring ☂️!")
    
# ==============================================================================================================

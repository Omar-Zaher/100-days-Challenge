# ISS Notifier

A Python script that automatically notifies you via email when the International Space Station (ISS) is overhead **and** it is night at your location.  

This project uses public APIs to track the ISS position and calculate local sunrise/sunset times to determine if it’s a good time to see the ISS in the night sky.

---

## Features

- Checks the real-time position of the ISS using the [Open Notify API](http://api.open-notify.org/iss-now.json).
- Determines whether it’s currently night using the [Sunrise-Sunset API](https://sunrise-sunset.org/api).
- Sends an email alert when the ISS is near your location (within ±5° latitude/longitude) **and** it is nighttime.
- Includes a 10-minute cooldown to prevent email spam.

---

## Requirements

- Python 3.7+  
- `requests` library  

Install dependencies using pip:

```bash
pip install requests
```
## Set UP

Update your latitude and longitude:

```python
my_lat = YOUR_LATITUDE
my_long = YOUR_LONGITUDE
```
Your Timezone Offset
```python
utc_offset = 4  # <--- Change this (e.g., -5 for EST, +1 for UK, +4 for Dubai) 
```

Email Credentials
```python
email = "YOUR_EMAIL"
password = "YOUR_APP_PASSWORD"
recipient = "RECEIVER_EMAIL"
```


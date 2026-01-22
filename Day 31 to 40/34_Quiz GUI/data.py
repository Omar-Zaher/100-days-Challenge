import requests as rq


response = rq.get("https://opentdb.com/api.php", params={"amount": 11,"type": "boolean"})
response.raise_for_status()
data = response.json()

question_data = data["results"]

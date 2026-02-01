# 🟦 Pixela Habit Tracker (Water Intake)

This is a simple **command-line habit tracker** built with Python and the **Pixela API**. It allows you to track your daily water intake by adding, updating, deleting, and viewing pixels on a Pixela graph.

The project assumes you have already set up your Pixela account and graph. The steps below explain **everything you need to do once**, so you can safely delete the commented setup code from the Python file afterward.

---

## 📌 What is Pixela?

[Pixela](https://pixe.la/) is a free API service that lets you record and visualize daily habits using graphs. Each data point is called a **pixel**, and each habit has its own **graph**.

---

## 🛠️ First-Time Pixela Setup (One-Time Only)

You only need to do these steps **once** when setting up Pixela for the first time.

### 1️⃣ Create a Pixela Account

You need a **username** and a **token**.

* Choose a unique username
* Create a secure token (this works like a password)

Send a POST request to Pixela’s user endpoint with the following data:

* `token`
* `username`
* `agreeTermsOfService`: "yes"
* `notMinor`: "yes"

Example:
```
param_info = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

result = rq.post(url= "https://pixe.la/v1/users", json = param_info)
print(result.text)
```

Once your account is created successfully, you **do not need to repeat this step**.

---

### 2️⃣ Create a Graph

Each habit is represented by a graph. For this project, the graph tracks **daily water intake**.

Graph configuration used:

* **Graph ID**: `graph1`
* **Name**: drinking_water
* **Unit**: liters
* **Type**: float
* **Color**: sora

You must include your token in the request header:

```
X-USER-TOKEN: <your_token>
```
Example:
```
#------- Creating Graph --------
graph_info ={
    "id" : "graph1",
    "name": "drinking_water",
    "unit": "liters",
    "type": "float",
    "color": "sora",   
}
graph_header ={
    "X-USER-TOKEN" : TOKEN
}

result = rq.post(url = url, json= graph_info, headers= graph_header)
print(result.text)
```
After the graph is created successfully, you **never need to recreate it** unless you delete it from Pixela.

---

### ✅ After Setup

Once your **account** and **graph** exist:

* You can delete or ignore all commented setup code in the Python file
* You only need:

  * `USERNAME`
  * `TOKEN`
  * `GRAPH_ID`

The rest of the program will work automatically.

---

## ▶️ How to Run the Program

1. Make sure you have Python installed
2. Install the Pixela wrapper (if required):

```
pip install pixela
```

3. Run the script:

```
python main.py
```

4. Enter:

   * Your Pixela username
   * Your Pixela token
   * Your graph ID

---

## 📋 Available Actions

When the program starts, you can choose one of the following:

1. **Add pixel** – Log today’s water intake
2. **Update pixel** – Change water intake for a specific date
3. **Delete pixel** – Remove data for a specific date
4. **Pull pixel data** – View graph data

The program will loop until a valid option is selected.

---

## 🧠 Notes

* Dates must be in the format: `YYYYMMDD`
* Quantity should be a numeric value (float allowed)
* Your token should be kept **private**

---

## 🚀 Future Improvements

* Input validation for dates and quantities
* Persistent menu loop (run multiple actions in one session)
* Support for multiple habits/graphs
* Create it with GUI

---

Happy tracking 💧

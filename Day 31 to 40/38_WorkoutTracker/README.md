# 🏃‍♂️ Workout Tracker Application

A simple Python application that allows users to log their workouts by describing them in natural language (e.g. "ran 2km"), automatically calculates calories burned, and stores the workout data in Google Sheets.

This project is part of the **100 Days of Python** course and demonstrates working with APIs, environment variables, and external services.

---

## ✨ Features

* Accepts workout descriptions in natural language
* Uses an external exercise API to analyze workouts
* Automatically extracts:

  * Exercise name
  * Duration (minutes)
  * Calories burned
* Saves workout data to Google Sheets using Sheety
* Secure API key handling using environment variables

---

## 🛠️ Technologies Used

* **Python 3**
* **Requests** library
* **Nutrition / Exercise API** (via 100 Days of Python proxy)
* **Sheety API** (Google Sheets integration)
* **Environment Variables** for security

---

## 📦 Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd WorkoutTracker
```

---

### 2️⃣ Install Dependencies

Make sure you have `requests` installed:

```bash
pip install requests
```

---

### 3️⃣ Set Up Environment Variables (Windows PowerShell)

```powershell
setx x_app_id "YOUR_APP_ID"
setx x_app_key "YOUR_APP_KEY"
setx sheety_endpoint "YOUR_SHEETY_ENDPOINT"
```

⚠️ Restart PowerShell or your IDE after running these commands.

---

### 4️⃣ Verify Environment Variables (Optional)

```powershell
echo $Env:x_app_id
echo $Env:x_app_key
echo $Env:sheety_endpoint
```

---

## ▶️ How to Run the Application

```bash
python main.py
```

When prompted:

```text
Enter your workout details: ran 2km
```

The workout will be analyzed and automatically added to your Google Sheet.

---

## 📊 Google Sheets Output

Each workout entry includes:

* Date
* Time
* Exercise name
* Duration (minutes)
* Calories burned

---

## 🔐 Security Notes

* API keys are **not hard-coded**
* Environment variables are used to protect sensitive data
* Make sure `.env` or secrets files are added to `.gitignore` if used

---

## 🚀 Future Improvements

* Support multiple exercises in one input
* Add error handling for API failures
* Create a simple GUI or web interface
* Add workout summaries and statistics

---

## 🙌 Acknowledgements

* **100 Days of Python** by Dr. Angela Yu
* Nutrition & Exercise API
* Sheety API

---

## 📌 Author

Built by **Omar Zaher** as part of a learning journey into Python, APIs, and automation.

Happy training 💪

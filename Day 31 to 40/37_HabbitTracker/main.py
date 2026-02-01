# ========================================================= Habbit Tracker ===========================================================

# ------- Imports ---------
from pixela import Pixela

# ------- Initilizing pixela account -------------
USER = input("Enter your username: \n")
TOKEN = input("Enter your token: \n")
GRAPH_ID = input("Enter your graph id: \n")


# ----- Adding a pixel -------
while True:
    ask_user = input(
        "What do you want to do?\n"
        "1- Add pixel\n"
        "2- Update pixel\n"
        "3- Delete pixel\n"
        "4- Pull pixel data\n"
    )

    if ask_user not in {"1", "2", "3", "4"}:
        print("Invalid choice. Please enter a number between 1 and 4.\n")
        continue

    info = Pixela(token=TOKEN, username=USER, graph_id="graph1")
    if ask_user == "1":
        quantity = input("How many liters did you drink today?\n")
        info.post(quantity)

    elif ask_user == "2":
        date = input("Enter the date you want to update (YYYYMMDD):\n")
        quantity = input("Enter the new quantity:\n")
        info.update(quantity, date)

    elif ask_user == "3":
        date = input("Enter the date you want to delete (YYYYMMDD):\n")
        info.delete(date)

    elif ask_user == "4":
        info.pull()
    
    break

# ================================================= End of Habbit Tracker ============================================================
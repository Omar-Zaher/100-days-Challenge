# =========== DATA FILE FOR COFFEE MACHINE ===========
# Note: These info were from ChatGPT it might not be 100% accurate.
COFFEE_MENU = {
    1: {
        "name": "Espresso",
        "price": 2.00,
        "recipe": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        }
    },
    2: {
        "name": "Americano",
        "price": 2.50,
        "recipe": {
            "water": 150,
            "coffee": 18,
            "milk": 0,
        }
    },
    3: {
        "name": "Latte",
        "price": 3.50,
        "recipe": {
            "water": 50,
            "coffee": 18,
            "milk": 150,
        }
    },
    4: {
        "name": "Cappuccino",
        "price": 3.00,
        "recipe": {
            "water": 50,
            "coffee": 18,
            "milk": 120,
        }
    },
    5: {
        "name": "Mocha",
        "price": 4.00,
        "recipe": {
            "water": 50,
            "coffee": 18,
            "milk": 120,
            "chocolate": 20
        }
    }
}

def logo():
    print ("""

   _____       __  __            __  __            _     _            
  / ____|     / _|/ _|          |  \/  |          | |   (_)           
 | |     ___ | |_| |_ ___  ___  | \  / | __ _  ___| |__  _ _ __   ___ 
 | |    / _ \|  _|  _/ _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
 | |___| (_) | | | ||  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
  \_____\___/|_| |_| \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
                                                                      
                                                                      
""")
# ===================================================== Improved Coffee Machine =====================================================

# ------------ Imports ------------
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable

# ------------ Variables ------------
money = MoneyMachine()
table = PrettyTable()
menu = Menu()
choices = [1,2,3]
items = menu.get_items()
maker = CoffeeMaker()
table.add_column("Numbers",choices)
table.add_column("Coffee",items)

# =================================================== Main Program ===================================================
while True:
    print(table)
    # ------------ User Choice ------------
    while True: 
            try:
                user_choice = int(input("Select a drink number: "))
                if user_choice not in choices:
                    print("Please select a valid drink number from the menu.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number corresponding to your drink choice.") 

    # ------------ Process Order ------------
    if user_choice == 1:
        drink = menu.find_drink(items[0])   # Latte
    elif user_choice == 2:
        drink = menu.find_drink(items[1])   # Cappuccino 
    else:
        drink = menu.find_drink(items[2])   # Espresso   
              
    # ------------ Check Resources & Make Coffee ------------
    if maker.is_resource_sufficient(drink):
        maker.make_coffee(drink)
        print(f"That will be ${drink.cost}")
        money.make_payment(drink.cost)
    
    # ------------ Another Order? ------------
        while True: 
            more = input("Would you like to order something else: ").lower()
            if more == "yes":
                break
            elif more == "no":
                money.report()
                print("I hope you have a good day then!")
                break
            else:
                print("Please enter yes or no!\n")
        
        if more == "no":
            break
    else:
        break
# =============================================================================================================        
# ==================================== Coffee Machine ====================================
# ------------ Imports ------------
import data

# ------------ Functions ------------
# Show Menu Function
def show_menu():
    print("\n==============================")
    print("       COFFEE MACHINE ")
    print("==============================")
    print("  [1] Espresso")
    print("  [2] Americano")
    print("  [3] Latte")
    print("  [4] Cappuccino")
    print("  [5] Mocha")
    print("==============================")
    
# Report Function   
def report(water, coffee, milk):
    print("\n========================================")
    print("         MACHINE RESOURCE REPORT")
    print("========================================")
    print(f" Water Level  : {water} ml")
    print(f" Coffee Beans : {coffee} g")
    print(f" Milk Level   : {milk} ml")
    print("========================================\n")
    
    
# ------------ Resources ---------------
water = 300
milk = 200
coffee = 100
chocolate = 50


# =================================================== Main Program ===================================================
while True:
    show_menu()
    
# ------------ User Choice ------------
    while True: 
        try:
            user_choice = int(input("Select a drink number: "))
            if user_choice not in [1, 2, 3, 4, 5]:
                print("Please select a valid drink number from the menu.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number corresponding to your drink choice.")   
            
# ------------ Process Order ------------
    user_choice = data.COFFEE_MENU[user_choice]
    option = user_choice["name"]
    price = user_choice["price"]

    print(f"Your order is: {option}\nand that will be ${price}")

# ------------ Payment ------------
    while True:  
        try:  
            money = float(input("How much would you like to pay: "))
        except ValueError:
            print ("Please type the answer in numbers!")
            continue
        if money < price:
            print("Sorry that is not enough!")
            
        else:
            break
    
    # ------------- Make Coffee ------------  
    water_needed = user_choice["recipe"]["water"]
    coffee_needed = user_choice["recipe"]["coffee"]
    milk_needed = user_choice["recipe"]["milk"]

    # Check resources
    if water < water_needed or coffee < coffee_needed or milk < milk_needed:
        print ("\n Not enough ingredients for this drink!")
        report (water,coffee,milk)
        print("Please ask the desk for a refill.\n")
        break
    elif money > price:
        change = round(money - price, 2)
        water -= water_needed
        coffee -= coffee_needed
        milk -= milk_needed
        print(f"\nHere is ${change} change.\nI hope you enjoy your {option}")
    else:
        water -= water_needed
        coffee -= coffee_needed
        milk -= milk_needed
        print(f"\nI hope you enjoy your {option}")
        
    # ------------ More Orders ------------
    while True: 
        more = input("Would you like to order something else: ").lower()
        if more == "yes":
            break
        elif more == "no":
            print("\nI hope you have a good day then!")
            break
        else:
            print("Please enter yes or no!\n")
    
    if more == "no":
        break
    
    
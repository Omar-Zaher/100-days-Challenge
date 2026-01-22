# ======================================================================== Higher Lower Game =================================================================

# ----------- Importing ------------
import random

# -----------  Data ------------
# Note: This data was made by AI and may not be accurate
data = {
    "China": 1440,
    "India": 1393,
    "United States": 332,
    "Indonesia": 276,
    "Pakistan": 225,
    "Brazil": 213,
    "Nigeria": 211,
    "Bangladesh": 166,
    "Russia": 146,
    "Mexico": 130
}
# =========================================================== Main Program =====================================================================
# --------- Shuffle Data ------------
country = list(data.keys()) # Shuffle does not work on dictionary directly
random.shuffle(country) 

# ----------- Functions ------------
# Drew Country Function
def option ():
    return country.pop()

# ------------ Game --------------
# Initalize first country and score
country_1 = option()
total = 0
while True:
    country_2 = option() # Second country in loop because it changes every round
    print (f"\nFirst country: {country_1}\n\nSecond country: {country_2}") 
    
    # Determine correct answer
    if data[country_1] < data[country_2]: # Compares populations
        answer = "higher"
    else:
        answer = "lower"
    
    # Get user input with validation    
    while True:
        choice = input("\nHigher or Lower? ").lower()
    
        if choice not in ["higher", "lower"]:
            print("\nInvalid input. Please type 'higher' or 'lower'.")
        else:
            break 
    
    # Check answer and update score or end game
    if choice == answer:
        total += 1
        country_1 = country_2 # Update first country for next round
    else:
        print (f"\nSorry your answer was wrong\nYour final score is: {total}\n")
        break
         
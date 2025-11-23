
# ============================================================== Number Guessing Game =============================================================
# ************ Importing ***************
import random
import logos


# 1- Random number between 1 and 100

number = random.randint(1,100)

 
# *********** Difficulty level **************
while True:
    difficulty = input("Choose your level\nEasy\nHard\nAnswer: ").lower() 
    if difficulty == "easy": # 3- if easy user has 10 rounds
        rounds = 10
        break
    elif difficulty == "hard": # 4- if Hard user has 5 rounds
        rounds = 5
        break
    else:
        print("Invalid choice. Please type 'Easy' or 'Hard'.") # Input validation

    
while rounds > 0: # While rounds are left user can guess the number
    try:
        user_guess = int(input("Guess a number between 1 and 100\nnumber:"))
        
        if user_guess == number: # Winning condition
            print(logos.win)
            rounds = 0 
        elif user_guess > number:
            print ("High")
        else:
            print ("Low")
        rounds -= 1
    except ValueError: # Error handling for non-integer inputs
        print ("Please type an absolute number")
        
if rounds == 0: # Losing condition
    print(logos.lose)
    print(f"The number was {number}")

 # =======================================================================================================================================       
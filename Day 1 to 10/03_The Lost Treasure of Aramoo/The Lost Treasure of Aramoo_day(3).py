# =============== Game Icon ======================================
from logos import lost_treasure

lost_treasure()
# =====================================================================

# Welcome 
print ("Welcome to The Lost Treasure of Aramoo!\n")

# Ask user if they want to play
start = input("Are you ready to Find the Treasure?\n write y for yes\n write n for no\nAnswer:")

# If user don't want to play
if start == "n":
    print ("Sorry to hear that, bye!")

# ============ Game ============

else:
    print ("Welcome on abroad! I am your captin. You must be ...")
    
    
# ********** User's Name ********************
    name = input("Whats your name?\nAnswer: ")
    print (f"Oh yeah I remembered you are {name}\nAnd your the one who is gonna gide us to the Treasure!\nWell Well here is your first question: \nYou stand at the edge of the jungle. Two paths lie ahead.\n ")
    
    # ********* Quesion 1 ****************
    First_Question = input("A. Take the coastal path — safer, but longer.\nB. Cut through the jungle — faster, but full of unknown dangers.\nAnswer:")
    if First_Question == "A":
        
        # ************ Question 2 ***********************
        print ("You encountered a group of friendly fishermen who offer you a clue about the treasure’s location.\nHere it is: I have no voice, yet I speak to you. I have no legs, yet I run. What am I?")
        Second_Question = input("A. Answer “Wind”\nB. Answer “River”\nC. Ignore the riddle and move on\nAnswer: ")
        
        if Second_Question == "B":
            # ********** Question 3 ********************************
            print ("A hidden passage opens, revealing a shortcut to the treasure cave.\nInside the cave a spectral guardian blocks your path. It offers you a challenge:\nTo pass, you must sacrifice one of these: your weapon, your food, or your map.")
            Last_Question = input("A. Sacrifice your weapon \nB. Sacrifice your food \nC. Sacrifice your map\nAnswer:")
            if Last_Question == "C":
                print (f"Congrats {name}! You Have Found the Treasure!")
                
            elif Last_Question == "B":
                print ("You Died of Hunger! \nEnd of the Game!")
                
            else:
                print ("A beast came and killed you! \nEnd of the Game!")
            # ***********************************************************
        
        else:
            print ("Oh no! You are lost in the jungle \nEnd of the Game!")
        # ************************************************
        
    else:
        print ("Oh no! You were Killed by wild beasts \nEnd of the Game!")
    # ****************************************
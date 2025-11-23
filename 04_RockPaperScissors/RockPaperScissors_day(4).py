# ============= importing modules =========================

import random
import logos

# =========================================================

# ============== Welcome =====================

print ("Welcome to Rock Paper Scissors")

# =========================================================


# ****** Visulizing Choices by ASCII art ***********

Rock = logos.Rock
Paper = logos.Paper
Scissors = logos.Scissors

# ============= Visualizing Choices ========================
ending = False
while ending == False:
    
# *********** Users input ************:

    users_choice = input("1- Rock\n2- Paper\n3- Scissors\nWhat is Your choice: ")
    
    if users_choice == "1":
        print(f"Your Choice:\n {Rock}" )

    elif users_choice == "2":
        print(f"Your Choice:\n {Paper}")
        
    elif users_choice == "3":
        print(f"Your Choice:\n {Scissors}")
    # ============= Computer Choice ========================

    # ******** Create a list ***********

    lis = ["rock","paper","scissors"]

    # ******* Randomize list ********

    Computer_choice = random.choice(lis)

    # ****** Visulizing Computers Choice ***********

    if Computer_choice == "rock":
        print(f"Computer Choice:\n {Rock}" )

    elif Computer_choice == "paper":
        print(f"Computer Choice:\n {Paper}" )
        
    elif Computer_choice == "scissors":
        print(f"Computer Choice:\n {Scissors}" )
    # =========================================================    
        
    # ================ Winning or lossing ============================

    if users_choice == "1" and Computer_choice == "scissors" or users_choice == "2" and Computer_choice == "rock" or users_choice == "3" and Computer_choice == "paper":
        print (logos.win)
        
    elif users_choice == "1" and Computer_choice == "paper" or users_choice == "2" and Computer_choice == "scissors" or users_choice == "3" and Computer_choice == "rock":
        print (logos.lose)

    else:
        print (logos.draw)
    
    user_input = input("Do you want to play again? (yes/no): ").lower()
    if user_input == 'yes':
        continue
    else:
        ending = True
        print("Goodbye!")
# =========================================================
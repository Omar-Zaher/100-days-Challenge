# ============= importing modules =========================

import random

# =========================================================

# ============== Welcome =====================

print ("Welcome to Rock Paper Scissors")

# =========================================================

# *********** Users input ************:

users_choice = input("1- Rock\n2- Paper\n3- Scissors\nWhat is Your choice: ")

# ****** Visulizing Choices by ASCII art ***********

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


"""


Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)

"""



Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""




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
    print ("Congrats You Won!")
    
elif users_choice == "1" and Computer_choice == "paper" or users_choice == "2" and Computer_choice == "scissors" or users_choice == "3" and Computer_choice == "rock":
    print ("You Lost:(")

else:
    print ("Wow! it's a tie")
    
# =========================================================
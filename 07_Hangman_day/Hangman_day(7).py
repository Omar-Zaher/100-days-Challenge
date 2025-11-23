# ========= Importing ===========

import random
import logos

# ==================================

logos.hangman()

print ("Welcome to Hangman!")

# 2- Make computer choose one
level = input("Choose Level:\nA:Easy\nB:Medium\nC:Hard\nPlease write your choice (A,B,C): ").lower()
word = ""

if level == "a":
    word = random.choice(logos.Easy)
    
elif level == "b":
    word = random.choice(logos.Medium)    
    
elif level == "c":
    word = random.choice(logos.Hard) 
    
else:
    print ("Error! No letter found!")  


# 3- Add blank spaces

for i in word:
    blanks = ["_"] * len(word)

print (blanks)

# =========================================================

# ================= Check the letter ================
lives = 0
gameover = False
letters_chosen = []
while gameover == False:
    
    blank = False
# 1- Ask player for letter

    letter = input("Choose your letter: ").lower()[0]
    if letter not in letters_chosen: 
    # 2- is letter in the word
        letters_chosen.append(letter)
        letter_found = False
        
        for index, i in enumerate(word):
        # 3- If yes, fill blanks
            if i == letter:
                letter_found = True
                blanks[index] = letter
                if "_" in blanks:
                    blank = True
                    
                        
                if blank == False:
                    print (f"{logos.win}\n The word was {word} 🥳")
                    gameover = True       
                print (f"Your answer {blanks}")
            
    #  4- If no, draw hangman(need to create a list for drawings) 
        if letter_found == False and lives < 6:
            print (logos.HANGMANPICS[lives])
            lives += 1
        elif lives >= 6: 
            print (logos.HANGMANPICS[lives])
            print (f"{logos.lose} \nThe word was {word} \nYour final Answer was: {blanks}")
            gameover = True   
    else:
        print ("You chose this letter before, Please choose another one")       
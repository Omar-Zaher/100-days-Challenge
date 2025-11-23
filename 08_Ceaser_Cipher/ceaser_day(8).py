# ========= Importing ===========

from logos import ceaser

# ==================================


# =================== Defining Functions ===================
# ****** Encode Function ******
def encode(word, shift, choice):
    encrypted = ""
    if choice == 2:
        shift *= -1 # Reverse shift for decryption
    for char in word:
        if char.isalpha(): # Check if character is a letter
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base) # Shift character
        else:
            encrypted += char # Non-alphabetic characters remain unchanged
    print("Encrypted message:", encrypted)
    
# ===========================================================    
    
# =================== Main Program ===================  
ceaser() # Display the Caesar Cipher logo
print ("Welcome to Caesar Cipher!")
end = False

while not end:
    try: # Error handling for invalid inputs
        welcome = int(input("How can we help you:\nType 1 for encryption\nType 2 for decryption\nChoice: "))
        message = input("What is the message?\n")
        shift = int(input("How many shifts?\n"))

        if welcome == 1 or welcome == 2:
            encode(message, shift,welcome)
        else:
            print("Invalid choice. Please enter 1 or 2.")

        again = input("Is there anything else I can help you with?\n(Please write Yes or No)\n").lower()
        if again == "no":
            print("Ok then, hope you have a good day!")
            end = True # Exit the loop
            
    except ValueError: # Catch non-integer inputs
        print("Please enter valid numbers for your choices and shifts.")

# ===========================================================


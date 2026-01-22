# ============ Importing =============

from logos import bidding

# =====================================

# ============ Main Program ============
bidding() # Display the Bidding Day logo

print ("Wecome to Bidding Day!\n")

# ********* Bidding Logic **************
bids = {}
more_bidders = "yes"
while more_bidders == "yes":
    try:
        name = input("What is your name?\nAnswer: ")
        value = int(input(f"Hello {name}! How much you are willing to bid? \nAnswer: "))
        bids[name] = value
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\nAnswer: ").lower()
        
        while more_bidders not in ["yes", "no"]: # Input validation
            more_bidders = input("Please type 'yes' or 'no'.\nAnswer: ").lower()

        if more_bidders == "yes":
            print("\n" * 15) # Clear the screen for the next bidder
            
    except ValueError:
        print("Invalid Input: Please enter a Number for the bid value.")

max_key = max(bids, key=bids.get) # Get the key with the highest value
max_value = bids[max_key] # Get the highest value

print (f"Congrats {max_key}! You have won🥳\n")

print("Final Bids:")
for bidder, amount in bids.items():
    print(f"- {bidder}: ${amount}")

# =====================================     

# ============================================================== Blackjack Game =============================================================
# ----------- Importing ------------
import random
import logos

# ----------- Preparing Deck ------------
deck = logos.cards.copy()
random.shuffle(deck) # Shuffle the deck

# ------------ Functions ------------
# ***** Draw Card Function *****
def draw_card():
   return deck.pop()

# ***** Calculate Total Function *****
def total_from_values(values):
    """Sum the values and adjust for Aces."""
    total = sum(values)
    aces = values.count(11) # Count Aces
    while total > 21 and aces > 0: # Adjust for Aces
        total -= 10  
        aces -= 1
    return total

# =========================================================== Main Program =====================================================================

# ----------- Initial Deal ------------
# ******** User's Cards *********
ascii1, value1 = draw_card() # First card for user
ascii2, value2 = draw_card()
player_cards = [ascii1, ascii2]
player_values = [value1, value2]

# ******** Dealer's Cards *********
dealer_ascii1, dealer_val1 = draw_card()
dealer_ascii2, dealer_val2 = draw_card()
dealer_cards = [dealer_ascii1, dealer_ascii2]
dealer_values = [dealer_val1, dealer_val2]

# ******** Show cards *********
# Initial display
print(f"Your cards:\n{ascii1}\n{ascii2}\nYour total: {total_from_values(player_values)}\n") 

# Initial dealer card display
print(f"Dealer's first card:\n{dealer_ascii1}\n")

# ------------ Game --------------
# ********* Player's Turn *********
while True:
   # end the turn if total is 21 or more
   if total_from_values(player_values) >= 21:
       break
   choice = input("Do you want to draw another card? Type 'yes' or 'no': ").lower()
   if choice == 'yes':
       ascii_new, value_new = draw_card()
       player_cards.append(ascii_new)
       player_values.append(value_new)
       print(f"You drew:\n{ascii_new}\nYour total: {total_from_values(player_values)}\n")
   else:
      break

# ********* Final User's Total *********
player_total = total_from_values(player_values)
print("Your final total:", player_total)

# ********* Dealer's Turn *********
print ("Dealer's cards:")
for card in dealer_cards:
   print(card)
dealer_total = total_from_values(dealer_values)
print("\nDealer's total:", dealer_total)

# Dealer draws until total is 17 or more
while dealer_total < 17:
    ascii_d, val_d = draw_card()
    dealer_cards.append(ascii_d)
    dealer_values.append(val_d)
    print("Dealer draws:", ascii_d)
    dealer_total = total_from_values(dealer_values)
    print("Dealer total now:", dealer_total)

# ----------- Result -----------
print("Final dealer total:", dealer_total)
print("Final player total:", player_total)

if player_total > 21:
    print(logos.lose)
elif dealer_total > 21:
    print(logos.win)
elif player_total > dealer_total:
    print(logos.win)
elif dealer_total > player_total:
    print(logos.lose)
else:
    print(logos.draw)
    
# ==============================================================================================================================================================

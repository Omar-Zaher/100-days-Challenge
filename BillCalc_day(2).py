# Welcome Message

print ("Welcome to the Bill Calculator!")

# ============ Functions (Not a part of the Course) ================

# ********* Error Handling **************
def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            number = int(user_input)
            return number
        except ValueError:
            print ("Invalid Input: Please enter a Number")
            
# ==========================================


# ========= User input =============
# Total Bill: 

Bill = get_number_input("What was the total bill?\n")

# Tip:

Tip = get_number_input("How much tip would you like to give?\n")

# Number of people:

Number_of_People = get_number_input("How many people wanna split the bill?\n")
# =====================================


# Calculate Total:

total = round((Bill + (Bill * Tip / 100) ) / Number_of_People , 2)

# Final Output

print (f"Each person should pay: ${total}")

        


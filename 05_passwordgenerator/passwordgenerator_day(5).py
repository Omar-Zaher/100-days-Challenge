# ========= Importing ==============

import random
import data

# ===============================

print ("Welcome to Password generator app!")

# ******* User input **************
num_letters = int(input("How many letters you want? "))
num_numbers = int(input("How many numbers you want? "))
num_symblos = int(input("How many symbols? "))

# ============ Functionality ===================
list = []

for i in range(0, num_letters):
    list.append(random.choice(data.letters))

for i in range(0, num_numbers):
    list.append(random.choice(data.numbers))

for i in range(0, num_symblos):
    list.append(random.choice(data.symbols))

random.shuffle(list)
password = "".join(list)
print (f"Your password is: {password}")
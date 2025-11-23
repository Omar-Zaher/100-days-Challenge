# ========= Importing ==============

import random

# ===============================

print ("Welcome to Password generator app!")

# ============ Main Variables ==============

letters = [
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z',
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [
    '!','@','#','$','%','^','&','*','(',')',
    '-','_','+','=','{','}','[',']','|','\\',
    ':',';','"',"'",'<','>',',','.','?','/'
]

# ============================================================

# ******* User input **************
num_letters = int(input("How many letters you want? "))
num_numbers = int(input("How many numbers you want? "))
num_symblos = int(input("How many symbols? "))

# ============ Functionality ===================
list = []

for i in range(0, num_letters):
    list.append(random.choice(letters))

for i in range(0, num_numbers):
    list.append(random.choice(numbers))

for i in range(0, num_symblos):
    list.append(random.choice(symbols))

random.shuffle(list)
password = "".join(list)
print (f"Your password is: {password}")
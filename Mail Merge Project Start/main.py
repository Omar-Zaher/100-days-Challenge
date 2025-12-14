#Create a letter using starting_letter.txt 
with open("Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()

#for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as names:
    names = names.readlines()

#Replace the [name] placeholder with the actual name.
x = "[name]"
for name in names:
    name = name.strip()
    letter = letter.replace(x, name)
    x = name
    
    #Save the letters in the folder "ReadyToSend".
    with open(f"Output/ReadyToSend/letter_to_{name}.txt", "w") as type:
        type.write(letter)




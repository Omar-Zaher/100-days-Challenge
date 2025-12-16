# ---- Import -----
import pandas

#----- Create dict from csv -----
data = pandas.read_csv("./26_Nato Alphabet/nato_phonetic_alphabet.csv")

dic = {row.letter:row.code for (index, row) in data.iterrows()}
 
#---- Ask user ----

user_input = input("What word you want to be translated to nato alphabet?\nWord:").upper()

# ---- Answer -------
answer = [dic[letter] for letter in user_input]
print(answer)
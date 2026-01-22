
import random

class Generator():
    def __init__(self):
        self.letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        
        
        self.numbers = ['0','1','2','3','4','5','6','7','8','9']
        
        
    def pass_generate(self):
        self.list =[]
        for _ in range(0, 6): # 6 letters
            self.list.append(random.choice(self.letters))

        for _ in range(0, 4): # 4 numbers
            self.list.append(random.choice(self.numbers))

        for _ in range(0, 2): # 2 symbols
            self.list.append(random.choice(self.symbols))

        # shuffle and joining the list
        random.shuffle(self.list)
        password = "".join(self.list)
        return password
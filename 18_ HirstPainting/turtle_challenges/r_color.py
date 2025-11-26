import random
class Color:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        
    # ---- Generating Random Color ----
    def random_color(self):
    
        self.r = random.randint(50,200)
        self.g = random.randint(50,100)
        self.b = random.randint(100,255)
        return (self.r, self.g, self.b)
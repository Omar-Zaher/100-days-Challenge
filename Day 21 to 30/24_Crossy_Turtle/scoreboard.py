from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = 0
        self.goto(x, y)
        self.update_score()
    
    def update_score(self):
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.write(f"{self.score}", align= "center", font= ("Arial", 20, "normal"))
    
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    def end(self):
        try:
            with open("data.txt", mode="r") as data:
                content = data.read().strip()
                old_high_score = int(content) if content else 0


        except FileNotFoundError:
            old_high_score = 0
        if self.score > self.high_score and self.score > old_high_score:
            self.high_score = self.score
        else:
            self.high_score = old_high_score   
             
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.clear()
        self.goto(0,260)
        self.write("GAME OVER!", align= "center", font= ("Arial", 24, "normal"))
        self.goto(0,240)
        self.write(f"Your High Score: {self.high_score}", align= "center", font= ("Arial", 13, "normal"))
        
    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()

from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        
        self.update_score()
    
    def update_score(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.speed("fastest")
        self.write(f"Score: {self.score}", align= "center", font= ("Arial", 13, "normal"))
    
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    def end(self):
        self.clear()
        self.home()
        self.write("GAME OVER!", align= "center", font= ("Arial", 24, "normal"))
        self.goto(0,-20)
        self.write(f"Your Score: {self.score}", align= "center", font= ("Arial", 13, "normal"))
        
    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()

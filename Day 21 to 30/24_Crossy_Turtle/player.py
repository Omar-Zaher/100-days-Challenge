from turtle import Turtle

class Player():
    def __init__(self):
        self.p = Turtle()
        self.p.shape("turtle")
        self.p.setheading(90)
        self.p.color("#FFFFFF")
        self.p.penup()
        self.p.shapesize(stretch_len=1.2, stretch_wid=1.2)
        self.p.goto(0, -240)
        self.p.speed("fastest")
        
        # Second turtle for outline effect
        self.p2 = Turtle()
        self.p2.shape("turtle")
        self.p2.setheading(90)
        self.p2.color("#16732A")
        self.p2.penup()
        self.p2.shapesize(stretch_len=0.95, stretch_wid=0.95)
        self.p2.goto(0, -240)
        self.p2.speed("fastest")
        
    def up(self):
        
        if self.p.ycor() < 280:
            self.p.setheading(90)
            self.p.forward(40)
            self.p2.setheading(90)
            self.p2.forward(40)
    
    def down(self):
        if self.p.ycor() > -280:
            self.p.setheading(270)
            self.p.forward(40)
            self.p2.setheading(270)
            self.p2.forward(40)
            
    def right(self):
        if self.p.xcor() < 280:
            self.p.setheading(0)
            self.p.forward(40)
            self.p2.setheading(0)
            self.p2.forward(40)
    
    def left(self):
        if self.p.xcor() > -280:
            self.p.setheading(180)
            self.p.forward(40)
            self.p2.setheading(180)
            self.p2.forward(40)
            
    def reset(self):
        self.p.goto(0, -240)
        self.p2.goto(0, -240)
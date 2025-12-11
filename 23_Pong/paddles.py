from turtle import Turtle

class Paddles():
    def __init__(self):
        self.paddle = Turtle()
    
    
    def draw(self,x,y):

        self.paddle.shape("square")
        self.paddle.setheading(90)
        self.paddle.shapesize(stretch_len=5, stretch_wid=1.5)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(x,y)
        self.paddle.speed("fastest")
        
    def up(self):
        if self.paddle.ycor() < 230:
            self.paddle.setheading(90)
            self.paddle.forward(30)
    
    def down(self):
        if self.paddle.ycor() > -230:
            self.paddle.setheading(270)
            self.paddle.forward(30)
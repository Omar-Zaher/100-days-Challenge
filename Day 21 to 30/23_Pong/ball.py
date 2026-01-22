from turtle import Turtle
import random



class Ball():
    def __init__(self):
        self.b = Turtle()
        self.heading = random.randrange(0,360)
        self.b.shape("circle")
        self.b.color("white")
        self.b.penup()
        self.b.speed(3)
        self.b.setheading(self.heading)
        self.dx = 3
        self.dy = 3
        
    
    def move (self):
        new_x = self.b.xcor() + self.dx
        new_y = self.b.ycor() + self.dy
        self.b.goto(x= new_x, y= new_y)
    
    def turn_y(self):
        self.dy *= -1
        
    def turn_x(self):
        self.dx *= -1
        
    def reset(self):
        self.b.home()
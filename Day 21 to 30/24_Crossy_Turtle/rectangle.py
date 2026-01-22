from turtle import Turtle, Screen
import random

class Rectangle (Turtle):
    def __init__(self,x,y,width,height,color="moccasin"):
        super().__init__()
        self.hideturtle()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
    
    def draw (self):
        self.penup()
        self.hideturtle()
        self.goto(self.x, self.y)
        self.fillcolor(self.color)
        self.begin_fill()
        for _ in range (2):
            self.forward(self.width)
            self.left(90)
            self.forward(self.height)
            self.left(90)
        self.end_fill()
        
# A palette of colors for the cars
CAR_COLORS = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]
screen = Screen()
screen.colormode(255)
class Car():
    def __init__(self, y_position):
        self.c = Turtle()
        self.c.pendown()
        self.c.shape("square") 
        self.c.shapesize(stretch_wid=1, stretch_len=2) 
        self.c.color(random.choice(CAR_COLORS))
        self.c.penup()
        x = random.randrange(-320,400)
        self.c.y = y_position
        self.c.goto(x, y_position) 
        self.c.setheading(180) 
        
        # Second turtle to make it look like a car
        self.c2 = Turtle()
        self.c2.pendown()
        self.c2.shape("square") 
        self.c2.shapesize(stretch_wid=0.75, stretch_len=1) 
        self.c2.color("white")
        self.c2.penup()
        self.c2.y = y_position
        self.c2.goto(x, y_position) 
        self.c2.setheading(180)
        
    def move(self, speed):
        self.c.forward(speed) 
        self.c2.forward(speed)
        if self.c.xcor() <= -320:
            x = random.randrange(320,600)
            self.c.goto(x,self.c.y)
            self.c2.goto(x,self.c2.y)
        
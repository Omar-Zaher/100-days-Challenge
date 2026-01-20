from turtle import Turtle
import random


class Food():
    def __init__(self):
        self.f = Turtle()
        self.shape = random.choice(["circle","square"])
        self.f.shape(self.shape)
        self.f.shapesize(stretch_wid= 0.7, stretch_len= 0.7)
        self.color = random.choice(["moccasin","wheat4"])
        self.f.color(self.color)
        self.f.penup()
        self.f.goto(0,100)
    
    def move_food(self):
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        self.color = random.choice(["moccasin","wheat4"])
        self.f.color(self.color)
        self.shape = random.choice(["circle","square"])
        self.f.shape(self.shape)
        self.f.goto(x,y)
        
    def end_food(self):
        self.f.hideturtle()
        
        
        
from turtle import Turtle
import random


class Food():
    def __init__(self):
        self.f = Turtle()
        self.f.shape("circle")
        self.f.color("green")
        self.f.penup()
        self.f.goto(0,100)
    
    def move_food(self):
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        self.f.goto(x,y)
        
        
        
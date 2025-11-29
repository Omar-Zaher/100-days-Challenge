from turtle import Screen, Turtle
import random

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

class Snake:
    def __init__(self):
        self.segments = []
        self.speed = 20
        self.direction = "Right"
        self.create_segments()
        self.head = self.segments[0]
        

    def create_segments(self):
        start_x = 0
        
        head = Turtle("circle")
        head.shapesize(stretch_wid=1, stretch_len=1.5)
        head.color("moccasin")
        head.penup()
        head.goto(start_x -10, 0)
        start_x -= 15
        self.segments.append(head)
        
        for _ in range(2):
            segment = Turtle("circle")
            segment.shapesize(stretch_wid=1, stretch_len=1.4)
            segment.color("wheat4")
            segment.penup()
            segment.goto(start_x, 0)
            start_x -= 15
            self.segments.append(segment)
        
        
    def move(self):
        # Move segments from tail to head
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)

        # Move head
        head = self.segments[0]
        if self.direction == "Right":
            head.setheading(0)
        elif self.direction == "Left":
            head.setheading(180)
        elif self.direction == "Up":
            head.setheading(90)
        elif self.direction == "Down":
            head.setheading(270)

        head.forward(self.speed)
        screen.update()
        #screen.ontimer(self.move, 120)  

    # Direction setters
    def up(self):
        if self.direction != "Down":
            self.direction = "Up"

    def down(self):
        if self.direction != "Up":
            self.direction = "Down"

    def left(self):
        if self.direction != "Right":
            self.direction = "Left"

    def right(self):
        if self.direction != "Left":
            self.direction = "Right"
            
    def new_segment(self, color, shape):
        position = self.segments[-1].position()
        segment = Turtle(shape)
        segment.color(color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    
    def stop(self):
        for i in self.segments:
            i.hideturtle()
            
         
    
        









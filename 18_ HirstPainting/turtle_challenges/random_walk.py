# ---- Importing ----
import turtle as t
from r_color import Color
import random

# ---- Setting up ------
screen = t.Screen()
t1 = t.Turtle()
c = Color()
t1.speed(10) # Set speed to 10
t1.pensize(10)
screen.colormode(255)
directions = [0,90,180,270] # Possible directions: right, up, left, down

# ---- Drawing Random Walk ----
for i in range(50): 
     
    t1.pencolor(c.random_color())
    t1.forward(30)
    t1.setheading(random.choice(directions)) # Choose random direction


screen.mainloop()
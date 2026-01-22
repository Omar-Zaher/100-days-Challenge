# ---- Importing ----
from turtle import Turtle, Screen
from r_color import Color

# ---- Setting up ------
c = Color()
screen = Screen()
t = Turtle()
screen.colormode(255)
t.speed("fastest")
t.pensize(2)
screen.bgcolor(0,0,0)

# ---- Drawing Spirograph ----
def spirograph(gap):
    for _ in range(int(360 / gap)):
        t.pencolor(c.random_color())
        t.circle(100)
        t.left(gap)

spirograph(5) # You can change the gap angle here

screen.mainloop()


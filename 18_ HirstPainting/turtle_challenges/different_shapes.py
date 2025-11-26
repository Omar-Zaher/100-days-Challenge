# ---- Importing ----
import turtle as t
from r_color import Color

# ---- Setting up ------
screen = t.Screen()
t1 = t.Turtle()
c = Color()
screen.colormode(255) # Set color mode to 255

# ---- Calculating Angle ----
def angle (n):
    return ((n-2)*180)/n 

# ---- Drawing Different Shapes ----
n = 3

while n < 10:
    angles = angle(n)
    t1.pencolor(c.random_color()) # Set random color
    for i in range (n):
        t1.forward(100)
        t1.right(180-angles)
    n += 1
        
screen.mainloop()
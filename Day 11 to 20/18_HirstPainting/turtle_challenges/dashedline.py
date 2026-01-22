# ---- Import turtle module ----
import turtle as t

# ---- Set up the screen and turtle ----
screen = t.Screen()
t1 = t.Turtle()

# ---- Draw dashed line ----
for i in range(10):
    t1.pendown() # Draw segment
    t1.forward(10)
    t1.penup() # Lift pen
    t1.forward(10)

screen.mainloop() # keep the window open
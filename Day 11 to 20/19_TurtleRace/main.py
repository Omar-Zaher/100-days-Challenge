# ===================================================== Turtle Race =====================================================

# ------ Imports ------
from turtle import Turtle, Screen
import random
import logos

# -------- Turtles  ----------
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()

# -------- User Bet Input --------
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\nEnter a color (red, blue, green, yellow, orange): ")
colors = ["red", "blue", "green", "yellow", "orange"]
turtles = [t1, t2, t3, t4, t5]
start_y = -100 # Starting y-coordinate for the first turtle

# --- Setting up turtles ---
for i, t in enumerate(turtles):
    t.color(colors[i])
    t.shape("turtle")
    t.penup()
    t.goto(x=-230, y=start_y) # Starting position
    start_y += 50 # distance between turtles

# -------- Race --------
while True:
    
    # Moving turtles forward by random distance
    t1.forward(random.randint(1,5))
    t2.forward(random.randint(1,5))
    t3.forward(random.randint(1,5))
    t4.forward(random.randint(1,5))
    t5.forward(random.randint(1,5))
    
    # Checking for winner and ending race
    if t1.xcor() >= 220:
        t1.hideturtle()
        winning = t1.pencolor()
        break
    elif t2.xcor() >= 220:
        t2.hideturtle()
        winning = t2.pencolor()
        break
    elif t3.xcor() >= 220:
        t3.hideturtle()
        winning = t3.pencolor()
        break
    elif t4.xcor() >= 220:
        t4.hideturtle()
        winning = t4.pencolor()
        break
    elif t5.xcor() >= 220:
        t5.hideturtle()
        winning = t5.pencolor()
        break

# -------- Result --------   
if user_bet == winning:
    print(logos.win)
else:
    print(f"{logos.lose}\nThe winning color was {winning}")
    
    
screen.mainloop()

# =================================================================================================
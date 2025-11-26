from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.speed(7)

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)
    
def turn_left():
    t.left(10)
    
def turn_right():
    t.right(10)
    
def clear_drawing():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    
# Key bindings
screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_drawing, "space")


screen.mainloop()
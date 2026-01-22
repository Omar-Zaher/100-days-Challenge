from turtle import Turtle
from button import Button

class Start ():
    
    def __init__(self):
        # --- UI Text Turtle (For "Welcome" text) ---
        self.ui = Turtle()
        self.ui.hideturtle()
        self.ui.penup()
        self.ui.color("white")
        self.b = Button(x=-50, y=-50, width=100, height=50, lable="Start")
        
    def show_welcome_screen(self):
        
        # Draw Title
        self.ui.clear()
        self.ui.goto(0, 50)
        self.ui.write("Pong", align="center", font=("Courier", 40, "bold"))
        
        # Draw Start Button
        self.b.draw_button()
        
    def reset(self):
        self.ui.clear()
        self.b.clear()
        

        
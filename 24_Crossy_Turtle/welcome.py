from turtle import Turtle

class Start ():
    
    def __init__(self):
        # --- UI Text Turtle (For "Welcome" text) ---
        self.ui = Turtle()
        self.ui.hideturtle()
        self.ui.penup()
        self.ui.color("black")
        
    def show_welcome_screen(self):
        
        # Draw Title
        self.ui.clear()
        self.ui.goto(0, 50)
        self.ui.write("Game Over", align="center", font=("Courier", 40, "bold"))
        
        # Draw Start Button
        self.b.draw_button()
        
    def reset(self):
        self.ui.clear()
        self.b.clear()
        

        
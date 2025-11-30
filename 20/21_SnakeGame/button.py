from turtle import Turtle

class Button(Turtle):
    def __init__(self):
        super().__init__()
        self.x = -50
        self.y = -50
        self.width = 100
        self.height = 30
        
    
    def draw_button (self, text):
        self.hideturtle()
        self.goto(self.x, self.y)
        self.fillcolor("moccasin")
        self.begin_fill()
        for _ in range (2):
            self.forward(self.width)
            self.left(90)
            self.forward(self.height)
            self.left(90)
        self.end_fill()
        self.penup()
        self.goto(self.x + self.width/2, self.y + self.height/4)
        self.write(text,align= "center", font= ("Arial", 12, "normal") )
        
    
    def check_button_click(self, x, y):
        half_w = self.width / 1.5
        half_h = self.height / 1.5

        return (self.x - half_w <= x <= self.x + half_w) and \
            (self.y - half_h <= y <= self.y + half_h)

    
    def reset(self):
        self.clear()
        self.hideturtle()
            
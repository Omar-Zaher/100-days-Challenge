from turtle import Turtle

class Button(Turtle):
    buttons = []
    def __init__(self,x,y,width,height,lable,color="moccasin"):
        super().__init__()
        self.hideturtle()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lable = lable
        self.color = color
        Button.buttons.append(self)
        
    
    def draw_button (self):
        self.hideturtle()
        self.goto(self.x, self.y)
        self.fillcolor(self.color)
        self.begin_fill()
        for _ in range (2):
            self.forward(self.width)
            self.left(90)
            self.forward(self.height)
            self.left(90)
        self.end_fill()
        self.penup()
        self.goto(self.x + self.width/2, self.y + self.height/4)
        self.write(self.lable,align= "center", font= ("Arial", 12, "normal") )
        
    
    def check_button_click(self, x, y):

        return (self.x <= x <= self.x + self.width) and \
            (self.y  <= y <= self.y + self.height)
            
            # starting point <= (x) (y) <= ending point

    @classmethod

    def reset(cls):
        for button in cls.buttons:
            button.clear()
            button.hideturtle()
            
from turtle import Screen, Turtle
import time
from paddles import Paddles
from scoreboard import ScoreBoard
from ball import Ball

# --- Screen Setup ---
width = 1000
height = 600
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=width, height=height)
p1 = Paddles()
p2 = Paddles()
score2 = ScoreBoard(50, 230)
score = ScoreBoard(-50, 230)
screen.tracer(0)

score.update_score()
score2.update_score()

# paddles 
p1.draw(width/2 - 50,0)
p2.draw(-(width/2 - 50),0)


screen.listen()
screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")
screen.onkey(p2.up, "w")
screen.onkey(p2.down, "s")

# ---- Ball --- 
ball = Ball()



def game_loop():
    
    ball.move()
    if ball.b.ycor() >= height/2-30 or ball.b.ycor() <= -(height/2-30):
        ball.turn_y()
        
    if (ball.b.xcor() > p1.paddle.xcor() - 10 and ball.b.xcor() < p1.paddle.xcor() + 10) and \
       (ball.b.ycor() < p1.paddle.ycor() + 50 and ball.b.ycor() > p1.paddle.ycor() - 50):
        ball.turn_x() 
    
    if (ball.b.xcor() > p2.paddle.xcor() - 10 and ball.b.xcor() < p2.paddle.xcor() + 10) and \
       (ball.b.ycor() < p2.paddle.ycor() + 50 and ball.b.ycor() > p2.paddle.ycor() - 50):
        ball.turn_x()

    if ball.b.xcor() < -(width/1.5):
        score2.add_score()
        ball.reset()
    if ball.b.xcor() > width/1.5:
        score.add_score()
        ball.reset()
        
      
    screen.update() 
    screen.ontimer(game_loop, 20) 
    
    
    
    
game_loop()









screen.mainloop()
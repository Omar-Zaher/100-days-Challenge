from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

snake = Snake()
screen = Screen()
screen.bgcolor("black")
screen.setup(width= 600, height = 600)
screen.title("Snake")
start_x = 0



# --- Game setup ---

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

  # start the loop
food = Food()
score = ScoreBoard()

def end_game():
    score.end()
    food.end_food()

running = True
while running:
    
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    
    
    if snake.head.distance(food.f) < 20: 
        snake.new_segment(color = food.color, shape= food.shape)
        food.move_food()
        score.add_score()
    
    # collision with wall
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        end_game()
        running = False
    
    for i in snake.segments[1:]:
        if snake.head.distance(i) < 15:
            end_game()
            running = False
            break
    
            

screen.mainloop()


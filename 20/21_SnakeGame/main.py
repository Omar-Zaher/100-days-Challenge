from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

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
snake.move()
while True:
    
    screen.update()
    
    
    if snake.head().distance(food.f) < 20: 
        food.move_food()
        snake.new_segment()


screen.mainloop()


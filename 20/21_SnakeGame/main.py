from turtle import Screen, Turtle
import time
from snake import Snake

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

snake.move()  # start the loop

screen.mainloop()


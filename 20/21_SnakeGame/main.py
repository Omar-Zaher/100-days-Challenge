from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from button import Button

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 600, height = 600)
screen.title("Snake")
start_x = 0
snake = Snake()
food = Food()
score = ScoreBoard()
button = Button()

# --- Game setup ---

def game():
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # start the loop
    

    def end_game():
        score.end()
        button.draw_button("Restart")


            
    speed = 0.2
    running = True
    while running:
        
        screen.update()
        time.sleep(speed)
        snake.move()
        
        
        if snake.head.distance(food.f) < 20: 
            snake.new_segment(color = food.color, shape= food.shape)
            food.move_food()
            score.add_score()
            speed -= 0.005
            
        
        # collision with wall
        
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            end_game()
            running = False
        
        for i in snake.segments[1:]:
            if snake.head.distance(i) < 15:
                end_game()
                running = False
                break

game()



def handle_click(x, y):
    if button.check_button_click(x,y):
        score.reset()
        snake.reset()
        button.reset()
        game()
        return True
    else:
        return False




screen.onscreenclick(handle_click)
       
        
        
        
game()
        
screen.mainloop()


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
restart = Button(x= -50, y = -50, width = 100, height = 25, lable = "Restart" )
start = Button(x= -50, y = 0, width = 100, height = 50, lable = "Start" )
easy = Button(x= -50, y = 50, width = 100, height = 25, lable = "Easy" )
medium = Button(x= -50, y = 0, width = 100, height = 25, lable = "Medium" )
hard = Button(x= -50, y = -50, width = 100, height = 25, lable = "Hard" )
buttons = [restart, start, easy, medium, hard]
dif = 1
speed = 0


# --- Game setup ---

def game():
    global speed
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # start the loop    

    running = True
    while running:
        
        screen.update()
        time.sleep(speed)
        snake.move()
        
        if dif == 1 :
            level_1()
        elif dif == 2:
            level_2()
        elif dif == 3:
            level_3()
            
        # collision with wall
        
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            running = False
            end_game()
        
        for i in snake.segments[1:]:
            if snake.head.distance(i) < 15:
                end_game()
                running = False
                break
        screen.onscreenclick(handle_click)


def handle_click(x, y):
    global speed
    global dif
    for button in buttons:
        if button.check_button_click(x,y):
            if button.lable == "Restart":
                # Check the current difficulty to reset to the correct speed
                if dif == 1:
                    speed = 0.2
                elif dif == 2:
                    speed = 0.15
                elif dif == 3:
                    speed = 0.1 # Standard start for Hard
                
                score.reset()
                snake.reset()
                button.reset()
                game()

            elif button.lable == "Start":
                button.reset()
                difficulty()

            elif button.lable == "Easy":
                speed = 0.2
                button.reset()
                dif = 1
                game()

            elif button.lable == "Medium":
                speed = 0.15
                button.reset()
                dif = 2
                game()

            elif button.lable == "Hard":
                speed = 0.1 
                button.reset()
                dif = 3 
                game()                  
                
def difficulty():
    easy.draw_button()
    medium.draw_button()
    hard.draw_button()
    

def end_game():
    score.end()
    restart.draw_button()
    
def level_1():
    global speed
    if snake.head.distance(food.f) < 20: 
            snake.new_segment(color = food.color, shape= food.shape)
            food.move_food()
            score.add_score()
            if speed > 0.1:
                speed -= 0.005
                
def level_2():
    global speed
    if snake.head.distance(food.f) < 20: 
            snake.new_segment(color = food.color, shape= food.shape)
            food.move_food()
            score.add_score()
            if speed > 0.06:
                speed -= 0.008
                
def level_3():
    global speed
    if snake.head.distance(food.f) < 20: 
            snake.new_segment(color = food.color, shape= food.shape)
            food.move_food()
            score.add_score()
            if speed > 0.04:
                speed -= 0.01


start.draw_button()
screen.onscreenclick(handle_click) 

       
       
screen.mainloop()


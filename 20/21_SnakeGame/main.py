# ========================================================================== Snake Game ==========================================================================

# ------- Imports -------
from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from button import Button

# --- Screen Setup ---
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)  # Turns off animation for instant drawing

# --- Game Objects ---
snake = Snake()
food = Food()
score = ScoreBoard()

# --- UI Text Turtle (For "Welcome" text) ---
ui = Turtle()
ui.hideturtle()
ui.penup()
ui.color("white")

# --- Buttons ---
# Start Button
start = Button(x=-50, y=-50, width=100, height=50, lable="Start")

# Difficulty Buttons (Spread out vertically)
easy = Button(x=-50, y=50, width=100, height=30, lable="Easy")
medium = Button(x=-50, y=0, width=100, height=30, lable="Medium")
hard = Button(x=-50, y=-50, width=100, height=30, lable="Hard")

# Ending buttons
restart = Button(x=-50, y=-60, width=100, height=25, lable="Restart")
main_menu = Button(x=-60, y=-100, width=120, height=30, lable="Main Menu")

# --- Global Variables ---
dif = 1
speed = 0.1
game_state = "welcome" 

# --- Logic Functions ---

def show_welcome_screen():
    global game_state
    game_state = "welcome"
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)
    
    # Draw Title
    ui.clear()
    ui.goto(0, 50)
    ui.write("SNAKE", align="center", font=("Courier", 40, "bold"))
    
    # Draw Start Button
    start.draw_button()
    screen.update()
    
    # Re-setup because screen.clear() wipes everything
    screen.listen()
    screen.onscreenclick(handle_click)

# --- Difficulty Selection Screen ---
def show_difficulty_screen():
    global game_state
    game_state = "select"
    
    # Clear the "SNAKE" title and Start button
    ui.clear()
    start.reset() 
    
    # Draw Menu
    ui.goto(0, 100)
    ui.write("Select Difficulty", align="center", font=("Courier", 20, "normal"))
    
    easy.draw_button()
    medium.draw_button()
    hard.draw_button()
    screen.update()

# --- Game Loop Functions ---
def start_game_loop():
    global game_state, speed
    game_state = "playing"
    
    reset_game_objects()
    # Clear Menu
    ui.clear()
    easy.reset()
    medium.reset()
    hard.reset()
    
    # Re-bind keys (screen.clear removes them)
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    
    running = True
    while running:
        screen.update()
        time.sleep(speed)
        snake.move()
        
        # Difficulty Logic
        if dif == 1: level_1()
        elif dif == 2: level_2()
        elif dif == 3: level_3()
            
        # Wall Collision
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            running = False
            end_game()
        
        # Tail Collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                running = False
                end_game()
                
        # We need to keep listening for clicks (though usually ignored during gameplay)
        screen.onscreenclick(handle_click)

# --- End Game Function ---
def end_game():
    global game_state
    game_state = "game_over"
    score.end()
    restart.draw_button()
    main_menu.draw_button()
    screen.update()

# --- Click Handlers for Each Game State ---
def handle_welcome_click(x, y):
    if start.check_button_click(x, y):
        show_difficulty_screen()

def handle_difficulty_click(x, y):
    global speed, dif
    if easy.check_button_click(x, y):
        dif = 1
        speed = 0.2
        start_game_loop()
    elif medium.check_button_click(x, y):
        dif = 2
        speed = 0.15
        start_game_loop()
    elif hard.check_button_click(x, y):
        dif = 3
        speed = 0.1
        start_game_loop()

def handle_game_over_click(x, y):
    global speed, dif
    if restart.check_button_click(x, y):
        restart.reset()
        score.reset()
        snake.reset()
        food.end_food()
        
        # Reset speed based on previous difficulty
        if dif == 1: speed = 0.2
        elif dif == 2: speed = 0.15
        elif dif == 3: speed = 0.1
        
        start_game_loop()
    elif main_menu.check_button_click(x, y):
        # Hide existing visuals
        restart.reset()
        main_menu.reset()
        snake.reset()
        food.end_food()
        score.reset()

        # Return to welcome screen
        show_welcome_screen()

# --- Click Handler ---
def handle_click(x, y):
    global game_state
    
    if game_state == "welcome":
        handle_welcome_click(x, y)
    elif game_state == "select":
        handle_difficulty_click(x, y)
    elif game_state == "game_over":
        handle_game_over_click(x, y)

# --- Level Physics ---

def level_1():
    global speed
    if snake.head.distance(food.f) < 20: 
        snake.new_segment(color=food.color, shape=food.shape)
        food.move_food()
        score.add_score()
        if speed > 0.1: speed -= 0.002
                
def level_2():
    global speed
    if snake.head.distance(food.f) < 20: 
        snake.new_segment(color=food.color, shape=food.shape)
        food.move_food()
        score.add_score()
        if speed > 0.05: speed -= 0.005
                
def level_3():
    global speed
    if snake.head.distance(food.f) < 20: 
        snake.new_segment(color=food.color, shape=food.shape)
        food.move_food()
        score.add_score()
        if speed > 0.035: speed -= 0.008

# --- Reset Game Objects ---       
def reset_game_objects():
    global snake, food, score
    snake = Snake()
    food = Food()


# --- Start Program ---
show_welcome_screen()
screen.mainloop()
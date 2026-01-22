# =========================================================== Crossy Turtle ===========================================================

# --- Imports ---
from turtle import Screen, Turtle
import rectangle as r
import time
import random
from player import Player
from welcome import Start
from scoreboard import ScoreBoard

# --- Screen Setup ---
width = 600
height = 600
screen = Screen()
screen.title("Crossy Turtle")
screen.bgcolor("black")
screen.setup(width=width, height=height)
screen.tracer(0)

# --- Configuration ---
LANE_HEIGHT = 40
START_Y = -300
TOTAL_LANES = height // LANE_HEIGHT # How many strips fit on screen

# --- World Generation ---
current_y = START_Y

road_lanes = [] # To keep track of where the road lanes are
for i in range(TOTAL_LANES):

    # Decide lane type (grass or road)
    if i < 3:
        lane_type = "grass"
    elif i < 5:
        lane_type = "road"
    elif i < 7:
        lane_type = "grass"
    elif i < 10:
        lane_type = "road"
    elif i < 11:
        lane_type = "grass"
    elif i < 13:
        lane_type = "road"
    else:
        lane_type = "grass"

    # Grass
    if lane_type == "grass":

        strip = r.Rectangle(x=-300, y=current_y, width=600, height=LANE_HEIGHT, color="#DAB055")
        strip.draw()
        
        # Add random dirt patches
        for dash_x in range(30): 
            dash = r.Rectangle(random.randrange(-300,300), y=current_y + random.randrange(1,20), width=random.randrange(1,5), height=random.randrange(1,5), color="#543d0c")
            dash.draw()
        
    # Road
    elif lane_type == "road":

        strip = r.Rectangle(x=-300, y=current_y, width=600, height=LANE_HEIGHT, color="#34495e")
        strip.draw()
        
        # Add lane divider dashes
        for dash_x in range(-280, 300, 60): 
            dash = r.Rectangle(x=dash_x, y=current_y + 15, width=25, height=5, color="white")
            dash.draw()
        
        road_lanes.append(current_y + 20)

    # Move up for the next loop
    current_y += LANE_HEIGHT

# --- Adding Cars ---
cars = []  
for i in road_lanes:
    car = r.Car(i)
    cars.append(car)
    
for i in road_lanes:
    car = r.Car(i)
    cars.append(car)

# --- Game Variables ---
speed = 2 
level = ScoreBoard(-250,250)
level.update_score() 

# --- Main Game Loop ---  
def game_loop():
    global p1, gameover, speed
    game_over = False

    # Move Cars/ Check for Collisions
    for car in cars:
        car.move(speed) 
        if car.c.distance(p1.p) < 20 :
            game_over = True 
            level.end()
        elif p1.p.ycor() > 250:
            level.add_score()
            p1.reset()
            speed += 1
               
            
    screen.update()
    if game_over == False:
    
        screen.ontimer(game_loop, 20) # Continue the game loop


# --- Player Setup ---
p1 = Player()
screen.listen()
screen.onkey(p1.up, "Up")
screen.onkey(p1.down, "Down")
screen.onkey(p1.right, "Right")
screen.onkey(p1.left, "Left")

# --- Start the Game ---
game_loop()

screen.update()
screen.mainloop()
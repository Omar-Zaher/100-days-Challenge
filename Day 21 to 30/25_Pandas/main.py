# ============================================================== U.S. States Game ============================================

# ---- Imports -----
import turtle as t
import pandas

# ----- Screen Setup ----------
turtle = t.Turtle()
screen = t.Screen()
screen.title("U.S. states game")
image = "./25_Pandas/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

# ------- Creating list ----------
data = pandas.read_csv("./25_Pandas/50_states.csv")
states = data.state.to_list()

# -------- Game loop ------------
game = 0
while game < 50:
    guess = screen.textinput(title= f"{game}/50 States Guessed", prompt= "Name a State").title()
    
    if guess == "Exit":
        break
    
    # if user input is a state
    if guess in states:
        state = t.Turtle()
        state.hideturtle()
        state.penup()
        row = data[data.state == guess].iloc[0] # x and y cords for the state I can also use (.item())
        state.goto(int(row.x),int(row.y))
        state.write(guess, align= "center", font= ("Arial", 12, "normal") )
        screen.update() 
        states.remove(guess) 
        game += 1 
     
    else:
        continue

missing_states = pandas.DataFrame(states)
missing_states.to_csv("Missing States.csv")

print (f"Number of states you still have to learn: {len(states)}")
# =================================================================================================================
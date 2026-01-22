# ====================================================== Pomodoro =====================================================

# ---- Imports ----
import tkinter as tk
import random
from pygame import mixer

# ---- Constants ----
WORK_DURATION = 25 * 60  # 25 minutes
BREAK_DURATION = 5 * 60   # 5 minutes
LONG_BREAK_DURATION = 15 * 60  # 15 minutes
CYCLES_BEFORE_LONG_BREAK = 4

# Colors
MAIN_COLOR = "#6994B0"
DARK_COLOR = "#0A2E50"
ORANGE = "#F39C12"
WHITE = "#fcfcf7"
GREY = "#adbed7"



# ----- Screen setup ---

window = tk.Tk()
window.title("Pomodoro")
window.geometry("1000x700")
window.configure(bg = MAIN_COLOR)

canvas = tk.Canvas(width = 1000, height = 700,bg = MAIN_COLOR, highlightthickness = 0)
canvas.pack()

# Create the bubbles in the background
for _ in range(0,40):
    r = random.randint(5,8)
    x =random.randint(2,900)
    y =random.randint(2,700)
    
    x1,y1 = (x - r), (y - r)
    x2,y2 = (x + r), (y + r)
    canvas.create_oval(x1, y1, x2, y2, fill=MAIN_COLOR, outline=ORANGE, width=1)

# Setting up the Canvas
canvas.create_oval(300,150,700,550,fill=MAIN_COLOR, outline=ORANGE, width=25 )
title_text = canvas.create_text(500,70, text="Pomodoro", font=("Arial", 75, "bold"), fill=WHITE)
timer_text = canvas.create_text(500, 335, text="00:00", font=("Arial", 50, "bold"), fill=WHITE)
timer_text2 = canvas.create_text(500, 385, text="FOCUS SESSION", font=("Arial",15,"bold"), fill=WHITE)
progress_arc = canvas.create_arc(
    300,150,700,550,
    start=90,         
    extent=359,          
    style="arc",
    outline= GREY,
    width=26
)

# ============================================ Functions ================================================
# ------ Buttons Functions --------
running = None
mode = None
# Start
def start():
    global running, mode 
    canvas.itemconfig(timer_text2, text = "FOCUS SESSION")
    if running:
        window.after_cancel(running)
    mode = WORK_DURATION
    countdown(WORK_DURATION)
    

# short break
def short_break():
    global running, mode 
    canvas.itemconfig(timer_text2, text = "BREAK SESSION") 
    if running:
        window.after_cancel(running)
    mode = BREAK_DURATION
    countdown(BREAK_DURATION)
    
    
# Long break
def long_break():
    global running, mode 
    canvas.itemconfig(timer_text2, text = "LONG BREAK") 
    if running:
        window.after_cancel(running)
    mode = LONG_BREAK_DURATION
    countdown(LONG_BREAK_DURATION)
    


# ------ Countdown --------

def countdown(count):
    global running, mode 
    minute = int(count // 60)
    sec = int(count % 60)
    extent = 359 * count/mode
    
    canvas.itemconfig(timer_text, text = f"{minute:02d}:{sec:02d}")
        
    if count > 0:
        running = window.after(1000, countdown, count - 1)
        canvas.itemconfig(progress_arc, extent = extent)
        
    elif mode == "work":
        canvas.itemconfig(progress_arc, extent = 359)
        play_alarm()
        canvas.itemconfig(timer_text, text = "Take a break")
        
        
    else:
        canvas.itemconfig(progress_arc, extent = 359)
        play_alarm()
        canvas.itemconfig(timer_text, text = "Its time to lock in!")

# ----- Alarm -------
mixer.init()        
def play_alarm():
    mixer.music.load("alarm.mp3") 
    mixer.music.play()

# ======================================================= Buttons ===========================================

# init font
button_font = ("Arial", 11, "bold")

# Start Button
start_button = tk.Button(
    text="START",
    font=button_font,
    bg=WHITE,
    fg=MAIN_COLOR,
    activebackground=GREY,
    activeforeground=WHITE,
    padx=20,            # Horizontal internal padding
    pady=10,            # Vertical internal padding
    borderwidth=0,
    relief="flat",
    cursor="hand1",
    command= start
)

# Short Break Button 
short_btn = tk.Button(
    text="SHORT BREAK",
    font=button_font,
    bg=GREY,
    fg=WHITE,
    activebackground=WHITE,
    activeforeground=GREY,
    padx=20,
    pady=10,
    borderwidth=0,
    relief="flat",
    cursor="hand1",
    command = short_break
    
)

# Long Break Button
long_btn = tk.Button(
    text="LONG BREAK",
    font=button_font,
    bg=GREY,
    fg=WHITE,
    activebackground=WHITE,
    activeforeground=GREY,
    padx=20,
    pady=10,
    borderwidth=0,
    relief="flat",
    cursor="hand1",
    command = long_break
)

# --- Placing them on the Canvas (Centered) ---

canvas.create_window(500, 620, window=start_button)   
canvas.create_window(350, 620, window=short_btn)     
canvas.create_window(650, 620, window=long_btn)     

window.mainloop()

# ======================================================================================================================
# ======================================================== Flashcard App ========================================================

# ------ Imports ----------
import tkinter as tk
from tkinter import PhotoImage
import pandas as pd
import random

# ------ Color Palete ------
TEXT_COLOR = "#FFFFFF"
BG_COLOR = "#0B132B"
FLASHCARD_COLOR = "#1C2541"
FLASHCARD_BG_COLOR = "#3A506B"
FONT = ("Arial", 20, "bold")


# ----- Screen Setup ----------
window = tk.Tk()
window.title("Flashcard App")
window.geometry("800x700")
window.config(bg=BG_COLOR)

# ----- Functions ---------
is_word_visible = True
score = 0

# Flip the card to show word/definition
def flip_card():
    global is_word_visible
    if is_word_visible:
        definition.lift()
    else:
        word.lift()
    is_word_visible = not is_word_visible

# Update score and load next card (for correct answer)
def score_update():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    next_card()

# Load the next flashcard   
def next_card():
    global is_word_visible
    data = pd.read_csv("./30_Flashcard/data/french_words.csv")
    random_row = data.sample().iloc[0] # Get a random row
    french_word = random_row["French"]
    english_word = random_row["English"]
    word.config(text=french_word)
    definition.config(text=english_word)
    word.lift() # Show the word side
    is_word_visible = True

# ---- Score Label -----
score_label = tk.Label(
    window,
    text="Score: 0",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 16, "bold"),
)
score_label.pack(pady=(20, 0))

# ----- Flashcard Setup ------
# Flashcard Frame
card_frame = tk.Frame(window, bg=BG_COLOR, width=1000, height=500)
card_frame.pack()
card_frame.pack_propagate(False)

# Flashcard Buttons (Word and Definition)
word = tk.Button(
    card_frame,
    text="Flashcard",
    bg=FLASHCARD_COLOR,
    fg=TEXT_COLOR,
    font=FONT,
    width=40,
    height=10,
    bd=0,
    activebackground=FLASHCARD_BG_COLOR,
    activeforeground=TEXT_COLOR,
    relief="flat",
    command=flip_card,
)
word.place(relx=0.5, rely=0.5, anchor="center")

definition = tk.Button(
    card_frame,
    text="Definition",
    bg=FLASHCARD_BG_COLOR,
    fg=TEXT_COLOR,
    font=FONT,
    width=40,
    height=10,
    activebackground=FLASHCARD_BG_COLOR,
    activeforeground=TEXT_COLOR,
    bd=0,
    relief="flat",
    command=flip_card,
)

definition.place(relx=0.5, rely=0.5, anchor="center")
definition.lower() # Start with word side visible


# ----- Right and Wrong Buttons ------
button_frame = tk.Frame(window, bg=BG_COLOR, width=1000, height=500)
button_frame.pack(pady=(0, 50))
button_frame.pack_propagate(False)

right_img = PhotoImage(file="./30_Flashcard/imgs/right.png")
right = right_img.subsample(2, 2)
right_button = tk.Button(
    button_frame,
    image=right,
    bd=0,
    relief="flat",
    highlightthickness=0,
    activebackground=BG_COLOR,
    command=score_update,
)

right_button.place(relx=0.6, rely=0.5, anchor="w")


wrong_img = PhotoImage(file="./30_Flashcard/imgs/wrong.png")
wrong = wrong_img.subsample(2, 2)
wrong_button = tk.Button(
    button_frame,
    bd=0,
    relief="flat",
    highlightthickness=0,
    image=wrong,
    activebackground=BG_COLOR,
    command=next_card,
)
wrong_button.place(relx=0.4, rely=0.5, anchor="e")

# ----- Run the App ------
next_card()  # Load the first card
window.mainloop()

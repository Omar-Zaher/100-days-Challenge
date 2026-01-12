# ================================================= Kanye Quotes Notifier =================================================

# ----- Imports -----
import tkinter as tk
import requests

# ----- Functions -----
def get_quote():
    try:
        response = requests.get(
            "https://api.kanye.rest/",
            timeout=5
        )
        response.raise_for_status()

        quote = response.json()["quote"]
        canvas.itemconfig(quote_text, text=quote)

    except requests.exceptions.RequestException:
        canvas.itemconfig(
            quote_text,
            text="Too many requests \nTry again in a moment."
        )

# ----- UI Setup -----
window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=300, height=414)
background_img = tk.PhotoImage(
    file="./32_ISS overhead notifier/kanye-quotes-start/background.png"
)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)


# Button
kanye_img = tk.PhotoImage(
    file="./32_ISS overhead notifier/kanye-quotes-start/kanye.png"
)
kanye_button = tk.Button(image=kanye_img, highlightthickness=0, command=get_quote,)
kanye_button.grid(row=1, column=0)


window.mainloop()

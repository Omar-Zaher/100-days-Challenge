# ====================================================== Password Manager ===============================================


# -------- Imports -------
import tkinter as tk
from tkinter import messagebox
from generator import Generator
import pyperclip 
import json

# ---- Color Palete ------

GREY = "#8d8f90"
BLUE = "#134c78"
LIGHTBLUE = "#4e7799"
WHITE = "#ecedec"
font = ("Arial", 12)

# ----- Screen Setup ----------
window = tk.Tk()
gen = Generator()
window.title("Password Manager")
window.geometry("600x400")
window.config(bg= WHITE)

canvas = tk.Canvas(window, width=600, height=200, bg= WHITE, highlightthickness= 0)
canvas.pack()

# ----- Adding logo -------
image = tk.PhotoImage(file = "logo.png")
img = image.subsample(2, 2) # Make logo smaller so it fits 
logo = canvas.create_image(300,100,image = img)


# ------ Functions ---------
def generate ():
    text = gen.pass_generate() # generates a random Password
    password.delete(0, tk.END) # clear the password if there is anything
    password.insert(0, text) # inserting the new password
    
    
    
def search ():
    app1 = app.get().title()
    try:
        with open("Passwords.json","r") as file:
            data = json.load(file)
            message = messagebox.showinfo(message=f"Your info for {app1}:\n{data[app1]}")
    except KeyError:
        message = messagebox.showinfo(message = f"Sorry this app ({app1}) wasn't found")
        
    
def add() :
    app1 = app.get().title()
    email1 = email.get()
    password1 = password.get()
    
    if app1  and email1 and password1 :
        
        pyperclip.copy(password1) # Copy Password to clipboard
        
        new_data = {
            app1 : {
                "Email": email1,
                "Password": password1
            }
        }
        
        is_ok = messagebox.askokcancel(title="Website", message= f"Do you want to add these inputs\nApp: {app1}\nEmail: {email1}\nPassword: {password1}")
        
        if is_ok:
            try:
                with open("Passwords.json", "r") as file:
                    data = json.load(file)  
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:    
                with open("Passwords.json", "w") as file:
                    json.dump(data, file, indent = 4)
                
            # Clear everything after adding
            app.delete(0, tk.END)
            email.delete(0, tk.END)
            password.delete(0, tk.END)
    
    # If there is an empty field         
    else:
        messagebox.showerror(message= "Please Fill in All Info!")
    
# ===================================================== Layout ===========================================

# ------- App -----------
app_text = tk.Label(text="App", font= font)
app_text.place(x=100, y=195)

app = tk.Entry()
app.place (x=200, y=200, width= 200)
app.focus() # focusing on the app Entry so the user can start typing on spot

# ------ Search ---------

pass_button = tk.Button(text="Search", bg= BLUE, foreground=WHITE, command=search)
pass_button.place (x=420, y=195, width= 80)


# -------- Email ----------
email_text = tk.Label(text="Email", font= font)
email_text.place(x=100, y=245)

email = tk.Entry()
email.place (x=200, y=250, width= 300)


# ----- Password --------
password_text = tk.Label(text="Password", font= font)
password_text.place(x=100, y=295)


password = tk.Entry()
password.place (x=200, y=300, width= 200)

pass_button = tk.Button(text="Generate", bg= GREY, foreground=WHITE, command=generate)
pass_button.place (x=420, y=295, width= 80)


# ----- Add --------
add_button = tk.Button(text="Add", bg= BLUE, foreground=WHITE, command= add)
add_button.place (x=200, y=345, width= 300)

# Main loop
window.mainloop()

# =================================================================================================================
# ==================================================== Converter: Miles to Km ====================================================

# --- imports ---
import tkinter as tk

# --- main window ---
window = tk.Tk()
window.title("Converter")
window.geometry("400x300")

# --- functions ---
def update_km(*arg):
    # Miles to Km
    if values_var.get() == 'miles':
        try:
            miles_val = miles_var.get() # Entry to string
            if miles_val == "":
                km_value.config(text="0")
                return
            
            new_value = float(miles_val) * 1.609
            km_value.config(text=f"{new_value:.2f}") # Display with 2 decimal places
        except ValueError:
            km_value.config(text="Error")
    
    # Pounds to Kg
    elif values_var.get() == 'pounds':
        try:
            pounds_val = miles_var.get() # Entry to string
            if pounds_val == "":
                km_value.config(text="0")
                return
            
            new_value = float(pounds_val) * 0.453592
            km_value.config(text=f"{new_value:.2f}") # Display with 2 decimal places
        except ValueError:
            km_value.config(text="Error")

#  Update second unit label
def update_second_unit(*arg):
    selected_unit = values_var.get()
    if selected_unit == 'miles':
        km.config(text="km")
    elif selected_unit == 'pounds':
        km.config(text="kg")


# --- UI setup ---
# Title
title = tk.Label(text="Units Converter",font=("Arial", 21, "bold"))
title.grid(column= 1, row = 0,padx= (50,0),pady= (50,0))


# Miles
miles_var = tk.StringVar() # To track changes in Entry
miles_var.trace_add("write", update_km) # Call update_km on change

user_input = tk.Entry(textvariable=miles_var)
user_input.grid(column= 1, row = 1,pady=(30,0))


values_var = tk.StringVar(value='miles') # Default value
values_var.trace_add("write", update_second_unit) # Call update_km on change


# Spinbox for unit selection
values = ('miles', 'pounds')
spinbox_string = tk.Spinbox(values=values, textvariable=values_var, width= 10)
spinbox_string.grid(column= 2, row = 1,pady=(30,0))


# Kelometers
km_value = tk.Label(text= 0,font=("Arial", 12), pady= 30)
km_value.grid(column= 1, row = 2)

km = tk.Label(text="km",font=("Arial", 12), pady= 30)
km.grid(column= 2, row = 2)

# --- main loop ---    
window.tk.mainloop()

# ========================================================================================================
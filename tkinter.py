# ================================
# PERSONAL BIO FORM
# ================================
# Topics:
# What is Tkinter? | Creating a Tkinter Window
# Label and Button Widgets
# Entry, Text, and Frame Widgets
# Tkinter Grid
 
from tkinter import *
 
# ------------------------------------------------
# PART 1 - CREATE A TKINTER WINDOW
# ------------------------------------------------
 
window = Tk()
window.title("Personal Bio Form")
window.geometry("450x450")
window.config(bg="lavender")
 
 
# ------------------------------------------------
# PART 2 - CREATE A FRAME
# ------------------------------------------------
 
form_frame = Frame(window, bg="white", padx=20, pady=20)
form_frame.grid(row=0, column=0, padx=30, pady=30)
 
 
# ------------------------------------------------
# PART 3 - ADD LABEL WIDGETS
# ------------------------------------------------
 
title_label = Label(
    form_frame,
    text="Personal Bio Form",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="purple",
    width=25
)
title_label.grid(row=0, column=0, columnspan=2, pady=10)
 
name_label = Label(form_frame, text="Name:", bg="white", font=("Arial", 11))
name_label.grid(row=1, column=0, sticky="w", pady=5)
 
age_label = Label(form_frame, text="Age:", bg="white", font=("Arial", 11))
age_label.grid(row=2, column=0, sticky="w", pady=5)
 
hobby_label = Label(form_frame, text="Hobby:", bg="white", font=("Arial", 11))
hobby_label.grid(row=3, column=0, sticky="w", pady=5)
 
about_label = Label(form_frame, text="About Me:", bg="white", font=("Arial", 11))
about_label.grid(row=4, column=0, sticky="nw", pady=5)
 
 
# ------------------------------------------------
# PART 4 - ADD ENTRY AND TEXT WIDGETS
# ------------------------------------------------
 
name_entry = Entry(form_frame, width=30)
name_entry.grid(row=1, column=1, pady=5)
 
age_entry = Entry(form_frame, width=30)
age_entry.grid(row=2, column=1, pady=5)
 
hobby_entry = Entry(form_frame, width=30)
hobby_entry.grid(row=3, column=1, pady=5)
 
about_text = Text(form_frame, width=23, height=5)
about_text.grid(row=4, column=1, pady=5)
 
 
# ------------------------------------------------
# PART 5 - BUTTON FUNCTION
# ------------------------------------------------
 
def show_bio():
    name = name_entry.get()
    age = age_entry.get()
    hobby = hobby_entry.get()
    about = about_text.get("1.0", END).strip()
 
    result_label.config(
        text="Hello, " + name + "!"
             "Age: " + age + ""
             "Hobby: " + hobby + ""
             "About: " + about
    )
 
 
# ------------------------------------------------
# PART 6 - ADD BUTTON WIDGET
# ------------------------------------------------
 
submit_button = Button(
    form_frame,
    text="Show My Bio",
    bg="purple",
    fg="white",
    font=("Arial", 11, "bold"),
    command=show_bio
)
submit_button.grid(row=5, column=0, columnspan=2, pady=15)
 
 
# ------------------------------------------------
# PART 7 - DISPLAY RESULT
# ------------------------------------------------
 
result_label = Label(
    form_frame,
    text="Your bio will appear here.",
    bg="lightyellow",
    fg="black",
    width=35,
    height=5,
    wraplength=300,
    justify="left"
)
result_label.grid(row=6, column=0, columnspan=2, pady=10)
 
 
# ------------------------------------------------
# PART 8 - RUN THE WINDOW
# ------------------------------------------------
 
window.mainloop()

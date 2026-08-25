# ================================
# MY PHOTO ALBUM
# ================================
# Topics:
# The Pillow (PIL) Library | Adding Images in Tkinter
# Messagebox Widget | Messagebox Function Types
# Toplevel Window
 
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
 
 
# ------------------------------------------------
# PART 1 - CREATE THE MAIN TKINTER WINDOW
# ------------------------------------------------
 
window = Tk()
window.title("My Photo Album")
window.geometry("450x500")
window.config(bg="lavender")
 
 
# ------------------------------------------------
# PART 2 - ADD A TITLE LABEL
# ------------------------------------------------
 
title_label = Label(
    window,
    text="My Photo Album",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="purple",
    width=25
)
title_label.pack(pady=15)
 
 
# ------------------------------------------------
# PART 3 - ADD IMAGE USING PIL
# ------------------------------------------------
# Make sure an image named "koe.jpg" is saved in the same folder.
 
image_file = Image.open("koe.jpg")
image_file = image_file.resize((300, 200))
 
photo = ImageTk.PhotoImage(image_file)
 
image_label = Label(window, image=photo, bg="lavender")
image_label.pack(pady=10)
 
 
# ------------------------------------------------
# PART 4 - MESSAGEBOX FUNCTION
# ------------------------------------------------
 
def show_reaction():
    messagebox.showinfo(
        "Photo Reaction",
        "This is a beautiful memory!"
    )
 
 
# ------------------------------------------------
# PART 5 - TOPLEVEL WINDOW FUNCTION
# ------------------------------------------------
 
def open_photo_details():
    details_window = Toplevel(window)
    details_window.title("Photo Details")
    details_window.geometry("350x250")
    details_window.config(bg="lightyellow")
 
    heading = Label(
        details_window,
        text="Photo Details",
        font=("Arial", 16, "bold"),
        bg="lightyellow",
        fg="purple"
    )
    heading.pack(pady=15)
 
    details = Label(
        details_window,
        text="Photo Name: My Favourite Memory\n"
             "Category: Personal Album\n"
             "Description: A special photo saved in my album.",
        font=("Arial", 11),
        bg="lightyellow",
        justify="left"
    )
    details.pack(pady=10)
 
    close_button = Button(
        details_window,
        text="Close",
        bg="purple",
        fg="white",
        command=details_window.destroy
    )
    close_button.pack(pady=15)
 
 
# ------------------------------------------------
# PART 6 - ADD BUTTON WIDGETS
# ------------------------------------------------
 
reaction_button = Button(
    window,
    text="React to Photo",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=show_reaction
)
reaction_button.pack(pady=10)
 
details_button = Button(
    window,
    text="View Photo Details",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=open_photo_details
)
details_button.pack(pady=10)
 
 
# ------------------------------------------------
# PART 7 - RUN THE WINDOW
# ------------------------------------------------
 
window.mainloop()
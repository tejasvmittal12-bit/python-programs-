# my-photo-album.py
# Activity: My Photo Album
# Lesson: Tkinter Widgets | Grade 4-6

# PART 1 - Import libraries and set up the main window
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title('My Photo Album')
window.geometry('400x420')

# PART 2 - Add a title label and display an image
title = Label(window, text='My Photo Album', fg='white', bg='purple', width=40)
title.pack(pady=10)
img_file = Image.open('img.jfif')
img_file = img_file.resize((300, 180))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window, image=photo)
pic.pack(pady=5)

# PART 3 - Create a function to show a message box
def show_message():
    messagebox.showinfo('Great!', 'You clicked the photo!')
msg_btn = Button(window, text='Click to React', bg='blue', fg='white', command=show_message)
msg_btn.pack(pady=5)

# PART 4 - Create a function to open a new window with photo details
def show_details():
    top = Toplevel()
    top.title('Photo Details')
    top.geometry('200x120')
    info = Label(top, text='Taken on: 1 June 2025')
    info.pack(pady=10)
    place = Label(top, text='Location: My Garden')
    place.pack()
    top.mainloop()
details_btn = Button(window, text='See Details', bg='green', fg='white', command=show_details)
details_btn.pack(pady=5)

# PART 5 - Run the main window loop
window.mainloop()
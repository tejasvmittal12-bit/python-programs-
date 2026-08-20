from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("koe.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)
label1 = Label(root, text="Hey User! Welcome to Denomination counter Application", bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root, text="Lets Get Started!", command=msg, bg='brown', fg='white')
button1.place(x=260 , y=360)
def topwin():
    top = Toplevel()
    top.title("Denomination calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")

    label= Label(top, text="Enter Total Amount", bg= 'lightgrey')
    Entry = Entry(top)
    lbl = Label(top, text= "Here are numbers of notes for each denomination", bg = 'lightgrey')

    l1 = Label(top, text="2000", bg='lightgrey')
    l2 = Label(top, text="500", bg='lightgrey')
    l3 = Label(top, text="100", bg='lightgrey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator(): 
        try:
            global amount
            amount = int(Entry.get())
            note_2000 = amount // 2000
            amount %= 2000
            note_500 = amount // 500
            amount %= 500
            note_100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note_2000))
            t2.insert(END, str(note_500))
            t3.insert(END, str(note_100))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    btn = Button(top, text="Calculate", command=calculator, bg='brown', fg='white')

    label.place(x=230, y=50)
    Entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()
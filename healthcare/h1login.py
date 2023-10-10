from tkinter import *
import sqlite3
import os
import sys
from tkinter import messagebox

root = Tk()
root.geometry('500x350')
root.title("Secured Data")


Un = StringVar()
Pw = StringVar()

def back():
    root.destroy()
    os.system('python main.py')

def login():
    un = Un.get()
    pw = Pw.get()
    if un == "" :
        messagebox.showinfo("msg","Enter Username")
    else:
        if pw == "":
            messagebox.showinfo("msg", "Enter Password")
        else:
            if un == "admin" and pw == "admin":
                root.destroy()
                os.system('python doctordet.py')


label_0 = Label(root, text="Login", width=20, font=("bold", 20))
label_0.place(x=90, y=53)
label_4 = Label(root, text="Username", width=20, font=("bold", 10))
label_4.place(x=80, y=150)
entry_5 = Entry(root, textvar=Un)
entry_5.place(x=240, y=150)
label_5 = Label(root, text="Password", width=20, font=("bold", 10))
label_5.place(x=80, y=200)
entry_6 = Entry(root, textvar=Pw, show="*")
entry_6.place(x=240, y=200)
Button(root, text='Login', width=20, bg='brown', fg='white', command=login).place(x=120, y=270)
Button(root, text='Cancel', width=20, bg='brown', fg='white', command=back).place(x=280, y=270)

root.mainloop()

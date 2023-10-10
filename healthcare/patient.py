from tkinter import *
import sqlite3
from tkinter import messagebox

import os
from PIL import ImageTk, Image
root = Tk()
root.geometry('1366x768')
root.title("Registration Form")
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.jpg')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
Fullname = StringVar()
Email = StringVar()
Contact = StringVar()
Un = StringVar()
Pw = StringVar()

def cancel():
    root.destroy()
    os.system('python Main.py')

def database():
    name1 = Fullname.get()
    email = Email.get()
    contact = Contact.get()
    un = Un.get()
    pw = Pw.get()

    if name1=="":
        messagebox.showinfo("Enter Name")
    else:
        if email == "":
            messagebox.showinfo("Enter Email")
        else:
             conn = sqlite3.connect('Form.db')
             with conn:
                cursor = conn.cursor()
                cursor.execute(
                'CREATE TABLE IF NOT EXISTS register (Fullname TEXT,Email TEXT,Contact TEXT,Un TEXT,Pw TEXT)')
                cursor.execute('INSERT INTO register (FullName,Email,Contact,Un,Pw) VALUES(?,?,?,?,?)',
                 (name1, email, contact, un, pw,))
                conn.commit()
                messagebox.showinfo("Record Saved")


label_0 = Label(root, justify=LEFT, bg='brown', text="Registration Here..", width=15, font=("bold", 20))
label_0.place(x=100, y=280)


label_1 = Label(root, text="FullName", bg='brown', justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=400, y=300)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=550, y=300)

label_2 = Label(root, text="Email", bg='brown', justify=LEFT, width=20, font=("bold", 10))
label_2.place(x=400, y=350)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=550, y=350)

label_3 = Label(root, text="Contact",bg='brown',justify=LEFT, width=20, font=("bold", 10))
label_3.place(x=400, y=400)

entry_3 = Entry(root, textvar=Contact)
entry_3.place(x=550, y=400)

label_4 = Label(root, text="Username", bg='brown',justify=LEFT, width=20, font=("bold", 10))
label_4.place(x=400, y=450)

entry_5 = Entry(root, textvar=Un)
entry_5.place(x=550, y=450)

label_5 = Label(root, text="Password",bg='brown', justify=LEFT, width=20, font=("bold", 10))
label_5.place(x=400, y=500)
def gkey():
    import random

    print(random.randint(0, 100))
    Pw.set(random.randint(0, 100))

entry_6 = Entry(root, textvar=Pw)
entry_6.place(x=550, y=500)
Button(root, text='Generate Key', width=20, bg='gray', fg='white', command=gkey).place(x=750, y=500)
Button(root, text='Submit', width=20, bg='gray', fg='white', command=database).place(x=450, y=550)
Button(root, text='Cancel', width=20, bg='gray', fg='white', command=cancel).place(x=600, y=550)


root.mainloop()

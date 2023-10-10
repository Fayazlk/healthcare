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
Sugg = StringVar()


def cancel():
    root.destroy()
    os.system('python Main.py')

def database():
    name1 = Fullname.get()
    sugg = Sugg.get()


    if name1=="":
        messagebox.showinfo("Doctor","Enter Name")
    else:
        if sugg == "":
            messagebox.showinfo("Doctor","Enter Suggestion")
        else:
             conn = sqlite3.connect('form.db')
             with conn:
                cursor = conn.cursor()
                cursor.execute(
                'CREATE TABLE IF NOT EXISTS doctorsugg (Fullname TEXT,sugg TEXT)')
                cursor.execute('INSERT INTO doctorsugg (FullName,sugg) VALUES(?,?,?)',
                 (name1, sugg))
                conn.commit()
                messagebox.showinfo("Doctor","Record Saved")


label_0 = Label(root, justify=LEFT, bg='brown', text="Doctor Suggestion", width=15, font=("bold", 20))
label_0.place(x=400, y=200)


label_1 = Label(root, text="Patient Name", bg='brown', justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=400, y=300)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=550, y=300)

label_2 = Label(root, text="Suggestion", bg='brown', justify=LEFT, width=20, font=("bold", 10))
label_2.place(x=400, y=350)

entry_2 = Entry(root, textvar=Sugg)
entry_2.place(x=550, y=350)


Button(root, text='Submit', width=20, bg='gray', fg='white', command=database).place(x=400, y=420)
Button(root, text='Cancel', width=20, bg='gray', fg='white', command=cancel).place(x=550, y=420)


root.mainloop()

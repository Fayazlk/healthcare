from tkinter import *
import sqlite3
import os
from tkinter import messagebox

from PIL import ImageTk, Image
root = Tk()
root.geometry('1366x768')
root.title("Blockchain")
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.jpg')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)

Un = StringVar()
Pw = StringVar()

def back():
    root.destroy()
    os.system('python main.py')
def reg():
    root.destroy()
    os.system('python register.py')
def sendlogin():
    un = Un.get()
    pw = Pw.get()
    if un=="":
        messagebox.showinfo("Blockchain","Enter Usermenu")
    else:
        if pw == "":
            messagebox.showinfo("Blockchain","Enter Password")
        else:
             conn = sqlite3.connect('form.db')
             with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROm doctor")
                rows = cur.fetchall()
                for row in rows:
                    dbuser = row[3]
                    dbPass = row[7]
                    if dbuser == un and dbPass==pw:
                        root.destroy()
                        os.system('python sendfile.py')
                        #os.system('python main.py')
             conn.close()

def receivelogin():
    un = Un.get()
    pw = Pw.get()
    if un=="":
        messagebox.showinfo("Elliptic","Enter Usermenu")
    else:
        if pw == "":
            messagebox.showinfo("Elliptic","Enter Password")
        else:
             conn = sqlite3.connect('Form.db')
             with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM doctor")
                rows = cur.fetchall()
                for row in rows:
                    dbuser = row[3]
                    dbPass = row[7]
                    if dbuser == un and dbPass==pw:
                        root.destroy()
                        os.system('python receivefile.py')
                        #os.system('python main.py')
             conn.close()


label_0 = Label(root, text="Login",bg='black',fg='white', width=20, font=("bold", 20))
label_0.place(x=100, y=350)
label_4 = Label(root, text="Username",bg='black',fg='white', width=20, font=("bold", 11))
label_4.place(x=100, y=450)
entry_5 = Entry(root, textvar=Un, font=("bold", 11))
entry_5.place(x=300, y=450)
label_5 = Label(root, text="ID",bg='black',fg='white', width=20, font=("bold", 11))
label_5.place(x=100, y=500)
entry_6 = Entry(root, textvar=Pw, show="*", font=("bold", 11))
entry_6.place(x=300, y=500)
#Button(root, text='Patient Login', width=15, bg='gray', fg='black', command=sendlogin, font=("bold", 11)).place(x=160, y=550)
Button(root, text='Doctor Login', width=15, bg='gray', fg='black', command=receivelogin, font=("bold", 11)).place(x=305, y=550)
#Button(root, text='Register', width=15, bg='gray', fg='black', command=reg, font=("bold", 11)).place(x=200, y=600)
root.mainloop()

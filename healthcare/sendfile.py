from cryptography.fernet import Fernet
# key generation
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
import image
import os
from PIL import ImageTk, Image

root = Tk()
root.geometry('1366x768')
root.title("Registration Form")
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back1.jpg')
photo = ImageTk.PhotoImage(img)
canv.create_image(1, 1, anchor=NW, image=photo)
Fullname = StringVar()
def cancel():
    root.destroy()
    os.system('python Main.py')
def database():
    name1 = Fullname.get()
    if name1 == "":
        messagebox.showinfo("ECC", "EnterMessage")
    else:
        file = open("msg.txt", "w")
        L = Fullname.get()
        file.writelines(L)
        file.close()
        messagebox.showinfo("File","Message Saved")
        root.destroy()


label_1 = Label(root, text="Enter Message", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=930, y=250)

entry_1 = Entry(root, textvar=Fullname, width=100)
entry_1.place(x=930, y=300)



Button(root, text='Save Message', width=10, bg='gray', fg='white', command=database).place(x=1100, y=600)


root.mainloop()
os.system("python keygeneration.py")
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()


# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('msg.txt', 'rb') as file:
    original = file.read()

# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open('msgencrypt.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
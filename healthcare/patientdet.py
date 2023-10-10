from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import re
from cryptography.fernet import Fernet



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
Email = StringVar()
Contact = StringVar()
Un = StringVar()
Pw = StringVar()
Age = StringVar()
Gkey = StringVar()
Faceimg = StringVar()
Ht = StringVar()
Wt = StringVar()
Bp = StringVar()
temp = StringVar()
Hr = StringVar()
Sympt= StringVar()
def cancel():
    root.destroy()
    os.system('python Main.py')


def gkey():
    import random

    print(random.randint(0, 100))
    messagebox.showinfo("Doctor",random.randint(0, 100))

def database():
    fullname1 = Fullname.get()
    email = Email.get()
    contact = Contact.get()

    l = len(contact)

    ht= Ht.get()
    wt = Wt.get()
    temp1 = temp.get()
    bp = Bp.get()
    hr = Hr.get()
    sympt = Sympt.get()
    gkey=Gkey.get()
    faceimg = Faceimg.get()

    file = open("msg.txt", "w")
    xxx="Name : " + fullname1+ "Email :" + email+ "Contact : " + contact + "Height : " + ht+ "Weight :" + wt+ "Temperatre : " + temp1+ "Bp : "+bp+ "Heart Rate : " + hr+ "Symptom : " +sympt
    file.writelines(xxx)
    file.close()

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
    if fullname1 == "":
        messagebox.showinfo("BLockChain", "Enter Name")

    else:
        if email == "":
            messagebox.showinfo("BLockChain", "Enter Email")
        else:
            if contact == "":
                messagebox.showinfo("BLockChain", "Enter Contact")
            else:
                if ht== "":
                    messagebox.showinfo("BLockChain", "Enter Height")
                else:
                    if wt== "":
                        messagebox.showinfo("BLockChain", "Enter Weight")
                    else:
                        if temp== "":
                            messagebox.showinfo("BLockChain", "Enter Temperature")
                        else:
                            if not (re.search(regex, email)):
                                messagebox.showinfo("BLockChain", "Enter valid Email")
                            else:
                                if l != 10:
                                    messagebox.showinfo("BLockChain", "Enter 10 digits only")
                                else:
                                    if not fullname1.isalpha():
                                        messagebox.showinfo("BLockChain", "Enter Name in alphabets Only ")
                                    else:




                                                    conn = sqlite3.connect('Form.db')
                                                    with conn:
                                                            cursor = conn.cursor()


                                                            cursor.execute('INSERT INTO patient (fullName,email,contact,Ht,Wt,temp,bp,Hr,Sympt,Gkey,photo) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                                                                (fullname1,email,contact,ht,wt,temp1,bp,hr,sympt,gkey,faceimg))

                                                            conn.commit()
                                                            messagebox.showinfo("BLockChain", "Record Saved")



def open_File():
    faceimg = askopenfilename(filetypes=[(".jpg", "*.jpg")])
    Faceimg.set(faceimg)
    fm = Faceimg.get()
    load = Image.open(fm)
    render = ImageTk.PhotoImage(load)

    # labels can be text or images
    img = Label(root, image=render)
    img.image = render
    img.place(x=900, y=300)


label_0 = Label(root, justify=LEFT, bg='white', text="Patient Details", width=30, font=("bold", 20))
label_0.place(x=100, y=230)

label_1 = Label(root, text="FullName ", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=300, y=300)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=450, y=300)

label_2 = Label(root, text="Email", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_2.place(x=300, y=350)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=450, y=350)

label_3 = Label(root, text="Contact", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_3.place(x=300, y=400)

entry_3 = Entry(root, textvar=Contact)
entry_3.place(x=450, y=400)

label_4 = Label(root, text="Height", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_4.place(x=300, y=450)

entry_5 = Entry(root, textvar=Ht)
entry_5.place(x=450, y=450)

label_5 = Label(root, text="Weight", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_5.place(x=600, y=450)

entry_6 = Entry(root, textvar=Wt)
entry_6.place(x=750, y=450)

label_7 = Label(root, text="Temperature", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_7.place(x=300, y=500)

entry_7 = Entry(root, textvar=temp)
entry_7.place(x=450, y=500)

label_8 = Label(root, text="Blood Pressure", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_8.place(x=600, y=500)
entry_7 = Entry(root, textvar=Bp)
entry_7.place(x=750, y=500)

label_7 = Label(root, text="Heart Rate", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_7.place(x=300, y=550)

entry_7 = Entry(root, textvar=Hr)
entry_7.place(x=450, y=550)

label_8 = Label(root, text="Symptoms", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_8.place(x=600, y=550)
entry_7 = Entry(root, textvar=Sympt)
entry_7.place(x=750, y=550)







label_8 = Label(root, text="Permission Key", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_8.place(x=300, y=600)
entry_8 = Entry(root, textvar=Gkey)
entry_8.place(x=450, y=600)

label_7 = Label(root, text="Photo", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_7.place(x=300, y=650)

entry_7 = Entry(root, textvar=Faceimg)
entry_7.place(x=450, y=650)

Button(root, text='Public Key', width=20, height=8, bg='red', fg='white', command=gkey).place(x=100, y=350)
Button(root, text='Upload', width=10, bg='gray', fg='white', command=database).place(x=850, y=650)
Button(root, text='Cancel', width=10, bg='gray', fg='white', command=cancel).place(x=930, y=650)
Button(root, text='Browse Photo', width=20, bg='gray', fg='white', command=open_File).place(x=600, y=650)

root.mainloop()

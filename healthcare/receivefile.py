from tkinter import messagebox

from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)

# opening the encrypted file
with open('msgencrypt.txt', 'rb') as enc_file:
    encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('msgdecrypt.txt', 'wb') as dec_file:
    dec_file.write(decrypted)
with open('msgdecrypt.txt', 'rb') as dc:
    dc1 = dc.read()
    messagebox.showinfo("Decrypted Message",dc1)
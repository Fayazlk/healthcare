from tkinter import messagebox

from tinyec import registry
import secrets
from cryptography.fernet import Fernet

# Function to calculate compress point
# of elliptic curves
def compress(publicKey):
    return hex(publicKey.x) + hex(publicKey.y % 2)[2:]


# The elliptic curve which is used for the ECDH calculations
curve = registry.get_curve('brainpoolP256r1')

# Generation of secret key and public key
Ka = secrets.randbelow(curve.field.n)
X = Ka * curve.g

Kb = secrets.randbelow(curve.field.n)
Y = Kb * curve.g


# (A_SharedKey): represents user A
# (B_SharedKey): represents user B
A_SharedKey = Ka * Y
print("A shared key :", compress(A_SharedKey))
B_SharedKey = Kb * X
print("(B) shared key :", compress(B_SharedKey))
print("Equal shared keys:", A_SharedKey == B_SharedKey)
if A_SharedKey ==B_SharedKey:
    key = Fernet.generate_key()

    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
messagebox.showinfo("File","Key Generated")
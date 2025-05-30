import os
import string
os.system("clear")

letters = list(string.ascii_lowercase)

def encrypt(message,shift):
    encrypted_message = []
    for x in message:
        match = False
        for index, y in enumerate(letters):
            if x == y:
                encrypted_message.append(letters[(index + shift)%26])
                match = True
                break
        if not match:
                encrypted_message.append(x)
    return(''.join(encrypted_message))

def cipher():
    print("Welcome to the Cipher Lab!!")
    work = input("Type 'encode' or 'e' to encrypt and 'decode' or 'd' to decrypt: ").rstrip().lower()
    if work in ("encode", "e"):
        message = input("Enter the message that is to be encrypted: ").rstrip()
        shift = int(input("Enter the shift index: "))
        print(f"The encrypted message is {encrypt(message, shift)}")
    elif work in ("decode", "d"):
        message = input("Enter the message that is to be decrypted: ").rstrip()
        shift = int(input("Enter the shift index: "))
        print(f"The decrypted message is {encrypt(message, -shift)}")
    else:
        print("Incorrect option selected. \n")

cipher()
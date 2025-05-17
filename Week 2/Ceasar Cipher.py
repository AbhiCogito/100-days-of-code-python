import os
import string
os.system("clear")

letters = list(string.ascii_lowercase)

def encrypt():
    message = input("Enter the message that is to be encrypted: ").rstrip()
    shift = int(input("Enter the shift index: "))
    encrypted_message = []
    for x in message:
        for index, y in enumerate(letters):
            if x == y:
                encrypted_message.append(letters[index + shift])
    return(''.join(encrypted_message))

def decrypt():
     message = input("Enter the message that is to be decrypted: ").rstrip()
     shift = int(input("Enter the shift index: "))
     encrypted_message = []
     for x in message:
        for index, y in enumerate(letters):
            if x == y:
                encrypted_message.append(letters[index - shift])
     return(''.join(encrypted_message))

def cipher():
    work = input("Type 'encode' to encrypt and 'decode' to decipher.").rstrip().lower()
    if work == "encode":
        print(f"The excrypted message is {encrypt()}")
    else:
         print(f"The decrypted message is {decrypt()}")

cipher()
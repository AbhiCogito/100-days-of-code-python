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
                if index + shift < 26:
                    encrypted_message.append(letters[index + shift])
                else:
                    encrypted_message.append(letters[index + shift - 26])
    return(''.join(encrypted_message))

def decrypt():
     message = input("Enter the message that is to be decrypted: ").rstrip()
     shift = int(input("Enter the shift index: "))
     encrypted_message = []
     for x in message:
        for index, y in enumerate(letters):
            if x == y:
                if index - shift < 0:
                    encrypted_message.append(letters[26 + (index + shift)])
                else:
                    encrypted_message.append(letters[index - shift])
     return(''.join(encrypted_message))

def cipher():
    print("Welcome to the Cipher Lab!!")
    work = input("Type 'encode' to encrypt and 'decode' to decipher: ").rstrip().lower()
    if work == "encode" or work == "decode":
        if work == "encode":
            print(f"The excrypted message is {encrypt()}")
        else:
            print(f"The decrypted message is {decrypt()}")
    else:
        print("Incorrect option selected. \n")
cipher()
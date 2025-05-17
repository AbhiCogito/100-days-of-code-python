import os
import random
os.system("clear")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

options = ["l", "n", "s"]
password = []
select = 0
letter_count = 0
symbol_count = 0
number_count = 0

while len(password) < nr_letters + nr_symbols + nr_numbers:
    select = random.choice(options)
    if select == "l" and letter_count < nr_letters:
        password.append(random.choice(letters))
        letter_count += 1
    elif select == "n" and number_count < nr_numbers:
        password.append(random.choice(numbers))
        number_count += 1
    elif select == "s" and symbol_count < nr_symbols:
        password.append(random.choice(symbols))
        symbol_count += 1

random.shuffle(password)
print(password)
print("Your password is:", ''.join(password), f"and its length is {len(password)}")
import os
import random
os.system("clear")


p_rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
p_paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
p_scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ["rock", "paper", "scissors"]
pc = random.choice(options)
print(pc)

if pc == "rock":
    pc_print = p_rock
elif pc == "paper":
    pc_print = p_paper
else:
    pc_print = p_scissors

while True:
    user_choice = int(input("Please select \n 1. Rock \n 2. Paper \n 3. Scissors \n"))

    if user_choice == 1:
        user = "rock" 
        user_print = p_rock
        break
    elif user_choice == 2:
        user = "paper" 
        user_print = p_paper
        break
    elif user_choice == 3:
        user = "scissors" 
        user_print = p_scissors
        break
    else:
        os.system("clear")
        print("Enter a valid option")

print(f"The user has selected {user} and the PC has selected {pc}.")
print(user_print)
print(pc_print)

if user == pc:
    print("It is a draw!")
elif (user == "rock" and pc == "scissors") or \
     (user == "paper" and pc == "rock") or \
     (user == "scissors" and pc == "paper"):
    print("User won")
else:
    print("PC won.")

import os
import random
os.system("clear")

number = random.choice(range(1,100))
counter = 0
guesses = []

mode = input("Enter 'e' for easy (10) attempts or 'h' for hard (5) attempts: ")

if mode == 'e':
    counter = 10
elif mode == 'h':
    counter = 5

def game(counter, number):

    while counter > 0:
        
        while True:
            guess = int(input("Please enter your guess: "))
            if guess in guesses:
                print("You have already guessed this number.")
            else:
                guesses.append(guess)
                print(f"You have {counter} guesses remaining.")
                break

        if guess == number:
            print(f"You won. The correct number is {guess}")
            return counter
        elif guess < number:
            counter -= 1
            print("Low")
        elif guess > number:
            counter -= 1
            print("High")

    return counter

counter = game(counter, number)

if counter == 0:
    print("You have exhausted all your attempts.")
    print(f"The correct number is {number}")
import os
import random
os.system("clear")

word_list = ["baboon", "triisha", "joinee", "oops"]
chosen_word = random.choice(word_list)
length_word = len(chosen_word)

print(chosen_word)

lives = 7
repeat = [] #To check for repeatition in letters
box = ["_"] * length_word

def game(lives):
    if "_" in box and lives > 0:
        guess = input("Enter your guess: ").strip().lower()
        found = False
        if guess in repeat:
            print("You have already guessed this word.")
            lives -=1
            return(lives)
        else:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    box[index] = guess
                    repeat.append(guess)
                    found = True
                else:
                    continue
            if found == False:
                lives -= 1
                print(f"Incorrect guess. Only {lives} chances remaining.")
            repeat.append(guess)
            print(" ".join(box), "      ", lives, "chances left.")
            return lives

while "_" in box and lives > 0:
    lives = game(lives)

if "_" not in box and lives > 0:
    print("You have won!!")
else:
    print("You have lost. The correct answer is", chosen_word)



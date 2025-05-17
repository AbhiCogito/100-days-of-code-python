import os
import random
os.system("clear")

word_list = ["baboon", "triisha", "joinee", "oops"]
chosen_word = random.choice(word_list)
length_word = len(chosen_word)

place_holder = ["_"] * length_word
answer = []
lives = int(input"Define how many chances you want: ")
index = [] #To count the one or more positions where the user-entered letter is present in the word

print(chosen_word, length_word, ' '.join(place_holder))

#Function to check whether the user-entered letter is present in the word & print the placeholder
def check_letter(guess):
    counter = 0
    for letter in chosen_word:
        counter +=1
        if letter == guess:
            index.append(counter)
            place_holder[counter-1] = guess
        else:
            continue


def game():
    if '_' in place_holder and lives > 0:
        guess = input("Guess a letter: ").strip().lower()
        check_letter(guess)
        print(' '.join(place_holder), "\nTotal chances remaining: ",lives)

while lives > 0 and "_" in place_holder:
    prev_place_holder = place_holder.copy()
    game()
    if place_holder == prev_place_holder:
        lives -=1
        print(f"Wrong guess. Only {lives} chances remaining.")

if '_' not in place_holder:
    print("Your guess is correct!", chosen_word)
else:
    print("You lost. The correct answer is ", chosen_word)


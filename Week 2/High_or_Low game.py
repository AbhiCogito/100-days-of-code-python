from HL_data import data
import os
import random
os.system("clear")
score = 0

def display_first_options():
    total_keys = list(range(len(data)))
    random_option1 = random.choice(total_keys)
    total_keys.remove(random_option1)
    random_option2 = random.choice(total_keys)
    total_keys.remove(random_option2)
    return random_option1, random_option2, total_keys

def play_game(option1, option2):
    global score

    while True:
        try:
            choice = int(input(f"Who has more followers: \n1. {data[option1]['name']} or \n2. {data[option2]['name']}: "))
            if choice in [1,2]:
                break
        except ValueError:
            pass    
        print("Invalid option. Select either option 1 or 2.")

    if choice == 1:
        selected = option1
        other = option2
    elif choice == 2:
        selected = option2
        other = option1
    
    if data[selected]['follower_count'] > data[other]['follower_count']:
        score += 1
        print(f"User won. Your current streak is {score} rounds. ")
        result = "won"
    elif data[selected]['follower_count'] < data[other]['follower_count']:
        print("You lost.")
        result = "lost"
    elif data[selected]['follower_count'] == data[other]['follower_count']:
        print("It is a tie.")
        result = "tie"

    print(f"{data[selected]['name']} has {data[selected]['follower_count']} followers.")
    print(f"{data[other]['name']} has {data[other]['follower_count']} followers.")

    return selected, result

def next_round(total_keys):
    
    if len(total_keys) <2:
        print(f"You havle exhausted all the options. Only {total_keys} is the value remaining.")
        return None, total_keys
        #How do I quit this entire function
    
    new_option = random.choice(total_keys)
    total_keys.remove(new_option)

    return new_option, total_keys


#Ask user if he wants to play the game

print("Welcome to the Higher or Lower game.")
user_option = 0
used_key = []

while True:
    #os.system("clear")
    choice = input(("Do you want to play?. \nPress 'y' for Yes and 'n' for No: "))

    if choice in ('y', 'yes'):
        score = 0
        option1, option2, total_keys = display_first_options()

        while True:
            selected, result = play_game(option1, option2)

            if result in ("won", "tie"):
                option1 = selected
                option2, total_keys = next_round(total_keys)
            elif result == "lost":
                print(f"Your score is {score}.")
                break

    elif choice in ('n', 'no'):
        print("Thank you for playing the game.")
        #Display score
        break
    else:
        print("Incorrect option. Select again. ")

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
            choice = int(input(f"\nWho has more followers:\n1. {data[option1]['name']} or\n2. {data[option2]['name']}\nEnter 1 or 2: "))
            if choice in [1, 2]:
                break
            else:
                pass
        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    if choice == 1:
        selected = option1
        other = option2
    else:
        selected = option2
        other = option1

    print(f"\n{data[selected]['name']} has {data[selected]['follower_count']} followers.")
    print(f"{data[other]['name']} has {data[other]['follower_count']} followers.")

    if data[selected]['follower_count'] > data[other]['follower_count']:
        score += 1
        print("You won!\n")
        result = "won"
    elif data[selected]['follower_count'] < data[other]['follower_count']:
        print("You lost.\n")
        result = "lost"
    elif data[selected]['follower_count'] == data[other]['follower_count']:
        print("It is a tie.\n")
        result = "tie"

    return selected, result

def next_round(selected, total_keys):
    if not total_keys:
        print("No more comparisons left. You completed the game!")
        print(f"Your final score is {score}.")
        return None, None, []

    new_option = random.choice(total_keys)
    total_keys.remove(new_option)
    return selected, new_option, total_keys

# Ask user if he wants to play the game
print("Welcome to the Higher or Lower game.")

while True:
    choice = input("\nDo you want to play? Press 'y' for Yes and 'n' for No: ").lower()

    if choice in ('y', 'yes'):
        option1, option2, total_keys = display_first_options()

        while True:
            selected, result = play_game(option1, option2)

            if result in ("won", "tie"):
                option1, option2, total_keys = next_round(selected, total_keys)
                if option2 is None:
                    break
            elif result == "lost":
                print(f"Your score is {score}.\n")
                break

    elif choice in ('n', 'no'):
        print("Thank you for playing the game.")
        break
    else:
        print("Incorrect option. Please select again.")
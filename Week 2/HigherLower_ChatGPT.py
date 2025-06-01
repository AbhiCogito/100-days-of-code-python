import os
import random
from HL_data import data

class HigherLowerGame:
    def __init__(self):
        self.score = 0
        self.remaining_indices = list(range(len(data)))
        self.option1 = None
        self.option2 = None

    def clear_screen(self):
        os.system("clear")

    def reset_game(self):
        self.score = 0
        self.remaining_indices = list(range(len(data)))
        self.option1, self.option2 = self.select_two_options()

    def select_two_options(self):
        options = random.sample(self.remaining_indices, 2)
        for opt in options:
            self.remaining_indices.remove(opt)
        return options[0], options[1]

    def get_user_choice(self):
        while True:
            try:
                choice = int(input(f"Who has more followers: \n1. {data[self.option1]['name']} or \n2. {data[self.option2]['name']}: "))
                if choice in [1, 2]:
                    return choice
            except ValueError:
                pass
            print("Invalid option. Select either option 1 or 2.")

    def play_round(self):
        choice = self.get_user_choice()

        selected = self.option1 if choice == 1 else self.option2
        other = self.option2 if choice == 1 else self.option1

        selected_followers = data[selected]['follower_count']
        other_followers = data[other]['follower_count']

        print(f"{data[selected]['name']} has {selected_followers} followers.")
        print(f"{data[other]['name']} has {other_followers} followers.")

        if selected_followers > other_followers:
            self.score += 1
            print(f"User won. Your current streak is {self.score} rounds.")
            return True
        elif selected_followers == other_followers:
            print("It is a tie.")
            return True
        else:
            print("You lost.")
            return False

    def next_option(self):
        if not self.remaining_indices:
            print("You've exhausted all options. No more comparisons left.")
            return False

        new_option = random.choice(self.remaining_indices)
        self.remaining_indices.remove(new_option)
        self.option1 = self.option2
        self.option2 = new_option
        return True

    def run(self):
        print("Welcome to the Higher or Lower game.")

        while True:
            choice = input("Do you want to play? (y/n): ").lower()

            if choice in ('y', 'yes'):
                self.reset_game()

                while True:
                    result = self.play_round()
                    if not result:
                        print(f"Your final score is {self.score}.")
                        break
                    if not self.next_option():
                        break

            elif choice in ('n', 'no'):
                print("Thank you for playing the game.")
                break
            else:
                print("Incorrect option. Select again.")


if __name__ == "__main__":
    game = HigherLowerGame()
    game.run()

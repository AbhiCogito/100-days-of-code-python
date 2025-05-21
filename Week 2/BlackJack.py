import os
import random
os.system("clear")

dealer_wallet = 1000
player_wallet = int(input("Enter the amount in your wallet: "))
player_bid = int(input("Please enter the bid amount: "))
#player_wallet -= player_bid
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_starting_card1 = random.choice(cards)
player_starting_card2 = random.choice(cards)
dealer_first_card = random.choice(cards)
player_cards = [player_starting_card1, player_starting_card2]
print(f"Your starting cards are {player_cards} \
      and the total is {sum(player_cards)}")
print(f"Dealer's first card is {dealer_first_card}")

def dealers_game(player_cards, player_wallet, player_bid, dealer_wallet):
    print("Checking dealer's game loop.")

def player_choice(player_cards, player_wallet, player_bid, dealer_wallet):
    choice = input("Press 'h' for Hit or 's' for Stand: ")
    if choice == 'h':
        player_cards.append(random.choice(cards))
        print(f"Your cards are {player_cards} and the total is {sum(player_cards)}")
        if sum(player_cards) == 21:
            print("Blackjack!! You are lucky.")
            player_wallet += player_bid
            return player_wallet, dealer_wallet
        elif sum(player_cards) > 21:
            print("Bust! You lose.")
            dealer_wallet += player_bid
            player_wallet -= player_bid
            print(f"You have ${player_wallet} remaining.")
            return player_wallet, dealer_wallet
        elif sum(player_cards) < 21:
            print("Want to Hit or Stand: ")
            return player_choice(player_cards, player_wallet, player_bid, dealer_wallet)
    elif choice == 's':
        dealers_game(player_cards, player_wallet, player_bid, dealer_wallet)
        return player_wallet, dealer_wallet

player_wallet, dealer_wallet = player_choice(player_cards, player_wallet, player_bid, dealer_wallet)
print(f"Dealer's wallet has {dealer_wallet} and player's wallet has {player_wallet}")





import os
import random
os.system("clear")

dealer_wallet = 1000
player_wallet = int(input("Enter the amount in your wallet: "))

def play_game(player_wallet, dealer_wallet):
    os.system("clear")
    print(f"The player has ${player_wallet} in the wallet.")

    player_bid = int(input("Please enter the bid amount: "))
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    if player_bid > player_wallet:
        print("Bid amount cannot be more than the amount in wallet.")
        exit()

    player_starting_card1 = random.choice(cards)
    player_starting_card2 = random.choice(cards)
    dealer_first_card = random.choice(cards)
    player_cards = [player_starting_card1, player_starting_card2]
    print(f"Your starting cards are {player_cards} and the total is {sum(player_cards)}")
    print(f"Dealer's first card is {dealer_first_card}")

    def dealers_game(player_cards, player_wallet, player_bid, dealer_wallet, dealer_first_card):
        dealer_cards = [dealer_first_card]
        dealer_cards.append(random.choice(cards))
        player_sum = sum(player_cards)
        dealer_sum = sum(dealer_cards)
        while dealer_sum < 17:
            dealer_cards.append(random.choice(cards))
            dealer_sum = sum(dealer_cards)
        if dealer_sum > 21:
            print(f"Dealer got {dealer_cards} and got bust. Player won!")
            dealer_wallet -= player_bid
            player_wallet += player_bid
        elif player_sum < dealer_sum < 22:
            print("Haha. The house always wins!")
            player_wallet -= player_bid
            dealer_wallet += player_bid
            print(f"Dealer's score is {dealer_sum} and player's score is {player_sum}")
            print(f"Dealer's wallet has {dealer_wallet} and player's wallet has {player_wallet}")
        elif player_sum == dealer_sum:
            print("Both have equal score.")
            if player_sum == dealer_sum == 21:
                print("Both of you have black jack. Very rare!")
            print(f"Dealer's score is {sum(dealer_cards)} and player's score is {sum(player_cards)}")
            print(f"Dealer's wallet has {dealer_wallet} and player's wallet has {player_wallet}")
        elif dealer_sum < player_sum:
            print("The player has won.")
            player_wallet += player_bid
            dealer_wallet -= player_bid
        return player_wallet, dealer_wallet


    def player_choice(player_cards, player_wallet, player_bid, dealer_wallet, dealer_first_card):
        choice = input("Press 'h' for Hit or 's' for Stand: ")
        if choice == 'h':
            player_cards.append(random.choice(cards))
            print(f"Your cards are {player_cards} and the total is {sum(player_cards)}")
            if sum(player_cards) == 21 and len(player_cards) == 2:
                print("Blackjack!! You are lucky.")
                return dealers_game(player_cards, player_wallet, player_bid, dealer_wallet, dealer_first_card)
            elif sum(player_cards) > 21:
                if 11 in player_cards:
                    player_cards.remove(11)
                    player_cards.append(1)
                    if sum(player_cards) >21:
                        print("Bust! You lose.")
                        dealer_wallet += player_bid
                        player_wallet -= player_bid
                        print(f"You have ${player_wallet} remaining.")
            elif sum(player_cards) < 21:
                return player_choice(player_cards, player_wallet, player_bid, dealer_wallet, dealer_first_card)
            return player_wallet, dealer_wallet
        elif choice == 's':
            return dealers_game(player_cards, player_wallet, player_bid, dealer_wallet, dealer_first_card)
    return player_choice(player_cards, player_wallet, player_bid, dealer_wallet, dealer_first_card)

while True:
    player_wallet, dealer_wallet = play_game(player_wallet, dealer_wallet)
    
    play_again = input("Do you want to play again Y or N: ")
    if play_again.lower() != 'y':
        print("Thanks for playing.")
        exit()


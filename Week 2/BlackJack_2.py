import os
import random

dealer_wallet = 1000

player_cards = []
dealer_cards = []

def start_game(player_cards, dealer_cards):
    os.system("clear")
    print("Welcome to the casino for playing BlackJack!")
    player_wallet = 0
    player_bid = 0
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    #Check that wallet > 0
    while player_wallet < 1:
        print("Wallet amount must be > 0.")
        player_wallet = int(input("Enter the amount in your wallet: "))
    player_bid = int(input("Enter the bid amount: "))
    
    #Check that bid is > 0 and bid < wallet
    while player_bid < 1 or player_bid > player_wallet:
        print("Player bid amount must be > 0 and < Wallet.")
        player_bid = int(input("Enter the bid amount: "))
    
    dealer_cards.append(random.choice(cards))
    for _ in range(2):
        player_cards.append(random.choice(cards))
    
    print(f"The player has {player_cards} and its sum is {sum(player_cards)}")
    return player_bid, player_wallet, player_cards, dealer_cards

def players_turn(player_bid, player_wallet, player_cards, dealer_cards):
    global dealer_wallet

    players_sum = sum(player_cards)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def hit_or_stand(player_cards, players_sum, player_wallet):
        global dealer_wallet

        if sum(player_cards) > 21:
            print(f"You got bust as your cards are {player_cards} and your score {sum(player_cards)} > 21.")
            player_wallet -= player_bid
            dealer_wallet += player_bid
            exit()

        choice = input("Press 'h' for Hit or 's' for Stand: ")
        if choice == 'h':
            player_cards.append(random.choice(cards))
            players_sum = sum(player_cards)
            print(f"Your cards are {player_cards} and the total is {players_sum}.")
            hit_or_stand(player_cards, players_sum, player_wallet)
        elif choice == 's':
            print("You have decided to stand. Check the dealer's game now.")

    while players_sum < 21:
        if players_sum == 21 and len(player_cards) == 2:
            print("You have blackjack!")
            return player_bid, player_wallet, player_cards, dealer_cards
        elif players_sum < 21:
            hit_or_stand(player_cards, players_sum, player_wallet)
            return player_bid, player_wallet, player_cards, dealer_cards
    else players_sum > 21:
            if 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)
                players_sum = sum(player_cards)
                hit_or_stand(player_cards, players_sum, player_wallet)
            else: 
                print("You got bust as your score > 21")
                player_wallet -= player_bid
                dealer_wallet += player_bid
                exit()

def dealers_turn(player_bid, player_wallet, player_cards, dealer_cards):
    global dealer_wallet

    players_sum = sum(player_cards)
    dealers_sum = sum(dealer_cards)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    while dealers_sum < 17:
        dealer_cards.append(random.choice(cards))
        dealers_sum = sum(dealer_cards)
        if dealers_sum > 21:
            if 11 in dealer_cards:
                dealer_cards.remove(11)
                dealer_cards.append(1)
                dealers_sum = sum(dealer_cards)
            else:
                print(f"Dealer got {dealer_cards} and got bust. Player won!")
                dealer_wallet -= player_bid
                player_wallet += player_bid
        elif players_sum < dealers_sum < 22:
            print("Haha. The house always wins!")
            player_wallet -= player_bid
            dealer_wallet += player_bid
            print(f"Dealer's score is {dealers_sum} and player's score is {players_sum}")
            print(f"Dealer's wallet has {dealer_wallet} and player's wallet has {player_wallet}")
        elif players_sum == dealers_sum:
            print("Both have equal score.")
            if players_sum == dealers_sum == 21:
                print("Both of you have black jack. Very rare!")
            print(f"Dealer's score is {dealers_sum} and player's score is {players_sum}")
            print(f"Dealer's wallet has {dealer_wallet} and player's wallet has {player_wallet}")
        elif dealers_sum < players_sum:
            print("The player has won.")
            player_wallet += player_bid
            dealer_wallet -= player_bid
        return player_wallet, dealer_wallet

# --- Game starts here ---
player_bid, player_wallet, player_cards, dealer_cards = start_game(player_cards, dealer_cards)
players_turn(player_bid, player_wallet, player_cards, dealer_cards)
dealers_turn(player_bid, player_wallet, player_cards, dealer_cards)

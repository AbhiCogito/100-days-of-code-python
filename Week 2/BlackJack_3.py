import os
import random
os.system("clear")

dealer_wallet = 1000
player_wallet = 0

player_cards = []
dealer_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start_game(player_cards, dealer_cards):

    os.system("clear")
    print("Welcome to the casino for playing BlackJack!")
    global player_bid, player_wallet
    player_bid = 0
    
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

def player_turn():
    global player_wallet, dealer_wallet, cards, player_bid

    while True:
        total = sum(player_cards)

        while total > 21 and 11 in player_cards:
            player_cards.remove(11)
            player_cards.append(1)
            total = sum(player_cards)

        if total > 21:
            print(f"Your cards are {player_cards} and your total is {total}")
            print("You got BUST")
            player_wallet -= player_bid
            dealer_wallet += player_bid
            print(f"Your current wallet balance: {player_wallet}")
            return player_wallet, dealer_wallet

        if total < 21:
            choice = input("Press 'h' for HIT and 's' for STAND.")
            if choice == 'h':
                player_cards.append(random.choice(cards))
                print(f"Your cards are {player_cards} and your total is {total}")
            elif choice == 's':
                return player_wallet, dealer_wallet

def dealer_turn():
    global player_wallet, dealer_wallet, cards, dealer_cards, player_bid

    total_player = sum(player_cards)
    total_dealer = sum(dealer_cards)

    while total_dealer < 17:
        dealer_cards.append(random.choice(cards))
        total_dealer = sum(dealer_cards)
        #what diff will this make if I put this code inside while loop and if placed outside loop
        #If placed inside loop, it will check for all the aces
        #If places outside loop, it will check for only the first ace
        while total_dealer > 21 and 11 in dealer_cards:
            dealer_cards.remove(11)
            dealer_cards.append(1)
            total_dealer = sum(dealer_cards)

    if total_dealer > 21:
        print("The dealer has gone bust.")
        print(f"Dealer got {dealer_cards} and total is {total_dealer}")
        print(f"You got {player_cards} and total is {total_player}")
        player_wallet += player_bid
        dealer_wallet -= player_bid
        print(f"Your current wallet balance: {player_wallet}")    
    elif total_dealer > total_player:
        player_wallet -= player_bid
        dealer_wallet += player_bid
        print(f"\n Dealer got {dealer_cards} and total is {total_dealer}")
        print(f"You got {player_cards} and total is {total_player}")
        print("You have lost.")
        print(f"Your current wallet balance: {player_wallet}\n")
    elif total_dealer < total_player:
        print("You have won.")
        player_wallet += player_bid
        dealer_wallet -= player_bid
        print(f"Dealer got {dealer_cards} and total is {total_dealer}")
        print(f"You got {player_cards} and total is {total_player}")
        print(f"Your current wallet balance: {player_wallet}\n")
    elif total_dealer == total_player:
        print("It is a tie.")
        print(f"Dealer got {dealer_cards} and total is {total_dealer}")
        print(f"You got {player_cards} and total is {total_player}")
        print(f"Your current wallet balance: {player_wallet}\n")
    return player_wallet, dealer_wallet

# --- Game starts here ---
print("Do you want to play BlackJack. \n")
while True:
    play_again = input("Enter 'y for Yes and 'n' for No.")

    if play_again == 'y':
        player_cards.clear()
        dealer_cards.clear()
        player_bid, player_wallet, player_cards, dealer_cards = start_game(player_cards, dealer_cards)
        player_turn()
        dealer_turn()
    elif play_again == 'n':
        print("Thank you for visiting the Casino.")
        break
    
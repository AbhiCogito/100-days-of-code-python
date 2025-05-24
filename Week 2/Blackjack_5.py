import os
import random
os.system("clear")
# --- Game Setup ---
player_wallet = 0
dealer_wallet = 1000
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start_game():
    global player_wallet

    while player_wallet == 0:
        amount = input("Please enter the amount in your wallet: ")
        if amount.isdigit():
            player_wallet = int(amount)
            
            if player_wallet > 0:
                break
            else:
                print("Wallet amount must be greater than 0.")
        else:
            print("Invalid input. Only integer values accepted.")

    while True:
        bid = input("Please enter the bid amount: ")

        if bid.isdigit():
            global player_bid
            player_bid = int(bid)
            if player_bid > 0 and player_bid <= player_wallet:
                break
            else:
                print("Player bid amount should be > 0 and <= Wallet.")
        else:
            print("Only integer values accepted.")

    return player_bid, player_wallet

def find_sum(card):
    total = sum(card)

    while total > 21 and 11 in card:
        card.remove(11)
        card.append(1)
        total = sum(card)
    
    return total

def player_shuffle(player_wallet):
    global cards, dealer_wallet
    player_cards = []
    dealer_cards = []

    for _ in range(2):
        player_cards.append(random.choice(cards))

    dealer_cards.append(random.choice(cards))
    
    player_sum = find_sum(player_cards)
    dealer_sum = find_sum(dealer_cards)

    print(f"You have received {player_cards} and your total is {player_sum}")
    print(f"The dealer has received {dealer_cards} and sum is {dealer_sum}.")

    while True:

        while player_sum < 21:
            choice = input("Press 'h for Hit and 's' for Stand. ")

            if choice == 'h':
                player_cards.append(random.choice(cards))
                player_sum = find_sum(player_cards)
                print(f"You have received {player_cards} and your total is {player_sum}")
            elif choice == 's':
                print(f"You have chosen to stand. \n Your cards are {player_cards} and your total is {player_sum}.")
                status = "continue"
                return player_wallet, player_cards, dealer_cards, status

        if player_sum > 21:
            print("You are bust.")
            player_wallet -= player_bid
            dealer_wallet += player_bid
            status = "Bust"
            print(f"You have ${player_wallet} remaining.")
            return player_wallet, player_cards, dealer_cards, status

        if player_sum == 21 and len(player_cards) == 2:
            print("Blackjack. Player won.")
            player_wallet += (1.5 * player_bid)
            dealer_wallet -= (1.5 * player_bid)
            status = "Win"
            print(f"You have ${player_wallet} remaining.")
            return player_wallet, player_cards, dealer_cards, status  

        if player_sum == 21 and len(player_cards) > 2:
            status = "continue"
            print("Your score is 21. Switching to dealer's turn.")
            print(f"You have ${player_wallet} remaining.")
            return player_wallet, player_cards, dealer_cards, status 

def dealer_shuffle(player_wallet, player_cards, dealer_cards):
    global cards, player_bid, dealer_wallet

    dealer_sum = find_sum(dealer_cards)
    player_sum = find_sum(player_cards)

    while dealer_sum < 17:
        dealer_cards.append(random.choice(cards))
        dealer_sum = find_sum(dealer_cards)

    if dealer_sum > 21:
        print("The dealer has gone bust. You win.")
        player_wallet += player_bid
        dealer_wallet -= player_bid
        print(f"The dealer has received {dealer_cards} and sum is {dealer_sum}.")
        print(f"You have ${player_wallet} remaining.")
    elif dealer_sum < player_sum:
        player_wallet += player_bid
        dealer_wallet -= player_bid
        print(f"The dealer has received {dealer_cards} and sum is {dealer_sum}.")
        print("You have won.")
        print(f"You have ${player_wallet} remaining.")
    elif dealer_sum > player_sum:
        player_wallet -= player_bid
        dealer_wallet += player_bid
        print(f"The dealer has received {dealer_cards} and sum is {dealer_sum}.")
        print("Dealer won.")
        print(f"You have ${player_wallet} remaining.")
    elif dealer_sum == player_sum:
        print(f"The dealer has received {dealer_cards} and sum is {dealer_sum}.")
        print("It is a tie!!")
        print(f"You have ${player_wallet} remaining.")
    return player_wallet

print("Welcome to Blackjack!")

while True:
    choice = input("Do you want to play? 'y' or 'n' : ")
    os.system("clear")
    if choice == 'y':
        player_bid, player_wallet = start_game()
        player_wallet, player_cards, dealer_cards, status = player_shuffle(player_wallet)

        if status == "Win" or status == "Bust":
            continue
        elif status == "continue":
            player_wallet = dealer_shuffle(player_wallet, player_cards, dealer_cards)
    else:
        print("Thank you for playing Blackjack.")
        break
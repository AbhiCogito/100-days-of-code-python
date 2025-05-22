import os
import random

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def calculate_total(cards):
    total = sum(cards)
    while total > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        total = sum(cards)
    return total

def get_valid_int(prompt, min_value):
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Enter a value >= {min_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def start_game():
    clear_screen()
    print("Welcome to the casino for playing BlackJack!")

    global player_wallet
    if player_wallet <= 0:
        player_wallet = get_valid_int("Enter the amount in your wallet: ", 1)

    bid = get_valid_int("Enter your bid amount: ", 1)
    while bid > player_wallet:
        print(f"Your bid cannot exceed your wallet balance ({player_wallet}).")
        bid = get_valid_int("Enter your bid amount: ", 1)

    player_cards = [random.choice(cards) for _ in range(2)]
    dealer_cards = [random.choice(cards)]

    print(f"\nYour cards: {player_cards}, total: {calculate_total(player_cards)}")
    print(f"Dealer shows: {dealer_cards[0]}")
    return bid, player_cards, dealer_cards

def player_turn(player_cards):
    while True:
        total = calculate_total(player_cards)
        if total > 21:
            print(f"\nYour cards: {player_cards}, total: {total}")
            print("You got BUST!")
            return False  # Player loses

        choice = input("\nPress 'h' for HIT or 's' for STAND: ").lower()
        if choice == 'h':
            player_cards.append(random.choice(cards))
            total = calculate_total(player_cards)
            print(f"Your cards: {player_cards}, total: {total}")
        elif choice == 's':
            return True  # Player stands
        else:
            print("Invalid input.")

def dealer_turn(dealer_cards):
    while calculate_total(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
    return calculate_total(dealer_cards)

def resolve_round(bid, player_cards, dealer_cards):
    global player_wallet, dealer_wallet
    player_total = calculate_total(player_cards)
    dealer_total = calculate_total(dealer_cards)

    print(f"\nFinal Results:")
    print(f"Dealer's cards: {dealer_cards}, total: {dealer_total}")
    print(f"Your cards: {player_cards}, total: {player_total}")

    if dealer_total > 21 or player_total > dealer_total:
        print("You win!")
        player_wallet += bid
        dealer_wallet -= bid
    elif dealer_total > player_total:
        print("Dealer wins!")
        player_wallet -= bid
        dealer_wallet += bid
    else:
        print("It's a tie!")

    print(f"Your wallet: {player_wallet}\n")

# --- Game Setup ---
player_wallet = 0
dealer_wallet = 1000
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# --- Main Game Loop ---
print("Welcome to Blackjack!\n")
while True:
    play = input("Do you want to play? (y/n): ").lower()
    if play == 'y':
        bid, player_cards, dealer_cards = start_game()
        if player_turn(player_cards):
            dealer_cards.append(random.choice(cards))  # Reveal dealer's second card
            resolve_round(bid, player_cards, dealer_cards)
        else:
            player_wallet -= bid
            dealer_wallet += bid
            print(f"Your wallet: {player_wallet}\n")
    elif play == 'n':
        print("Thank you for visiting the Casino!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

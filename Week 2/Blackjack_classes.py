import os
import random

class Deck:
    
    def __init__(self):
        self.deck = []
        self.selected_cards = []
        self.used_cards = []

    def generate_deck(self):
        self.deck = []
        suits = ["♠", "♥", "♦", "♣"]
        values = list(range(1, 14))
        
        for suit in suits:
            for value in values:
                self.deck.append((suit, value))  

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        if not self.deck:
            print("No more cards left in the deck.")
            return None
        card = self.deck.pop()
        self.selected_cards.append(card)

class Card:
    def __init__(self):
        pass

    def first_round(self)
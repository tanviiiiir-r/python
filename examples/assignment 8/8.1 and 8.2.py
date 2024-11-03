import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        value_str = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}.get(self.value, str(self.value))
        return f"{value_str} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.cards = [Card(value, suit) for suit in suits for value in range(1, 14)]

    def __str__(self):
        return "\n".join(str(card) for card in self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

deck = Deck()
print("Original Deck:")
print(deck)

deck.shuffle()
print("\nShuffled Deck:")
print(deck)

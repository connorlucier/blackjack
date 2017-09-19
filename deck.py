import random
import secrets

from card import Card

suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
names = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King']


class Deck:

    def __init__(self):
        self.cards = []

        val = 1
        for name in names:
            for suit in suits:
                value = 10 if val > 10 else val
                self.cards.append(Card(value, name, suit))
            val += 1

        for _ in range(secrets.randbelow(3) + 1):
            random.shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) < 1:
            print('No cards left in deck!')
        else:
            return self.cards.pop()

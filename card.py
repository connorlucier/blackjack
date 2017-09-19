class Card:

    def __init__(self, value, name, suit):
        self.value = value
        self.name = name
        self.suit = suit

    def __str__(self):
        return self.name + ' of ' + self.suit

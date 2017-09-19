class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.bust = False

    def __str__(self):
        result = ''
        for card in self.cards:
            result += str(card) + '\n'
        return result

    def insert(self, card):
        self.cards.append(card)
        self.recalculate()

    def add_card(self, deck):
        if len(deck.cards) > 0:
            self.cards.append(deck.remove_card())
            self.recalculate()

    def remove_card(self, index):
        card = self.cards.pop(index)
        self.recalculate()
        return card

    def compare(self, index1, index2):
        return True if self.cards[index1].name == self.cards[index2].name else False

    def clear(self):
        self.cards = []
        self.value = 0
        self.bust = False

    def print(self, hidden):
        if hidden == True:
            for i in range(len(self.cards)):
                if i == 0:
                    print(self.cards[i])
                else:
                    print('??? of ???')
            print()
        else:
            print(str(self))

    def recalculate(self):
        total = 0
        num_aces = 0

        for card in self.cards:
            if card.name == 'Ace':
                num_aces += 1
            else:
                total += card.value

        while num_aces > 0:
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
            num_aces -= 1

        if total > 21:
            self.bust = True
        self.value = total

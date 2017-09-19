from hand import Hand
from deck import Deck

if __name__ == '__main__':
    print('Welcome to Blackjack!\n')

    deck = Deck()
    dealer = Hand()
    player = []
    player_bust = []
    player.append(Hand())

    play_again = True

    while play_again:

        if len(deck.cards) < 4:
            print('\nNot enough cards! One moment please.\n')
            new_deck = Deck()
            deck.cards.extend(new_deck.cards)

        for _ in range(2):
            player[0].add_card(deck)
            dealer.add_card(deck)

        print('Your Hand:')
        player[0].print(False)
        print('Dealer\'s Hand:')
        dealer.print(True)

        player_bust.append(False)
        dealer_bust = False

        print('Initial hand value: ' + str(player[0].value))

        print('\nYour Turn.\n')

        hand_number = 0
        for hand in player:

            if len(hand.cards) == 2 and hand.compare(0, 1) is True:
                print('Your initial hand is two cards with the same value.')

                if input('Do you want to split your hand? (y/n) ').lower() == 'y':
                    new_hand = Hand()
                    new_hand.insert(hand.remove_card(0))
                    new_hand.add_card(deck)
                    hand.add_card(deck)

                    player.append(new_hand)
                    player_bust.append(False)

                    print('\nYour new hands:')
                    for i in range(len(player)):
                        print(str(player[i]))

            if len(player) > 1:
                print('Hand ' + str(hand_number + 1) + ':')
                print('\n' + str(hand))

            while player[hand_number].value <= 21 and input('Do you want to hit? (y/n) ').lower() == 'y':
                if len(deck.cards) == 0:
                    print('No more cards! Cannot hit.')
                    break

                player[hand_number].add_card(deck)

                print('\nCurrent hand:')
                player[hand_number].print(False)
                print('Current hand value: ' + str(player[hand_number].value))

            print('\nYour final hand:')
            player[0].print(False)

            if player[0].value <= 21:
                print('Final hand value: ' + str(player[hand_number].value))
            else:
                print('You bust with ' + str(player[hand_number].value) + '!')
                player_bust[hand_number] = True

            hand_number += 1

        print('\nDealer\'s Turn.\n')

        print('Dealer\'s full hand:')
        dealer.print(False)

        while dealer.value < 17 and dealer.value <= 21:
            print('Dealer has ' + str(dealer.value) + ' and must hit.\n')
            if len(deck.cards) == 0:
                print('No more cards! Cannot hit.')
                break

            dealer.add_card(deck)

            print('Dealer\'s current hand:')
            dealer.print(False)

        if dealer.value <= 21:
            print('Dealer must stay with ' + str(dealer.value) + '.')
        else:
            print('Dealer busts with ' + str(dealer.value) + '!')
            dealer_bust = True

        for i in range(len(player)):
            if (player[i].value > dealer.value and not player_bust[i]) or (dealer_bust and not player_bust[i]):
                if len(player) > 1:
                    print('You win on hand ' + str(i + 1) + '!')
                else:
                    print('You win!')
            elif player[i].value == dealer.value and not player_bust[i]:
                if len(player) > 1:
                    print('You tie the dealer on hand ' + str(i + 1) + '.')
                else:
                    print('You tie the dealer.')
            else:
                if len(player) > 1:
                    print('You lose on hand ' + str(i + 1) + '!')
                else:
                    print('You lose!')

        play_again = True if input('\nPlay again? (y/n) ').lower() == 'y' else False

        if play_again:
            player = []
            player_bust = []

            player.append(Hand())
            player_bust.append(False)
            dealer.clear()

    print('\n\nThanks for playing Blackjack!\n\n')

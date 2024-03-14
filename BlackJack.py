import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


class Player:

    def __init__(self, name, balance=100):
        self.name = name
        self.balance = balance
        # A new player has no cards
        self.all_cards = []

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)

    def __str__(self):
        return f'{self.name} has ${self.balance}.'

print('Welcome to BlackJack!')
print('─'*15)
playername = Player(input('Whats your name?'))
print(playername)
handno=0


while True:
    handno+=1
    dealer_hand = []
    player_hand = []
    dealer_deck = Deck()
    dealer_deck.shuffle()

    if playername.balance<=0:
        print('Your balance has reached 0. Thank you for playing!')
        break
    if handno>1:
        keep_play = input('Do you want to keep playing?')
        if keep_play.isdigit():
            print('Please enter a valid response.')
            continue
        if keep_play == 'y' or keep_play == 'Y' or keep_play == 'yes' or keep_play == 'YES' or keep_play == 'Yes':
            pass
        else:
            print('─' * 15)
            print('Thank you for playing! Your final balance is ${}'.format(playername.balance))
            exit()
    while True:
        print('─' * 15)
        bet=input('Whats your bet?')

        if bet.isdigit():
            pass
        else:
            print('Thats an invalid quantity. Try again.')
            continue

        print('─' * 15)

        bet=int(bet)

        if bet>playername.balance:
            print('You dont have enough balance to place that bet.')
            continue
        else:
            break

    bet = int(bet)

    player_hand.append(dealer_deck.deal_one())

    dealer_hand.append(dealer_deck.deal_one())

    player_hand.append(dealer_deck.deal_one())

    dealer_hand.append(dealer_deck.deal_one())

    player_count=player_hand[0].value+player_hand[1].value
    dealer_count=dealer_hand[0].value+dealer_hand[1].value
    turn=0






    if player_hand[0].value==1 or player_hand[1].value==1: #ACE IN HAND
        player_count_big_ace = player_count + 10
        if player_hand[0].value == 1 or player_hand[1].value == 1:
            if dealer_hand[0].value == 1 or dealer_hand[1].value == 1:
                if dealer_count == 11 and player_count == 11:
                    print('Both {} and the dealer have a BlackJack! It is a tie.'.format(playername))
                    continue

        if dealer_count==11 and player_count!=11:
            if dealer_hand[0].value == 1 or dealer_hand[1].value == 1:
                print('Dealer has a BlackJack')
                playername.balance-=bet
                print('You have lost ${}. Your new balance is ${}'.format(bet, playername.balance))
                continue


        print('The Dealer has a {} showing.'.format(dealer_hand[1]))
        print('You have a {} and a {}.'.format(player_hand[0], player_hand[1]))

        while player_count < 22:
            if player_count == 11 and turn == 0:
                if player_hand[0].value == 1 or player_hand[1].value == 1:
                    print('{} has a Blackjack'.format(playername.name))
                    player_count=21
                    playername.balance += bet * 1.5
                    print('You earned ${}. Your new balance is ${}'.format(1.5*bet, playername.balance))
                    break
            elif turn==0 and player_count!=11:
                print('Your Total is {} or {}'.format(player_count_big_ace, player_count))
                print('─' * 15)
            turn = 1

            #if player_count_big_ace >= 21:
                #if player_count >= 21:
                    #print('Your final total is {}'.format(player_count))
                    #print('─' * 15)
                    #break

            another_card = input('Do you want another card?')
            print('─' * 15)
            if another_card == 'y' or another_card == 'Y' or another_card == 'yes' or another_card == 'YES' or another_card == 'Yes':

                if player_count<22 or player_count_big_ace<22:
                    new_card = dealer_deck.all_cards.pop()
                    player_count += new_card.value
                    player_count_big_ace += new_card.value

                    if player_count==21 and player_hand[0].value!=1 and player_hand[1].value!=1:
                        print('You have drawn a {}'.format(new_card))
                        print('Your new total is 21')
                        print('─' * 15)
                        break

                    elif player_count < 22 and player_count_big_ace < 22:
                        print('You have drawn a {}'.format(new_card))
                        print('Your new total is {} or {}'.format(player_count_big_ace,player_count))
                        print('─' * 15)

                    elif player_count < 22 and player_count_big_ace > 21:
                        print('You have drawn a {}'.format(new_card))
                        print('Your new total is {}'.format(player_count))
                        print('─' * 15)

                    elif player_count > 21 and player_count_big_ace > 21:
                        print('You have drawn a {}'.format(new_card))
                        print('Your final total is {}'.format(player_count))
                        print('─' * 15)
                        break

            elif player_count_big_ace<=21:
                    player_count=player_count_big_ace
                    print('Your final total is {}'.format(player_count))
                    print('─' * 15)
                    break
            else:
                    print('Your final total is {}'.format(player_count))
                    print('─' * 15)
                    break

        if player_count >= 22:
            print('Dealer has won with {} against the players {}'.format(dealer_count, player_count))
            playername.balance -= bet
            print('You have lost ${}. Your new balance is ${}'.format(bet, playername.balance))
            print('─' * 15)
            continue

        while dealer_count < 22 and turn > 0:
            if dealer_count < player_count:
                new_card = dealer_deck.all_cards.pop()
                dealer_count += new_card.value
                print('The dealers has drawn a {}'.format(new_card))
                print('The dealers new total is {}'.format(dealer_count))
                print('─' * 15)
            else:
                print('The dealers final total is {}'.format(dealer_count))
                print('─' * 15)
                break

            if dealer_count == player_count:
                print('Theres been a Tie')
                print('─' * 15)
                break
            elif dealer_count > player_count and dealer_count < 22:
                print('Dealer has won with {} against the players {}'.format(dealer_count, player_count))
                playername.balance -= bet
                print('You have lost ${}. Your new balance is ${}'.format(bet, playername.balance))
                print('─' * 15)
                break
            else:
                print('You have won! {} against the dealers {}.'.format(player_count, dealer_count))
                playername.balance += bet
                print('You earned ${}. Your new balance is ${}'.format(bet, playername.balance))
                print('─' * 15)
                break


    #No Aces
    else:
        print('The Dealer has a {} showing.'.format(dealer_hand[1]))
        print('You have a {} and a {}.'.format(player_hand[0],player_hand[1]))
        print('Your Total is {}'.format(player_count))
        print('─' * 15)

        if dealer_count == 11:
            if dealer_hand[0].value == 1 or dealer_hand[1].value == 1:
                print('Dealer has a BlackJack')
                playername.balance -= bet
                print('You have lost ${}. Your new balance is ${}'.format(bet, playername.balance))
                continue

        while player_count<22:

            if player_count==21:
                print('Your final total is {}'.format(player_count))
                break
            turn=1
            another_card=input('Do you want another card? ')
            print('─' * 15)

            if another_card=='y' or another_card=='Y' or another_card=='yes' or another_card=='YES' or another_card=='Yes':
                new_card=dealer_deck.all_cards.pop()
                player_count+=new_card.value
                print('You have drawn a {}'.format(new_card))
                print('Your new total is {}'.format(player_count))
                print('─' * 15)
            else:
                print('Your final total is {}'.format(player_count))
                print('─' * 15)
                break

        if player_count>21:
            print('Dealer has won with {} against the players {}'.format(dealer_count,player_count))
            playername.balance -= bet
            print('You have lost ${}. Your new balance is ${}'.format(bet, playername.balance))
            print('─' * 15)
            continue

        while dealer_count<22 and turn>0:
            if dealer_count<player_count:
                new_card=dealer_deck.all_cards.pop()
                dealer_count+=new_card.value
                print('The dealers has drawn a {}'.format(new_card))
                print('The dealers new total is {}'.format(dealer_count))
                print('─' * 15)
            else:
                print('The dealers final total is {}'.format(dealer_count))
                print('─' * 15)
                break



        if dealer_count==player_count:
            print('Theres been a Tie')
            print('─' * 15)


        elif dealer_count>player_count and dealer_count<22:
            print('Dealer has won with {} against the players {}'.format(dealer_count,player_count))
            playername.balance -= bet
            print('You have lost ${}. Your new balance is ${}'.format(bet, playername.balance))
            print('─' * 15)


        else:
            print('You have won! {} against the dealers {}.'.format(player_count,dealer_count))
            playername.balance += bet
            print('You earned ${}. Your new balance is ${}'.format(bet,playername.balance))
            print('─' * 15)

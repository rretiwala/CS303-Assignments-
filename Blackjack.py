#  File: Blackjack.py

#  Description: Creates blackjack game

#  Student Name: Raza Retiwala

#  Student UT EID: mrr2975

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51920

#  Date Created: 2/17

#  Date Last Modified: 2/19

import random

class Card(object):

    RANKS = (1,3,4,5,6,7,8,9,10,11,12,13)

    SUITS = ('C', 'D', 'H', 'S')

    suit_value = {'D':100, 'C':200, 'H':300, 'S':400}

    #initiate
    def __init__(self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    #create string representations
    def __str__(self):
        if (self.rank == 1):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)

        return rank + self.suit

    #create <, =, >
    def score(self):
        return self.suit_value[self.suit] + self.rank

    def __eq__(self, other):
        return self.score() == other.score()

    def __ne__(self, other):
        return not(self == other)

    def __gt__(self, other):
        return self.score() > other.score()

    def __ge__(self, other):
        return self.score() >= other.score()

    def __lt__(self, other):
        return self.score() < other.score()

    def __le__(self, other):
        return self.score() <= other.score()


class Deck(object):

    #initiate, create the deck
    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card1 = Card(rank, suit)
                self.deck.append(card1)


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

class Player(object):

    #Initialize
    def __init__(self, cards):
        self.cards = cards

    #when player hits, append a card
    def hit(self, card):
        self.cards.append(card)

    #count the persons points
    def get_points(self):
        count = 0
        for card in self.cards:
            if (card.rank > 9):
                count += 10
            elif (card.rank == 1):
                count += 11
            else:
                count += card.rank

        #deduct 10 points for the ace
        for card in self.cards:
            if count <= 21:
                break
            elif (card.rank == 1):
                count -= 9

        return count

    # does the player have 21 points or not
    def has_blackjack(self):
        return (len(self.cards) == 2) and (self.get_points() == 21)

    # complete the code so that the cards and points are printed
    def __str__(self):
        hand = ''
        for item in self.cards:
            hand += str(item) + ' '
        return hand + '- ' + str(self.get_points()) + ' points'


class Dealer(Player):

    def __init__(self,cards):
        Player.__init__(self, cards)
        self.show_one_card = True

    #overrides the hit function in the parent class
    #if the points are < 17, hit, after that allow all of the cards to be shown
    def hit(self, deck):
        self.show_one_card = False
        while self.get_points() < 17:
            self.cards.append(deck.deal())


    #just return one card if it's not hit yet
    def __str__(self):
        if self.show_one_card:
            return str(self.cards[0])
        else:
            return Player.__str__(self)

class Blackjack(object):

    def __init__(self, num_players = 1):
        self.deck = Deck()
        self.deck.shuffle()
        self.num_players = num_players
        self.player_list = []

        for i in range(num_players):
            hand = Player([self.deck.deal(), self.deck.deal()])
            self.player_list.append(hand)


        #create the dealer
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])

    def play(self):
        #print cards that each player has
        for i in range(len(self.player_list)):
            print ('Player '+str(i+1)+' : '+ str(self.player_list[i]))

        #dealers hand
        print ('Dealer: ' + str(self.dealer))
        print ()

        player_points = []
        for i in range(self.num_players):
            if not self.player_list[i].has_blackjack():
                while True:
                    choice = input('Player ' + str(i+1) +', do you want to hit? [y / n]: ')
                    if choice in ('y', 'Y'):
                        (self.player_list[i]).hit(self.deck.deal())
                        points = self.player_list[i].get_points()
                        print('Player ' + str(i + 1) + ': ' + str(self.player_list[i]))
                        if points >= 21:
                            break
                    else:
                        break
            if self.player_list[i].has_blackjack():
                player_points.append(100)
            else:
                player_points.append(self.player_list[i].get_points())
            print ()

        #dealer hits
        self.dealer.hit(self.deck)
        if self.dealer.has_blackjack():
            dealerPoints = 100
        else:
            dealerPoints = (self.dealer).get_points()
        print('Dealer: ' + str(self.dealer) + ' - ' + str(dealerPoints))
        print ()

        i = 0
        if ((dealerPoints > 21) and (dealerPoints != 100)):
            for item in player_points:
                if item == 100:
                    print (print('Player ' + str(i + 1) + ' wins'))
                elif item > 21:
                    print('Player ' + str(i + 1) + ' loses')
                else:
                    print('Player ' + str(i + 1) + ' wins')
                i +=1
        elif dealerPoints < 21:
            for item in player_points:
                if (item > dealerPoints) and ((item <= 21) or (item == 100)):
                    print('Player ' + str(i + 1) + ' wins')
                elif item == dealerPoints:
                    print('Player ' + str(i + 1) + ' ties')
                else:
                    print('Player ' + str(i + 1) + ' loses')
                i += 1
        elif dealerPoints == 100:
            for item in player_points:
                if item == 100:
                    print('Player ' + str(i + 1) + ' ties')
                else:
                    print('Player ' + str(i + 1) + ' loses')
                i+=1
        else:
            i = 0
            for item in player_points:
                if item == 100:
                    print('Player ' + str(i + 1) + ' wins')
                elif item == dealerPoints:
                    print('Player ' + str(i + 1) + ' ties')
                else:
                    print('Player ' + str(i + 1) + ' loses')
                i += 1





def main ():
    numPlayers = eval (input ('Enter number of players: '))

    while (numPlayers < 1 or numPlayers > 6):
        numPlayers = eval (input ('Enter number of players: '))
    print ()

    game = Blackjack (numPlayers)
    game.play()

main()
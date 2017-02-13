#  File: Poker.py

#  Description: Poker Game

#  Student's Name: Raza Retiwala

#  Student's UT EID: mrr2975

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 51920

#  Date Created: 2/10/17

#  Date Last Modified:

import random

class Card(object):

    RANKS = (2,3,4,5,6,7,8,9,10,11,12,13,14)

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
        if (self.rank == 14):
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

class Poker(object):

    #initialize
    def __init__(self, num_players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        numcards_in_hand = 5

        #hand the cards out to the players
        for i in range(num_players):
            self.players.append([])

        for i in range(numcards_in_hand):
            #for however many cards you want to give to each players
            for k in range(len(self.players)):
                #runs through every player and appends the top of the deck
                self.players[k].append(self.deck.deal())


    def play(self):

        #sort the hand of each players
        for i in range(len(self.players)):
            #sorts the hand
            sortedHand = sorted(self.players[i], reverse = True)

            #creates string object for output
            self.players[i] = sortedHand[:]
            hand = ''
            for item in self.players[i]:
                hand += str(item) + ' '

            #outputs
            print('Player ' + str(i + 1) + " : " + hand)

        #determine the points of each player
        player_points = []
        points = {10: "Royal Flush", 9:"Straight Flush", 8:"Four of a Kind", 7:'Full House', 6:'Flush', 5:'Straight', 4:'Three of a Kind', 3:"Two Pair", 2:'One Pair', 1:'High Card'}
        classifications = []

        for hands in self.players:
            # classifies each hand by it's type, gets the point for the cards
            point = Poker.check_classification(self, hands)
            classifications.append(point)

            #sorts the hand, strips all the suits for the point system, reverses it.
            hand = sorted(self.strip_hand(hands), reverse = True)

            #calculates the totals
            total = self.count_points(hand, point)
            player_points.append(total)

        item = max(player_points)

        print ()

        for i in range(len(classifications)):
            print ("Player", str(i+1) + ' :', points[classifications[i]])

        print ()
        print ("Player", str(player_points.index(item) + 1), "wins." )

    def count_points(self, hand, point):
        if point == 8:
            if hand.count(hand[0]) == 4:
                c1 = hand[0]
                c5 = hand[4]
            else:
                c1 = hand[4]
                c5 = hand[0]

            c2 = c1
            c3 = c1
            c4 = c1

            return point * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
        elif point == 7:
            if hand.count(hand[0]) == 3:
                c1 = hand[0]
                c5 = hand[3]

            else:
                c1 = hand[2]
                c5 = hand[0]

            c2 = c1
            c3 = c1
            c4 = c5
            return point * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5
        elif point == 4:
            if hand.count(hand[0]) == 3:
                c1 = hand[0]
                c2 = c1
                c3 = c1
                c4 = hand[3]
                c5 = hand[4]
            elif hand.count(hand[1]) == 3:
                c1 = hand[1]
                c2 = c1
                c3 = c1
                c4 = hand[0]
                c5 = hand[4]
            elif hand.count(hand[2]) == 3:
                c1 = hand[2]
                c2 = c1
                c3 = c1
                c4 = hand[0]
                c5 = hand[1]

            return point * 13 ** 5 + c1 * 13 ** 4 + c2 * 13 ** 3 + c3 * 13 ** 2 + c4 * 13 + c5
        elif point == 3:
            if hand.count(hand[0]) == 2:
                if hand.count(hand[2]) == 2:
                    c1 = hand[0]
                    c2 = c1
                    c3 = hand[2]
                    c4 = c3
                    c5 = hand[4]
                elif hand.count(hand[3]) == 2:
                    c1 = hand[0]
                    c2 = c1
                    c3 = hand[3]
                    c4 = c3
                    c5 = hand[2]
            elif hand.count(hand[1]) == 2:
                c1 = hand[1]
                c2 = c1
                c3 = hand[3]
                c4 = c3
                c5 = hand[0]

            return point * 13 ** 5 + c1 * 13 ** 4 + c2 * 13 ** 3 + c3 * 13 ** 2 + c4 * 13 + c5


        elif point == 2:
            if hand.count(hand[0]) == 2:
                c1 = hand[0]
                c2 = c1
                c3 = hand[2]
                c4 = hand[3]
                c5 = hand[4]
            if hand.count(hand[1]) == 2:
                c1 = hand[1]
                c2 = c1
                c3 = hand[0]
                c4 = hand[3]
                c5 = hand[4]
            if hand.count(hand[2]) == 2:
                c1 = hand[2]
                c2 = c1
                c3 = hand[0]
                c4 = hand[1]
                c5 = hand[4]
            if hand.count(hand[3]) == 2:
                c1 = hand[3]
                c2 = c1
                c3 = hand[0]
                c4 = hand[1]
                c5 = hand[2]

            return point * 13 ** 5 + c1 * 13 ** 4 + c2 * 13 ** 3 + c3 * 13 ** 2 + c4 * 13 + c5

        else:
            c1 = hand[0]
            c2 = hand[1]
            c3 = hand[2]
            c4 = hand[3]
            c5 = hand[4]

            return point * 13 ** 5 + c1 * 13 ** 4 + c2 * 13 ** 3 + c3 * 13 ** 2 + c4 * 13 + c5

    def check_classification(self, hand):

        if Poker.is_royal(self, hand):
            return 10
            #return ('Royal')
        elif Poker.is_straight_flush(self, hand):
            return 9
            #return ('Straight Flush')
        elif Poker.four_of_a_kind(self, hand):
            return 8
            #return ('Four in hand')
        elif Poker.full_house(self, hand):
            return 7
            #return ('Full House')
        elif Poker.flush(self, hand):
            return 6
            #return ('Flush')
        elif Poker.straight(self, hand):
            return 5
            #return ('Straight')
        elif Poker.three_of_a_kind(self, hand):
            return 4
            #return ('Three of a kind')
        elif Poker.two_pair(self, hand):
            return 3
            #return ('Two pair')
        elif Poker.one_pair(self, hand):
            return 2
            #return ('One pair')
        else:
            return 1
            #return ('High Card')


    def strip_hand(self, hand):
        new_hand = []
        for item in hand:
            new_hand.append(item.rank)

        new_hand_sorted = sorted(new_hand, reverse = True)
        return new_hand_sorted

    def is_royal(self, hand):
        same_suit = True

        for i in range(len(hand)-1):
            if (hand[i].suit != hand[i+1].suit):
                return False

        same_rank = True

        for i in range(len(hand)):
            same_rank = same_rank and (hand[i].rank == 14 - i)


        return (same_rank and same_suit)

    def is_straight_flush(self, hand):
        same_suit = True

        for i in range(len(hand) - 1):
            if (hand[i].suit != hand[i + 1].suit):
                return False

        numbers_ranked = True

        for i in range(len(hand) -1):
            if (hand[i].rank != (hand[i+1].rank + 1)):
                return False

        return (numbers_ranked and same_suit)

    def four_of_a_kind(self, hand):
        hand = self.strip_hand(hand)

        return ((hand.count(hand[0]) == 4) or (hand.count(hand[4]) == 4))

    def full_house(self, hand):
        hand = self.strip_hand(hand)

        return (hand.count(hand[0]) == 3 and hand.count(hand[4]) == 2) or (hand.count(hand[4]) == 3 and hand.count(hand[0]) == 2)


    def flush(self, hand):
        for i in range(len(hand) -1):
            if hand[i].suit != hand[i+1].suit:
                return False

        return True

    def straight(self, hand):
        hand = self.strip_hand(hand)

        for i in range(len(hand)-1):
            if (hand[i] != hand[i +1] + 1):
                return False

        return True

    def three_of_a_kind(self, hand):
        hand = self.strip_hand(hand)

        for i in range(len(hand) - 1):
            if (hand.count(hand[i]) == 3):
                return True
        return False

    def two_pair(self, hand):
        hand = self.strip_hand(hand)

        for i in range(3):
            if hand.count(hand[i]) == 2:
                if hand.count(hand[i+2]) == 2:
                    return True

        return False

    def one_pair(self, hand):
        hand = self.strip_hand(hand)

        for i in range(4):
            if hand.count(hand[i]) == 2:
                return True


def main():
    number = int(input("Enter number of players: "))

    while (number < 2) or (number > 6):
        number = int(input("Enter number of players: "))
    game = Poker(number)
    game.play()

main()
# playing with cards and testing
# Jared M.
# 2/7/2019

import random


class Card(object):
    """A playing card
    Will create a card with suit and rank"""

    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    """A hand of playing cards
    that can hold cards with suits and ranks
    they can also be added to or be taken from
    Make a list of hands before using"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """A deck of playing cards that can be populated, shuffled, and dealt from using .populate,
    .shuffle, and .deal"""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(PositionableCard(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue to deal. Out of cards!")


class PositionableCard(Card):
    """Get down to the list item with indexing then use .flip to show or hide the card"""

    def __init__(self, rank, suit, face_up=False):
        super(PositionableCard, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(PositionableCard, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


if __name__ == "__main__":
    print("You ran  this module directly (and did not import it).")
    input("\n\nPress the enter key to exit.")

#Jared McMahon
#12/6/2018
#cards

deck = []
player1_hand = []
player2_hand = []
import random

def makedeck(deck):
    """populate the deck of cards"""
    SUITS = ["hearts","diamonds","clubs","spades"]
    VALUES = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for e in SUITS:
        for i in VALUES:
            card = i+" "+e
            deck.append(card)
    return deck



def shuffledeck(deck):
    for i in range(len(deck)):
        j=random.randrange(len(deck))
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
    return deck

def dealcard(deck,player1_hand,player2_hand):
    for i in range(5):
        card = deck.pop()
        player1_hand.append(card)
        card = deck.pop()
        player2_hand.append(card)
    return player1_hand, player2_hand




def main(deck,player1_hand,player2_hand):

    player1_hand, player2_hand = dealcard(shuffledeck(makedeck(deck)),player1_hand,player2_hand)
    print("player 1's hand: ", player1_hand, "\nPlayer 2's hand: ", player2_hand)




main(deck,player1_hand,player2_hand)






























































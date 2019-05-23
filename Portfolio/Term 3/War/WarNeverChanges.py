# blackjack
# 2 players
# Brandon Robbins, Jared McMahon, Parker Gowans, Logan Douglas , Kyle Baldwin(Random Kid)
# 02/25/19

#############################################################################################

# imports

import cards, games, random


class War_Hand(cards.Hand):

    """ allows for the name and the place to be added for each player and sets the names of the players"""

    def __init__(self, name, place):
        super(War_Hand, self).__init__()
        self.name = name
        self.place = place

    def __str__(self):
        """changes the string to display how many cards you have and display what is in your hand"""

        rep = self.name + ":\t" + str(len(self.cards))
        return rep


class War_Player(War_Hand):

    """win battle displays the winner
    lose_game return if they lost
     determines who wins the battle such as lose and win
    """

    def win_battle(self):
        print(self.name, "Won the fight")
        return self.place

    def lose_game(self):
        if len(self.cards) == 0:
            return 1
        return 0


class War_Deck(cards.Deck):

    """uses war card for value system
    Dominic: Uses the set value system for the game of war"""

    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                self.cards.append(War_Card(rank, suit))


class War_Card(cards.Card):
    """value for each of the cards to see which is greater
     sets up the value system for the game of war"""

    ACE_VALUE = 1


    @property
    def value(self):
        if self.face_up:
            v = War_Card.RANKS.index(self.rank) + 1
        else:
            v = None
        return v

    def __str__(self):
        rep = self.rank + self.suit
        return rep






class War_Field(cards.Hand):
    """Sets up the field which is where cards are played and determined which is bigger """

    @property
    def winner(self):

        #returns who won the battle or if it was a tie
        winner = None

        #special condition for Ace card and King Card
        if self.cards[0].value == 1 and self.cards[1].value == 13:
            winner = 0
            return winner

        elif self.cards[1].value == 1 and self.cards[0].value == 13:
            winner = 1
            return winner

        # normal checks for who wins
        elif self.cards[0].value > self.cards[1].value:
            winner = 0

        elif self.cards[0].value < self.cards[1].value:
            winner = 1

        elif self.cards[0].value == self.cards[1].value:
            winner = "tie"
        return winner


    # push cards to the war pot
    def give_to_pot(self, target):
        for i in range(len(self.cards)):
            self.give(self.cards[0], target)


class War_Pot(cards.Hand):
    def __init__(self, winner=None):
        super(War_Pot, self).__init__()
        self.winner = winner


    def give_winner(self):
        #Gives cards to winner if not a tie
        for card in range(len(self.cards)):
            self.give(self.cards[0], self.winner)




class War_Game(object):

    """Holds rules and actions in the flesh of the game"""

    # Sets up attributes
    def __init__(self, names):
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()
        self.player1 = War_Player(names[0], 0)
        self.player2 = War_Player(names[1], 1)
        self.players = [self.player1, self.player2]
        self.pot = War_Pot()
        self.field = War_Field()

    def battle(self):

        """Creates the scenario that evaluates the winner"""

        # Players play card into the field
        self.player1.give(self.player1.cards[0], self.field)
        self.player2.give(self.player2.cards[0], self.field)
        print(self.field)
        winner = self.field.winner
        self.field.give_to_pot(self.pot)
        if winner == "tie":

            for i in range(1):

                if len(self.player1.cards) == 0:
                    break

                for i in range(3):

                    try:
                        self.player1.give(self.player1.cards[0], self.pot)

                    except:
                        print("player has no cards left for war will use last card")
                        self.pot.give(self.pot.cards[-1], self.player1)

                        break

            for i in range(1):
                if len(self.player2.cards) == 0:
                    break

                for i in range(3):
                    try:
                        self.player2.give(self.player2.cards[0], self.pot)

                    except:
                        print("player has no cards left for war and will use last card")
                        self.pot.give(self.pot.cards[-1], self.player2)

                        break

# Choices the winner based on highest card

            print("A war has started number of cards in pot is:", len(self.pot.cards))
            if len(self.player2.cards) != 0 and len(self.player1.cards) != 0:
                self.battle()

        else:  # This  is the winning condition for giving the cards to the tie winner
            self.players[winner].win_battle()
            self.pot.winner = self.players[winner]
            self.pot.give_winner()


    def play(self):
        """Sets rules and runs game"""
        self.deck.deal(self.players, 26)
        win=""
        round = 0

        while win == "":
            round = round + 1
            print("Round ", round)
            random.shuffle(self.player1.cards)
            random.shuffle(self.player2.cards)
            print(self.player1)
            print(self.player2)
            self.battle()
            lose1 = self.player1.lose_game()
            lose2 = self.player2.lose_game()
            if lose1 == 1 and lose2 == 1:
                win = "Tie, Nobody is a winner everyone sucks"
            elif lose1 == 1:
                win = self.player2.name
            elif lose2 == 1:
                 win = self.player1.name
            input("press enter to continue")
        print(win, "Won The Game You Murdered People")


def main():

    name1 = games.name_check("enter player 1's name (no numbers)")
    name2 = games.name_check("enter player 2's name (no numbers)")
    names = [name1, name2]

    game = War_Game(names)

    game.play()








main()

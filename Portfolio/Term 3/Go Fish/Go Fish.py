#Jared M.
#Go Fish
#3/15/2019

import cards

class GFcards(cards.Card):

    @property
    def value(self):
        v = GFcards.RANKS.index(self.rank) + 1
        return v


class GFdeck(cards.Deck):

    def populate(self):
        for suit in GFcards.SUITS:
            for rank in GFcards.RANKS:
                self.cards.append(GFcards(rank, suit))


class GFplayer(cards.Hand):

    def __init__(self, name):
        super(GFplayer, self).__init__()
        self.name = name
        self.matches = cards.Hand()

    def request(self):
        while True:
            request = input("What card are you looking for?")
            for card in self.cards:
                request = request.upper()
                if card.rank == request:
                    return request

            print("you can only ask for cards that you are already holding in your hand.")

    def draw_GoFish(self, request, otherHand, deck):
        requested = request
        goFish = True

        for card in otherHand.cards:
            if requested == card.rank:
                otherHand.give(card, self.matches)
                for selfCard in self.cards:

                    if requested == selfCard.rank:
                        self.give(selfCard, self.matches)
                        goFish = False

        if goFish:
            print("Go Fish, Draw a card off the top of the deck!")
            self.cards.append(deck.cards[0])
            deck.cards.remove(deck.cards[0])

    def checkPairs(self):
        for selfCard in self.cards:
            for card in self.cards:
                if card.value == selfCard.value and card.suit != selfCard.suit:
                    self.give(card, self.matches)
                    self.give(selfCard, self.matches)

    def getWinner(self):
        if len(self.cards) == 0:
            winner = self.name
        else:
            winner = ""
        return winner


class gofish_game(object):

    def __init__(self):
        self.deck = GFdeck()
        self.deck.populate()
        self.deck.shuffle()

        names = []
        names += input("Player 1, what is your name?: ")
        names += input("Player 2, what is your name?: ")
        self.player1 = GFplayer(names[0])
        self.player2 = GFplayer(names[1])
        self.players = [self.player1, self.player2]
        self.deck.deal(self.players, 5)

    def play(self):
        while True:
            self.player1.checkPairs()
            winner = self.player1.getWinner()
            if winner != "":
                break
            print(self.player1.name, "Your pairs are: ", self.player1.matches)
            input(self.player1.name + "'s cards are about to be shown, player 2 please look away."
                                      " Please press enter to advance\n")
            print(self.player1.name, "You have:", self.player1, "\n")
            request = self.player1.request()
            self.player1.draw_GoFish(request, self.player2, self.deck)
            winner = self.player1.getWinner()
            print(self.player1.matches, "\n\n")
            if winner != "":
                break

            self.player2.checkPairs()
            winner = self.player2.getWinner()
            if winner != "":
                break
            print(self.player2.name, "Your pairs are: ", self.player2.matches)
            input(self.player2.name + "'s cards are about to be shown, player 1 please look away."
                                      " Please press enter to advance\n")
            print(self.player2.name, "You have:", self.player2, "\n")
            request = self.player2.request()
            self.player2.draw_GoFish(request, self.player1, self.deck)
            winner = self.player2.getWinner()
            print(self.player2.matches, "\n\n")
            if winner != "":
                break

        print("Congratulations", winner)

def main():
    game = gofish_game()
    game.play()



main()



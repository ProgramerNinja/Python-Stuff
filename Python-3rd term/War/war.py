import cards, games

####Classes
class War_Card(cards.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.RANKS.index(self.rank)+1

        else:
            v = None
        return v

class War_Deck(cards.Deck):
    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                self.add(War_Card(rank, suit))

class War_Hand(cards.Hand):
    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name

class War_Player(War_Hand):
    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def war(self,pot):
        for i in range(3):
            self.give(self.cards[0],pot)

    def play(self,hand):
        top_card = self.cards[0]
        self.give(top_card,hand)


class War_Field(War_Hand):

    @property
    def check_winner(self):
        if self.cards[0].value > self.cards[1].value:
            winner = 0
        elif self.cards[0].value < self.cards[1].value:
            winner = 1
        else:
            winner = "war"
        return winner

    def give_to_pot(self,pot):
        for i in range(len(self.cards)):
            print(pot)
            print(self.cards)
            self.give(self.cards[0],pot)
class War_Pot(War_Hand):
    def give_to_winner(self,winner):
        for i in range(len(self.cards)):
            self.give(self.cards[0],winner)




class War_Game(object):
    def __init__(self,names):
        self.players = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)
        self.field = War_Field("field")
        self.pot = War_Pot("Pot")
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):

        self.deck.deal(self.players,per_hand = 26)
        for player in self.players:
            print(player.name+":",len(player.cards))

        print("Both players play a card.")
        self.players[0].play(self.field)
        self.players[1].play(self.field)

        print(self.field)
        winner = self.field.check_winner
        self.field.give_to_pot(self.pot)
        if winner == 0 or winner == 1:
            self.pot.give_to_winner(winner)
            print(self.players[winner].name)
            print(self.pot)
        else:
            self.players[0].war(self.pot)
            self.players[1].war(self.pot)
            print(self.pot)
        for player in self.players:
            print(player.name+":",len(player.cards))




        #print(player.name+"'s card is",player.cards[0])



names = []
for i in range(2):
    name = input("Enter your name: ")
    names.append(name)

game = War_Game(names)
game.play()
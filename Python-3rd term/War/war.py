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

class War_Game(object):
    def __init__(self,players):
        self.players = []
        for name in players:
            player = War_Player(name)
            self.players.append(player)

        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        self.deck.deal(self.players,per_hand = 26)
        for player in self.players:
            print(player)


players = []
for i in range(2):
    name = input("Enter your name: ")
    players.append(name)
deck = War_Deck()
hand = War_Hand(players)
game = War_Game(players)
game.play()
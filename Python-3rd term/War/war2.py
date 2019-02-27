import cards, games

class War_Card(cards.Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.RANKS.index(self.rank)+1

        else:
            v = None
        return v



import Deck


class Player():
    def __init__(self):
        self.hand = []
    
    def draw(self):
        self.hand.append(Deck.draw())

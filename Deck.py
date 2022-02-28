import Card
import numpy as np

class Deck():
    def __init__(self):
        self.cards = []
        self.colors = ['red', 'blue', 'green', 'yellow']

    def init_deck(self):
        for number in range(10): #0-9
            for color in self.colors:
                self.cards.append(Card.Card(number, color))

    def shuffle(self):
        np.random.shuffle(self.cards)
<<<<<<< HEAD
        
    def remove_card(self, card):
        self.cards.remove(card)
=======
>>>>>>> 563805ac307eafc39ccf8df3f5aed343ad645282

    def print(self):
        print("------ deck ------\n")
        for card in self.cards:
            print(card.print(), end = '')
        print()

    def draw(self):
<<<<<<< HEAD
        card = self.cards.pop(0)
        self.remove_card(card)
        return card
=======
        return self.cards.pop(0)
>>>>>>> 563805ac307eafc39ccf8df3f5aed343ad645282

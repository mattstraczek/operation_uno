from Card import Card
import numpy as np

class Deck():
    def __init__(self):
        """ Constructs a Deck object that contains a shuffled deck. """
        self.deck = []
        self.inititializeDeck()
        self.shuffle()

    def inititializeDeck(self): # will pass in Ruleset class to receive parameters for a specialized deck
        """ Initializes a standard deck of UNO cards (will be overriden with ruleset). """
        colors = ['red', 'blue', 'green', 'yellow']
        numbers = range(0,10,1)
        for color in colors:
            for number in numbers:
                if number!=0:
                    self.deck.append(Card(color, number))
                self.deck.append(Card(color, number))

    def shuffle(self):
        """ Shuffles the deck using numpy's random shuffle method. """
        np.random.shuffle(self.deck)

    def draw(self):
        """ Draws and removes the card at the top of the deck. """
        return self.deck.pop(0)

    def __str__(self):
        """ Overridden toString() method displays the deck. """
        cards = "------ DECK ------ ("
        cards += str(len(self.deck)) + " cards)\n"
        for card in self.deck:
            cards += str(card) + "\n"
        return cards

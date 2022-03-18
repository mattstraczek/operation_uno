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
        colors = ["RED","BLUE","GREEN","YELLOW"]
        cards_zero   = [Card(c,0) for c in colors]
        cards_number = [Card(c,v) for c in colors for v in range (1,10)]*2
        cards_action = [Card(c,v) for c in colors for v in ["SKIP","REVERSE","DRAW 2"]]*2
        cards_wild   = [Card("WILD",v) for v in ["CARD","DRAW 4"]]*4
        self.deck = cards_zero + cards_number + cards_action + cards_wild

    def shuffle(self):
        """ Shuffles the deck using numpy's random shuffle method. """
        np.random.shuffle(self.deck)

    def draw(self):
        """ Draws and removes the card at the top of the deck. """
        return self.deck.pop(0)
    
    def peek(self):
        """ Shows the card at the top of the deck without removing. """
        return self.deck[0]

    def __str__(self):
        """ Overridden toString() method displays the deck. """
        cards = "------ DECK ------ ("
        cards += str(len(self.deck)) + " cards)\n"
        for card in self.deck:
            cards += str(card) + "\n"
        return cards

from Card import Card
import numpy as np
import random
from Ruleset import Ruleset

class Deck():
    # ruleset  -> ruleset to apply to deck functions, default=default ruleset
    # seed     -> random seed for generating the deck, default=random

    def __init__(self, ruleset=Ruleset(), seed=None):
        """ Constructs a Deck object that contains a shuffled deck. """
        self.ruleset = ruleset
        self.deck = []
        self.inititializeDeck()
        self.shuffle(seed)

    def inititializeDeck(self): # will pass in Ruleset class to receive parameters for a specialized deck
        """ Initializes a shallow copy of the ruleset deck. """
        for card in self.ruleset.deck:
           self.deck.append(card)

    def shuffle(self, seed=None):
        """ 
        Shuffles the deck using numpy's random shuffle method. 
        If a seed does not exist, randomize normally.
        """
        if seed:
            random.seed(seed)
        random.shuffle(self.deck)

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

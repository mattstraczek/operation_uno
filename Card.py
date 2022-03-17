import pygame

class Card:
    def __init__(self, color, value):
        """ Constructs a Card object that contains the color and number of the card. """
        self.color = color
        self.value = value

    def __eq__(self, other):
        """ Overloaded equal operator compares two cards """
        return self.color == other.color and self.value == other.value

    def __str__(self):
        """ Overridden toString() method displays the card. """
        #return str(self.color) + " " + str(self.value)
        return '\n{0:<6} {1:<6}'.format(str(self.color), str(self.value))

        
    # import numpy.random as r

    # def generatePlayersCards(n_players, available_deck):
        # player_cards = r.choice(available_deck, size=2*n_players, replace=False).reshape(n_players, 2)
        # updated = np.setdiff1d(available_deck, player_cards)
        # return (player_cards, updated)
    
    # def generateDealerCards(available_deck):
        # dealer_cards = r.choice(available_deck, 5, replace=False)
        # updated = np.setdiff1d(available_deck, dealer_cards)
        # return (dealer_cards, updated)

import pygame

class Card:
    def __init__(self, color, number):
        """ Constructs a Card object that contains the color and number of the card. """
        self.color = color
        self.number = number

    def __str__(self):
        """ Overridden toString() method displays the card. """
        return str(self.color) + " " + str(self.number)
        
    # import numpy.random as r

    # def generatePlayersCards(n_players, available_deck):
        # player_cards = r.choice(available_deck, size=2*n_players, replace=False).reshape(n_players, 2)
        # updated = np.setdiff1d(available_deck, player_cards)
        # return (player_cards, updated)
    
    # def generateDealerCards(available_deck):
        # dealer_cards = r.choice(available_deck, 5, replace=False)
        # updated = np.setdiff1d(available_deck, dealer_cards)
        # return (dealer_cards, updated)

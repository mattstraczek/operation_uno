import pygame

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def print(self):
        return str(self.color) + " " + str(self.number) + "\n"
    

    # import numpy.random as r

    # def generatePlayersCards(n_players, available_deck):
        # player_cards = r.choice(available_deck, size=2*n_players, replace=False).reshape(n_players, 2)
        # updated = np.setdiff1d(available_deck, player_cards)
        # return (player_cards, updated)
    
    # def generateDealerCards(available_deck):
        # dealer_cards = r.choice(available_deck, 5, replace=False)
        # updated = np.setdiff1d(available_deck, dealer_cards)
        # return (dealer_cards, updated)
#from Ruleset import Ruleset
from Deck import Deck
from Player import Player
from AI import AI 
from Button import Button
import pygame

class Game:

    def __init__(self, num_players, num_ai):
        """ Constructs a Game object with players and AI, deals cards, and starts a game. """
        print("Initializing Game")
        self.players = []
        self.num_players = num_players
        self.num_ai = num_ai
        self.deck = Deck()
        print(self.deck, "\n") # Testing
        self.initializePlayers()
        self.deal()
        print(self.deck, "\n") # Testing
        self.difficulty = "easy"

    def initializePlayers(self):
        """ Initializes player and AI objects for the game. """
        for i in range(self.num_players):
            self.players.append(Player("Player " + str(i)))
        for i in range(self.num_ai):
            self.players.append(AI("AI " + str(i)))

    def deal(self):
        """ Deals cards to each player (including AI). """
        for i in range(7): # Deals 7 cards, but Ruleset will override this number later on
            for player in self.players:
                player.addCard(self.deck.draw())

        for player in self.players: 
            print(player) # Testing
        
    def changeNumPlayers(self, num_players):
        self.num_players = num_players

    def changeSoundEffects(self, sound):   #TODO
        return

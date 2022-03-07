#from Ruleset import Ruleset
from Deck import Deck
from Player import Player
from AI import AI 
from Button import Button
import pygame
import numpy as np

class Game:

    def __init__(self, num_players, num_ai):
        """ Constructs a Game object with players and AI, deals cards, and starts a game. """
        print("Initializing Game")
        self.players = []
        self.num_players = num_players
        self.num_ai = num_ai
        self.deck = Deck()
        # print(self.deck, "\n") # Testing
        self.initializePlayers()
        self.deal()
        # print(self.deck, "\n") # Testing
        self.difficulty = "easy"
        self.sound = "on"

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
                self.draw(player)

        # for player in self.players: 
            # print(player) # Testing
    
    def draw(self, player):
        player.addCard(self.deck.draw())


    def startGame(self):
        """ Begins a game of UNO. """
        topCard = self.deck.draw()
        np.random.shuffle(self.players)
        turn = 1
        total_players = self.num_players + self.num_ai
        winner = False
        while(not winner):
            print("Turn", turn)
            print("Top Card is", topCard)
            currPlayer = self.players[(turn-1) % total_players]
            playedCard = currPlayer.playCard(topCard)
            if not playedCard:
                self.draw(currPlayer)
            else:
                topCard = playedCard
            if currPlayer.isWin():
                winner = True
            print()
            turn+=1
        
        print(currPlayer.name, "is the winner!")

    def changeNumPlayers(self, num_players):
        """ Changes number of players """
        self.num_players = num_players

    def changeSoundEffects(self, sound):
        """ Changes if sound effects are on/off """
        self.sound = sound

    def changeDifficulty(self, difficulty):
        """ Changes difficulty of game instance """
        self.difficulty = difficulty

    def getNumPlayers(self):
        """ Returns number of players """
        return self.num_players

    def getSoundEffects(self):
        """ Returns sound (on/off) state """
        return self.sound

    def getDifficulty(self):
        """ Returns difficulty of game instance """
        return self.difficulty

    def printGameState(self):
        print('NumPlayers: ', self.num_players, '\nSound: ', self.sound, '\nDifficulty: ', self.difficulty)

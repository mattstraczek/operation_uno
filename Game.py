from Deck import Deck
from Player import Player
from AI import AI 
from Button import Button
from Ruleset import Ruleset
import pygame
import numpy as np

class Game:

    def __init__(self):
        """ Constructs a Game object with players and AI, deals cards, and starts a game. """
        self.difficulty = "easy"
        self.sound = "on"
        self.players = []
        self.num_players = 0
        self.num_ai = 0
        self.deck = []

    def initializeGame(self, num_players, num_ai):
        """ Initializes a Game object with players and AI, deals cards, and starts a game. """
        print("Initializing Game")
        self.players = []
        self.num_players = num_players
        self.num_ai = num_ai
        self.deck = Deck()
        # print(self.deck, "\n") # Testing
        self.initializePlayers()
        self.deal()
        # print(self.deck, "\n") # Testing

    def initializePlayers(self):
        print(self.num_players, self.num_ai)
        """ Initializes player and AI objects for the game. """
        for i in range(self.num_players):
            self.players.append(Player("Player " + str(i)))
        for i in range(self.num_ai):
            self.players.append(AI("AI " + str(i)))
        np.random.shuffle(self.players)
        print("Turn order:")
        for player in self.players:
            print(player.name, end=" ")  
        print()

    def deal(self):
        """ Deals cards to each player (including AI). """
        for player in self.players:
            self.draw(player, 7) # Deals 7 cards, but Ruleset will override this number later on

        # for player in self.players: 
            # print(player) # Testing
    
    def draw(self, player, num_times):
        for i in range(num_times):
            player.addCard(self.deck.draw())


    def startGame(self, num_players, num_ai):
        """ Begins a game of UNO. """
        self.initializeGame(num_players, num_ai)
        topCard = self.deck.draw()
        turn = 1
        total_players = self.num_players + self.num_ai
        winner = False
        while not winner:
            print("Turn", turn)
            print("Top Card is", topCard)
            currPlayer = self.players[(turn-1) % total_players]
            playedCard = currPlayer.playCard(topCard)
            if not playedCard:
                self.draw(currPlayer, 1)
                # play card or keep it?

            elif playedCard.color=="WILD":
                # ask player for card color
                if playedCard.value=="DRAW 4":
                    self.draw(self.players[(turn) % total_players], 4)
                    print("Added 4 cards to", self.players[(turn) % total_players].name)
                    turn+=1
                topCard.color = playedCard.value
                topCard.value = "ANY"

            else:
                if playedCard.value=="REVERSE":
                    self.players.reverse()
                    print("Reverse")
                    turn-=1

                elif playedCard.value=="SKIP":
                    print("Skipped", self.players[(turn) % total_players].name, "turn")
                    turn+=1

                elif playedCard.value=="DRAW 2":
                    self.draw(self.players[(turn) % total_players], 2)
                    print("Added 2 cards to", self.players[(turn) % total_players].name)
                    turn+=1

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

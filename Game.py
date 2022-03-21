from Deck import Deck
from Player import Player
from Ruleset import Ruleset
import numpy as np

class Game:
    # isMultiplayer -> whether or not game is multiplayer
    # ruleset       -> current game ruleset, leave empty for default ruleset
    # num_players   -> number of AI in singleplayer, total player in multiplayer, default=1
    # difficulty    -> bot difficulty, TBD
    # playerNames   -> list of player names, default=empty
    # deckSeed      -> random seed for deck generation, default=random
    # runGame       -> when false will prevent game from starting, use for debugging only

    def __init__(self, isMultiplayer, num_players=1, difficulty="Easy", playerNames=[]):
        """ Constructs a Game object with players and AI, deals cards, and starts a game. """
        self.isMultiplayer = isMultiplayer
        self.ruleset = Ruleset()
        self.deck = Deck(self.ruleset)

        # Initialize players
        self.players = []

        if isMultiplayer:
            for player in playerNames:
                self.players.append(Player(player))
                # add option to add bots to the game?
        else:
            self.players.append(Player("Player Name")) # need to fetch from profile.py class or something
            for i in range(num_players):
                self.players.append(Player("AI " + str(i), True, difficulty))
        self.deal()
        self.main_player = self.players[0]
        self.turn = 1
        self.actual_turn = 1
        np.random.shuffle(self.players)
        self.top_card = self.deck.draw()
                
    def deal(self):
        """ Deals cards to each player (including AI). """
        for player in self.players:
            self.draw(player, self.ruleset.deal_quantity) # Deals 7 cards, but Ruleset will override this number later on
        # for player in self.players: 
            # print(player) # Testing
    
    def draw(self, player, num_times):
        for i in range(num_times):
            print(player.name, "drew", self.deck.peek())
            player.addCard(self.deck.draw())

    def nextTurn(self):
        currPlayer = self.players[(self.turn-1) % len(self.players)]
        
        #currPlayer.draw()
        #if ai:
        #pickCard AI
        played_card = currPlayer.playCardAI(self.top_card)
        self.updateGameState(played_card, currPlayer)
        self.turn += 1
        self.actual_turn += 1
        #else, human
        #return
        #let gamewindow reflect changes in hand and Deck

        # #check if theres a winner 
        # if currPlayer.isWin():
        #     return currPlayer.name
        # let gamewindow reflect changes in hand and Deck

    def updateGameState(self, playedCard, currPlayer):
        total_players = len(self.players)

        if not playedCard:
            print(currPlayer.name, "skipped their turn")
        elif playedCard:
            if playedCard.value=="REVERSE":
                self.players.reverse()
                print("Turn order:", end="")
                for player in self.players:
                    print(player.name, end=" | ")  
                print()
                print("Reverse")
                self.turn = total_players - (self.turn % total_players)

            elif playedCard.value=="SKIP":
                print("Skipped", self.players[(self.turn) % total_players].name, "turn")
                self.turn+=1

            elif playedCard.value=="DRAW 2":
                self.draw(self.players[(self.turn) % total_players], 2)
                print("Added 2 cards to", self.players[(self.turn) % total_players].name)
                self.turn+=1

            elif playedCard.value=="DRAW 4":
                self.draw(self.players[(self.turn) % total_players], 4)
                print("Added 4 cards to", self.players[(self.turn) % total_players].name)
                self.turn+=1

            self.top_card = playedCard


    def updateTopCard(self, selected_card):
        self.top_card = selected_card

    def startGame(self):
        """ Begins a game of UNO. """
        np.random.shuffle(self.players)
        print("Turn order:", end="")
        for player in self.players:
            print(player.name, end=" | ")  
        print()

        topCard = self.deck.draw()
        turn = 1
        actualTurn = 1
        total_players = len(self.players)
        winner = False

        while not winner:
            print("Turn number:", turn, end=", ")
            currPlayer = self.players[(turn-1) % total_players]
            print("Actual Turn", actualTurn, ":", currPlayer)
            print("Top Card is", topCard)

            if currPlayer.isAI:
                playedCard = currPlayer.playCardAI(topCard)
                if not playedCard:
                    self.draw(currPlayer, 1)
                    playedCard = currPlayer.playCardAI(topCard)
            else:
                playedCard = currPlayer.playCardHuman(topCard, True)
                if not playedCard:
                    self.draw(currPlayer, 1)
                    playedCard = currPlayer.playCardHuman(topCard, False)

            if not playedCard:
                print(currPlayer.name, "skipped their turn")
            elif playedCard:
                if playedCard.value=="REVERSE":
                    self.players.reverse()
                    print("Turn order:", end="")
                    for player in self.players:
                        print(player.name, end=" | ")  
                    print()
                    print("Reverse")
                    turn = total_players - (turn % total_players)

                elif playedCard.value=="SKIP":
                    print("Skipped", self.players[(turn) % total_players].name, "turn")
                    turn+=1

                elif playedCard.value=="DRAW 2":
                    self.draw(self.players[(turn) % total_players], 2)
                    print("Added 2 cards to", self.players[(turn) % total_players].name)
                    turn+=1

                elif playedCard.value=="DRAW 4":
                    self.draw(self.players[(turn) % total_players], 4)
                    print("Added 4 cards to", self.players[(turn) % total_players].name)
                    turn+=1

                topCard = playedCard

            if currPlayer.isWin():
                winner = True
            print()
            turn+=1
            actualTurn+=1
        
        print(currPlayer.name, "is the winner!")

    
    def changeSoundEffects(self, sound):
        """ Changes if sound effects are on/off """
        self.sound = sound

    def getSoundEffects(self):
        """ Returns sound (on/off) state """
        return self.sound

    def printGameState(self):
        print('NumPlayers: ', self.num_players, '\nSound: ', self.sound, '\nDifficulty: ', self.difficulty)
    
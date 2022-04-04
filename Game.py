from Deck import Deck
from Player import Player
from Ruleset import Ruleset
import numpy as np

class Game:
    # isMultiplayer -> whether or not game is multiplayer
    # num_players   -> number of AI in singleplayer, total player in multiplayer, default=1
    # difficulty    -> bot difficulty, TBD
    # playerNames   -> list of player names, default=empty

    # prototype parameters: please ask Jacob if there are issues
    # ruleset       -> current game ruleset, leave empty for default ruleset 
    # deckSeed      -> random seed for deck generation, default=random
    # runGame       -> removed [depreciated]

    def __init__(self, isMultiplayer, num_players=1, difficulty="Easy", playerNames=[], ruleset=Ruleset(), deckSeed=None):
        """ Constructs a Game object with players and AI, deals cards, and starts a game. """
        if (type(isMultiplayer) != type(True) or type(num_players) != type(4) or type(difficulty) != type("test") or type(playerNames) != type([]) or type(ruleset) != type(Ruleset)):
            print("type mismatch")
    
        self.isMultiplayer = isMultiplayer
        self.ruleset = ruleset
        self.deckSeed = deckSeed
        self.deck = Deck(self.ruleset, deckSeed)

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
        self.total_players = len(self.players)
        self.main_player = self.players[0]
        self.deal()
        self.turn = 1
        self.actual_turn = 1
        np.random.shuffle(self.players)
        self.top_card = self.deck.peek()

    def deal(self):
        """ Deals cards to each player (including AI). """
        for player in self.players:
            self.draw(player, self.ruleset.deal_quantity) # Deals 7 cards, but Ruleset will override this number later on
        # for player in self.players: 
            # print(player) # Testing
    
    def draw(self, player, num_times):
        """ Passed in player draws a random card from self.deck exactly 'num_times'. """
        for i in range(num_times):
            print(player.name, "drew", self.deck.peek())
            player.addCard(self.deck.draw())

    def skipTurn(self):
        """ Updates turn count of game instance. Effectively skips a turn. """
        self.turn += 1
        self.actual_turn += 1

    def updateTurnHuman(self, curr_player, played_card):
        """ Handles the hands-on placing of a card and its game logic by a non-AI player. """
        curr_player.removeCard(played_card)
        self.updateGameState(played_card, curr_player)
        self.actual_turn += 1
        self.turn += 1

    def getCurrPlayer(self):
        """ Returns the current turn's player. """
        currPlayer = self.players[(self.turn-1) % len(self.players)]
        return currPlayer.name

    def nextTurn(self):
        """ Handles game logic for an AI-player's turn. If player is not AI, return control of program to the user by returning True. """
        currPlayer = self.players[(self.turn-1) % len(self.players)]
        if currPlayer.isAI:
            played_card = currPlayer.playCardAI(self.top_card)
            if not played_card:
                self.draw(currPlayer, 1)
                played_card = currPlayer.playCardAI(self.top_card)
            self.updateGameState(played_card, currPlayer)
            self.turn += 1
            self.actual_turn += 1
            return False
        else:
            return True

    def checkWinner(self):
        """ Checks state of the game for winner. """
        for player in self.players:
            if player.isWin():
                return True
        return False

    def updateGameState(self, playedCard, currPlayer):
        """ Core game logic for a given turn and player. Handles general cards, SKIPs, REVERSEs, and DRAWs. 
            Updates the corresponding top card of the deck. """
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
                self.turn = self.total_players - (self.turn % self.total_players)

            elif playedCard.value=="SKIP":
                print("Skipped", self.players[(self.turn) % self.total_players].name, "turn")
                self.turn+=1

            elif playedCard.value=="DRAW 2":
                self.draw(self.players[(self.turn) % self.total_players], 2)
                print("Added 2 cards to", self.players[(self.turn) % self.total_players].name)
                self.turn+=1

            elif playedCard.value=="DRAW 4":
                self.draw(self.players[(self.turn) % self.total_players], 4)
                print("Added 4 cards to", self.players[(self.turn) % self.total_players].name)
                self.turn+=1

            self.top_card = playedCard

    def changeSoundEffects(self, sound):
        """ Changes if sound effects are on/off """
        self.sound = sound

    def getSoundEffects(self):
        """ Returns sound (on/off) state """
        return self.sound

    def printGameState(self):
        print('NumPlayers: ', self.num_players, '\nSound: ', self.sound, '\nDifficulty: ', self.difficulty)
    
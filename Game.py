from Deck import Deck
from Player import Player
from Ruleset import Ruleset
import numpy as np

class Game:

    def __init__(self, isMultiplayer, num_players=2, difficulty="Easy", playerNames=[]):
        """ Constructs a Game object with players and AI, deals cards, and starts a game. """
        self.isMultiplayer = isMultiplayer
        self.deck = Deck()

        # Initialize players
        self.players = []
        if isMultiplayer:
            for player in playerNames:
                self.players.append(Player(player))
                # add option to add bots to the game?
        else:
            self.players.append(Player("Player Name"))
            for i in range(num_players):
                self.players.append(Player("AI " + str(i), True, difficulty))
        
        # Deals cards to each player
        self.deal()

        self.startGame()

    def deal(self):
        """ Deals cards to each player (including AI). """
        for player in self.players:
            self.draw(player, 7) # Deals 7 cards, but Ruleset will override this number later on
        # for player in self.players: 
            # print(player) # Testing
    
    def draw(self, player, num_times):
        for i in range(num_times):
            print(player.name, "drew", self.deck.peek())
            player.addCard(self.deck.draw())

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

    
    '''def changeSoundEffects(self, sound):
        """ Changes if sound effects are on/off """
        self.sound = sound

    def getSoundEffects(self):
        """ Returns sound (on/off) state """
        return self.sound

    def printGameState(self):
        print('NumPlayers: ', self.num_players, '\nSound: ', self.sound, '\nDifficulty: ', self.difficulty)
    '''
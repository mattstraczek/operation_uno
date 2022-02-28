<<<<<<< HEAD
import Ruleset, Deck, Player, pygame

players = []
=======
import Ruleset, Deck, Player, AI, pygame

players = []
num_players = 0
num_ai = 0
>>>>>>> 563805ac307eafc39ccf8df3f5aed343ad645282

class Game:
    def __init__(self, num_players, num_ai):
        print("Initializing Game")
<<<<<<< HEAD
        self.num_players = num_players

    def deal():
        print()

    
=======
        self.players = []
        self.num_players = num_players
        self.num_ai = num_ai
        deck = Deck.Deck()
        deck.init_deck()
        deck.shuffle()
        self.deck = deck
        self.init_players()
        self.deal()

    def init_players(self):
        for i in range(self.num_players):
            self.players.append(Player.Player("Player " + str(i)))
        for i in range(self.num_ai):
            self.players.append(AI.AI("AI " + str(i)))
    
    def deal(self):
        for i in range(7):
            for player in self.players:
                player.addCard(self.deck.draw()) # remove card from deck and add to player's hand

        for player in self.players:
            print(player)

    def initial_deal():
        return
        
    def playGame():
        return
>>>>>>> 563805ac307eafc39ccf8df3f5aed343ad645282

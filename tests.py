from Game import Game
from Deck import Deck
import unittest

from Ruleset import Ruleset

"""
How to use the unittest framework:

1. Create a function for the particular function (ex. deck drawing or game init)

2. Set up test case by running the function and init the supposed output

3. Use on of the following functions to check conditions
    - assertEqual(a, b) -> a == b
    - assertNotEqual(a, b) -> a != b
    - assertTrue(x) -> bool(x) is True
    - assertFalse(x) -> bool(x) is False
    - assertIs(a, b) -> a is b
    - assertIsNot(a, b) -> a is not b
    - assertIsNone(x) -> x is None
    - assertIsNotNone(x) -> x is not None
    - assertIn(a, b) -> a in b
    - assertNotIn(a, b) -> a not in b
    - assertIsInstance(a, b) -> isinstance(a, b)
    - assertNotIsInstance(a, b) -> not isinstance(a, b)

"""

class UnoTestCases(unittest.TestCase):

    def testInitDeck(self):
        r = Ruleset()
        self.maxDiff = None
        deck = Deck(r, 10)
        deck2 = Deck(r, 500)
        deck3 = Deck(r, 10)
        self.assertNotEqual(deck.__str__(), deck2.__str__())
        self.assertNotEqual(deck3.__str__(), deck2.__str__())
        self.assertEqual(deck.__str__(), deck3.__str__())
    
    def testShuffleDeck(self):
        r = Ruleset()
        self.maxDiff = None
        deck = Deck(r)
        original = deck.__str__()
        deck.shuffle()
        shuffled = deck.__str__()
        self.assertNotEqual(original, shuffled)
    
    def testDrawCard(self):
        r = Ruleset()
        self.maxDiff = None
        deck = Deck(r)
        originalDeckCount = len(deck.deck)
        topCard = deck.deck[0]
        original = deck.__str__()
        drawn = deck.draw()
        self.assertNotEqual(original, deck)
        self.assertEqual(topCard.__str__(), drawn.__str__())
        self.assertEqual((originalDeckCount - 1), len(deck.deck))

    def testDealCard(self):
        ruleset = Ruleset()
        game = Game(False, 4, "Easy", [], 1024, ruleset, True)
        print(len(game.players))
        self.assertTrue(len(game.players) == 4)
        for player in game.players:
            self.assertTrue(len(player.hand) == ruleset.dealQuantity)
        
        self.assertTrue(len(game.deck.deck) == len(ruleset.cardSet) - 4*ruleset.dealQuantity)

        # game = Game(0, 3)
        # testDeck = Deck()
        # self.assertTrue(len(game.players) == 3)
        # # the following assumes the game rule that the players will receive at least one card
        # self.assertTrue(len(game.players[0].hand) > 0)
        # self.assertTrue(len(game.deck.deck) < len(testDeck.deck))

        # game = Game(7, 0)
        # testDeck = Deck()
        # self.assertTrue(len(game.players) == 7)
        # # the following assumes the game rule that the players will receive at least one card
        # self.assertTrue(len(game.players[0].hand) > 0)
        # self.assertTrue(len(game.deck.deck) < len(testDeck.deck))

        # game = Game(1, 1)
        # testDeck = Deck()
        # self.assertTrue(len(game.players) == 2)
        # # the following assumes the game rule that the players will receive at least one card
        # self.assertTrue(len(game.players[0].hand) > 0)
        # self.assertTrue(len(game.deck.deck) < len(testDeck.deck))

    # def testChangePlayers(self):
    #     game = Game(1, 6)
    #     game2 = Game(4, 0)
    #     self.assertTrue(game.num_players == 1)
    #     self.assertTrue(game2.num_players == 4)
    #     game.changeNumPlayers(4)
    #     game2.changeNumPlayers(0)
    #     self.assertTrue(game.num_players == 4)
    #     self.assertTrue(game2.num_players == 0)



if __name__ == '__main__':
    unittest.main()
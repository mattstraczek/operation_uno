from Game import Game
from Deck import Deck
import unittest
import numpy as np
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
        self.maxDiff = None
        r = Ruleset()
        deck = Deck(r, 10)
        deck2 = Deck(r, 500)
        deck3 = Deck(r, 10)
        self.assertNotEqual(deck.__str__(), deck2.__str__())
        self.assertNotEqual(deck3.__str__(), deck2.__str__())
        self.assertEqual(deck.__str__(), deck3.__str__())
    
    def testShuffleDeck(self):
        self.maxDiff = None
        r = Ruleset()
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
        for i in range(10):
            game = TestHelperFunctions.dealHelper(i)
            ruleset = Ruleset()
            # players array should be one more than the AIcount (i)
            self.assertTrue(len(game.players) == i + 1)
            # all hands should be at the appropriate amount
            for player in game.players:
                print("player hand: " + str(len(player.hand)) + " | " + str(ruleset.dealQuantity))
                self.assertTrue(len(player.hand) == ruleset.dealQuantity)
            # deck length should be reduced by the amount of players times the drawQuantity
            self.assertTrue(len(game.deck.deck) == len(ruleset.cardSet) - (i + 1)*ruleset.dealQuantity)



class TestHelperFunctions():
    def dealHelper(AIcount):
        ruleset = Ruleset()
        game = Game(False, ruleset, AIcount, "Easy", [], np.random.randint(0, 1000), False)
        return game

if __name__ == '__main__':
    unittest.main()
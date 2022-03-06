from Game import Game
from Deck import Deck
import unittest

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

class UnoTestCases:

    def testInitDeck():
        deck = Deck()
        deck2 = Deck()
        unittest.assertNotEqual(deck.__str__(), deck2.__str__())



if __name__ == '__main__':
    unittest.main()
import pygame

class Card:
    def __init__(self, color, value):
        """ Constructs a Card object that contains the color and number of the card. """
        self.color = color
        self.value = value

    def __eq__(self, other):
        """ Overloaded equal operator compares two cards """
        return self.color == other.color and self.value == other.value

    def __str__(self):
        """ Overridden toString() method displays the card. """
        #return str(self.color) + " " + str(self.value)
        return str(self.color) + " " + str(self.value)
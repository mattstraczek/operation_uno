import pygame

class Card:
    def __init__(self, color, number):
        """ Constructs a Card object that contains the color and number of the card. """
        self.color = color
        self.number = number

    def __str__(self):
        """ Overridden toString() method displays the card. """
        return str(self.color) + " " + str(self.number)
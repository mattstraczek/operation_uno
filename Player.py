from Card import Card
from Ruleset import Ruleset
import numpy as np

class Player():
    def __init__(self, name, isAI=False, difficulty="Easy"):
        """ Constructs a AI object with a name and an empty hand. """
        # print("Creating", name) # Testing
        self.name = name
        self.hand = []
        self.isAI = isAI
        self.difficulty = difficulty
    
    def addCard(self, card):
        """ Adds a card to the AI's hand. """
        # print("Adding", card, "to", self.name, "'s hand") # Testing
        self.hand.append(card)

    def playCard(self, topCard):
        if self.isAI:
            return self.playCardAI(topCard)
        else:
            return self.playCardAI(topCard) # change to human later
        

    def playCardAI(self, topCard):
        """ AI plays a card depending on difficulty level """
        # Add different difficulties
        for card in self.hand:
            if Ruleset.isValid(card, topCard):
                self.hand.remove(card)
                if card.color=="WILD":
                    card = Card(self.maxColor(), card.value)
                print(self.name, "is placing", card)
                return card

    def playCardHuman(self, topCard):
        return
        

    def maxColor(self):
        """ Finds the color that the AI has the most of. """
        colors = [0] * 4
        for card in self.hand:
            if card.color=="RED":
                colors[0]+=1
            elif card.color=="BLUE":
                colors[1]+=1
            elif card.color=="GREEN":
                colors[2]+=1
            elif card.color=="YELLOW":
                colors[3]+=1
        
        maxIndex = np.argmax(colors)
        if maxIndex==0:
            return "RED"
        elif maxIndex==1:
            return "BLUE"
        elif maxIndex==2:
            return "GREEN"
        elif maxIndex==3:
            return "YELLOW"


    def isWin(self):
        """ Returns True if the player has an empty hand (won the game) and false otherwise """
        return not self.hand

    def displayHand(self):
        """ Returns a string containing all cards in the player's hand. """
        cards = ""
        for card in self.hand:
            if not card==self.hand[0]:
                cards += " | "
            cards += str(card)
        return cards

    def __str__(self):
        """ Overridden toString() method displays AI's name and hand. """
        return str(self.name) + "'s hand: " + str(self.displayHand())

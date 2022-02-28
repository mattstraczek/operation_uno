from Card import Card

class Player():
    def __init__(self, name):
        """ Constructs a Player object with a name and an empty hand. """
        print("Creating", name) # Testing
        self.name = name
        self.hand = []
    
    def addCard(self, card):
        """ Adds a card to the player's hand. """
        print("Adding", card, "to", self.name, "'s hand") # Testing
        self.hand.append(card)

    def playCard():
        """ Play's the card and removes from player's hand. """
        
        return

    def displayHand(self):
        """ Returns a string containing all cards in the player's hand. """
        cards = ""
        for card in self.hand:
            cards += str(card) + ', '
        return cards

    def __str__(self):
        """ Overridden toString() method displays player's name and hand. """
        return str(self.name) + "'s hand: " + str(self.displayHand())
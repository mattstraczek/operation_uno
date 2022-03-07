from Card import Card

class AI():
    def __init__(self, name):
        """ Constructs a AI object with a name and an empty hand. """
        # print("Creating", name) # Testing
        self.name = name
        self.hand = []
    
    def addCard(self, card):
        """ Adds a card to the AI's hand. """
        print("Adding", card, "to", self.name, "'s hand") # Testing
        self.hand.append(card)

    def playCard(self, topCard):
        """ Play's the card and removes from player's hand. """
        print(self)
        for card in self.hand:
            if card.color == topCard.color or card.number == topCard.number:
                self.hand.remove(card)
                print(self.name, "is placing", card)
                return card

    def isWin(self):
        """ Returns True if the player has an empty hand (won the game) and false otherwise """
        return not self.hand

    def displayHand(self):
        """ Returns a string containing all cards in the player's hand. """
        cards = ""
        for card in self.hand:
            cards += str(card) + ', '
        return cards

    def __str__(self):
        """ Overridden toString() method displays AI's name and hand. """
        return str(self.name) + "'s hand: " + str(self.displayHand())

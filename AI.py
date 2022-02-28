import Deck

name = ""

class AI():
    def __init__(self, name):
        print("Creating", name)
        self.name = name
        self.hand = []
    
    def addCard(self, card):
        print("Adding", card, "to", self.name, "'s hand")
        self.hand.append(card)

    def displayHand(self):
        handCards = ""
        for card in self.hand:
            handCards += (card.cardInfo() + ", ")
        return handCards

    def __str__(self):
        return str(self.name) + "'s hand: " + str(self.displayHand())
       

    def playCard():
        return
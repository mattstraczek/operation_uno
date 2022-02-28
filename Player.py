import Deck

class Player():
    def __init__(self):
        self.hand = []
    
    def draw(self):
        self.hand.append(Deck.draw())
        
class Player():
    def __init__(self, name):
        self.name = str(name)
        print("Creating", name)
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

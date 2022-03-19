from Card import Card
class Ruleset():
    # cardSet      -> unshuffled set of cards to include when generating deck
    # dealQuantity -> number of cards each player starts with, default=7
    def __init__(self, cardSet=[], dealQuantity=7):
        self.dealQuantity = dealQuantity
        self.cardSet = cardSet
        
        # generate default deck if cardSet is left to default value 
        if self.cardSet == []:
            colors = ["RED","BLUE","GREEN","YELLOW"]
            cards_zero   = [Card(c,0) for c in colors]
            cards_number = [Card(c,v) for c in colors for v in range (1,10)]*2
            cards_action = [Card(c,v) for c in colors for v in ["SKIP","REVERSE","DRAW 2"]]*2
            cards_wild   = [Card("WILD",v) for v in ["CARD","DRAW 4"]]*4
            self.cardSet = cards_zero + cards_number + cards_action + cards_wild

    def isValid(card, topCard):
        if card.color=="WILD":
            return True
        elif str(card.value) == str(topCard.value):
            return True
        return card.color == topCard.color

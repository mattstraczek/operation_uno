from Card import Card
class Ruleset():
    # cardSet      -> unshuffled set of cards to include when generating deck
    # dealQuantity -> number of cards each player starts with, default=7
    def __init__(self):
        self.initialize_standard_game() # by default, but can be overwritten with new rules

    def isValid(self, card, topCard):
        if card.color=="WILD":
            return True
        elif str(card.value) == str(topCard.value):
            return True
        return card.color == topCard.color

    def initialize_standard_game(self):
        colors = ["RED","BLUE","GREEN","YELLOW"]
        cards_zero   = [Card(c,0) for c in colors]
        cards_number = [Card(c,v) for c in colors for v in range (1,10)]*2
        cards_action = [Card(c,v) for c in colors for v in ["SKIP","REVERSE","DRAW 2"]]*2
        cards_wild   = [Card("WILD",v) for v in ["CARD","DRAW 4"]]*4
        self.deck = cards_zero + cards_number + cards_action + cards_wild
        self.deal_quantity = 7



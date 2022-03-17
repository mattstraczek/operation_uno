class Ruleset():

    def __init__(self):
        return

    def isValid(card, topCard):
        if card.color=="WILD":
            return True
        elif card.value == topCard.value:
            return True
        return card.color == topCard.color

    def StandardGame(self):
        return
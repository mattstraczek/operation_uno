#from Ruleset import Ruleset
from Deck import Deck
from Player import Player
from AI import AI 
from Button import Button
import pygame
import numpy as np

class Game:

    def __init__(self, num_players, num_ai):
        """ Constructs a Game object with players and AI, deals cards, and starts a game. """
        print("Initializing Game")
        self.players = []
        self.num_players = num_players
        self.num_ai = num_ai
        self.deck = Deck()
        print(self.deck, "\n") # Testing
        self.initializePlayers()
        self.deal()
        print(self.deck, "\n") # Testing
        self.difficulty = "easy"

    def initializePlayers(self):
        """ Initializes player and AI objects for the game. """
        for i in range(self.num_players):
            self.players.append(Player("Player " + str(i)))
        for i in range(self.num_ai):
            self.players.append(AI("AI " + str(i)))

    def deal(self):
        """ Deals cards to each player (including AI). """
        for i in range(7): # Deals 7 cards, but Ruleset will override this number later on
            for player in self.players:
                player.addCard(self.deck.draw())

        for player in self.players: 
            print(player) # Testing

    def changeDifficulty(self, difficulty):
        self.difficulty = difficulty
        
    '''def playGame():
        """ Begins a game of UNO. """
        topCard = deck.deal()
        print("Current card is", str(topCard))
        np.random.shuffle(self.players)
        turn = 0
        playersLength = len(players)
        winner = false
        while(~winner):
            self.players[turn%playersLength].playCard()'''

    def changeNumPlayers(self, num_players):
        self.num_players = num_players

    def changeSoundEffects(self, sound):   #TODO
        return

    def playGame(self):
        # changable constants -----

        screen_x = 800
        screen_y = 600
        background_size = (screen_x, screen_y)

        colors = {
            "white": (255, 255, 255),
            "grey": (230, 230, 230),
            "green": (0,255,0),
            "blue": (0,0,255),
            "red": (255,0,0),
            "dark_red": (139,0,0),
            "crimson": (246,26,26),
            "black": (0, 0, 0),
            "purple": (48, 25, 52),
            "yellow": (255, 255, 0)
        }

        background_color = colors["purple"]

        # functions -------------------------

        def displayWindow(window):
            window.fill(background_color) # change color if you want

        def displayMessage(msg, color, dest, display):
            screen_text = font.render(msg, True, color)
            display.blit(screen_text, dest)

        # window set up
        pygame.init()
        window = pygame.display.set_mode(background_size)
        pygame.display.set_caption('Operation-Uno')

        # text and font
        font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', 60)
        button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', 22)

        exit_button = Button(colors["green"], [100, 125], [100, 50], button_font, "Back", green, (37,186,176))

        run = True
        while run:
            mouse_pos = pygame.mouse.get_pos()

            # ---------------- updates -----------------
            exit_button.updateButton(mouse_pos, window)

            for event in pygame.event.get(): 
                # ----------- ongoing checks (controls, updates, etc) ----------
                
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.isHovered():
                        print('Pressed Exit Button')
                        return
                        
            
            # ---------- renders --------------
            displayWindow(window)
            displayMessage("OPERATION UNO", colors["white"], [150, 25], window)
            exit_button.displayButton(window)
            
            # ----------- final update --------------
            pygame.display.update()

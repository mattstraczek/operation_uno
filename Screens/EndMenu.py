import pygame, sys
from Components import Button, Message
from Screens import PlayMenu
import Game
import Ruleset
import Deck

class EndMenu():
    def __init__(self, winner, width=800, height=600, bg_color=pygame.Color("Purple")):
        """ Initializes the End Menu with default size of 800x600 and a purple background """
        self.title = "End Menu"
        self.w = width
        self.h = height
        self.bg_color = bg_color
        self.winner = winner

    def display(self):
        """ Displays the End Menu and its components """
        # Initializes the main screen width and title
        end_menu = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption(self.title)

        # Determines the font size based on screen dimensions
        if self.w <= self.h:
            fontSize = self.w // 50
        else:
            fontSize = self.h // 20

        text_font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', fontSize*2)
        end_msg = Message.Message(end_menu, "GAME OVER", text_font, pygame.Color("Blue"), [self.w/2, self.h/4])
        win_msg = Message.Message(end_menu, winner + " WINS!", text_font, pygame.Color("Green"), [self.w/2, self.h/5])
        # loss_msg = Message.Message(end_menu, "YOU LOSE!", text_font, pygame.Color("Red"), [self.w/2, self.h/5])

        # Initialize colors
        red    = pygame.Color("Red")
        yellow = pygame.Color("Yellow")
        green  = pygame.Color("Green")
        blue   = pygame.Color("Blue")
        white  = pygame.Color("White")

        # Initializes buttons
        button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize)
        back_button = Button.Button(end_menu, blue, [self.w*7/8,self.h*7/8], [fontSize*5, fontSize*2.5], button_font, "Back", white, yellow)

        # Initialize Ruleset/Cardset
        # cardset = Deck.Deck()
        # ruleset = Ruleset.Ruleset()
        
        current = True
        while current:
            # Fills the screen with the background color
            end_menu.fill(self.bg_color)

            # Registers button presses and changes screens accordingly
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.isHovered():
                        play_menu = PlayMenu.PlayMenu(self.w, self.h)
                        play_menu.display()
                        pygame.display.quit()
                        return

            if(self.winner == player):
                win_msg.displayMessage()
            # else:
            #     loss_msg.displayMessage()
            
            # Displays the components of main menu
            back_button.displayButton()
            
            # Displays end_msg
            end_msg.displayMessage()

            # Refreshes the screen to update the changes
            pygame.display.update()
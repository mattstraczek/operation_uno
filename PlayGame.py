#from Ruleset import Ruleset
from Deck import Deck
from Player import Player
from AI import AI 
from Button import Button
from Game import Game
import pygame

class PlayGame:
    # This will serve as additional menu functionality
    def playGameMenu(self):
        # changeable constants -----
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
            "black": (0,0,0),
            "purple": (48,25,52),
            "yellow": (255,255,0)
        }

        background_color = colors["blue"]

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

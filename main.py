import Ruleset, Game, Deck, Button, pygame
from Utilities import *

# changable constants -----

screen_x = 800
screen_y = 600
background_size = (screen_x, screen_y)
background_color = (38, 38, 38)

white = (255, 255, 255)
grey = (230, 230, 230)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)
black = (0, 0, 0)

# functions -------------------------

def displayWindow(window):
    window.fill(background_color) # change color if you want

def displayMessage(msg, color, dest, display):
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, dest)

# main ----------------------------

if __name__ == '__main__':
    run = True
    # instantiate our needed classes here
    d = Deck.Deck()
    d.init_deck()
    d.print()
    d.shuffle()
    d.print()
    
    # window set up
    pygame.init()
    window = pygame.display.set_mode(background_size)
    pygame.display.set_caption('Operation-Uno')

    # text and font
    font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', 48)
    button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', 22)

    # buttons
    menu_button = Button.Button(grey, [100, 100], [100, 35], button_font, "Test", grey)

    #  game loop -------------------------
    
    while run:
        for event in pygame.event.get(): 
            # ----------- ongoing checks (controls, updates, etc) ----------
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and menu_button.buttonHover(mouse_pos):
                print('Pressed')
                
        
        # ---------- renders --------------
        displayWindow(window)
        displayMessage("Operation-Uno", white, [200, 25], window)
        menu_button.displayButton(window)
        
        # ----------- update --------------
        pygame.display.update()

# run main


import Ruleset, Game, Deck, Button, pygame

# changable constants -----

screen_x = 800
screen_y = 600
background_size = (screen_x, screen_y)

white = (255, 255, 255)
grey = (230, 230, 230)
green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)
dark_red = (139,0,0)
crimson = (246,26,26)
black = (0, 0, 0)
purple = (48, 25, 52)
yellow = (255, 255, 0)

background_color = purple

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
    font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', 60)
    button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', 22)

    # buttons
    play_button = Button.Button(green, [100, 125], [100, 50], button_font, "Play", green, (37,186,176))
    diff_button = Button.Button(red, [100, 200], [200, 50], button_font, "Difficulty Mode", red, (37,186,176))
    num_players_button = Button.Button(blue, [100, 275], [200, 50], button_font, "Number Players", blue, (37,186,176))
    sound_button = Button.Button(yellow, [100, 350], [200, 50], button_font, "Sound Effects", yellow, (37,186,176))

    #  game loop -------------------------

    while run:
        for event in pygame.event.get(): 
            # ----------- ongoing checks (controls, updates, etc) ----------
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.updateButton(mouse_pos, window):
                    play_button.buttonClicked(True)
                    print('Pressed Play Button')
                if diff_button.updateButton(mouse_pos, window):
                    diff_button.buttonClicked(True)
                    print('Pressed Difficulty Button')
                if num_players_button.updateButton(mouse_pos, window):
                    num_players_button.buttonClicked(True)
                    print('Pressed Num Players Button')
                if sound_button.updateButton(mouse_pos, window):
                    sound_button.buttonClicked(True)
                    print('Pressed Sound Button')

                
        
        # ---------- renders --------------
        displayWindow(window)
        displayMessage("OPERATION UNO", white, [150, 25], window)
        play_button.displayButton(window)
        diff_button.displayButton(window)
        num_players_button.displayButton(window)
        sound_button.displayButton(window)
        
        # ----------- update --------------
        pygame.display.update()

# run main

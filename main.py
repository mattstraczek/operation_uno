import pygame
from Screens import MainMenu, GameWindow
from Game import Game
#from Game import Game
#from PlayGame import PlayGame
#from Difficulty import Difficulty
#from NumPlayers import NumPlayers
#from SoundEffects import SoundEffects

# from pygame import mixer
# from mixer import music
import os
import pygame.mixer as mixer
from pygame.mixer import music as msound

if __name__ == '__main__':
    pygame.init()
    info = pygame.display.Info()
    # do some math to establish a 2:1 screen dimension
    screen_w, screen_h = info.current_w, info.current_h
    screen_buffer_w, screen_buffer_h = 0, 0 
    if info.current_w / info.current_h > 2: # if height is the limiting factor
        screen_w = info.current_h * 2
        screen_h = info.current_h
        screen_buffer_w = (info.current_w - screen_w) // 2
        screen_buffer_h = 0
    else:
        screen_w = screen_w
        screen_h = screen_w // 2
        screen_buffer_w = 0
        screen_buffer_h = (info.current_h - screen_h) // 2

    main_menu = MainMenu.MainMenu(info.current_w, info.current_h, screen_w, screen_h, screen_buffer_w, screen_buffer_h)
    main_menu.display()

    # for quick testing of game_window
    # game_instance = Game(False, 4, 'easy')
    # game_window = GameWindow.GameWindow(game_instance, info.current_w, info.current_h)
    # game_window = GameWindow.GameWindow(width=info.current_w, height=info.current_h)
    # game_window.display()
    '''
    run = True
    # instantiate our needed classes here
    # todo: change Game to accept no params and have a setparams method
    #Game.startGame()
    game_instance = Game()
    # window set up
    pygame.init()
    # Retrieve monitor info
    info = pygame.display.Info()
    window = pygame.display.set_mode((info.current_w, info.current_h))
    
    pygame.display.set_caption('Operation-Uno')

    # text and font
    font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', 60)
    button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', 22)
    png = pygame.image.load('Resources/Images/uno.png')

    # buttons
    play_button = Button(colors["green"], [15, 175], [100, 50], button_font, "Play", colors["green"], (37,186,176))
    diff_button = Button(colors["red"], [15, 250], [200, 50], button_font, "Difficulty Mode", colors["red"], (37,186,176))
    num_players_button = Button(colors["blue"], [15, 325], [200, 50], button_font, "Number Players", colors["blue"], (37,186,176))
    sound_button = Button(colors["yellow"], [15, 400], [200, 50], button_font, "Sound Effects", colors["yellow"], (37,186,176))
    pygame.mixer.init()
    
    #  game loop -------------------------
    msound.load("Resources/Sounds/Fanfare-sound.wav")
    msound.play(-1)
    if (game_instance.getSoundEffects() == "off"):
            msound.pause()
    else:
        msound.play(-1)

    while run:
        mouse_pos = pygame.mouse.get_pos()

        # Have the background fanfare playing while the menu is running
        

        # ---------------- updates -----------------
        play_button.updateButton(mouse_pos, window)
        diff_button.updateButton(mouse_pos, window)
        num_players_button.updateButton(mouse_pos, window)
        sound_button.updateButton(mouse_pos, window)

        for event in pygame.event.get(): 
            # ----------- ongoing checks (controls, updates, etc) ----------
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.isHovered():
                    print('Pressed Play Button')
                    game_instance.printGameState()
                    print(num_players)
                    game_instance.startGame(num_players, 2)
                    PlayGame.playGameMenu(game_instance)
                if diff_button.isHovered():
                    print('Pressed Difficulty Button')
                    # msound.load("Resources/Sounds/Dealing-cards.wav")
                    # msound.play(1)
                    # explosionSound = mixer.Sound("Resources/Sounds/Dealing-cards.wav")
                    # explosionSound.play()
                    Difficulty.changeDifficulty(game_instance)
                if num_players_button.isHovered():
                    print('Pressed Num Players Button')
                    num_players = NumPlayers.changeNumPlayers(game_instance)
                if sound_button.isHovered():
                    print('Pressed Sound Button')
                    SoundEffects.changeSoundEffects(game_instance)
                    if (game_instance.getSoundEffects() == "off"):
                        msound.pause()
                    else:
                        msound.play(-1)
                
        
        # ---------- renders --------------
        displayWindow(window)
        displayMessage("OPERATION UNO", colors["white"], [150, 25], window)
        play_button.displayButton(window)
        diff_button.displayButton(window)
        num_players_button.displayButton(window)
        sound_button.displayButton(window)
        window.blit(png, (225, 150))
        # pygame.display.flip() # Do we need this? I feel like this will change the layout of the window
        
        # ----------- final update --------------
        pygame.display.update()
'''
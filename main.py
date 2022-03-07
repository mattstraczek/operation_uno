from Game import Game
from PlayGame import PlayGame
from Button import Button
from Difficulty import Difficulty
from NumPlayers import NumPlayers
from SoundEffects import SoundEffects
import pygame
# from pygame import mixer
# from mixer import music
import os
import pygame.mixer as mixer
from pygame.mixer import music as msound

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

# main ----------------------------

if __name__ == '__main__':
    run = True
    # instantiate our needed classes here
    game_instance = Game(2, 1) # initializes a default game with 2 players (1 AI)
    
    # window set up
    pygame.init()
    window = pygame.display.set_mode(background_size)
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
                    NumPlayers.changeNumPlayers(game_instance)
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

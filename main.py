from Game import Game
from Button import Button
import pygame
import os

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

# main ----------------------------

if __name__ == '__main__':
    run = True
    # instantiate our needed classes here
    game_instance = Game(2, 1) # initializes a default game with 2 players and 1 AI
    
    # window set up
    pygame.init()
    window = pygame.display.set_mode(background_size)
    pygame.display.set_caption('Operation-Uno')

    # text and font
    font = pygame.font.Font('Resources/Font/OpenSans-ExtraBold.ttf', 60)
    button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', 22)
    png = pygame.image.load('Resources/Images/uno.png') # Loading the image into the program from the Resources folder

    # buttons
    play_button = Button(colors["green"], [100, 125], [100, 50], button_font, "Play", colors["green"], (37,186,176))
    diff_button = Button(colors["red"], [100, 200], [200, 50], button_font, "Difficulty Mode", colors["red"], (37,186,176))
    num_players_button = Button(colors["blue"], [100, 275], [200, 50], button_font, "Number Players", colors["blue"], (37,186,176))
    sound_button = Button(colors["yellow"], [100, 350], [200, 50], button_font, "Sound Effects", colors["yellow"], (37,186,176))

    #  game loop -------------------------

    while run:
        mouse_pos = pygame.mouse.get_pos()

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
                    game_instance.playGame()
                if diff_button.isHovered():
                    print('Pressed Difficulty Button')
                    #game_instance.changeDifficulty()
                if num_players_button.isHovered():
                    print('Pressed Num Players Button')
                    #game_instance.changeNumPlayers()
                if sound_button.isHovered():
                    print('Pressed Sound Button')
                    #game_instance.changeSoundEffects()

                
        
        # ---------- renders --------------
        displayWindow(window)
        displayMessage("OPERATION UNO", colors["white"], [150, 25], window)
        play_button.displayButton(window)
        diff_button.displayButton(window)
        num_players_button.displayButton(window)
        sound_button.displayButton(window)
        display.blit(png, (500, 300)) # Renders the image to the display
        pygame.display.flip() # Updates the screen to reflect the image's 
        
        # ----------- final update --------------
        pygame.display.update()

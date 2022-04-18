import pygame
from Screens import MainMenu, GameWindow
from Game import Game
from CardSprite import CardSprite
from ButtonSprite import ButtonSprite
from Card import Card
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

def singleUpdate(card, new_pos):
    if card.squared_distance(new_pos) > 100:
        card.update(new_pos)
        return False
    else:
        print("done")
        card.place()
        return True

if __name__ == '__main__':
    pygame.init()
    info = pygame.display.Info()
    # do some math to establish a 2:1 screen dimension
    screen_w, screen_h = info.current_w, info.current_h

    #main_menu = MainMenu.MainMenu(w=info.current_w, h=info.current_h)
    #main_menu.display()

    # for quick testing of game_window
    # game_instance = Game(False, 3, 'easy')
    # game_window = GameWindow.GameWindow(game_instance, info.current_w, info.current_h)
    # game_window.display()



    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((info.current_w, info.current_h))

    background = pygame.image.load("VioletBackground.png")
    red_card = Card("Red", 5)
    card = CardSprite((100, 100), (100, 100), red_card)
    card_group = pygame.sprite.Group()
    card_group.add(card)
    
    red    = pygame.Color("Red")
    yellow = pygame.Color("Yellow")
    green  = pygame.Color("Green")
    blue   = pygame.Color("Blue")
    white  = pygame.Color("White")
    black = pygame.Color("Black")

    fontSize = info.current_w // 50
    button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize)
    draw_btn = ButtonSprite(screen, (screen_w/2, screen_h/2), (screen_w/8,screen_w/16), "DRAW", button_font, red, yellow)
    button_group = pygame.sprite.Group()
    button_group.add(draw_btn)
    # def __init__(self, pos, dim, message, font, base_text_color, hover_text_color, base_border_color, hover_border_color):

    single = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        screen.blit(background, (0,0))
        card_group.draw(screen)

        button_group.draw(screen)
        button_group.update()

        if single:
            if singleUpdate(card, (100, 500)):  
                single = False
        clock.tick(60)


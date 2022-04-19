import pygame
from Screens import MainMenu, GameWindow, GameWindow_test
from Game import Game
from CardSprite import CardSprite
from ButtonSprite import ButtonSprite
from Card import Card
from Deck import Deck
#from Game import Game
#from PlayGame import PlayGame
#from Difficulty import Difficulty
#from NumPlayers import NumPlayers
#from SoundEffects import SoundEffects
import numpy as np
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

    # main_menu = MainMenu.MainMenu(w=info.current_w, h=info.current_h)
    # main_menu.display()

    # for quick testing of game_window
    game_instance = Game(screen_w, screen_h, False, 3, 'easy')
    game_window = GameWindow_test.GameWindow_test(game_instance, info.current_w, info.current_h)
    game_window.display()



    # clock = pygame.time.Clock()
    # screen = pygame.display.set_mode((info.current_w, info.current_h))

    # background = pygame.image.load("VioletBackground.png")
    # background = pygame.transform.scale(background, (screen_w, screen_h))

    # red_card = Card("Red", 5)
    # card = CardSprite((100, 100), (100, 100), Card("Red", 5))
    # card1 = CardSprite((500, 100), (100, 100), Card("Red", 5))

    
    # card_group = pygame.sprite.Group()
    # card_group.add(card)
    # card_group.add(card1)

    # deck = Deck(screen_w, screen_h).sprite_deck
    # print(deck)

    # red    = pygame.Color("Red")
    # yellow = pygame.Color("Yellow")
    # green  = pygame.Color("Green")
    # blue   = pygame.Color("Blue")
    # white  = pygame.Color("White")
    # black = pygame.Color("Black")

    # fontSize = info.current_w // 50
    # button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize)
    # draw_btn = ButtonSprite(screen, (screen_w/2, screen_h/2), (screen_w/8,screen_w/16), "DRAW", button_font, red, yellow)
    # button_group = pygame.sprite.Group()
    # button_group.add(draw_btn)
    # # def __init__(self, pos, dim, message, font, base_text_color, hover_text_color, base_border_color, hover_border_color):

    # single = True

    # for card in deck:
    #     card.update_pos((np.random.rand()*screen_w*7/8+screen_w/16, np.random.rand()*screen_h*7/8+screen_h/16))

    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()

    #     pygame.display.flip()
    #     # screen.blit(background, (0,0))
    #     screen.fill(red)

    #     card_group.draw(screen)

    #     button_group.draw(screen)
    #     button_group.update()

    #     # deck.draw(screen)
    #     # deck.update()

    #     card.update_pos((100, 500))
    #     card1.update_pos((1000, 100))

    #     card_group.update()

    #     clock.tick(60)


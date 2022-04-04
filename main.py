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

    # main_menu = MainMenu.MainMenu(info.current_w, info.current_h, screen_w, screen_h, screen_buffer_w, screen_buffer_h)
    # main_menu.display()
    
    main_menu = MainMenu.MainMenu(w=info.current_w, h=info.current_h)
    main_menu.display()

    # for quick testing of game_window
    # game_instance = Game(False, 3, 'easy')
    # game_window = GameWindow.GameWindow(game_instance, info.current_w, info.current_h)
    # game_window.display()
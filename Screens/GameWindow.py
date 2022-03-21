#from Ruleset import Ruleset
from Deck import Deck
from Player import Player
from AI import AI 
from Components import Button, Message, Image
from Game import Game
import pygame, sys

class GameWindow:
    def __init__(self, game_instance, width=800, height=600, bg_color=pygame.Color("Black")):
        self.title = "UNO Game"
        self.game_instance = game_instance
        self.w = width
        self.h = height
        self.bg_color = bg_color
        self.card_imgs = []
    def display(self):
        clock = pygame.time.Clock()
        game_window = pygame.display.set_mode((self.w, self.h))
        for i in range(1,8):
            card_img = Image.Image(game_window, [self.w*i/32, self.h*7/8], [self.w/8, self.h/8], "Resources/Cards/BLUE 0.png")
            self.card_imgs.append(card_img)
        selected_card = None

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif not selected_card and event.type == pygame.MOUSEBUTTONDOWN:
                    for card in self.card_imgs:
                        if card.isHovered():
                            selected_card = card
                            selected_card.clicked = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    if selected_card:
                        selected_card.clicked = False
                        selected_card = None

            game_window.fill(self.bg_color)
            pos = pygame.mouse.get_pos()

            for card in self.card_imgs:
                card.displayImage()

            if selected_card:
                selected_card.updatePos(pos)
                selected_card.displayImage()

            pygame.display.flip()
            clock.tick(60)

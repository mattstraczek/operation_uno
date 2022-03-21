#from Ruleset import Ruleset
from Deck import Deck
from Player import Player
from AI import AI 
from Components import Button, Message, Image
from Game import Game
import pygame, sys

def updateHand(self, player, window):
    temp_hand = []
    for i in range(len(player.hand)):
        temp_hand.append(Image.Image(window, [self.w*i/32 + 615, self.h*7/8], [self.w/8, self.h/8], player.hand[i]))
    return temp_hand
# def updateTopCard():
# def removeCard(player):
# def placeCard(player):

class GameWindow:
    def __init__(self, game_instance, width=800, height=600, bg_color=pygame.Color("Black")):
        self.title = "UNO Game"
        self.game_instance = game_instance
        self.w = width
        self.h = height
        self.bg_color = bg_color
        self.card_imgs = []
        self.middle_bound = pygame.Rect((self.w / 2 - self.w / 8, self.h / 2 - self.h / 8), (self.w / 4, self.h / 4))
        #self.draw_button
    def display(self):
        clock = pygame.time.Clock()
        game_window = pygame.display.set_mode((self.w, self.h))
        self.top_card = Image.Image(game_window, [self.w/2, self.h/2], [self.w/8, self.h/8], self.game_instance.top_card)

        selected_card = None

        players = self.game_instance.players
        
        while True:
            self.card_imgs = updateHand(self, self.game_instance.main_player, game_window)
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
                        if selected_card.checkInBounds(self.middle_bound):
                            selected_card.updateBasePos((self.middle_bound.centerx, self.middle_bound.centery))
                            self.game_instance.main_player.hand.remove(selected_card.card)
                            self.game_instance.updateTopCard(selected_card.card)
                            self.top_card.updateCard(self.game_instance.top_card)
                        selected_card = None

                #if draw_button.isHovered


            game_window.fill(self.bg_color)
            pos = pygame.mouse.get_pos()

            for card in self.card_imgs:
                card.displayImage()

            if selected_card:
                selected_card.updatePos(pos)
                selected_card.displayImage()

            self.top_card.displayImage()

            pygame.draw.rect(game_window, pygame.Color("White"), self.middle_bound, 2, 10)
            pygame.display.flip()
            clock.tick(60)

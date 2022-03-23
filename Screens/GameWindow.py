from Components import Button, Message, Image, CardImage
from Game import Game
import pygame, sys
from time import sleep, time
import numpy as np

def updateCards(self, player, base_card_pos, window):
    num_cards = len(player.hand)
    card_offsets = np.linspace(-num_cards/2, num_cards/2, num_cards)
    if base_card_pos[0] == self.w/2: # top or bottom of screen
        for i in range(num_cards):
            self.card_imgs.append(CardImage.CardImage(window, [base_card_pos[0]+self.w*card_offsets[i]/32, base_card_pos[1]], [self.w/8, self.h/8], player.hand[i]))
    else:
        for i in range(num_cards):
            self.card_imgs.append(CardImage.CardImage(window, [base_card_pos[0], base_card_pos[1]+self.h*card_offsets[i]/32], [self.w/8, self.h/8], player.hand[i]))

# def updateTopCard():
# def removeCard(player):
# def placeCard(player):

'''
import threading 

def ai_play(): 
    print("2 seconds finished") 

timer = threading.Timer(2.0, func)
timer.start()'''

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
        self.top_card = CardImage.CardImage(game_window, [self.w/2, self.h/2], [self.w/8, self.h/8], self.game_instance.top_card)

        selected_card = None
        finished_turn = True
        last_time = time()

        total_players = self.game_instance.total_players
        card_positions = []
        if total_players==2:
            card_positions.append((self.w/2, self.h*7/8))
            card_positions.append((self.w/2, self.h*1/8))

        if total_players==3:
            card_positions.append((self.w/2, self.h*7/8))
            card_positions.append((self.w/8, self.h/2))
            card_positions.append((self.w*7/8, self.h/2))

        if total_players==4:
            card_positions.append((self.w/2, self.h*7/8))
            card_positions.append((self.w/8, self.h/2))
            card_positions.append((self.w/2, self.h*1/8))
            card_positions.append((self.w*7/8, self.h/2))

        index = self.game_instance.players.index(self.game_instance.main_player)
        player_dict = {}
        for i in range(total_players):
            print(i)
            player_dict[i] = self.game_instance.players[(index+i)%(total_players-1)]

        while not self.game_instance.winnerExists():
            if finished_turn:
                if time()-last_time > 2:
                    last_time = time()
                    if self.game_instance.nextTurn():
                        finished_turn = False
                else:
                    sleep(0.1)
                
            
            self.card_imgs = []
            for i in range(total_players):
                updateCards(self, player_dict[i], card_positions[i], game_window)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                elif not selected_card and event.type == pygame.MOUSEBUTTONDOWN:
                    #if draw_button.isHovered:

                    for card in self.card_imgs:
                        if card.isHovered():
                            selected_card = card
                            selected_card.clicked = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    if selected_card:
                        if selected_card.checkInBounds(self.middle_bound):
                            if self.game_instance.ruleset.isValid(selected_card.card):
                                selected_card.updateBasePos((self.middle_bound.centerx, self.middle_bound.centery))
                                self.top_card.updateCard(self.game_instance.top_card)
                                finished_turn = True
                        selected_card.clicked = False
                        selected_card = None

            self.top_card.updateCard(self.game_instance.top_card)

            game_window.fill(self.bg_color)
            pos = pygame.mouse.get_pos()

            for card in self.card_imgs:
                card.displayImage()

            self.top_card.displayImage()

            if selected_card:
                selected_card.updatePos(pos)
                selected_card.displayImage()

            pygame.draw.rect(game_window, pygame.Color("White"), self.middle_bound, 2, 10)
            pygame.display.flip()
            clock.tick(60)

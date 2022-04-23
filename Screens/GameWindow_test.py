from Components import Button, Message, Image, CardImage
from CardSprite import CardSprite
from Game import Game
import pygame, sys
from time import sleep, time
import numpy as np
from pygame import mixer as mix

class GameWindow_test:
    def __init__(self, game_instance, width=800, height=600, bg_color=pygame.Color("Purple")):
        """ Initializes a game window to display a game. """
        self.title = "UNO Game"
        self.game_instance = game_instance
        self.w = width
        self.h = height
        self.bg_color = bg_color

    def update_cards(self, player, base_card_pos):
        """ Updates the position of the cards in player's hand """
        num_cards = len(player.hand)
        card_offsets = np.linspace(-num_cards/2, num_cards/2, num_cards)
        if base_card_pos[0] == self.w/2: # top or bottom of screen
            for i in range(num_cards):
                player.hand.sprites()[i].update_pos((base_card_pos[0]+self.w*card_offsets[i]/32, base_card_pos[1]))
        else:
            for i in range(num_cards):
                player.hand.sprites()[i].update_pos((base_card_pos[0], base_card_pos[1]+self.h*card_offsets[i]/32))

    def update_graphics(self, game_window):
        """ Updates the graphics of the game """
        # Draws the background
        game_window.fill(self.bg_color)

        # Updates player hand display
        for player in self.game_instance.players:
            player.hand.draw(game_window)
            player.hand.update(False, False)

        # Updates the cards that have been played display
        self.game_instance.played_cards.draw(game_window)
        self.game_instance.played_cards.update(True, True)

        if self.can_draw:
            self.draw_button.displayButton()
        else:
            self.skip_button.displayButton()

        pygame.display.flip()
        self.clock.tick(60)

    def initialize_player_positions(self, num_players):
        card_positions = []
        bottom = (self.w/2, self.h*7/8)
        left = (self.w/8, self.h/2)
        top = (self.w/2, self.h*1/8)
        right = (self.w*7/8, self.h/2)
        card_positions.append(bottom)
        if num_players==2:
            card_positions.append(top)
        if num_players==3:
            card_positions.append(left)
            card_positions.append(top)
        if num_players==4:
            card_positions.append(left)
            card_positions.append(top)
            card_positions.append(right)
        return card_positions
    
    # def pause(self, t):
    #     if time()-self.last_time > t:
    #         last_time = time()
    #         self.paused = False
    #     else:
    #         self.paused = True

    def update_next_turn(self, events, mouse_pos):
        curr_player = self.game_instance.getCurrPlayer()
        if curr_player.isAI:
            print(curr_player)
            self.game_instance.nextTurn()
            self.paused = True
            return True

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.draw_button.isHovered() and self.can_draw:
                    self.game_instance.draw(self.game_instance.main_player, 1)
                    self.can_draw = False
                    self.mouse_down = True
                    # print("Main player drew")
                    return True

                elif self.skip_button.isHovered() and not self.can_draw and not self.mouse_down:
                    self.game_instance.skipTurn()
                    self.can_draw = True
                    # print("Main player skipped turn")
                    return True

                if self.selected_card:
                    if self.game_instance.ruleset.isValid(self.selected_card, self.game_instance.top_card):
                        self.game_instance.updateTurnHuman(self.game_instance.main_player, self.selected_card)
                        self.paused = True
                        self.can_draw = True
                        return True
        return False

    def display(self):
        """ Displays the game window and allows for a game to be played using the logic of the imported components. """
        self.clock = pygame.time.Clock()
        self.last_time = time()

        game_window = pygame.display.set_mode((self.w, self.h))

        num_players = self.game_instance.total_players
        card_positions = self.initialize_player_positions(num_players)

        index = self.game_instance.players.index(self.game_instance.main_player)
        player_dict = {}
        for i in range(num_players):
            player_dict[i] = self.game_instance.players[(index+i)%(num_players)]

        # Update the positions of the cards to their players' hands
        for i in range(num_players):
            self.update_cards(player_dict[i], card_positions[i])

        # Update the position of the top card
        self.game_instance.top_card.update_pos((self.w/2, self.h/2))
        self.selected_card = None
        self.paused = True  # initial pause of the game
        red    = pygame.Color("Red")
        yellow = pygame.Color("Yellow")
        green  = pygame.Color("Green")
        blue   = pygame.Color("Blue")
        white  = pygame.Color("White")
        black = pygame.Color("Black")

        if self.w <= self.h:
            fontSize = self.w // 50
        else:
            fontSize = self.h // 20

        self.can_draw = True
        self.mouse_down = False

        button_font = pygame.font.Font('Resources/Font/OpenSans-Regular.ttf', fontSize)
        self.draw_button = Button.Button(game_window, red, [self.w*7/8, self.h*7/8], [fontSize*4, fontSize*2], button_font, "Draw", red, yellow)
        self.skip_button = Button.Button(game_window, red, [self.w*7/8, self.h*7/8], [fontSize*4, fontSize*2], button_font, "Skip", red, yellow)

        while True: # no winner
            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_down = False
                    if not self.selected_card:
                        for card in self.game_instance.main_player.hand:
                            if card.rect.collidepoint(mouse_pos):
                                self.selected_card = card
                    elif self.selected_card:
                        if not self.selected_card.rect.collidepoint(mouse_pos):
                            self.selected_card = None

            if self.paused:
                if time()-self.last_time > 2:
                    self.last_time = time()
                    print("here")
                    self.paused = False
                else:
                    pass
            
            if not self.paused:
                if(self.update_next_turn(events, mouse_pos)):
                    self.last_time = time()

            for i in range(num_players):
                self.update_cards(player_dict[i], card_positions[i])

            self.update_graphics(game_window)

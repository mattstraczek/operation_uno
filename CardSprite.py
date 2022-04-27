import pygame
import numpy as np

class CardSprite(pygame.sprite.Sprite):
    def __init__(self, pos, dim, card):
        super().__init__()
        # pos = (center x, center y), dim = (width, height)

        self.card = card    # saves the card for comparison
        self.pos = pos      # saves the position of the card
        self.initial_pos = pos
        self.is_selected = False

        # Loads in the image and scales the image to fit dim accordingly
        self.front = pygame.image.load("Resources/Cards/" + str(card) + ".png")
        image_dim = self.front.get_size()
        image_scale = min(dim[0]/image_dim[0], dim[1]/image_dim[1])
        self.dim = tuple(i*image_scale for i in image_dim)
        self.front = pygame.transform.scale(self.front, self.dim)

        self.back = pygame.image.load("Resources/Cards/Back-of-card.png")
        self.back = pygame.transform.scale(self.back, self.dim)

        self.image = self.back
        
        # Rectangle that bounds the image
        self.rect = self.image.get_rect(center=pos)
    
        # Place Card Sound
        pygame.mixer.init()
        self.place_sound = pygame.mixer.Sound("Resources/Sounds/PlaceCard.wav")

    def update(self, is_placing, should_rotate):
        """ Updates the position of the card to a place towards the new position """
        curr_x = self.rect.centerx
        curr_y = self.rect.centery

        delta_x = (self.pos[0]-self.initial_pos[0])*self.squared_distance(self.pos, self.rect.center)**0.5/5000
        delta_y = (self.pos[1]-self.initial_pos[1])*self.squared_distance(self.pos, self.rect.center)**0.5/5000

        if(self.initial_pos[0]==self.pos[0] and self.initial_pos[1]==self.pos[1]):
            return

        # moving right
        if (delta_x > 0 and curr_x > self.pos[0] or delta_x < 0 and curr_x < self.pos[0] or abs(delta_x)<=5) and (delta_y > 0 and curr_y > self.pos[1] or delta_y < 0 and curr_y < self.pos[1] or abs(delta_y)<=5):
            self.rect.center = self.pos
            self.initial_pos = self.pos
            if is_placing:
                self.place()
            if should_rotate:
                self.image = pygame.transform.rotozoom(self.image, np.random.rand()*60-30, 1)
                self.rect = self.image.get_rect(center=self.rect.center)
            return

        self.rect.centerx += delta_x #if self.pos[0] > self.rect.centerx else -delta_x
        self.rect.centery += delta_y #if self.pos[1] > self.rect.centery else -delta_y

    def squared_distance(self, pos1, pos2):
        """ Returns the squared distance between the current position and the new position """
        return (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2

    def place(self):
        """ Plays the placing card sound effect """
        self.place_sound.play()

    def update_card(self, new_card, replace_image):
        """ Updates the current card with a new card and updates the image """ 
        self.card = new_card
        self.front = pygame.image.load("Resources/Cards/" + str(new_card) + ".png")
        self.front = pygame.transform.scale(self.front, self.dim)
        if replace_image:
            self.image = self.front

    def update_pos(self, new_pos):
        self.pos = new_pos
        # self.rect = self.image.get_rect(center=self.pos)

    def toggle_face(self):
        """ Toggles between showing the front and back of the card """
        self.image = self.front if self.image==self.back else self.back

    def __str__(self):
        """ Overridden toString() method displays the card. """
        return str(self.card.color) + " " + str(self.card.value)
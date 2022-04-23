import pygame
import numpy as np

class CardSprite(pygame.sprite.Sprite):
    def __init__(self, pos, dim, card):
        super().__init__()
        # pos = (center x, center y), dim = (width, height)

        self.card = card    # saves the card for comparison
        self.pos = pos      # saves the position of the card
        self.initial_pos = pos

        # Loads in the image and scales the image to fit dim accordingly
        self.image = pygame.image.load("Resources/Cards/" + str(card) + ".png")
        image_dim = self.image.get_size()
        image_scale = min(dim[0]/image_dim[0], dim[1]/image_dim[1])
        self.dim = tuple(i*image_scale for i in image_dim)
        self.image = pygame.transform.scale(self.image, self.dim)

        # Rectangle that bounds the image
        self.rect = self.image.get_rect(center=pos)
    
        # Place Card Sound
        self.place_sound = pygame.mixer.Sound("Resources/Sounds/PlaceCard.mp3")

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
                rotated_image = pygame.transform.rotate(self.image, np.random.rand()*60-30)
                self.rect = rotated_image.get_rect(center=self.rect.center)
                self.image = rotated_image
            return

        self.rect.centerx += delta_x #if self.pos[0] > self.rect.centerx else -delta_x
        self.rect.centery += delta_y #if self.pos[1] > self.rect.centery else -delta_y

    def squared_distance(self, pos1, pos2):
        """ Returns the squared distance between the current position and the new position """
        return (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2

    def place(self):
        """ Plays the placing card sound effect """
        self.place_sound.play()

    def update_card(self, new_card):
        self.card = new_card
        self.image = pygame.image.load("Resources/Cards/" + str(new_card) + ".png")
        self.image = pygame.transform.scale(self.image, self.dim)

    def update_pos(self, new_pos):
        self.pos = new_pos

    def __str__(self):
        """ Overridden toString() method displays the card. """
        return str(self.card.color) + " " + str(self.card.value)
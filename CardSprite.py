import pygame
  
class CardSprite(pygame.sprite.Sprite):
    def __init__(self, pos, dim, card):
        # pos = (center x, center y)
        # dim = (width, height)
        super().__init__()

        self.card = card    # saves the card for comparison

        self.image = pygame.image.load("Resources/Cards/" + str(card) + ".png")
        image_dim = self.image.get_size()
        image_scale = min(dim[0]/image_dim[0], dim[1]/image_dim[1])

        self.dim = tuple(i*image_scale for i in image_dim)
        self.image = pygame.transform.scale(self.image, self.dim)
        self.rect = self.image.get_rect(center=pos)
    
        self.place_sound = pygame.mixer.Sound("PlaceCard.mp3")

    def update(self, new_pos):
        if self.squared_distance(new_pos) < 100:
            self.rect.center = new_pos

        delta_x = (int)(abs(self.rect.centerx-new_pos[0])**0.35)
        delta_y = (int)(abs(self.rect.centery-new_pos[1])**0.35)
        self.rect.x += delta_x if new_pos[0] > self.rect.centerx else -delta_x
        self.rect.y += delta_y if new_pos[1] > self.rect.centery else -delta_y

    def squared_distance(self, new_pos):
       return (self.rect.centerx-new_pos[0])**2 + (self.rect.centery-new_pos[1])**2

    def place(self):
        self.place_sound.play()

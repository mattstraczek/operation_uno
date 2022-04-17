import pygame
  
class CardSprite(pygame.sprite.Sprite):
    def __init__(self, pos, dim, card):
        # pos = (center x, center y)
        # dim = (width, height)
        super().__init__()

        self.image_path = "Resources/Cards/" + str(card) + ".png"
        self.image = pygame.image.load(self.image_path)
        image_dim = self.image.get_size()
        image_scale = min(dim[0]/image_dim[0], dim[1]/image_dim[1])

        self.dim = tuple(i*image_scale for i in image_dim)
        self.image = pygame.transform.scale(self.image, self.dim)
        self.rect = self.image.get_rect(center=pos)
    
        self.place_sound = pygame.mixer.Sound("PlaceCard.mp3")

    def update(self, new_pos):
        if self.squared_distance(self.rect.center, new_pos) < 50:
            self.rect.center = new_pos
            self.place()

        delta_x = (int)(abs(self.rect.x-new_pos[0])**0.25)
        delta_y = (int)(abs(self.rect.x-new_pos[0])**0.25)
        if new_pos[0] > self.rect.center[0]:
            self.rect.x += delta_x
        else:
            self.rect.x -= delta_x
        if new_pos[1] > self.rect.center[1]:
            self.rect.y += delta_y
        else:
            self.rect.y -= delta_y

    def squared_distance(self, pos, new_pos):
       return (pos[0]-new_pos[0])**2 + (pos[1]-new_pos[1])**2

    def place(self):
        self.place_sound.play()

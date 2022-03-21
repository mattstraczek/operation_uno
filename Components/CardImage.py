import pygame

class CardImage:
    def __init__(self, window, pos, size, card):
        self.window = window
        self.base_pos = pos
        self.pos = pos
        self.size = size
        self.clicked = False
        self.card = card

        self.png = pygame.image.load("Resources/Cards/" + str(card) + ".png")
        png_dims = self.png.get_size()
        png_scale_factor = min(size[0]/png_dims[0], size[1]/png_dims[1])
        self.new_png_dims = tuple(i*png_scale_factor for i in png_dims)
        self.image = pygame.transform.scale(self.png, self.new_png_dims)
        self.image_rect = self.image.get_rect(center=pos, size=self.new_png_dims)

    def displayImage(self):
        if not self.clicked:
            self.pos = self.base_pos
        self.image_rect = self.image.get_rect(center=self.pos, size=self.new_png_dims)
        self.window.blit(self.image, self.image_rect)

    def isHovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos[0] in range(self.image_rect.left, self.image_rect.right) and mouse_pos[1] in range(self.image_rect.top, self.image_rect.bottom)

    def checkInBounds(self, bounds):
        mouse_pos = pygame.mouse.get_pos()
        #return mouse_pos[0] in range(bounds[0][0], bounds[1][0]) and mouse_pos[1] in range(bounds[0][1], bounds[1][1])
        return mouse_pos[0] in range(bounds.left, bounds.right) and mouse_pos[1] in range(bounds.top, bounds.bottom)

    def updateImage(self, image_path):
        png = pygame.image.load(image_path)
        png_dims = png.get_size()
        png_scale_factor = min(self.size[0]/png_dims[0], self.size[1]/png_dims[1])
        self.new_png_dims = tuple(i*png_scale_factor for i in png_dims)
        self.image = pygame.transform.scale(png, self.new_png_dims)
        self.image_rect = self.image.get_rect(center=self.pos, size=self.new_png_dims)

    def updatePos(self, new_pos):
        if self.clicked:
            self.pos = new_pos

    def updateBasePos(self, new_pos):
        self.base_pos = new_pos
    
    def updateCard(self, new_card):
        '''Updating Top Card'''
        self.card = new_card
        self.png = pygame.image.load("Resources/Cards/" + str(self.card) + ".png")
        self.image = pygame.transform.scale(self.png, self.new_png_dims)
    # def updateSize(self, new_size): not sure if needed

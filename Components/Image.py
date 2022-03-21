import pygame

class Image:
    def __init__(self, window, pos, size, image_path):
        self.window = window
        self.pos = pos
        self.size = size

        png = pygame.image.load(image_path)
        png_dims = png.get_size()
        png_scale_factor = min(size[0]/png_dims[0], size[1]/png_dims[1])
        new_png_dims = tuple(i*png_scale_factor for i in png_dims)
        self.image = pygame.transform.scale(png, new_png_dims)
        self.image_rect = self.image.get_rect(center=pos, size=new_png_dims)

    def displayImage(self):
        self.window.blit(self.image, self.image_rect)

    def isHovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos[0] in range(self.image_rect.left, self.image_rect.right) and mouse_pos[1] in range(self.image_rect.top, self.image_rect.bottom)

    def updateImage(self, image_path):
        png = pygame.image.load(image_path)
        png_dims = png.get_size()
        png_scale_factor = min(self.size[0]/png_dims[0], self.size[1]/png_dims[1])
        new_png_dims = tuple(i*png_scale_factor for i in png_dims)
        self.image = pygame.transform.scale(png, new_png_dims)
        self.image_rect = self.image.get_rect(center=self.pos, size=new_png_dims)

    def updatePos(self, new_pos):
        self.pos = new_pos
    
    # def updateSize(self, new_size): not sure if needed
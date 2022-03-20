import pygame

class Image:
    def __init__(self, window, color, image, pos, base_color, hover_color, scale=1.1):
        self.image = image
        self.pos = pos
        self.window = window
        self.color = color
        # self.msg = msg
        self.base_color = base_color
        self.hover_color = hover_color
        # self.text = self.font.render(self.msg, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=pos)
        self.image_rect = self.image.get_rect(center=pos)

        default_size = (10, 10)
        self.image_transform = transform.scale(self.image, default_size)
        
        self.base_image_rect = self.image.get_rect(center=pos, size=image_transform)
        self.base_button_rect = self.image.get_rect(topleft=[pos[0]-image_transform[0]//2, pos[1]-image_transform[1]//2], size=image_transform)
        
        scaleSize = tuple(i*scale for i in image_transform)
        self.scale_image_rect = self.image.get_rect(center=pos, size=scaleSize)
        self.scale_button_rect = self.image.get_rect(topleft=[pos[0]-scaleSize[0]//2, pos[1]-scaleSize[1]//2], size=scaleSize)

        self.image_rect = self.base_image_rect
        self.button_rect = self.base_button_rect
    
    '''
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        return position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom)       
             
    def changeColor(self, position):
        if self.checkForInput(position):
            self.text = self.font.render(self.msg, True, self.hovering_color)
        else:
            self.text = self.font.render(self.msg, True, self.base_color)
    '''

    def displayImage(self):
        if self.isHovered():
            self.button_rect = self.scale_button_rect
            pygame.draw.rect(self.window, self.hover_color, self.button_rect, 2)
        else:
            self.button_rect = self.base_button_rect
            pygame.draw.rect(self.window, self.base_color, self.button_rect, 2)
        
        self.window.blit(self.text, self.text_rect)

    def isHovered(self):
        # Gets the mouse position
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos[0] in range(self.button_rect.left, self.button_rect.right) and mouse_pos[1] in range(self.button_rect.top, self.button_rect.bottom)

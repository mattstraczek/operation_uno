import pygame

class Button:
    '''
    def __init__(self, image, pos, msg, text_color, font, base_color, hover_color):
        self.image = image
        self.pos = pos
        self.msg = msg
        self.text_color = text_color
        self.font = font
        self.base_color = base_color
        self.hover_color = hover_color
        self.text = self.font.render(self.msg, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=pos)
        self.text_rect = self.text.get_rect(center=pos)

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
    
    def __init__(self, color, pos, size, font, msg, base_color, hover_color):
        # initializes the Button, sets each element of Button
        self.color = color
        self.pos = pos
        self.size = size
        self.font = font
        self.msg = msg
        self.base_color = base_color
        self.hover_color = hover_color
        self.text = self.font.render(msg, True, base_color)
        self.text_rect = self.text.get_rect(center=pos, size=size)
        self.button_rect = self.text.get_rect(topleft=[self.pos[0]-self.size[0]//2, self.pos[1]-self.size[1]//2], size=size)

    def displayButton(self, mouse_pos, window):
        if self.isHovered(mouse_pos):
            self.text = self.font.render(self.msg, True, self.hover_color)
            pygame.draw.rect(window, self.hover_color, self.button_rect, 2)
        else:
            self.text = self.font.render(self.msg, True, self.base_color)
            pygame.draw.rect(window, self.base_color, self.button_rect, 2)
        
        window.blit(self.text, self.text_rect)

    def isHovered(self, mouse_pos):
        return mouse_pos[0] in range(self.button_rect.left, self.button_rect.right) and mouse_pos[1] in range(self.button_rect.top, self.button_rect.bottom)        

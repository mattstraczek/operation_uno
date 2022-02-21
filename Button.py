import pygame

class Button:
    def __init__(self, color, pos, size, font, msg, msg_color):
        self.color = color
        self.pos = pos
        self.size = size
        self.font = font
        # render
        self.screen_text = self.font.render(msg, True, msg_color)
        self.text_rect = self.screen_text.get_rect(center=[self.pos[0] + self.size[0]//2, self.pos[1] + self.size[1]//2])

    def displayButton(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]),  2, 3)
        window.blit(self.screen_text, self.text_rect)
    
    def buttonHover(self, mouse_pos):
        if self.pos[0] <= mouse_pos[0] <= self.pos[0] + self.size[0] and self.pos[1] <= mouse_pos[1] <= self.pos[1] + self.size[1]:
            return True
        return False

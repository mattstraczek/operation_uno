import pygame

class Button:
    def __init__(self, color, pos, size, font, msg, msg_color, highlight_color):
        # initializes the Button, sets each element of Button
        self.color = color
        self.pos = pos
        self.size = size
        self.font = font
        self.msg = msg
        self.msg_color = msg_color
        self.highlight_color = highlight_color
        self.state = "idle"
        self.clicked = False
        # render
        self.screen_text = self.font.render(msg, True, msg_color)
        self.text_rect = self.screen_text.get_rect(center=[self.pos[0] + self.size[0]//2, self.pos[1] + self.size[1]//2])

    def displayButton(self, window):
        # Displays the button
        if self.state == "idle": # if the button is not in contact by the user
            pygame.draw.rect(window, self.color, pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]),  2, 3)
            window.blit(self.screen_text, self.text_rect)
        elif self.state == "hover": # if the button is hovered over by the user
            pygame.draw.rect(window, self.highlight_color, pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]),  2, 3)
            window.blit(self.screen_text, self.text_rect)
    
    def updateButton(self, mouse_pos, window): 
        if self.pos[0] <= mouse_pos[0] <= self.pos[0] + self.size[0] and self.pos[1] <= mouse_pos[1] <= self.pos[1] + self.size[1]:
            # render
            self.screen_text = self.font.render(self.msg, True, self.highlight_color)
            self.text_rect = self.screen_text.get_rect(center=[self.pos[0] + self.size[0]//2, self.pos[1] + self.size[1]//2])
            #change state
            self.state = "hover"
        else:
            # render
            self.screen_text = self.font.render(self.msg, True, self.msg_color)
            self.text_rect = self.screen_text.get_rect(center=[self.pos[0] + self.size[0]//2, self.pos[1] + self.size[1]//2])
            #change state
            self.state = "idle"

    def isHovered(self):
        if self.state == 'hover':
            return True
        return False

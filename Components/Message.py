import pygame

class Message():
    def __init__(self, window, msg, font, color, pos):
        self.msg = msg
        self.font = font
        self.color = color
        self.pos = pos
        self.window = window

    def displayMessage(self):
        text = self.font.render(self.msg, True, self.color)
        text_rect = text.get_rect(center=self.pos)
        self.window.blit(text, text_rect)

    def changeMessage(self, new_msg):
        self.msg = new_msg
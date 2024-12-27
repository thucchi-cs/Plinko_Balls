import pygame
from constants import *

class Ball_Button:
    def __init__(self):
        self.w = width // 6
        self.h = self.w // 2
        self.x = width // 2 - self.w // 2
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, (0, 255, 0), (self.x, self.y, self.w, self.h))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
        
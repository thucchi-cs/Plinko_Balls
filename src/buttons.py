import pygame
from global_vars import *

class Ball_Button:
    def __init__(self):
        self.w = width // 6
        self.h = self.w // 4
        self.x = ((width // 2) + board_start) - self.w // 2
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, (0, 255, 0), (self.x, self.y, self.w, self.h))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
        